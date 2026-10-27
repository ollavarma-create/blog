---
title: "The Scientific Crisis of the LLM Era: Confabulation, Reproducibility, and the Erosion of Science"
translation-key: "tieteen-eroosio-llm"
date: 2026-05-25
draft: false
tags:
  - artificial intelligence
  - science
  - confabulation
  - LLM
  - reproducibility crisis
  - open science
categories:
  - artificial intelligence
  - research
  - future
description: "How the scientific reproducibility crisis and large language model confabulation intertwine, and which new methods may restore the reliability of science?"
summary: "Science is in transition: the reproducibility crisis and LLM confabulation threaten the reliability of knowledge. We explore the root causes of the problem and present solutions such as Proof-Carrying Papers and Schrödinger’s Machine."
---

Report AI assistant: Qwen3.6-Plus Deep Research.

# **1. Introduction**

This report examines the weakening reliability of scientific knowledge, a phenomenon increasingly referred to as the *replication crisis*. The analysis explores the key root causes of the crisis: methodological problems, research biases, and academic incentive systems, as well as a new and rapidly growing threat: the **confabulation (hallucination)** produced by **large language models (LLMs)**.

The goal of this report is to present a clear and structured overview of how these two phenomena intertwine and together form a major challenge for modern science. The text also introduces new solution models, such as the *Proof-Carrying Papers* approach and the *Schrödinger’s Machine* concept, both of which aim to restore transparency and reproducibility to scientific knowledge.

Overall, the report offers an analytical, balanced, and accessible overview of the current state of scientific methods and the challenges ahead.

# 2. Root Causes of the Replication Crisis and Research Biases

The scientific replication crisis is not merely the sum of failures in individual studies, but a broad and deeply rooted problem affecting the very foundations of scientific knowledge. In many fields, previously published results cannot be reproduced, weakening trust in the entire research system. Behind this lies a complex combination of methodological practices, organizational cultures, and human biases.

## 2.1 Questionable Research Practices (QRPs)

One of the central causes of the replication crisis is the widespread use of *questionable research practices (QRPs)*. These include:

- **p-hacking**: the researcher modifies the analysis or data until the result becomes statistically significant (p < 0.05).

- **HARKing (Hypothesizing After the Results are Known)**: the hypothesis is written only after seeing the results, making the study appear predictive rather than explanatory.

These practices make research findings appear convincing while remaining methodologically unreliable.

Although Bayesian methods can reduce some problems in statistical inference, they do not prevent HARKing or Bayesian “p-hacking”: posterior distributions can also be manipulated.

## 2.2 Human Biases

Methodological problems are tightly intertwined with psychological biases. The most central of these is **confirmation bias**, the tendency to seek and interpret information in ways that support pre-existing beliefs.

Confirmation bias affects every stage of the research process, from selecting the research question to analysis and interpretation. Peer reviewers and readers are also vulnerable to it, reinforcing the publication of biased results.

Another major bias is **publication bias**: positive and “newsworthy” findings are far more likely to be published than negative or neutral results.

This systematically creates an overly optimistic picture of reality and distorts meta-analyses that rely on already biased literature.

## 2.3 The Academic Incentive System

The “publish or perish” culture pushes researchers to produce rapidly publishable results, encouraging risky methodological choices and QRP practices. Career advancement, funding, and reputation are often tied to the number of publications rather than their quality or reproducibility.

This incentive structure has been recognized as problematic in many fields, including psychology, social sciences, and computer science.

## 2.4 Consequences: Epistemological Erosion

When research methods are flexible, biases are strong, and incentives are distorted, scientific knowledge begins to erode. Reproducibility, one of the foundational pillars of the scientific method, weakens, and the scientific process begins to resemble ritual rather than reliable knowledge acquisition.

This development has been described using terms such as:

- **epistemic decay**

- **collapse of trust**

Although open science practices and preregistration have improved the situation, the problem is deep and requires cultural change: a shift in focus from quantity to quality.

# 3. Large Language Model Confabulation: A System-Level Threat to Science

Although the replication crisis developed gradually over time and originates from human methodological and cultural choices, the fastest and most powerful accelerator in recent years has been the widespread adoption of *large language models (LLMs)* in scientific work. LLMs are used to support writing, summarization, code generation, and even the creation of research ideas. At the same time, they have introduced a new structural problem: *confabulation (hallucination)*.

