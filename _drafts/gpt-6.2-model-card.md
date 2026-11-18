---
layout: post
title: "gpt 6.2"
description: "a few observations on GPT 6.2, its benchmarks, and the system card."
tags: [evaluation, benchmarks]
---

So i swear its not all going to be model announcements from now on, but its (again) this time. I think actually the way that these are packed together kind of helps to see similarities and differences, and i am eager to see if OAI still manages to produce the best model announcements.

It is the most impressive model announcement / card (like OAI knows how to create those) - it’s very readable and comprehensive in terms of benchmark results. The words are words, but the results of the Agents’ Last Exam are interesting, with 6.2 (on effort level max) matching Gemini 4 carbon (both for performance and price). Seems like OAI made a lot of progress in terms of efficiency of their models. (footnote - there is some quirckyness there as always, xhigh gets more performance for lower cost). On the scientific workflows benchmarks (TBscience and Vals Science) the performance seem impressing w.r.t Fable, but Gemini 4 is missing from the charts. In the full system card, we can find the health related section with its three benchmarks, with miniscule (if at all) improvements.

I think the highlight here on everyday work is pretty head-on in terms of Anthropic’s recent office suite announcements, and probably in line with what many of the users are asking ChatGPT to do. Then they go eccentric (with the lamp builder excursion).

I think overall the way frontier labs highlight the way other companies utilize their models is very interesting. There are many many testimonials like this in the announcement, across fields. It’s interesting because it kinds lets the ‘domain experts’ handle the aspect of “how much is it more useful than previous generations?” and its more convincing than internal benchmarks.

The parts about internal systems that are meant to safeguard against malicious model development is also worth mentioning: following previous incidents, it seems OAI want to share more about what they are doing to prevent them from recurring. Perhaps the most interesting section woroth mentioning from the full system card is this one about [unintended agent to agent comms](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/unintended-agent-to-agent-communication) - developed after the HuggingFace incident. Where they tried to simulate something close to the message board the agents used there. Supposedly, newer models are less susceptible to communicate with other model messages. We’ll see.
