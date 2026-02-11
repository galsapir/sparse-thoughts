---
layout: post
title: cognitive offloading, exoskeletons, and remaining sentient
description: "How to use AI coding tools without losing the skills and satisfaction that make programming worthwhile."
audio: "assets/audio/offloading-cognition.mp3"
---

How can someone who enjoys thinking — enjoys the cognitive load — use coding agents and LLMs to foster continued learning, and not skill degradation? And what are some useful mental frameworks to have in mind?

I think this is really about the reality we all live: the reality of coding agents and chatting with LLMs and how it affects us building (or eroding?) our skills. I always considered myself fortunate that I didn't have those tools when I was under the stress of a lot of coursework during undergrad (or grad school / PhD for that matter). Every time I wanted some sort of output, I had no choice but to learn how to make it happen. Like many things, I value it a lot more in retrospect. But eh, I mean I'm not sure anyone wants to hear about the good ol' days. This is not what we are here for.

I'm writing about this because it's a topic that has been pecking at me probably since I first tried ChatGPT way back when. It was less prominent in the past because of two things: models, and harnesses. At this point in time, the models are good enough to actually take away most of our cognitive work (if we are not careful), and the harnesses are good (or, treacherous) enough to make it almost frictionless.

## the problem, stated

The trigger for this specific piece was the recent Anthropic study on AI assistance and coding skills.[^1] The headline finding — AI assistance led to 17% lower quiz scores (50% vs 67%) — comes with important caveats: small sample size, and controlled conditions that don't fully mirror real work. But I think the researchers' thinking is more interesting than the numbers themselves, particularly how they characterized the different interaction patterns. High-scorers (65-86%) asked conceptual questions, requested explanations alongside code, used AI to check their own understanding. Low-scorers (24-39%) fully delegated, progressively relied more, debugged iteratively without understanding. The *how* matters enormously.[^2]

What I found most interesting was the "unraveling" of these patterns — the fact that you could characterize what distinguished the people who learned from those who didn't, even when both groups had access to the same tools. And this was with a sidebar assistant (i.e., not agentic tools like Claude Code). The effects are likely worse with more autonomous tools (they also note this in the discussion).

This isn't just about code: the same pattern shows up in social skills, in writing, in thinking itself.[^3] The phenomenon is general: we are outsourcing our thinking, and we don't fully understand what that means for us.

## why this interests me

I'll be honest — the reason I'm interested in this is because it scares me to "deskill". I'm using these tools all the time, and I'm preoccupied with how this affects my mind and cognition. This is also why I took the SolveIt[^4] course (which I might write more about in the future).