## 3.1 The Nature of Confabulation

Confabulation refers to situations where an LLM produces linguistically fluent and seemingly logical content that is factually incorrect or entirely fabricated. For example, a model may:

- describe experiments in detail that were never conducted

- refer to studies that do not exist

- present scientific results that have no real source

The phenomenon resembles neurological confabulation, where humans fill memory gaps with plausible-sounding fiction. For an LLM, this is not an error but a consequence of its structure: the model does not *know* what it does not know. It generates the statistically most probable continuation of text, not verified knowledge.

Confabulation is not random. Research shows that:

- vague or poorly formulated prompts increase hallucinations

- models are unable to evaluate their own knowledge

- models fill missing information with “plausible fiction”

This makes confabulation a system-level risk rather than a simple user mistake.

## 3.2 LLMs Inherit and Amplify Human Biases

Because LLMs are trained on massive text corpora, they inherit all the biases embedded in human-generated knowledge. These include:

- **confirmation bias**

- **positivity bias**

- **publication bias**

If training data mainly consists of positive findings, the model learns a “world” where experiments almost always succeed. As a result, an LLM may generate:

- generalized and overly optimistic interpretations

- distorted summaries

- fabricated positive findings

This creates a self-reinforcing cycle: biased literature → biased model → even more biased new content.

## 3.3 The Model’s Own Biases

LLMs do not merely inherit biases; they also possess structural biases of their own:

- **overgeneralization**: the model presents limited results as universally valid

- **citation bias**: the model favors famous and highly cited sources

- **source bias**: LLM-generated text gains algorithmic preference in search systems compared to human-written text

These biases strengthen existing problems and make it more difficult for new, unpopular, or challenging research directions to gain visibility.

## 3.4 System-Level Impact on Science

LLM confabulation is not merely a source of isolated errors; it threatens the entire structure of scientific knowledge. When researchers use LLMs for:

- literature summarization → the model may distort original findings

- article writing → the model may fabricate claims and citations

- idea generation → the model may produce “scientific-sounding” fiction

This endangers the core principles of the scientific method:

- **reproducibility**

- **verifiability**

- **transparency**

When the final stages of scientific work are automated using tools capable of producing convincing yet unreliable content, the entire research pipeline becomes vulnerable to error.

LLMs can therefore function as *engines of crisis*: they do not merely add errors but reinforce and accelerate existing structural problems.

# 4. The Spread of False Citations: The Most Dangerous Form of Confabulation

Confabulation (*hallucination*) is a well-known problem of *large language models (LLMs)*, but its most dangerous and persistent form is the generation of false citations. This means that the model produces scientific references that appear completely authentic but have never been published. The phenomenon is not marginal; it is a system-level threat to the reliability and long-term preservation of scientific knowledge.

## 4.1 Why Citations Are Especially Dangerous

The problem of false citations is not limited to isolated mistakes. It directly affects the core of the scientific method:

- **reproducibility**: research cannot be verified if the source does not exist

- **knowledge accumulation**: false references become embedded in the literature

- **scientific synchronization**: future research is built upon fictional information

When such citations end up in published articles, they permanently “contaminate” scientific databases. This differs from ordinary errors: a confabulated citation is not merely incorrect, it is *invented*, and cannot be traced or corrected without manual auditing.

## 4.2 The Scale of the Phenomenon: Millions of False Citations

Several large-scale audits have shown that the problem has grown rapidly alongside the spread of LLMs:

- arXiv audits have identified **millions** of false citations

- one study analyzing 2.5 million papers and 111 million citations discovered **146,000** completely nonexistent references

- PubMed audits estimated that **1 in 200** publications in 2026 contained confabulated citations

- more than **98%** of false citations remained permanently in databases without correction

These figures demonstrate that this is not an occasional slip-up but a rapidly spreading structural problem.

## 4.3 Why the Citations Appear So Convincing

LLMs are capable of generating citations that look entirely authentic:

- correctly formatted author lists

- plausible publication years

- names of real journals

- even realistic DOI identifiers

