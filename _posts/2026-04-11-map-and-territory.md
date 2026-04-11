---
layout: post
title: "maps, territory and LMs"
description: "Borges' cartographers, Baudrillard's stages of simulation, and Polanyi's tacit knowledge: on the skill of reading AI-generated maps without losing touch with the territory."
tags: [culture]
audio: "assets/audio/map-and-territory.mp3"
---

Borges has a very short story about an empire whose cartographers kept producing larger and larger maps, until they built one the size of the empire itself.[^1] the following generations, less enchanted, saw it was useless and abandoned it to the weather. maps are useful precisely because they are reductions. when the pursuit of fidelity destroys the compression it destroys the point.

for the purposes of this text, LMs are our maps.[^2]

i'll cut to the chase (bear with me though). LMs have become really good. so good that they are now well beyond useful representations of the territory, and are in many ways beginning to [reshape the territory itself](https://www.programmablemutter.com/p/the-political-economy-of-ai). this means, i think, that we need to be much better at reading maps without losing our connection to the territory. we need more ways to stay engaged while reading and interacting with them. much of our (professional) interaction with computers is mediated through LMs now: when examining a new codebase, when reading a paper, when priming ourselves towards a task. sometimes even as an interface for thinking. this is an abstraction layer that we are not really willing to avoid at this point (and im not saying that we should) but it changes what we need to be good at.

Baudrillard, writing in 1981, proposed four stages that describe how representations relate to reality.[^3] i think they map (pun acknowledged) really nicely to LMs, and in a way that is unique, because LMs seem to occupy different stages all at once, depending on the use case.

in stage one, the image is a faithful copy of reality. LMs were in a sense designed this way: trained to predict and reproduce patterns in human-generated text as accurately as possible, a compressed but structurally faithful representation of what we've written and thought.[^4]

in stage two, the image masks and distorts reality. LMs do this too. what you get back is a smoothed-out, averaged version of the territory, and subtle distortions are easy to miss precisely because the surface looks coherent. ask an LM to explain the causes of the 2008 financial crisis and you'll get subprime mortgages and deregulation. ask again with different framing, same answer. the response feels authoritative, but it's closer to a popularity-weighted consensus than to the still-unresolved debates among economists.[^5]

in stage three, the image masks the absence of reality. once you have a good enough approximation, engagement with the territory itself becomes less needed. you (may) stop checking sources because the answer looks right. you stop exploring because the recommendation feels sufficient. the financial crisis question again: asking it feels like research but is really just consuming a pre-averaged explanation. the activity looks the same, but something has been hollowed out.

stage four, when the representation has no relation to reality at all, is trickier. i'm not sure we're there yet, though part of what makes stage four unsettling is that you might not know when you've arrived. it possibly emerges when much of the content available for training new systems is mostly output of previous systems, or when "the chat" becomes everyone's primary source of knowledge, "becoming both the image of god and god."[^6]

what's uncomfortable is that the transitions between these stages aren't clear. we can't point to the exact moment when a useful map starts substituting for the territory. it's slippery, and that slipperiness is what makes it hard to stay aware.

LMs are not like other maps.

a cartographic map looks the same to every reader. an LM doesn't. the output changes with [slight modifications to the prompt](https://arxiv.org/abs/2604.05051), and it has been shown that the sophistication of the model's responses correlates with the educational background of the person prompting it.[^7] this map is very much in the eyes of the beholder. it's also malleable in ways that static maps never were: you can zoom in and out of topics, approach them from different angles, connect information across fields that would be harder to bridge otherwise.

this is genuinely useful. it clears away clutter and creates space to truly reflect on a research project, on a complex codebase, on ideas that are half-formed. these "means of summarization," as Henry Farrell called them,[^8] are useful even though we always have access to the full territory (the entire web), partly because of the flexibility of input and output, and mainly because they are much better at understanding what we want.

unlike any previous map, this one is also becoming an object of study in its own right. since these maps arrived, everyone wants to be a cartographer: building, tinkering, adapting these systems, exploring what's inside them. in many areas of AI research, models are explored not as maps of reality but as something useful on their own terms. houellebecq's protagonist in *the map and the territory* argued that the map is more interesting than the territory. in AI research, this is increasingly literally the case.[^9]

so here is where i think the actually interesting part is.

using these maps well, knowing when to trust them, when to zoom in, when to stop and touch the territory, is a skill, and it is largely a tacit one. it's also a personal one: because the map looks different to each reader, the intuitions you develop are calibrated to your own version of it, not to a shared public artifact. by tacit i mean something close to what Michael Polanyi meant when he wrote, with admirable directness, "we can know more than we can tell."[^10]

