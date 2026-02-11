---
layout: post
title: narrating your blog with local AI
description: "Open-source TTS crossed a quality threshold. Here's a tool that adds audio narration to Jekyll blogs using Kokoro-82M — runs locally on Apple Silicon, takes an evening to set up, costs nothing."
audio: "assets/audio/narrating-your-blog.mp3"
---

A friend who drives a lot asked if there was an audio version of my posts. There wasn't. So I looked into it — and it turned out to be absurdly easy.<!--more-->

The whole thing took an evening. That's the part worth writing about.

Open-source text-to-speech crossed a quality threshold sometime in 2025, and I completely missed it. Kokoro-82M[^1] is 82 million parameters — tiny — Apache 2.0 licensed, and it sounds good enough that I had to double-check I wasn't accidentally using a paid API. On an M4 MacBook it generates 15 minutes of audio in about 60 seconds. Chatterbox by Resemble AI beat ElevenLabs in blind listening tests. Multiple open models now compete with the proprietary leaders. This happened fast.

## what I built

I wrote a small tool called [blog-narrator](https://github.com/galsapir/blog-narrator) that adds "listen to this post" audio to Jekyll blogs. It strips markdown to clean narration text,[^2] generates speech locally via Kokoro through [mlx-audio](https://github.com/Blaizzy/mlx-audio) on Apple Silicon, and embeds a minimal audio player that shows up on posts that have audio. No API keys, no cloud, no cost.

The workflow: write your post, run `narrate _posts/your-post.md`, commit, push. Done.

What strikes me isn't the technology — it's the ratio. An evening of work, zero ongoing cost, and every post on my blog now has a listenable version. A year ago this would have required an API subscription, careful rate limiting, probably a CI pipeline. Now it's a Python script and a Jekyll include.

I keep noticing this pattern. Things that used to require real infrastructure quietly becoming a single local command. Not because someone built a product for it, but because the underlying models got good enough that you can just wire them up yourself. The fruit hangs so low now that it feels irresponsible not to pick it.

## setup

If you want to add this to your Jekyll blog:

```bash
pip install git+https://github.com/galsapir/blog-narrator.git
```

Copy the [audio player include](https://github.com/galsapir/blog-narrator/blob/main/jekyll/_includes/audio-player.html) to your `_includes/` directory, add one line to your post layout, create a `narrate.yml` config, and run `narrate` on your posts. The [README](https://github.com/galsapir/blog-narrator) has the full details.

Requires macOS with Apple Silicon, Python 3.10+, and ffmpeg.

---

[^1]: By Hexgrad. The [HuggingFace TTS Arena](https://huggingface.co/spaces/TTS-AGI/TTS-Arena) tracks quality rankings across open and proprietary TTS models — worth a look if you're curious about the landscape.

[^2]: Frontmatter, code blocks, images, footnotes, Liquid tags get stripped. Links and headers become plain text. The goal is prose that sounds natural when read aloud.
