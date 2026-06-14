---
layout: post
redirect_from: /what-did-they-actually-measure/
title: "what did they actually measure?"
description: "a nature medicine paper says general llms beat specialized clinical tools: a close read of what its main benchmark actually measured, and what it left out."
date: 2026-06-14
tags: [health, evaluation]
audio: "assets/audio/what-did-they-actually-measure.mp3"
---

a nature medicine paper has been showing up in my feed recently: the one claiming general-purpose llms beat specialized clinical tools (openevidence, uptodate) on medical benchmarks.[^paper] i am having a hard time letting it go, so i want to write down why, as plainly as i can. the short version: they say they are measuring how good these systems are for medicine, and what they are actually measuring is much narrower than that.

i will only talk about their own benchmark, the "real clinical queries" (RCQ) set. the other two stages do not interest me much.[^saturated] RCQ is the part the authors call their "primary evidence" anyway, and the part that got picked up, so it is the one worth arguing with.

the headline is a head-to-head of six systems on 74 questions[^n], sampled from physicians' queries to nyu langone's internal hipaa-compliant gpt. so: things doctors (i hope!) typed into a chat box. the queries are de-identified, stripped of their context, and we never get to see them. the single example they do show is a request to "write a patient-friendly list of red flag symptoms and return precautions for back pain", which is then scored on, among other things, "clarity for clinicians".

that example does a lot of work (if you let it): it is a patient-handout task, really not the thing you use openevidence or uptodate to do. the job of a reference tool is to hand you the relevant guideline and tell you where it applies, especially when the question sits outside your own field, which is a good part of why clinicians reach for them at all. and citations, the actual surface of that job, were not evaluated. so the thing these tools exist to do is the thing the benchmark does not look at.

i wanted to show you one of the answers they marked as wrong, to make this concrete. there is not one in the paper. the only example response they print is a good one, there to illustrate the scoring screen. the errors live in a table of counts, and the data is sealed, so i cannot go and check. the primary evidence is judgments i cannot inspect, of answers i cannot read, to questions i cannot see: i imagine you see where this is going.

i guess the thing is, "general beat specialized" is not the interesting question. it assumes a single axis of competition. the question i actually care about is whether grounding, citations and auditability matter for these tasks, and whether anything here touches them. unfortunately, as far as i can tell, nothing does.

then there is the figure everyone shares (their 2c). it reads as a competence gap. but their own breakdown says the separation sits mostly in clarity, not correctness: they put the weakness down to communication rather than knowledge.[^axes] on the axis that should matter most, whether the answer is right, the gap is small and the tools are fine. so the headline, read slowly, is closer to this: 

>**clinicians from some field (we are not told which, and i am not even sure the raters are the authors, i am guessing) are handed a context-free question and answer from some other doctor in some other field, and find the chattier model easier to read.** 

i would argue the thing that looks like a deficiency for openevidence there, terse and citation-shaped instead of a skimmable essay, is closer to a feature, at least next to a generic google ai answer.

benchmarking ai for medicine is important: that is exactly why it is frustrating to watch it done this loosely and then amplified (in nature medicine, of all places). i do not have a clean benchmark to offer in return.[^repro] i keep landing on a smaller question instead.[^oe] what would [a test that actually probed the thing these tools are for](/evaluating-agents-in-health/) even look like? i do not think this one tried.

[^paper]: vishwanath et al., *general-purpose large language models outperform specialized clinical ai tools on medical benchmarks*, nature medicine (2026). doi:[10.1038/s41591-026-04431-5](https://www.nature.com/articles/s41591-026-04431-5).

[^saturated]: the other two stages are MedQA and openai's healthbench. MedQA-style items are effectively in the models' training data, and healthbench is saturated across recent gpts: useful for catching gross degradation, not for ranking frontier systems ([i have written about this before](/science-paper/)). worth noting healthbench is also graded by the same frontier models being evaluated, and gpt, built by the benchmark's author, wins it by about nine points.

[^n]: to be precise, the set is 100 queries. once refusals are dropped, the bar heights use up to about 568 model-question ratings, but the pairwise significance, the tiering that licenses "frontier beat clinical, tools tied google", is computed on the 74 questions all six systems answered. so 74 is the number sitting under the strongest claims.

[^axes]: their own numbers: models differ most on clarity (kendall's *w* about 0.29) and least on clinical correctness (about 0.14).

[^repro]: a few technical things i am leaving as footnotes rather than the point. they claim a fixed generation seed where the apis plainly ignore it, and "reproducibility" with live web search on, which makes temp=0 mostly moot. the released defaults cap output length for one model (claude) and not the others, while length was never normalized and completeness and clarity were scored anyway. and the analysis code that builds the figures is not in the released repo, while the RCQ data itself is sealed, so the primary result cannot be reproduced from what they published.

[^oe]: openevidence, one of the tools in the study, put out its own thread pulling the paper apart: contamination, healthbench's stylistic rubric, the missing held-out set. some of it lands where i do, which is worth noting and also worth discounting, since they are the vendor that came out behind and not a neutral party. their thread also leans on an undisclosed-conflict story (the authors' hospital apparently runs a competing in-house model and was turned down for api access, after which the paper "coincidentally appeared") that i cannot verify and am not leaning on here. the piece i do agree with is their closing question: the right evaluation should match the distribution of real clinical use, not a contaminated quiz or one creator's style guide. easy to say from where they are sitting, but not wrong