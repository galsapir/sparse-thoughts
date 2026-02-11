---
layout: post
title: data activation thoughts
description: "How to transform structured medical data into reasoning traces that improve LLM clinical performance—patient similarity and contrastive approaches."
audio: "assets/audio/data_activation.mp3"
---

The landscape is shifting in recent years — it's a cliche to start texts like this these days, but the fact that it's a cliche doesn't make it any less true.[^1] In 2019, the folks at Andreessen Horowitz wrote this about data (in a piece titled [The Empty Promise of Data Moats](https://a16z.com/the-empty-promise-of-data-moats/)): "Instead of getting stronger, the defensible moat erodes as the data corpus grows and the competition races to catch up." (Trying to prove some data has value — I've experienced it firsthand.)

LLMs have shifted where value comes from. It's no longer enough to simply have proprietary data; what matters now is how effectively you can make that data useful to these systems (and therefore, to anything else that lives off that). So, if traditional data moats are eroding, the new competitive edge lies in data **activation**. The pressing question becomes: **how quickly can you connect your proprietary data to LLMs in ways that demonstrably improve their performance** (before someone else figures out how to replicate your insights without your data)?

Before we continue I want to think about a simple metaphor here — LLMs can *ingest* the data. They'll happily consume every row and column you throw at them. But (and this is important) without the right transformation, they can't *metabolize* it. The nutritional value passes through unabsorbed. They're missing the "enzymes" I guess you can call it. Data activation is about providing those enzymes: converting raw information into a form the model can actually digest and turn into a **capability**.

<!--more-->

## Why this matters now (healthcare as case study)

Looking specifically at healthcare data, the opportunity is immense — and let's face it, time limited. Looking at OpenAI's [report](https://cdn.openai.com/pdf/2cb29276-68cd-4ec6-a5f4-c01c5e7a36e9/OpenAI-AI-as-a-Healthcare-Ally-Jan-2026.pdf) from January 2026: more than 5% of all ChatGPT messages globally are healthcare-related. 25% of weekly active users ask health-related questions. More than 40 million people turn to ChatGPT **daily** for healthcare guidance (!!!).

The big labs are clearly taking notice: within the span of a single week (January 2026), OpenAI launched "ChatGPT for Healthcare" (already rolling out to institutions like Cedars-Sinai, Memorial Sloan Kettering, and Stanford Medicine) and Anthropic announced "Claude for Healthcare" with HIPAA-ready infrastructure and native integrations to medical databases/ontologies (CMS Coverage Database, ICD-10, PubMed). To me, it looks like healthcare is now a primary battleground for frontier AI companies.[^2]

Yet, if you look at the numbers from OpenRouter, they claim that health remains "[the most fragmented of the top categories](https://openrouter.ai/state-of-ai)". What does this mean? According to OpenRouter, it signals both the domain's complexity and the inadequacy of current general-purpose models.

## One (potential) method for data activation

It seems that recent research already demonstrates that the bridge between structured medical data and improvements in LLM reasoning is working.

[Tables2Traces](https://openreview.net/forum?id=cqNAjXUBOV) established a framework for converting raw, tabular patient-level data into contrastive reasoning traces that can be used for LLM fine-tuning. They tried to "mirror how a clinician would think" — what they did is pretty simple. For every patient record, they identified similar patients with different outcomes (someone similar who died and someone similar who survived). Once they had those triplets of patients they prompted a strong LLM to generate explanations for the divergence. These reasoning traces become fine-tuning data for smaller models.

For their specific use-case they showed significant improvement (>17% in domain-specific MedQA and even generalization capabilities — they trained only on cardiovascular cases but noted improvement in other areas of medicine as well). The paper's "simple vs. full" comparison also provides empirical evidence: naively converting tables to patient narratives doesn't work (and can hurt performance). So the models actually need the structured reasoning scaffold — the contrastive comparison, together with the reasoning and quasi-counterfactual thinking, is what makes the difference.

**Saying it a bit differently** — they kind of show that the value in structured medical data is like potential energy trapped behind a dam. The power is real, but it just sits there. Naive table-to-text conversion doesn't work; you're essentially drilling a small hole in the dam and expecting electricity. The reasoning scaffold (in their case — contrastive comparison, counterfactual thinking) is the turbine. It converts stored potential into usable power.

Another work worth mentioning is [EHR-R1](https://arxiv.org/abs/2510.25628v2). They synthesized 300k "high-quality" traces using a different method — something they call a "thinking-graph pipeline": [1] extract medical entities from each patient's longitudinal EHR (including free-text), [2] quantify associations between medical entities, then [3] map entities to medical ontology ([UMLS concepts](https://www.nlm.nih.gov/research/umls/index.html)) and use graph search to recover medical relations that connect context entities to the target labels. They then prompted an LLM with the patient record plus these retrieved relations to produce a structured reasoning chain, which became the supervision data. The results? Their model outperforms strong commercial/open models, averaging >30 points over GPT-4o on EHR-Bench (which they also created).

Another [paper](https://www.nature.com/articles/s41746-025-01681-4) shows this scales pretty well: fine-tuned 8B parameter models have achieved 89.3% accuracy while being 85x cheaper than their 70B teacher models.

So I think the existence proof is established: structured EHR/biobank data can be transformed into reasoning supervision that measurably improves LLM clinical performance.

## What's still unclear

I think Tables2Traces proved feasibility in some sense, but synthetic traces are still in the "unverified" realm. This gap showed mostly in the way physicians treated those traces (mostly, they didn't think the traces were very good). And there's a deeper issue — [recent work](https://arxiv.org/abs/2509.21933) shows that traces can sometimes be "unfaithful," meaning they don't accurately reflect the actual basis for a decision. Plainly: the trace says one thing, the model's decision is different.

It's also worth noting that these papers tend to show improvements on less capable models. That's not an accident — showing improvements on stronger models is harder (or the improvements aren't there). We should be honest about that.

So the question that keeps bothering me: what's the right transformation? The papers above offer some approaches — contrastive reasoning, knowledge graphs, ontology grounding. There are others being explored (RL-based methods, temporal modeling for longitudinal records). But I don't have a clean answer. The dam metaphor still holds — the potential energy is real — but we're still figuring out how to build the right turbine.

---

[^1]: Speaking of cliches — I'm aware this piece is full of em-dashes, which have become a telltale sign of AI-assisted writing. But as [Nabeel Qureshi pointed out](https://x.com/nabeelqu/status/2012219522833359071), David Foster Wallace was doing this decades ago. The italics for emphasis, the informality, the casual speech tone. I'll keep my em-dashes.

[^2]: In some sense, what once seemed like a disadvantage — healthcare's lagging technological infrastructure — may now be an asset: a greenfield opportunity with less legacy baggage to work around. But that might be substance for a different post.
