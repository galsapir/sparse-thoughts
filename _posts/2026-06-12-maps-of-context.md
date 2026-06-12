---
layout: post
redirect_from: /maps-of-context/
title: "maps of context"
description: "running PEEK's context maps on top of my second brain: a few hundred stable tokens of orientation can shape how the next hundred thousand get spent."
date: 2026-06-12
tags: [agents, memory, second-brain, PEEK]
audio: "assets/audio/maps-of-context.mp3"
---

i read two agent papers a few weeks back, planning to write about both. by now one of them feels like a footnote while the other is the one i actually kept using.

the one that survived is [PEEK](https://arxiv.org/abs/2605.19932). PEEK maintains a small context map: a compact artifact that sits in the agent's prompt and tells it how to orient inside a recurring external context. what is in this repo, corpus, or dataset? which entities matter? what schemas or constants have been useful before? where did the agent get stuck last time? (many words to say it's basically a map. as they write in their intro: "Orientation knowledge is the reusable map a human analyst would keep after several passes through a corpus". i love that they also use the word cartographer a paragraph below.)

this sounds almost too small. a few hundred or thousand tokens, appended to the system prompt. but these systems are tokens-in, tokens-out machines, and a small piece of stable orientation changes what gets searched first and what counts as a dead end. a few hundred stable tokens can shape how the next hundred thousand get spent.

a lot of current agent work feels like inference-time escalation: more context, more tool calls, more retries, more thinking time. sometimes that is the right answer. but it is expensive in two ways: one is model tokens, latency, money and the other is human attention. babysitting time. re-explaining the same context. noticing the same failure mode again. reconstructing the map of a project every time you come back to it.

i have written before about LMs as maps. useful maps, dangerous maps, maps that smooth the territory and sometimes substitute for it. PEEK adds a useful wrinkle: the map does not have to live only inside the model (who said it did?). it can be external, inspectable and editable. a small artifact about a specific territory[^1]. the version of the map i worry about is the hidden one, the chat history that feels like understanding but cannot easily be audited. an external context map carries the same risks of distortion and staleness, but at least you can read it, notice that it is wrong, and update it. the "living AGENTS.md" framing is pretty close: a compact orientation document for a recurring context. what should an agent know before working here again?

PEEK only tests this against constant context: a fixed corpus with repeated tasks. my situation is different, and it is the part i actually want to write about. my [second brain](https://sparsethought.com/2026/04/23/second-brain-start/) accumulates hundreds of memories per project, and the agents reading it kept arriving without a picture of the current lay of the land. so for the past couple of weeks i have been running (mostly) their original [implementation](https://github.com/zhuohangu/peek) on top of it. here the territory is the opposite of "constant" by nature: the project changes under the map, and the trail is part of the territory. the map has to capture what changed vs what still holds, and where the dangerous assumptions are. memory stores traces: facts, decisions, corrections, things that went wrong and the context map tries to turn those traces into orientation.

the setup so far: maps for four scopes. only one really lives, the work project i have been inside daily; it has accumulated about forty updates, with older entries displaced along the way to stay inside its 2k token budget, which is just the update mechanism doing its job. the other three barely moved, because the agents barely went there.

i wanted an anecdote here, a moment where the map visibly steered an agent. i do not have one, and i suspect that is sort of the point. when orientation works it is invisible: the agent just does not go down last month's dead end, does not ask me to re-explain the schema. nothing happens, which is the desired outcome and also pretty pointless as a story.

what i do have is suggestive numbers. on that active project, memory recalls that returned zero results dropped from about 73% to 45% after the map appeared, and the average number of results per recall went from 0.4 to 1.5. before either of us gets excited: over the same period this project became the thing i was working on day in and day out. its share of all recall activity roughly tripled, memory volume grew, the task mix changed. retrieval behavior improved around the same time the maps appeared, and my current logs cannot attribute the improvement to the maps. that is the honest version of the claim (and it is weaker than i would like).

update cadence turned out to be the easy part, at least so far. fully live maps are tempting, but every task has local turbulence, and if the map absorbs all of it, it stops being orientation and becomes residue. so i update at checkpoints: after a meaningful session, after a confusion resolves, after a project phase ends. a breathing map, but not one that constantly rewrites itself.

one thing PEEK does not really dwell on is layering. context is not flat. an agent enters a task through nested contexts: the user, the project, the repo or corpus, the specific question being worked on today. a single map either becomes too generic to help or too local to survive contact with the next task. the useful version probably looks more like layered AGENTS.md files: stable orientation at the top, project orientation beneath it, task orientation closest to the work, with different layers updating at different speeds. (i built the mechanism for this, per-scope maps with a global layer above them. but the project that would actually exercise the nesting is still early, so for now this stays a hunch with infrastructure.)

maybe the interesting unit is the agent together with the artifacts that let useful work persist: memory, maps, traces, evals, version history. what did we already pay to understand, and did we preserve it in a form that helps next time?

the part that is genuinely open for me is measurement. the fix is simple (and already in place!): log map reads with a session id, attach the same id to recall events, and compare sessions where a map was loaded against sessions where one was not. zero-result rate is probably the smallest useful proxy. though i am not sure which direction "better" even points. a map that works might mean fewer recalls overall, because the orientation is already in context, in which case the metric i am watching would go down for the right reason. i will know more after a few weeks of logging this properly.

[^1]: of course, the territory is different. LMs map, more or less, the world; here we are talking about one small (but arguably useful) piece of work.