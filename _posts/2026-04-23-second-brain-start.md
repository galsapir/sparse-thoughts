---
layout: post
redirect_from: /second-brain-start/
title: "a week with a second brain"
description: "notes from five days of running a memory MCP across Claude Code, desktop, mobile, and Codex: what's in there, what's already not working, and why the corpus is mostly corrections."
tags: [tools, memory, second-brain]
audio: "assets/audio/second-brain-start.mp3"
---

i've been running a memory MCP as a "second brain" for the past week. a few notes, since the angle feels worth writing about even if i can't tell yet whether it actually works.

most of my work happens across a few different surfaces: Claude Code in the terminal, Claude Desktop on my mac, Claude mobile, a remote Claude Code session on an EC2 box, and now Codex for a second opinion (and i'd like to stay open to whatever comes next, maybe [pi](https://pi.dev/)). each surface is a separate conversation, and context that accumulated in one place doesn't make it to the others. you can paste it across, but you mostly don't.

two recent posts nudged me into doing something about this. oscar austegard's [muninn at 100 days](https://muninn.austegard.com/blog/muninn-at-100-days.html), which takes the autonomous companion angle seriously, and tim kellogg's [on forgetting](https://timkellogg.me/blog/2026/04/14/forgetting), which sits somewhere almost opposite to it. i'm not sure where i land between them, but reading them made me notice that what i was missing wasn't really agent autonomy, more like shared substrate. somewhere i could say "remember this" once and not say it again three days later in a different window / on a different project (since Claude's memory is currently not shared between projects).

anyway, i wrote a small memory MCP. typescript, sqlite with FTS, local-only for v0 (the cloud path is drafted and deferred). a handful of tools: `remember`, `recall`, `list_recent`, `forget`, `feedback`. one fact per `remember` call, with a scope and some tags. nothing clever, mostly so i could start using it as fast as possible. there's also a profile endpoint that returns a pinned identity plus some usage discipline for Claude, which i'll come back to.

five days in, i have a couple dozen memories. they're almost all operational: a pipeline gotcha i kept getting wrong, a workflow rule about launching subagents with worktree isolation, a design decision i wanted to lock in place. nothing grand. the kind of things that would cost me fifteen minutes to re-derive, and that i would re-derive wrong.

reading back through the corpus, something is obvious: most of what's stored is corrections: "X isn't what i thought it was". the database is closer to a log of places the map was wrong than to a classic "zettelkasten". which is maybe fine, since those are exactly the things i'd silently re-derive wrong next time. but it gives the second brain a particular "epistemic" shape, closer to debugging residue than to a durable archive of ideas. the [previous post](/2026/04/11/map-and-territory) argued that LMs are maps that average and smooth; if that's the right frame, then a second brain might be a record of the places where the averaged map failed and i had to touch the territory.

a few things already aren't working, five days in, and i want to name them specifically (and hopefully correct soon).

the biggest one is that i can see what's written but not what's recalled. there's no retrieval visibility from the inside (at least not via the tool surface i've given myself). i can't tell whether the stored memory is actually being surfaced when it matters, which means the most important question, is this useful, isn't answerable from the data i have. i'll need to add some kind of retrieval log before i can say anything honest about whether the system is earning its place.

the second is that the corpus is one-sided: it stores what i learned but almost nothing about where Claude went wrong.[^1] this is a blind spot if part of the point is to calibrate over time, not just to record what i figured out.

the third is that the tag system is undeveloped. some memories are tagged with project-local terms (`parsed_long`, `databricks`), some with cross-cutting ones (`lesson`, `form-vs-essence`), some with eight tags, some with zero. there's a taxonomy question i haven't answered, and i suspect the right answer only shows up once i start retrieving by tag in anger, which loops back to the first point.

the fourth is that capture is bursty rather than continuous. the IDs are time-sortable, and if you plot them, memories arrive in clusters of five to ten at the end of a session, then nothing for twelve hours.[^2] "second brain" implies something ambient. the actual shape is punctuated. whether that's a bug or a useful property of the design, i genuinely don't know yet.

one thing that does feel valuable already: the profile. i spent more time on this than on anything else in the system: a `profile.md` that pins down who i am, how i work, and what my tacit preferences are. week one is a good time to write it, while the corpus is small and you can still hold the whole picture in your head. but articulating things you normally just assume turns out to be real work. things i've told Claude three times in three different sessions and would rather tell once.[^3]

it's too early to tell whether any of this is worth the overhead. three things i'm watching for over the next few weeks: whether the right memory surfaces at the right time without me asking for it, whether the corpus drifts toward useful or toward noise, and whether a monthly review of it gives me something worth reading.

one unexpected thing has already happened, though. reviewing what's been stored is itself a reflection ritual. a few dozen memories over five days turns out to be a reasonable proxy for what i was actually thinking about this week, and reading them back has almost nothing to do with the system at all. i wrote some things down and now i can read them back. that's older than any of this.

i hope i'll get to write more about it when there's more to say.

---

[^1]: when Claude fabricates a schema or misses an obvious fix, i don't write that down. the `feedback` tool exists for exactly this, and i haven't used it once. there might be a version of this where Claude maintains its own error log separately, but that's a different project.

[^2]: some of this is probably an artifact: connectivity issues between the EC2 instance and the database meant i ended up documenting things in retrospect rather than in the moment.

[^3]: two entries from the profile, for flavor. one is working-style: "prefers sequential PRs over concurrent branches; when a review-driven fix changes mutation semantics, run a fresh focused review pass before merging." one is reading-style: "reads character rhetoric as performance; asks what an emotional or spiritual register does for the character, sincerity aside."