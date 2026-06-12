---
layout: post
redirect_from: /small-changes/
title: "small changes"
description: "three small workflow shifts pointing in the same direction: portable context, cross-model delegation, and agent-first development."
date: 2026-05-07
tags: [agents, tools, meta]
audio: "assets/audio/small-changes.mp3"
---

a quick one. small adjustments to how i work with agents, none of them deep on their own. but i can feel them adding up, the workflow shifting in a way that feels worth pausing on before any of it stops feeling new. that's mostly why i'm writing this.

the first change is that i've been trying to be more platform-agnostic. the reason is fairly mundane: i don't want to feel locked in. i want to be free to play with different systems, switch between them, experiment, and i also want all of those systems to be familiar with me when i do. the memory system part of this i've [already](/2026/04/23/second-brain-start/) [written](/2026/05/01/second-brain-week-two/) about at length. more recently i've also adapted my main `CLAUDE.md` and my skill files into a format that doubles as `AGENTS.md` (which is what Codex and a few other systems read), [here](https://gist.github.com/galsapir/e337f4194f1aa951689e15cb0d469d55), so the same context follows me regardless of which agent i happen to be talking to. simon willison has a [nice post](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) on this, and more broadly on designing the loops agents run in.

with that in place, i've been using Codex a lot more. it's good. but the ways i've ended up using it are what i find interesting. sometimes i use it directly, but a lot of the time i let Claude delegate to it. the pattern is: i do the planning, scoping, and thinking inside Claude (which for whatever reason still feels like the more comfortable place for those parts), and when there's a task that's bounded enough to hand off, i ask Claude to dispatch it through `codex exec`. then i get the result back and look at it alongside Claude's own framing of what was supposed to happen. having two models with somewhat different priors on the same scoped task ends up being useful (or, more honestly, it's also a low-friction way for me to keep assessing both, since the two systems feel pretty close now). a parallel version of this is my [adversarial-review skill](https://github.com/galsapir/skills), which sends a piece of work to a different model family for a second opinion.[^1] same instinct, different shape. the skills themselves have become agent-agnostic thanks to [skills.sh](https://skills.sh/), so the same skill runs unchanged whether i'm in Claude Code or Codex.

the other pattern is on the development side. almost everything i build now is software that i think should be agent-first (still readable and obvious to a human looking at it, but written on the assumption that most of the actual operating will be delegated to an agent), easily usable by an agent with no human in the loop. and i've started writing it in a way that constantly tests this. take [cite-cli](/2026/03/13/cite-tool/), which i wrote about a couple of months ago. when i added the multi-markdown workflow feature recently, the test i actually cared about was: drop a fresh agent into the repo with no context and ask it to accomplish a small task with the new feature. that's where you find out where your `--help` is unclear, where the README assumes too much, where your error messages aren't helpful. you're effectively writing software for a new type of user, and you can test it against that same type of user before anyone else touches it.

if there's a connecting thread (and i'm honestly not sure there is, this might just be three separate things that happened to land in the same couple of weeks), it's something like: making my tools and my context legible to agents in a way that's portable across systems. the agnostic context file, the cross-model delegation, the agent-first development. they all kind of point at treating agents as a category, not as a vendor choice. i'll see if it holds up.

---

[^1]: i've also been testing open-source models on Bedrock as review agents: Kimi K2, Moonshot, and others in that bucket. the critiques are noticeably weaker and they hallucinate more, so adversarial review stays mostly on frontier models for now.
