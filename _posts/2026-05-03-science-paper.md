---
layout: post
redirect_from: /science-paper/
title: "on the comparator in clinical AI"
description: "A 2024 finding in 2026, a buried result the paper doesn't engage with, and the wrong comparator: on Brodeur et al.'s Science paper."
tags: [health, evaluation]
audio: "assets/audio/science-paper.mp3"
---

a paper from [Brodeur et al. (2026)](https://www.science.org/doi/10.1126/science.adz4433) has been making the rounds the past few days.[^1] the framing it's traveling with is "OpenAI's o1 correctly diagnosed 78.3% of cases in NEJM clinicopathologic conferences, outperforming human physicians." it didn't click for me when i first saw it, and after sitting with it for a day i think i can articulate why, from the perspective of a (ex)physician and researcher. let me get this out of the way first: it's a thorough piece of work, and my issue isn't with the methods.

## what they did

the paper reports six experiments. five use curated clinical case vignettes: NEJM clinicopathological conferences (CPCs) for differential diagnosis and test selection, NEJM Healer cases for documenting clinical reasoning, Grey Matters cases for management reasoning, a set of landmark diagnostic cases from a 1994 study, and probabilistic reasoning cases on primary care topics. the sixth uses 76 real emergency department cases from BIDMC, with model and physician differential diagnoses scored at three touchpoints (initial triage, ER physician evaluation, admission to floor or ICU). across the experiments, OpenAI's o1-preview is compared against GPT-4 and against physician baselines drawn from prior published studies, hundreds of physicians in total. blinding in the ED arm was robust: the two scoring physicians correctly identified AI versus human only 15.2% and 3.1% of the time. the headline result is that o1-preview meets or beats both GPT-4 and physician baselines on most tasks, with the largest gaps where information is sparsest (initial ER triage).

## the central finding stopped being interesting around 2024

an arxiv preprint of essentially this work was up in december 2024.[^2] in 2026, with chatgpt for health, openevidence, claude in the clinic, and ambient scribes becoming standard, telling me an LLM beats a physician on a CPC is something close to telling me it beat a human at chess: it's the water we all live in. according to the AMA's 2026 survey, 81% of US physicians now report using AI in some form in their practice, up from 38% in 2023 and 66% in 2024.[^3] saying "the model outperforms physicians on curated cases" with rigor doesn't make it interesting at this stage. the comparator that matters in 2026 is not the unaided physician, because the unaided physician is increasingly a hypothetical.

this is a long way of saying that the result framed as the paper's headline is a 2024 finding that landed in 2026. what would have been interesting is the result the paper itself underplays.

## the buried finding

on the Grey Matters management cases, physicians using GPT-4 scored a median of 41% (IQR 31 to 54). GPT-4 alone scored 42% (IQR 33 to 52). physicians without any model scored 34% (IQR 23 to 48). on the landmark diagnostic cases, physicians with GPT-4 scored a median of 76%, physicians with conventional resources 74%, GPT-4 alone 92%. the model alone outperformed the model plus physician. physicians given the tool barely outperformed physicians without it.

the paper reports these numbers and doesn't engage with why. that "why" is the most interesting question the paper raises, and it gets a sentence. either the 2024 finding still generalizes, in which case the question worth asking is what's happening between physicians and these tools that erases the model's advantage. or it no longer generalizes, in which case the headline result is also dated: the comparator isn't the unaided physician anymore, it's the physician with the tool. either way the buried finding deserves the foreground. the accompanying Perspective by Hopkins and Cornelisse, in the same issue of Science, foregrounds it where the paper doesn't, citing the same effect from earlier work and writing that the collaborative configuration "itself must be tested."[^4]

## clinical vignettes are pretty bad maps for the territory

the harder thing to say, and i'll try to say it without dunking on the methods, because you have to compare against something: a CPC, an NEJM Healer case, a USMLE question, all of these are artifacts where the messy work of clinical medicine has already been done. someone took a real patient and a real chart and a real history that didn't quite hang together, and they did the curation: pulled out the relevant labs, summarized the timeline, decided which of the patient's seven complaints mattered for this question. by the time you have a vignette, the answer is almost downstream of the curation, and most of the value a good physician adds is upstream of where the vignette starts.

the ED arm is the most honest part of the paper for this reason: they at least try to use unstructured data from real patients. but even there, the AI and the comparator physicians get the same pre-extracted information at three predefined touchpoints. the curation step, where a clinician at triage figures out which of the eight things a patient is reporting is the actual presenting concern and which lab value is going to matter in three hours, is invisible. i don't think this is a fixable problem with vignette-based benchmarking. the authors themselves note in the discussion that benchmarks rely on the careful work of clinicians to "clean up" cases and may overstate AI performance on messier data. that's the right footnote in the wrong paper.

## what would have been worth asking

two questions, since the paper invites them.

what do physicians actually delegate to AI systems in 2026, and what do they keep? when i talk to colleagues, the answer is overwhelmingly "documentation, summarization, the boring parts." very few are using these tools as differential generators in the way the paper measures. so what does 78.3% top-k accuracy on a CPC tell us about a workflow that essentially nobody is running?

what are the new failure modes of the physician plus AI duo? this is where i think the next stretch of clinical AI research lives. the buried finding above hints at one, something about the joint system performs worse than either component, and we don't know what. is it overreliance, is it anchoring on the model's first suggestion, is it deskilling on the tasks the model handles, is it something else entirely? a properly powered study of that question, ideally on real workflows with ambient AI in the loop, would be worth a Science paper.[^5]

## why it matters where this was published

if this had appeared in JAMA or NEJM AI, i'd shrug and move on. medical journals publish a lot of work that's mostly a sanity check on what clinicians already suspect, and that's fine. Science is read by people outside medicine. when a CS researcher, a physicist, or a policy person sees "performance of a large language model on the reasoning tasks of a physician" in Science in 2026, they read it as: this is the state of the art, this is where the field is. and the field has moved. ambient scribes are becoming standard. physicians are figuring out, sometimes well and sometimes badly, how to integrate these tools into real workflows. the interesting questions have shifted from "can the model do it" to "what happens when the model and the human do it together, in a real workflow, with messy data and time pressure and liability." a Science-level platform at this moment, ideally from these same authors who have done a lot of foundational work in the area, could have been a reflection on where the field is now. instead it's a thorough answer to a 2024 question, and the accompanying Perspective is doing more of the 2026 work than the paper itself.

i don't think this is a bad paper. it's a careful one, and the methodological choices are defensible inside the frame the authors chose. it's just that the frame itself was set in 2024, and it shows.

---

[^1]: Brodeur et al., "Performance of a large language model on the reasoning tasks of a physician," *Science* 392 (2026), DOI: 10.1126/science.adz4433. strictly, 78.3% is the rate at which o1-preview included the correct diagnosis somewhere in its differential. top-1 accuracy was 52%; including potentially helpful or very close diagnoses brings the figure to 97.9%.

[^2]: arxiv:2412.10849, december 2024. same work; the preprint was titled "Superhuman performance of a large language model on the reasoning tasks of a physician", with "Superhuman" dropped for the Science version.

[^3]: AMA 2026 Augmented Intelligence Research survey: 81% of physicians report using AI professionally, with documentation and research summarization the most common use cases. ([source](https://www.ama-assn.org/practice-management/digital-health/more-80-physicians-use-ai-professionally-ama-survey)) notably, 88% expressed some level of concern about AI-driven skill loss, which is the question the buried finding in this paper actually speaks to.

[^4]: Hopkins and Cornelisse, "AI can reason like a physician — what comes next?", *Science* 392 (2026), DOI: 10.1126/science.aeg8766. they cite Goh et al. (Nat Med 2025) on the physicians-with-GPT-4 effect and write that "determining the optimal implementation will likely require an evaluation that compares AI alone, clinician alone, and clinician with AI."

[^5]: there's a related thread i'm leaving for another post: how the work of medicine reorganizes around these tools, which tasks get unbundled, where liability lives, who supervises what. abbott's *system of professions* is the right starting point. a benchmark score is orthogonal to all of it.