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

Tags come from the canonical vocabulary in `_data/tags.yml` — see the Tagging section below for the full procedure.

## Tagging

The canonical tag vocabulary lives in [_data/tags.yml](_data/tags.yml): one entry per tag with a one-line definition, in filter-row display order, plus a `candidates:` ledger of tags-in-waiting. That file drives the /thoughts filter buttons, so a tag absent from it is invisible to readers. Filter states are linkable (`/thoughts/#evaluation`).

**Tagging a new post** (runs as pre-publish checklist item 7):

1. Walk the vocabulary top to bottom; apply every tag whose definition the post substantively satisfies. The test is "would a reader who clicked this filter be glad this post appeared?", not "does the word occur?".
2. Budget 1-3 tags, hard cap 4. Reading roundups: `reading` plus up to 3 tags for the heaviest clusters only. Over cap: keep tags earned by the post's own thesis, drop ones triggered by examples or asides.
3. First tag is the primary shelf: the filter a satisfied reader of this post would click next.
4. Never invent a tag mid-draft. A recurring concept with no home goes into the `candidates:` ledger in `_data/tags.yml` (with this post's filename); the post ships with existing tags only.

**Minting a tag**: when a candidate has 3 posts (published plus the one in hand) that would carry it substantively, move it to `vocabulary:` with a one-line definition and retro-tag the older posts in the same commit. A tag that exists only on new posts is a bug. Proper nouns (tools, models, papers) must clear the same bar through substantive engagement — built on it, ran it for weeks, critiqued it — never passing mentions. `claude-code` cleared at 6 posts; `PEEK` at 1 post was the anti-pattern.

**Gardening** (every ~10 posts, roughly quarterly). Count applications:

```bash
grep -h '^tags:' _posts/*.md | sed 's/tags: \[//; s/\]//; s/, /\n/g' | sort | uniq -c | sort -rn
```

Then: merge or drop any tag stuck at 1 post; promote mint-ready candidates; split a tag only when it covers >40% of posts AND a nameable subcluster of 3+ exists (standing watch: `evaluation`; `benchmarks` was split out of it this way). Aim for roughly posts/4 to posts/5 total tags (12-15 tags at 60 posts).

**Bans**: tags that would apply to >50% of posts (`ai`, `llm`); multi-word tags with spaces (tags are space-joined into a `data-tags` HTML attribute — kebab-case is fine); synonyms of existing tags (`second-brain` was merged into `memory`, `culture` into `cognition` for this reason).

## Pre-publish checklist

Before `git commit`:

1. Front matter complete: layout, redirect_from (`/slug/`), title (lowercase, quoted), description (quoted), date, tags as YAML list `[a, b]` (not string `a, b`), audio
2. Body starts with the first paragraph, not a `#` heading
3. Footnotes use `[^N]` syntax (with caret), not plain `[N]`. Kramdown renders plain `[N]` as literal text, not clickable footnotes.
4. No `{}` author notes remain in body — `grep '{' _posts/YYYY-MM-DD-slug.md`
5. No bare URLs — all links are proper markdown `[text](url)`. Kramdown does not reliably auto-link bare URLs.
6. No em-dashes (`—` or `--`) — Gal uses `:` for descriptions, `,`/`;` for prose
7. Tags follow the Tagging section: every tag exists in `_data/tags.yml` vocabulary, 1-3 tags (cap 4), primary tag first, new concepts ledgered not minted
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
