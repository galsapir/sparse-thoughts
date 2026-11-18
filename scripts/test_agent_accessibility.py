# ABOUTME: Checks generated site artifacts that make Sparse Thoughts easy for agents to crawl.
# ABOUTME: Builds the real Jekyll site and verifies redirects, indexes, and excluded files.
from html import unescape
from pathlib import Path
import re
import subprocess


REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = REPO_ROOT / "_site"
SITE_URL = "https://sparsethought.com"


def build_site() -> None:
    subprocess.run(
        ["zsh", "-lc", 'eval "$(rbenv init -)" && bundle exec jekyll build'],
        cwd=REPO_ROOT,
        check=True,
    )


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise AssertionError(f"{path} has no front matter")

    end = text.find("\n---", 4)
    if end == -1:
        raise AssertionError(f"{path} front matter is not closed")

    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def post_url(path: Path) -> str:
    if permalink := front_matter(path).get("permalink"):
        return f"{SITE_URL}{permalink}"

    parts = path.stem.split("-", 3)
    if len(parts) != 4:
        raise AssertionError(f"{path} does not use YYYY-MM-DD-slug.md naming")

    year, month, day, slug = parts
    return f"{SITE_URL}/{year}/{month}/{day}/{slug}/"


def tracked_posts() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "_posts/*.md"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [REPO_ROOT / line for line in result.stdout.splitlines()]


def assert_contains(text: str, expected: str, context: str) -> None:
    if expected not in text:
        raise AssertionError(f"{context} missing {expected!r}")


def assert_not_contains(text: str, unexpected: str, context: str) -> None:
    if unexpected in text:
        raise AssertionError(f"{context} contains {unexpected!r}")


def test_buttondown_is_ignored() -> None:
    gitignore = (REPO_ROOT / ".gitignore").read_text().splitlines()
    if "buttondown/" not in gitignore:
        raise AssertionError(".gitignore must ignore buttondown/")


def test_generated_llms_txt_lists_posts() -> None:
    llms_text = (SITE_DIR / "llms.txt").read_text()

    for path in sorted(tracked_posts()):
        metadata = front_matter(path)
        title = metadata["title"]
        url = post_url(path)
        assert_contains(llms_text, f"[{title}]({url})", "llms.txt")
        if description := metadata.get("description"):
            assert_contains(llms_text, description, "llms.txt")


def test_posts_have_slug_redirects() -> None:
    for path in sorted(tracked_posts()):
        metadata = front_matter(path)
        if "permalink" in metadata and "redirect_from" not in metadata:
            continue

        url = post_url(path)
        redirect_path = metadata["redirect_from"]
        redirect_page = SITE_DIR / redirect_path.strip("/") / "index.html"
        if not redirect_page.exists():
            raise AssertionError(f"{redirect_page} does not exist")
        assert_contains(redirect_page.read_text(), url, str(redirect_page))


def test_internal_docs_are_not_published() -> None:
    for path in [
        SITE_DIR / "CLAUDE" / "index.html",
        SITE_DIR / "README" / "index.html",
        SITE_DIR / "buttondown",
    ]:
        if path.exists():
            raise AssertionError(f"{path} should not be published")

    sitemap_text = (SITE_DIR / "sitemap.xml").read_text()
    assert_not_contains(sitemap_text, "/CLAUDE/", "sitemap.xml")
    assert_not_contains(sitemap_text, "/README/", "sitemap.xml")


def test_post_copy_actions() -> None:
    for path in sorted(tracked_posts()):
        url = post_url(path)
        post_page = SITE_DIR / url.removeprefix(f"{SITE_URL}/") / "index.html"
        html = post_page.read_text()

        actions = html.find('class="post-actions"')
        signup = html.find('class="subscribe-section"')
        if not 0 <= actions < signup:
            raise AssertionError(f"{url} should have copy actions before the signup")

        for label in ("Copy citation", "Copy BibTeX", "Copy as Markdown"):
            assert_contains(html[actions:signup], f">{label}</button>", url)

        source = re.search(r"<template data-post-markdown>(.*?)</template>", html, re.S)
        body = path.read_text().split("\n---\n", 1)[1].strip()
        body = body.replace("{{ site.baseurl }}", "")
        if source is None or unescape(source[1]) != body:
            raise AssertionError(f"{url} should provide the full Markdown body")


def main() -> None:
    build_site()
    test_buttondown_is_ignored()
    test_generated_llms_txt_lists_posts()
    test_posts_have_slug_redirects()
    test_internal_docs_are_not_published()
    test_post_copy_actions()


if __name__ == "__main__":
    main()
