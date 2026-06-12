---
layout: post
redirect_from: /long-horizon-tasks/
title: "long-horizon tasks"
description: "two modes of working with agents: synced mode does the expensive work of defining the chunk, delegate mode runs cheap on it, and the cost is (probably) the point."
date: 2026-05-21
tags: [agents, meta]
audio: "assets/audio/long-horizon-tasks.mp3"
---

my screen has looked the same for a few weeks now. on the left, codex (sometimes claude) in a main pane where i'm reading through a plan, asking why it picked this decomposition, sketching an html walkthrough of what the change would touch. on the right, a smaller pane handling things i don't have to think about: a typecheck error in a file unrelated to the main work, a quick rename, a script to dump a table. one window is where i'm gaining understanding, the other is where i'm offloading chores while i do it.

i've started calling this synced mode. expensive in attention (i'm there for every minute decision), but that's the point. this is where the spec gets built, the shared language gets agreed on, the tests that actually catch things get written.

i've been noticing a second mode, and it only opens up after the first one has done enough work. and when it does, it's cheap precisely because synced mode was expensive.

at some point the design has enough detail. i can see the boundaries, i trust the tests, i trust the surrounding system to catch a bad move. and the question shifts: do i really want to babysit every minute decision from here? usually no. that's delegate mode.

the switch is mostly a feeling, but it's gated on something testable: are the boundaries solid enough that a wrong call is recoverable? has it bitten me yet? not yet. but i can imagine looking at a decision log and going "this specific call wasn't yours to make". the bet is that occasional misjudgments are cheaper than the attention it would have cost to prevent them. and when something does look off, concise traces let me literally walk the steps back.

that last part is what i turned into a [long-horizon skill](https://github.com/galsapir/skills/tree/main/skills/long-horizon): an implementation-notes file the agent keeps as it goes (decisions that weren't in the spec, tradeoffs, deviations, things i should know), terse on purpose, a scanning surface rather than documentation.

the part i think people will miss is that delegate mode is downstream of a lot of synced work. without the invested shared language[^1], the agreed-on design, the tests that actually catch things, the notes are just a list of choices i have no basis to evaluate. i'm honestly not sure which of those three is doing most of the work (my guess is shared language, but i can't cleanly separate them). what i'm more sure of is that all three were paid for in synced mode.

the question i'm left with is whether delegate mode can be entered any other way. you can turn it on, sure, but you don't get the cheapness without having paid for it elsewhere. i think (probably) the cost is the point. the chunk has to be defined enough and understandable enough all around for delegate mode to actually work, and producing that definition is what synced mode is for. there isn't a shortcut, just a relocation of the cost.

---

[^1]: ubiquitous language in the ddd sense. aihero has a [good piece](https://www.aihero.dev/skills-changelog-ubiquitous-language-grill-with-docs) framing it.