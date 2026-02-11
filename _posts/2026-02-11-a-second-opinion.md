---
layout: post
title: "a second opinion"
date: 2026-02-11
description: "Building a Claude Code skill that gets a second opinion from a different model family — and what the first real test revealed about what AI review can and can't catch."
---

I've been noticing something about how I work with Claude. It's not dramatic — no moment where the model led me off a cliff and I realized too late. It's more of a drift. The models have gotten good enough that my default reaction to most outputs is "yeah, that's probably right." And most of the time it is. But "most of the time" is doing a lot of work in that sentence.

The issue isn't that I'm getting burned. It's that I've stopped checking. For high-stakes things — a spec, a significant architectural decision — I still verify. But the threshold for what counts as "high-stakes" keeps creeping upward, because the models keep being right enough to justify the creep. It's the same slow drift I wrote about before,[^1] just showing up in a new way: not as skill degradation from outsourcing the thinking, but as a quiet erosion of the habit of questioning the output.

I also wanted an excuse to try the OpenAI Codex models — I've been hearing good things and was curious about the intelligence, what they catch, what they care about — but didn't want to significantly change my day-to-day workflow to do it.[^2] So I built a Claude Code skill that lets me get a second opinion from a different model at distinct checkpoints — moments where the stakes feel high enough that I want extra confidence before moving on.

## what it is

It's called `adversarial-review`. You point it at a file, a diff, a spec, a GitHub issue, and it sends the thing to a different model for a second opinion. One extra call, not an elaborate multi-agent consensus protocol where three models argue for dozens of thousands of tokens until they converge. Just: here's what I'm working on, what does a different set of weights think about it?

It supports a few backends — Codex (OpenAI's GPT family), `claude -p` (a separate Claude instance with fresh context), and AWS Bedrock. The most interesting case is Codex, because it's a genuinely different model family. When GPT and Claude agree on a finding, that convergence means more than either model flagging it alone. When they disagree, that's interesting too.

The prompt template asks the reviewer to steelman first — articulate the author's intent before critiquing — and requires concrete impact for every finding ("what actually breaks or degrades?", not "best practice says..."). Each finding gets a severity and confidence rating, and I specifically wanted the confidence rating because LOW confidence is honest uncertainty, which is more useful than false authority. The output ends with a verdict: SHIP, ITERATE, or RETHINK.

The skill and the prompt template are [here](https://github.com/galsapir/claude-skills) if anyone wants to look or use them — they already include the improvements I describe below.

## the recursive first test

The first thing I actually tested it on was the skill itself. I sent the Bedrock wrapper script to Codex for review, and the review came back with real findings — no error handling around the boto3 calls, no file I/O error handling, hardcoded token limits. Both Codex and Claude agreed on the high-severity items (which was a useful signal in itself).

But then I looked at the skill more broadly and realized the whole thing didn't follow Anthropic's own [skill-creator guidelines](https://github.com/anthropics/skills). The frontmatter had non-spec fields, the prompt template was in the wrong directory, the SKILL.md was overly verbose — trying to hand-hold the orchestrating model instead of trusting it. So the first review led to a significant restructuring: the SKILL.md went from 139 lines to 75, the prompt template moved to a `references/` directory where it belongs, and the frontmatter got cleaned up to match the actual spec. The tool's first review ended up improving itself.

## the real test, and what it tells us

After the self-review, I pointed it at something more substantial — a spec for replacing our health chatbot's architecture, moving from a DSPy state machine to Anthropic's Agent SDK. This is the kind of thing I'd normally want a peer engineer to look at, but the review was done by Codex with GPT-5.3.

The review came back with a verdict of ITERATE and several findings. Being honest about how it went: I'd rate it maybe a 6/10 as a review. It added one genuinely valuable finding — a security gap where the SDK's `bypassPermissions` combined with absolute file paths could expose PHI — plus a useful clarification about concurrency in the subprocess tool. It actually searched the SDK docs to verify claims rather than just pattern-matching on the spec text, and the understanding section was accurate, which builds trust in the rest.

But there was noise, too. It flagged streaming message ordering as a concern, suggesting turn IDs and sequence numbers — which makes sense for HTTP polling in a distributed system, but not for a WebSocket POC with a single user. WebSockets are ordered and reliable; the finding showed pattern-matching from a known category of concerns rather than understanding the actual transport. It also flagged subprocess capacity limits that the spec itself already acknowledged as POC-irrelevant.

More telling is what it missed entirely. The review was asked to challenge SDK API assumptions — are those import paths correct? Is `receive_response()` the actual method name? — and it searched the docs but never reported back on what it found. No comment on whether the Langfuse tracing integration would actually work. No challenge to the system prompt design, which embeds clinical safety guardrails as a raw string — is that robust? Can it be jailbroken? These are essence questions, and the review didn't touch them.

This maps almost exactly onto a distinction I've written about before.[^3] The tool can check form — structural patterns, security anti-patterns, missing error handling. It can't check essence — whether the SDK API actually works the way the spec assumes, whether the clinical guardrails are robust, whether the implementation plan ordering makes sense given the domain. The one real finding it surfaced (permissions/PHI exposure) is something any competent reviewer would catch by pattern-matching. The things it missed require actually understanding the specific SDK, the clinical context, the domain.

For zero human effort beyond invoking the command, one real finding plus one useful clarification is a positive ROI on ~46K tokens. But it's not a substitute for a peer engineer who knows the SDK. The bar isn't "is this as good as a senior engineer" — it's "is this better than not checking at all," which, given the drift I described at the top, is the actual alternative.

After the 6/10 review I went back and made targeted improvements to the skill — the kind that directly addressed why it scored poorly without bloating the prompt or touching the parts that already worked. Three things: the reviewer now has to explicitly address every focus area you give it (so it can't silently skip "challenge SDK API assumptions" anymore), the prompt is stage-aware so it calibrates severity to whether you're reviewing a POC or production code (no more distributed-systems concerns for a single-connection WebSocket), and for specs specifically it now has to verify technical claims and report back with a CONFIRMED/INCORRECT/UNVERIFIABLE status. I haven't re-run the full review yet, so I can't say whether these changes actually move the needle — that's next.

---

[^1]: I wrote about cognitive offloading and the drift toward less engagement in [cognitive offloading, exoskeletons, and remaining sentient](https://galsapir.github.io/sparse-thoughts/2026/02/03/offloading-cognition/). The interview format I mentioned there — using AI as an interlocutor rather than a doer — is the same impulse, just applied differently. The `/interview` command is about staying engaged during the thinking phase; this one is about catching things during the review phase.

[^2]: I didn't want to switch tools or start a separate workflow — I just wanted to be able to tap into a different model's perspective from within my existing setup.

[^3]: The form vs. essence gap — being able to verify citations and tool calls but struggling to assess whether the output actually helps — is something I explored in [how we actually evaluate agents (health)](https://galsapir.github.io/sparse-thoughts/2026/01/29/evaluating-agents-in-health/).