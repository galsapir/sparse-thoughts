---
layout: post
title: "a small tool for diagrams"
date: 2026-02-18
description: "Building a small Claude Code skill for generating editable draw.io diagrams — and why investing in narrow, single-purpose tools is surprisingly high-leverage."
---

I needed a way to make diagrams for posts and papers. The requirements were simple: something I could mostly just ask Claude to create, something that looked decent for scientific work, and something I could edit afterward — not a PNG I'd have to regenerate from scratch every time I wanted to move a box.

I looked at excalidraw and tldraw first, explored a few implementations, and ended up going with draw.io's XML format. The reasons were mostly practical — it's widely supported, the files open directly in the draw.io editor, and the XML structure turned out to be something Claude handles well.

The result is [drawio-claude](https://github.com/galsapir/drawio-claude). The workflow is simple: you point Claude Code at the repo, the skills built with the [skill creator](https://github.com/galsapir/claude-skills/) guidelines tell it how to generate `.drawio` files, and then you just ask for what you need in plain text. Describe a diagram, give it context, and it produces an editable file you can open directly in draw.io. Here's an example — an evaluation cycle figure I'm working on for a preprint:

![Example diagram generated with drawio-claude]({{ site.baseurl }}/assets/images/tdd-flywheel.drawio.svg)

A caveat: I built this mostly through detailed prompting and my [interview skill](https://github.com/galsapir/claude-skills/), not by deeply understanding how draw.io's XML works under the hood. I invested time in making sure the skill instructions were good and tested the outputs, but I didn't sit down and learn the format. For this kind of single-purpose tool, I think that's fine — the point is that it works and I can fix things in the editor when it doesn't.

The broader point: I think investing a small amount of time in building a narrow internal tool is surprisingly high-leverage right now. Even if it serves one specific purpose. The eval post was partly about that — we built custom evaluation tooling that only made sense for our specific health agent, and it ended up being one of the most valuable things we did. This is the same instinct applied to something much smaller. The cost of building these things has dropped enough that "should I build a small tool for this?" is almost always worth asking.