The problem is that these references *lead nowhere*. They may contain:

- URLs that cannot be found in archives

- titles of real articles with incorrect page numbers

- combinations of real authors and fabricated titles

This makes them difficult to detect, especially when embedded within otherwise well-written text.

A well-known case involved a machine learning book published by Springer Nature that had to be withdrawn from the market because it contained a large number of entirely fabricated citations.

## 4.4 Where the Problem Comes From

Three key factors contribute to the emergence of false citations:

### 1. The Training Data Is Biased

LLMs learn the form and structure of citations, but not their actual existence. If the training data contains biases (e.g., positivity bias), the model learns to generate similarly biased references.

### 2. User Prompts Are Often Poorly Formulated

Requests such as “add references” or “provide sources” cause the model to fill gaps with fiction because it cannot verify the existence of citations.

### 3. LLMs Cannot Verify Citations

The model does not check:

- whether the article exists

- whether the DOI is correct

- whether the citation corresponds to a real publication

It only generates the statistically most plausible-looking citation.

This creates a self-reinforcing network: the LLM learns false citations → produces new ones → these become part of future training data → the model relearns them.

## 4.5 Effects on Science

The spread of false citations causes several severe consequences:

- **scientific verifiability weakens**: sources cannot be confirmed

- **research becomes built upon fictional foundations**

- **young researchers are especially vulnerable**: they rely on LLM tools without sufficient experience to recognize errors

- **scientific history becomes distorted**: fictional citations become permanent parts of the literature

This is one of the most serious threats to the cumulative nature of scientific knowledge.

## 4.6 Initial Attempts at Solutions

The scientific community has begun developing tools to combat the problem:

- **CiteAudit**: verifies citations against web caches and databases

- **GPTZero**: identifies LLM-generated citations

- **documentation of LLM use**: a proposal that every article’s methodology section should disclose where and how LLMs were used

However, these are corrective rather than preventive solutions. A real solution requires:

- mandatory publication of open data and code

- transparent workflows

- new publication models that prevent confabulation from entering scientific literature

# 5. Proof-Carrying Papers (PCP): Redefining Reproducibility

The erosion of scientific knowledge and the risks caused by LLM confabulation have created the need for a new publication model that restores transparency and reproducibility to the core of the scientific method. One of the most promising solutions is the *Proof-Carrying Papers (PCP)* model. It proposes a transition from the traditional static article format toward a dynamic, verifiable, and openly auditable publication process.

## 5.1 The Core Idea of PCP

In the PCP model, every scientific article is accompanied by an automatically generated *proof*: a machine-generated, complete, and transparent description of how the results were obtained. The proof contains:

- version numbers of the data used

- the version and hyperparameters of the model or LLM used

- the complete analysis code

- all parameters, settings, and computational pathways

This transforms an article into a *verifiable system* rather than merely narrative text. A researcher can “rerun the paper” and confirm that the results are reproducible using exactly the same settings.

## 5.2 How PCP Solves Current Problems

### 1. Reproducibility Is No Longer Optional

In the current system, reproducibility depends on researchers’ goodwill and data availability. PCP makes reproducibility a built-in feature: without complete proof, the paper cannot be published.

### 2. QRPs Become Automatically Visible

Because all analytical steps are transparent:

- p-hacking

- HARKing

- unclear analytical pathways

...can no longer remain hidden inside narrative text.

### 3. LLM Confabulation Can Be Isolated

If an LLM generates a false citation or claim, it becomes visible in the proof:

- incorrect code paths

- missing data

- incompatible sources

The error can be removed without rejecting the entire study.

### 4. Open Science Becomes Practical Reality

PCP makes open data and open code mandatory. Without them, no proof can be generated.

## 5.3 PCP in Practice

PCP is not merely a theoretical concept. Several fields have already developed prototypes:

- in materials science, LLM-based systems are used to validate model predictions

- in agent-based models (ABM), PCP-style approaches help solve replication problems

- computational sciences have developed systems that automatically generate proofs of analytical pipelines

These examples demonstrate that PCP is feasible with current technologies.

## 5.4 Challenges and Requirements

PCP requires major changes to scientific infrastructure:

- new tools for automatic proof generation

- reform of publication systems

