---
layout: post
redirect_from: /curation-all-the-way-down/
title: "curation all the way down: on clinical AI benchmarks"
description: "the curation regression, the openness trade-off, and what a substrate worth evaluating against would actually need: on Medmarks."
date: 2026-05-16
tags: [health, evaluation]
audio: "assets/audio/curation-all-the-way-down.mp3"
---

[medmarks v1.0](https://arxiv.org/abs/2605.01417) dropped last week from the medARC group and got real attention, deservedly. it's the largest fully open medical LLM eval suite to date: 30 benchmarks across a verifiable subset (Medmarks-V) and an open-ended LLM-as-a-judge subset (Medmarks-OE), 61 models on 71 configurations. eight of the benchmarks (collectively Medmarks-T) ship with train/test splits as [verifiers](https://github.com/PrimeIntellect-ai/verifiers) environments, which means they're directly usable as RL substrate for post-training. the verifiers framing is the right abstraction at the right moment, and the breadth of model coverage is real work that someone needed to do. nothing that follows is meant as a dismissal.

what it pulled out of me is a thread that started with the [Brodeur et al. science paper](https://sparsethought.com/2026/05/03/science-paper/) and hasn't resolved (the [eLetter](https://bsky.app/profile/sapir.bsky.social/post/3mlvtuxm6tk2a) did get published, which was nice).

## the curation regression

the argument i made about Brodeur was that a CPC vignette is a bad map for clinical territory because most of the work a good physician does sits upstream of the vignette. someone with clinical expertise has already pulled out the relevant labs, summarized the timeline, decided which of the patient's four complaints mattered for this question. by the time you have a vignette, the answer is almost downstream of the curation, and most of the value a clinician adds is upstream of where the vignette starts.

sitting with medmarks for a few days, what's clearer to me is that this isn't a property of vignettes. it's a property of the "substrate", and the substrate goes all the way down.

USMLE-style MCQs are curated, obviously. so are clinical case reports, NEJM healer cases, CPCs. but EHR notes are also curated, by clinicians who already know what they're doing, increasingly with clinical AI in the loop themselves. ambient AI recordings of an ED encounter are curated too: they capture a physician already asking the right questions, ordering the right tests, doing the right physical exam. the curation step isn't a property of the dataset format. it's a property of the data being produced by someone who already metabolized the messy reality before it hit any recording surface.

so where does the regression stop? where is the "raw enough" substrate? i don't fully know, but a few candidates are worth naming.

patient-direct interaction with these systems, in the wild. r/AskDocs has been [studied this way](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2804309), [chatgpt-for-health](https://openai.com/index/introducing-chatgpt-health/) usage is happening at scale, openevidence has direct-to-patient surface area. patients describing symptoms in their own words, before any clinician has touched the encounter, is the closest thing to raw input that exists at scale today. it's messy and has obvious selection biases. and patients still curate themselves before any model sees them, narrowing complaints, ordering symptoms, deciding what's worth typing. the curation step hasn't disappeared, it's just moved upstream of the encounter. but (and that's important) it's also the only setting where what's left of it is visibly the model's problem rather than someone else's.

prospective phenotyping cohorts. UK Biobank, All of Us, the [Human Phenotype Project](https://humanphenotypeproject.org)[^1]. these have a property worth flagging separately from the curation argument: they sample the spectrum between health and disease, not just the disease end. they have their own selection biases, obviously: people who agree to a multi-decade multi-omic study skew healthier, more educated, and more compliant than the general population, so the spectrum they sample isn't the population spectrum either. EHR-derived training data is overwhelmingly biased toward disease states, because EHRs exist to document encounters with the healthcare system, which mostly happen after something has gone wrong. the transition zone, the slow drift from baseline into pathology, is barely documented in any corpus currently used to train or evaluate clinical AI. that's a substantive gap in the map, not just a question of how the map was drawn. it's also where i think much of the next several years of work lives, even if cohorts aren't the whole answer.

closed-loop simulators. simulated patients with known ground-truth pathophysiology, where the model does the curation work itself. these exist in early forms (medmarks includes AgentClinic and MedR-Bench), but they don't yet ground out in real biology in a way i find convincing. worth watching.

## the second problem: openness

the other thing medmarks foregrounds for me is contamination.

a benchmark that is fully open and published with its data gets trained on by the next generation of models. this is well understood; medmarks itself sits inside the saturation curve it's documenting, and MultiMedQA is the cautionary tale they cite in their own intro.

making a benchmark also serve as an RL training environment, as medmarks does with the Medmarks-T subset, sharpens this tension rather than resolving it. the point of a verifiers environment with a reward function is that you can post-train against it directly. but a benchmark you can post-train against is, by construction, a benchmark whose signal degrades with every model release that trains on it. you're not measuring a capability so much as how recently someone optimized against your reward function.

this isn't a knock on the choice to build verifiers environments, which is (i think) the right abstraction. it's a knock on the implicit assumption that "fully open" is an unalloyed good for evaluation. [MedHELM](https://arxiv.org/abs/2505.23802) made the opposite call, restricting much of its data, and gets criticized for replicability. but a benchmark that survives more than one or two model release cycles probably has to be at least partly closed. the field doesn't have a good answer for this trade-off yet, and "fully open" is currently winning by default rather than by argument.

## what would i actually want

a substrate i'd find convincing would have to do three things at once.

it would have to include enough rawness that the curation step itself is part of what gets evaluated. not "given this neat case vignette, what's the differential?" but something closer to "given this stream of unstructured patient input over time, decide what to ask next, what to examine, what to order, when to escalate."

it would have to cover the health-disease spectrum, not just disease states. prospective cohort data is the only substrate i currently know of that does this at scale, which is most of the reason i find that direction interesting and not only because i happen to work on one.

and it would have to be closed enough to survive. some form of held-out evaluation, gated access, or controlled release that doesn't collapse the moment the artifact is published. i.e., saturation as a feature of openness has to be priced in.

i don't have a worked proposal here, and i'm aware that "ethically hard to study" is a boring stopping point for the unmediated-interaction direction. the honest version is that none of the existing substrates do all three things, and most don't do any. medmarks does excellent curation work on the materials we have. the question i'm left with after reading it is whether the materials we have are the materials we need.

---

[^1]: where i work. flagging the obvious bias in saying that prospective cohort data is interesting.