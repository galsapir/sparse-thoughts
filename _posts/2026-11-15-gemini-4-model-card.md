---
layout: post
redirect_from: /gemini-4-model-card/
title: "gemini 4 model card"
description: "a few observations on Gemini 4, token efficiency, and its model card."
date: 2026-11-15
tags: [evaluation, benchmarks]
audio: "assets/audio/gemini-4-model-card.mp3"
---

Gemini 4 Carbon [became broadly available this week](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/), and i like to skim the model cards and announcements to see what they can reveal.

i actually like the “elements” theme in Gemini’s model names. hydrogen is the light version (makes sense), carbon is in the big boys club, and argon? well, like the noble gas, it doesn’t like to mingle: Google first released it to Fairwind for cyber work, including an “argon cyber permissive” version. carbon came afterward and represents an improvement. right now, argon seems positioned as the middle tier between hydrogen and carbon, at least in terms of its intended role.[^tiers]

the flag Gemini models keep waving seems to be token efficiency / budget. this seems especially true for the larger models (see the comparison with Fable below), though hydrogen’s token prices are higher than Haiku’s.[^pricing] getting a clear picture of the release takes some work, though. Google likes to mix IDE/harness features (like “/swarm”) with model features. the [actual model card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Carbon-Model-Card.pdf) is very, very thin, while the press announcement is pretty, ah, a mixed bag, i suppose you could call it.

on benchmarks, they partnered with Artificial Analysis to create [MKA, the multimodal knowledge agent benchmark](https://artificialanalysis.ai/evaluations/mka). this seems like a place where that efficiency shows: performance basically on par with Anthropic’s models, at much lower cost. in the chart, the highest Gemini cost is about $4, compared with about $32 for Fable.

![MKA Climb WSR scores: Claude Fable 5.2 at 57%, Gemini 4 Carbon at 54%, Claude Opus 5.5 at 53%, Claude Sonnet 5.5 at 52%, and Gemini 4 Argon at 51%.](/assets/images/gemini-4/mka.png)

the evidence around scientific reasoning seems less strong. we get a sort of “testimonial” from [Axiom Bio](https://www.axi.om/), but i didn’t find much else.

on prompt injection, they seem to be leading the charts. to be honest, this is the first time i’ve seen this specific benchmark, so i don’t have much context for it. at least on this one, they lead the pack.

![Gray Swan IPI prompt injection benchmark at k = 15. Gemini 4 Carbon has a reported attack success rate of 0%, followed by Gemini 4 Argon at 0.7%. Lower is better.](/assets/images/gemini-4/prompt-injection.png)

and it’s always nice to see big companies send small winks. the [pelican quest video](https://www.youtube.com/watch?v=dNbkThtNzS8) is a funny little example.

overall, it seems like the teams there have been doing solid work lately. i might get a chance to test these models properly on our own tasks. the gaps between frontier models feel pretty narrow these days, but maybe this particular flavor will turn out to be interesting. not sure yet.

[^tiers]: this isn’t a clean performance ranking. [Google reports](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) that hydrogen scores above argon on the Artificial Analysis Intelligence Index, while positioning hydrogen for fast execution and argon and carbon for deeper reasoning.

[^pricing]: as of November 15, standard API prices per million input/output tokens are [$1.50/$7.50 for hydrogen](https://aistudio.google.com/docs/pricing) and [$0.10/$0.50 for Haiku 5.5](https://www.anthropic.com/claude/haiku) for prompts up to 100K tokens ($0.50/$2.50 above 100K). token prices alone don’t tell us the cost of completing a task.