There's another reason, more connected to my work. I've written before about the gap between checking form and checking essence — how we can verify citations and tool calls, but struggle to know if the output actually helps the patient / user.[^5] I'm now realizing the same (or similar) problem applies to self-assessment. I can check the form of my work: Did I ship? Does it run? But I can't easily verify the essence: Do I actually understand what I built? The verification problem I face professionally is now personal (and that's uncomfortable).

## mental frameworks

Two images help me think about this.

The first is the exoskeleton. This framing "dates back" to 2024 — research on knowledge workers using GenAI.[^6] We can think of coding tools (and LLMs in general) as an exoskeleton — they grant us abilities we can't have without them. Iron Man suit. But here's the thing: it's useless to go to the gym in an Iron Man suit if what you actually want is to build muscle, and when we use these tools for work we care about, we want to be improving as well — not just producing output while our underlying capabilities atrophy. So we need to understand how we can utilize these exoskeletons in a way that doesn't degenerate us.

The second image is darker: the rat with an electrode in the nucleus accumbens. Someone on Bluesky pointed this out[^7] — the compulsive AI use where you keep entering short prompts, getting outputs, entering more prompts, caught in a loop that feels productive but yields only short-lived dopamine hits without the actual fulfillment of achieving something or gaining understanding. It kills the joy of craftsmanship, the satisfaction that comes from struggling with a problem and actually solving it yourself.

This hollowness, I've found, is actually a signal.[^8] When I offload the cognitive work needed to form a clear picture in my mind — of what is happening, of all the moving parts, of how they interact — it immediately feels more hollow, less satisfying. The satisfaction comes from understanding, and when you skip that, you feel it. Jeremy Howard and Johno Whitaker talk about this quite a bit in SolveIt — the difference between the empty productivity of rapid prompting and the deeper satisfaction of actually learning something.[^9]

The question is whether this signal stays sharp over time, or whether it dulls as the tools get better and the friction gets lower.

## what comes out of it — some practices

So what do I actually do? It starts with making a choice. Due to limited time, the choice is always phrased negatively: "what is NOT important enough for me to understand deeply?" For example, this blog was built using Jekyll, which I really didn't bother to understand. I have to mentally acknowledge — with some angst — that I don't care enough here to understand what is going on. I'm fine with this, because it clears time and mental space for things I do find important: research, core topics in my work, code I'm writing. This choice frees me in a sense.

Then, for the things I do feel are important to understand, I try a few things. One is something akin to close reading.[^10] What I try to do is actually read for myself, with concrete questions in mind, to try and form understanding — preferably in a few layers. When I feel like I've finished and written my notes on the matter, I try to critically view them, see what I've missed. I don't do this with all the text I consume, only with information-dense pieces that I want to truly *understand*.

In code, it's a lot harder to stay engaged — it's so tempting to become that rat with the NAc electrode, continuing to enter short prompts into Claude Code. One thing I try is opening prompts in a separate window (ctrl+g in CC) and actually investing time clarifying exactly what I want, because the act of articulating forces me to think. I also reread the prompt after dictating it — usually using [Handy](https://handy.computer)[^11] — which helps me input more context while stimulating my thought process. I try to actually invest time in the output I get as well, understanding why choices were made; this limits the amount of output I produce, but it means I can stand behind whatever comes out. It was nice to see these patterns emerge in the "good spots" in the Anthropic paper — the high-scorers were doing something like this.

Another practice that's been valuable is what I'd call the interview format — using AI as an interlocutor rather than a doer. It's not quite "critic" — it's more like a reviewer or even a kind of psychoanalyst (not in the "ChatGPT is your therapist!!" type of way) — someone who is present and poses questions, trying to get more out of me. The thing is, we know more than what we can say, so it helps when something prompts you to externalize more of your thought process. When I ask Claude or SolveIt to interview me about something I'm trying to understand — to probe my thinking, challenge my conclusions — I'm still doing the cognitive work, the thinking stays mine. It's different from asking Claude to write something for me and accepting the output. I've come across others doing this online; I know I'm not the only one, but it feels right and valuable.

And then there's writing itself, which might be the most important friction-creating practice I have. You can't verify your own understanding through feeling alone, but writing forces externalization — incoherence becomes visible, gaps surface, and it's harder to lie to yourself when stuff that's incoherent or implies lack of understanding is right there on the page. I can actually see it sometimes: I write something and then notice this kind of logical jump and think, wait a minute, how did you get there? Do you have enough evidence to support this claim? Maybe you missed something? This is one of the reasons I try to write more — the process itself forms understanding in ways that passive consumption or even active prompting doesn't.

## limitations and open questions

I keep thinking about Instagram Reels, about the entertainment becoming the thing itself.[^12] We can say people need to develop the ability not to sit crouched all day watching TikToks. But did most people actually develop that ability? Or did they just... adapt to a lower baseline? If that analogy holds, vigilance around cognitive offloading may be a minority practice — most people might simply offload, and the baseline of what counts as "understanding your work" will shift downward for the population as a whole.[^13]

There's also the fact that I can't really A/B test myself — the Anthropic researchers could measure comprehension decline because they had a control group and a test at the end, but I don't have that luxury. The "what have I learned" question, asking myself this daily, weekly, monthly, is my attempt at an essence check, but I'm not sure it's reliable since it requires honesty, and honesty requires structures that make self-deception visible.

And then there's the question of whether the hollowness signal recalibrates. What if it dulls over time? What if I get used to a lower baseline of satisfaction and stop noticing the gap? A year from now, would I trust that same internal signal to still be reliable?

I'm not sure there's a clean answer here. Maybe the honest thing is to sit with the uncertainty — we've built tools we can't fully evaluate, and now we're using those tools in ways we can't fully evaluate either. The epistemic uncertainty compounds.

---

[^1]: [How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills), Anthropic, Jan 2026.
[^2]: This isn't meant to be a comprehensive summary of the research — the paper itself is worth reading in full. I'm focusing on the aspects that stuck with me.
[^3]: See for example the NYT piece on AI and social skills: [link](https://www.nytimes.com/2026/01/30/opinion/ai-social-skills-relationships.html).
[^4]: [SolveIt](https://solve.it.com) — Jeremy Howard's course on AI-assisted learning that emphasizes understanding over output.
[^5]: I wrote about this in [how we actually evaluate agents (health)](https://galsapir.github.io/sparse-thoughts/2026/01/29/evaluating-agents-in-health/).
[^6]: [GenAI as an Exoskeleton: Experimental Evidence on Knowledge Workers Using GenAI on New Skills](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4944588), Wiles et al.
[^7]: [This Bluesky post](https://bsky.app/profile/catblanketflower.yuwakisa.com/post/3mdubzm2e4k2s).
[^8]: This felt like a bit of a eureka moment when I first noticed it — the hollowness itself as information about whether I'm actually engaging with the work.
[^9]: Jeremy Howard's SolveIt course emphasizes this distinction repeatedly — the difference between getting an answer and building understanding.
[^10]: See the [UCalgary guide on close reading](https://ullyot.ucalgaryblogs.ca/teaching/close-reading/).
[^11]: [Handy](https://handy.computer) is a tool I use for voice input — great for getting more context into prompts while keeping the thinking active.
[^12]: I wrote about this previously: [the entertainment is instagram reels](https://galsapir.github.io/sparse-thoughts/2026/01/26/entertainment-instagram-reels/).
[^13]: I hope I'm wrong here, but I suspect not.