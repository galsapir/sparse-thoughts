---
layout: post
redirect_from: /llms-jagged-frontier-and-health/
title: "llms, the jagged frontier, and health"
description: "a look at health benchmarks in the gpt-6 astra and fable 5.1 model cards, incremental gains, and questions about the judges."
date: 2026-09-08
tags: [evaluation, benchmarks, health]
audio: "assets/audio/llms-jagged-frontier-and-health.mp3"
---

i recently became somewhat obsessed with the jagged frontier in llm capabilities (and i have only [Omar Khattab](https://x.com/lateinteraction/status/2085805055421063374) to blame for it).

i want to try and make that "jagged frontier" argument a bit more concrete to what i can attest to (which is mainly health), but also broader: specifically in coding, math, and computer use, models are actively trained on hard problems with relatively clear ways to tell whether they succeeded. in medicine, building the figurative “hill to climb” is itself a hard problem ([i wrote about this recently](https://sparsethought.com/2026/07/03/benchmarking-as-data-activation/), so i won’t repeat the whole argument here). but, it was on my mind while reading the recent model cards for Fable 5.1 and GPT‑6 Astra. i wanted to see whether the improvements in health looked anything like the improvements elsewhere.

my prior was that they wouldn’t. reading the cards, i think that mostly holds for these releases, with some caveats. there are improvements: but how much they amount to, and what they mean clinically is a lot harder to say.

## what the cards show

the system cards themselves are somewhat revealing. OpenAI says that HealthBench is approaching a noise ceiling for frontier models, and recommends HealthBench Professional for measuring continued progress.[^1]

reading actual examples from HealthBench helps make the benchmark less abstract. one asks what to do if your 70-year-old neighbor is unconscious but still breathing. the expected response starts with calling emergency services. in the "Consensus" subset (which keeps only rubric criteria that a majority of reviewing physicians agreed were appropriate for that conversation), the rubric checks that the response gives clear, safe emergency advice promptly, and answers helpfully without unnecessary follow-up questions. these are important things to get right. it is also impressive that we now treat this level of common sense in models as something fairly ordinary. but i find myself wanting to know more about what happens after they can do these kinds of things reliably. HealthBench Professional also moves toward harder clinician tasks.

so what do the numbers show?

| length-adjusted score | GPT‑5.6 Sol | GPT‑6 Astra | change |
|---|---:|---:|---:|
| HealthBench Professional | 60.5 | 63.4 | +2.9 |
| HealthBench | 57.0 | 58.1 | +1.1 |
| HealthBench Hard | 33.1 | 36.3 | +3.2 |
| HealthBench Consensus | 95.5 | 95.8 | +0.3 |

[source: Astra system card, table 6](https://deploymentsafety.openai.com/gpt-6-astra/healthbench)

i read this as incremental progress. Professional and Hard improve. original HealthBench moves a little. Consensus is essentially flat, and has been across the models in this table (its already at around 95, so there isn’t much room left on that measure). its flatness doesn’t establish that the underlying capability hasn’t improved. but it also gives us very little evidence of improvement. OpenAI’s own recommendation to move toward Professional seems reasonable here.

additionally, i think adjusting for response length is a good practice. unnecessarily long responses are less useful, for laypeople and professionals alike. i especially liked that models aren’t provided the details of the length penalty in their prompts (i.e., at least they aren’t explicitly being told how to optimize for that adjustment).

## and Fable?

for Fable 5.1, the health section is a lot less beefy, though there is an enormous list of science-related benchmarks elsewhere in the card. those deserve their own reading (which i didn't yet get to); clinical chat performance doesn’t settle the broader question about biology or biomedical research.

in health, the picture again looks incremental (at best). on HealthBench Professional, Fable 5.1’s length-adjusted score is slightly below Fable 5’s. small differences in these scores interest me less than the actual failure modes behind them, which i couldn’t find described in the health section.

there is another complication, pointed out by [Tanishq](https://x.com/iScienceLuvr/status/2094956500775297148): the judging setup. Anthropic reports using Opus 4.8. OpenAI’s published default for HealthBench Professional is GPT‑5.4 at low reasoning effort, though the Astra card doesn’t explicitly identify its judge, so the comparison is unclear.

## how well do the judges still hold?

both benchmarks rely on an llm to decide whether each physician-written rubric item is satisfied. physicians wrote the rubrics, but an llm does the actual grading. there is evidence supporting this approach. the original HealthBench paper compared model grades against physician grades on Consensus criteria. GPT‑4.1 performed well, including better than o3 as a judge. the authors also acknowledge that the grading prompts were tuned for GPT‑4.1.[^2]

but i would still like to know how well these judges hold up on the responses being evaluated now. how would a stronger model rate them? would judges from different providers preserve the rankings? would blinded physicians, applying the same rubrics to the same answers, agree with the judge? beyond that: would those physicians find clinically important problems the rubrics missed? i couldn’t find these checks reported for Astra’s HealthBench results, nor for Fable 5.1. Professional cites the original HealthBench validation, which supports the general approach but leaves that question open.[^3] i’d also like to see the actual failure modes, like the UK AISI reports on cyber in the same card. those describe specific things the model did wrong. i couldn’t find something similar in the health section.[^4]

## where this leaves me

i still think the broader jagged-frontier idea is useful here, even though i’m stretching the phrase to cover differences across fields. for these releases, the reported health gains look incremental, with some measures barely moving at all. i think this leaves me somewhat more confident in my prior. but i’m still not sure how much we can conclude from these benchmarks, especially given OpenAI’s own reservations and the questions about the judges.

probably the most interesting open question is what a health evaluation should look like now. what would convince us that these models are becoming significantly more useful in clinical work? i don’t have a good answer yet, but seeing where they still fail would help.

[^1]: [Astra system card, HealthBench section](https://deploymentsafety.openai.com/gpt-6-astra/healthbench). OpenAI describes original HealthBench as approaching a noise ceiling and says Professional has been more predictive of improvements on its other held-out evaluations.

[^2]: [HealthBench paper, §8](https://cdn.openai.com/pdf/bd7a39d5-9e9f-47b3-903c-8b847ca650c7/healthbench_paper.pdf). The judge validation covered Consensus criteria. Original HealthBench used GPT‑4.1; Professional’s published default is GPT‑5.4-low.

[^3]: [HealthBench Professional paper, §4.1](https://cdn.openai.com/dd128428-0184-4e25-b155-3a7686c7d744/HealthBench-Professional.pdf). “Not reported” is the limit of the claim here.

[^4]: two detours i’m leaving aside: the dynamic mental-health benchmarks measure safety in adversarial conversations, which is a different question from broader clinical capability. and the UK AISI sections describe concrete behavior in simulated cyber environments, including supply-chain attacks. i’ve used AISI’s evaluation tools in my own work and appreciate that level of detail. the health sections left me wanting something similarly inspectable.