the tacit knowledge here isn't about spotting obvious hallucinations. it's subtler: a feeling that something hasn't been verified, an uneasiness about a claim you're not sure the data supports, a sense that the output is too smooth.[^11] it's the kind of thing a clinician means when they say a patient "looks sick" before the labs come back, or a developer means when they talk about "code smell." you attend from pattern recognition you can't fully articulate to a judgment that something needs checking.

Polanyi has a really nice example of a blind person learning to use a probe.[^10] at first you feel the impact of the probe against your hand. but as you learn, your awareness shifts: you stop feeling the probe and start feeling what the probe touches. the proximal sensation becomes distal perception. using LMs well might be something like this: at first you attend to the output itself (is this correct? does this look right?). over time, if you develop the skill, you begin to attend through the output to the "territory" behind it.

this skill is learned through practice and resists being codified into rules or checklists. a piece about maps, then, that arrives at the conclusion that the most important skill for navigating them can't itself be mapped.[^12]

i should probably note: the analogy of LMs as maps is itself a map, and i've tried to use it where it's useful without forcing it where it isn't. LMs are also tools, research subjects, economic forces, things that reshape the territory they represent. no single frame captures all of this.

the current LMs we use are the worst ones we'll ever get to use. they will get better (in all aspects). the skill of reading maps well, of maintaining that productive uneasiness, will matter more next year than it does now.

Borges' cartographers fell in love with map-making and forgot what it was for. the next generation, less enchanted, abandoned the map to the weather. neither response seems right to me. somewhere between obsession and indifference, there is the delicate practice of using these maps well, and of staying honest about how our own relationship to them keeps changing.

---

[^1]: jorge luis borges, "on exactitude in science" (1946). the full story is one paragraph long: https://kwarc.info/teaching/TDM/Borges.pdf

[^2]: i use "LMs" loosely here to mean the whole stack: language models, the systems built around them, the agents, the tools. the map is the whole thing, not just the weights.

[^3]: Jean Baudrillard, *simulacra and simulation* (1981). the four stages are drawn from his theory of how images progressively detach from reality.

[^4]: whether "faithful representation" was ever truly the goal of language model training is debatable: prediction and representation aren't the same thing. but functionally, the result is a compressed mirror of human-generated text, which behaves like a faithful copy in many contexts.

[^5]: the loop compounds: more people absorb the simplified explanation, more content reflects that framing, the model becomes even more confident in offering it. the map shapes the territory it claims to describe.

[^6]: this echoes Baudrillard's argument about the byzantine iconoclasts, who feared that creating images of god would reveal there was nothing behind the images. when the representation becomes authoritative enough, the distinction between "represents knowledge" and "is knowledge" quietly collapses.

[^7]: see anthropic's economic index report (january 2026) on how model output sophistication correlates with the educational background of the person prompting: https://www.anthropic.com/research/anthropic-economic-index-january-2026-report

[^8]: henry farrell, "the map is eating the territory" (2024). his treatment of the political economy of AI-as-summarization is thorough and worth reading in full. i'm deliberately not covering that ground here.

[^9]: michel houellebecq, *the map and the territory* (2010). his protagonist achieves fame by photographing road maps, arguing they are more beautiful than the landscapes they represent. to be clear: studying models on their own terms is important and legitimate work. i'm observing the shift, not criticizing it.

[^10]: michael polanyi, *the tacit dimension* (1966). LMs are, funnily enough, also a bit like this: they contain more than they can easily surface, and you have to prompt them in certain ways to make them reveal what they have. a kind of loosely encrypted zip file of human knowledge.

[^11]: as an example: a colleague ran a hypothesis-generation agent on a prompt about liver ultrasound correlations in large populations. it retrieved 18 papers, applied five "research facets," and produced five hypotheses with titles, research questions, and experiment plans. the structure was impeccable. but the first hypothesis simply restated the input prompt. the third grabbed a zero-citation paper about skeletal muscle oxygenation and proposed "do this but for liver" with no consideration of whether that makes anatomical sense. the map of how science works was used to produce the appearance of science working.

[^12]: i've written more about the related problem of cognitive offloading and maintaining engagement with these tools in "cognitive offloading, exoskeletons, and remaining sentient" (https://galsapir.github.io/sparse-thoughts/2026/02/03/offloading-cognition/).
