# Sparse Thoughts

Personal Jekyll blog at sparsethought.com. Customized Lanyon theme. Ruby 3.3.0 via rbenv.

## Build

```bash
eval "$(rbenv init -)" && bundle exec jekyll build
```

Output goes to `_site/`. Use `--watch` for auto-regen during local dev.

## Post structure

Posts live in `_posts/YYYY-MM-DD-slug.md`. Front matter template:

```yaml
---
layout: post
title: "lowercase title"
description: "lowercase one-line description, quoted."
date: YYYY-MM-DD
tags: [tag1, tag2]
audio: "assets/audio/slug.mp3"
---
```

**Body starts with the first paragraph, never a `# heading`.** The post layout renders the front-matter title as an H1 automatically; a body `#` produces a duplicate H1 on the post page and replaces the first-paragraph excerpt with the heading on the homepage. This bug shipped on 2026-05-16 in the raw-enough-data post.

Existing tags (grep `_posts/*.md` to confirm before relying on this list): `agents`, `tools`, `health`, `evaluation`, `culture`, `reading`, `meta`, `memory`, `second-brain`. Avoid tags that would apply to nearly every post (`ai`, `llm`).

## Pre-publish checklist

Before `git commit`:

1. Front matter complete: layout, title (lowercase, quoted), description (quoted), date, tags as YAML list `[a, b]` (not string `a, b`), audio
2. Body starts with the first paragraph, not a `#` heading
3. Footnotes use `[^N]` syntax (with caret), not plain `[N]`. Kramdown renders plain `[N]` as literal text, not clickable footnotes.
4. No `{}` author notes remain in body — `grep '{' _posts/YYYY-MM-DD-slug.md`
5. No bare URLs — all links are proper markdown `[text](url)`. Kramdown does not reliably auto-link bare URLs.
6. No em-dashes (`—` or `--`) — Gal uses `:` for descriptions, `,`/`;` for prose
7. Tags valid (`grep '^tags:' _posts/*.md` to confirm against existing set)
8. Audio generated (see below); `audio:` field present in front matter
9. `bundle exec jekyll build` finishes clean
10. Diff structure against the most recent published post to spot front-matter or opening mismatches

## Audio narration

Tool: [blog-narrator](https://github.com/galsapir/blog-narrator). Uses Kokoro-82M via mlx-audio. Config in `narrate.yml` (voice `af_heart`, speed 1.0, min_words 300).

Venv lives at `/tmp/narrator-venv` and gets wiped on reboot. Rebuild per session:

```bash
uv venv /tmp/narrator-venv --python 3.12
uv pip install "blog-narrator @ git+https://github.com/galsapir/blog-narrator.git" --python /tmp/narrator-venv/bin/python
uv pip install pip --python /tmp/narrator-venv/bin/python
/tmp/narrator-venv/bin/narrate _posts/YYYY-MM-DD-slug.md
```

The third command (`uv pip install pip`) is load-bearing: mlx-audio shells out to `pip` at first synthesis to install spacy's `en-core-web-sm` model, and `uv venv` does not include pip by default.

Do **not** use `--prerelease=allow` — spacy 4 / thinc 9 have a numpy ABI incompatibility that produces a half-broken venv (python binaries present but `narrate` missing).

The tool writes `assets/audio/slug.mp3` and auto-patches the post's `audio:` front-matter field. Synthesis takes roughly 1 minute per ~150 words on an M-series Mac.

## Commit & ship

After the checklist passes:

```bash
git add _posts/YYYY-MM-DD-slug.md assets/audio/slug.mp3
git commit -m "add post: <title>"
git push origin main
```

Do not `git add -A` or `git add .` — there's frequently untracked WIP in the repo (`buttondown/`, scratch drafts) that should not be committed.