- expansion of peer review from narrative evaluation to proof verification

- cultural change: the quality of the process must become more important than the “news value” of results

Still, the core idea of PCP is powerful: *science is not merely results, but process*. PCP makes that process visible, verifiable, and trustworthy.

# 6. Schrödinger’s Machine: Dynamic and Uncertainty-Aware Knowledge Production

The *Proof-Carrying Papers (PCP)* model offers a concrete solution to the reproducibility problem, but alone it is not enough to solve a deeper issue in scientific knowledge: the handling of *uncertainty*. Science never produces absolute truths, only probabilities and estimates. From this perspective emerges the vision of *Schrödinger’s Machine*, a system that does not produce isolated claims but explicitly models uncertainty and incomplete knowledge.

## 6.1 Uncertainty at the Core of Scientific Knowledge

The scientific method never provides absolute certainty. Every result is:

- conditional

- limited

- uncertain

- subject to revision

Schrödinger’s Machine makes this principle explicit. Instead of providing a single statement (“X is true”), the system produces:

- a probability estimate

- an uncertainty interval

- an explanation of the sources of uncertainty

For example:

“This claim is likely true (80%), but uncertainty remains high because the training data in this area is limited.”

This is much closer to genuine scientific reasoning than current LLMs, which often provide confident answers even when uncertainty should dominate.

## 6.2 How Schrödinger’s Machine Works

Schrödinger’s Machine is not merely an LLM but a complete architecture that includes:

- **uncertainty quantification**

- **self-knowledge estimation**

- **probability distribution generation**

- **transparent explanations of uncertainty**

This means that the system:

- knows when it does not know

- does not fill gaps with fiction

- does not reinforce claims lacking sufficient evidence

- avoids confabulation because it does not attempt certainty where certainty is impossible

In other words, Schrödinger’s Machine addresses the root cause of confabulation: the model’s inability to evaluate its own knowledge.

## 6.3 Benefits for Scientific Work

The adoption of Schrödinger’s Machine would bring several advantages:

### 1. Reduced Impact of Biases

Because the system does not reinforce claims it is uncertain about, confirmation bias and positivity bias cannot dominate.

### 2. Dramatic Reduction of Confabulation

The model does not invent sources or results because it does not attempt to fill gaps with certainty.

### 3. More Realistic Scientific Interaction

The user receives not “truth,” but:

- a probability distribution

- an uncertainty interval

- an explanation of uncertainty

This reflects how researchers actually think.

### 4. Better Decision-Making

Explicit uncertainty modeling is critical in areas such as:

- simulation research

- risk analysis

- medical decision-making

- policy recommendations

Schrödinger’s Machine automates this process.

## 6.4 Relationship to the PCP Model

PCP and Schrödinger’s Machine complement one another:

- **PCP** ensures *reproducibility* and *transparency*

- **Schrödinger’s Machine** ensures *uncertainty modeling* and *confabulation minimization*

Together, they form a vision of the future of science:

- open

- verifiable

- self-correcting

- respectful of uncertainty

- resistant to confabulation

---

## Final Remarks: Science Is Not Truth, but Process

The scientific method has never been perfect, but its greatest strength has always been its ability to correct itself. The replication crisis and LLM-related confabulation do not signal the end of science; rather, they are a clear warning that old publication and verification practices can no longer keep pace with the speed of digital-era knowledge production.

The problem is not artificial intelligence itself, but how we integrate it into processes that are not yet structurally prepared for verifiability. The solution is not to ban AI, but to build an infrastructure in which transparency, reproducibility, and honest acknowledgment of uncertainty are mandatory rather than optional.

Proof-Carrying Papers and Schrödinger’s Machine are not merely technical experiments. They are concrete demonstrations that the scientific community is ready to take the next step. They transform knowledge from a static claim into a dynamic, machine-verifiable system that collaborates with humans.

The science of the future will not depend on machines or humans being flawless. It will depend on making errors visible, marking uncertainty clearly, and ensuring that every claim can be traced back to its sources. If we succeed in building such an ecosystem, we will not merely halt the erosion of knowledge — we will make the scientific method more reliable than ever before.

**Science is not finished truth.** It is a method for seeking it. And now we finally have tools that can help us do so more honestly.
