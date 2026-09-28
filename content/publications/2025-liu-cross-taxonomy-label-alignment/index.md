---
title: Cross-Taxonomy Label Alignment in Transportation Networks With
  Prompt-Driven Large Language Models
authors:
  - me
  - Inhi Kim
date: 2025-11-18T00:00:00Z
hugoblox:
  ids:
    doi: 10.1109/itsc60802.2025.11423624
publication_types:
  - paper-conference
publication: 2025 IEEE 28th International Conference on Intelligent
  Transportation Systems (ITSC)
publication_short: "ITSC"
abstract: "Integrating transportation datasets from diverse sources is critical for comprehensive analysis and intelligent infrastructure planning. A major obstacle to effective integration lies in taxonomy heterogeneity, where datasets differ in points of interest (POI) categories, road type classifications, and land use taxonomies. Addressing these inconsistencies requires cross-taxonomy label alignment, a challenge that remains inadequately explored due to the reliance on costly human annotations and the limited effectiveness of rule-based matching approaches. This paper presents a novel framework that combines prompt-driven pseudo-labeling and multi-view representation learning to address cross-taxonomy label alignment. Large language model (LLM) prompts generate initial semantic pseudo-labels to guide pretraining, while multi-view input representations are constructed by combining DeepWalk-based structural embeddings with encoded source taxonomy labels. The framework is first trained in a semi-supervised manner using pseudo-labels, followed by fine-tuning with a limited amount of human-verified labels to further refine alignment quality. Extensive experiments demonstrate that the proposed method substantially outperforms rule-based and prompt-only baselines, maintaining robust performance even when only 1% of labeled samples are available. These results demonstrate that leveraging LLM-guided semantic supervision alongside structural representations enables robust and scalable cross-taxonomy adaptation, even under severely limited supervision."
summary: A prompt-driven pseudo-labeling and multi-view representation learning
  framework that aligns labels across heterogeneous transportation taxonomies
  under severely limited supervision.
tags:
  - Cross-Taxonomy Label Alignment
  - Transportation Data Integration
  - Large Language Models
  - Semi-Supervised Learning
links:
  - type: source
    url: http://dx.doi.org/10.1109/ITSC60802.2025.11423624
  - type: pdf
    url: paper.pdf
featured: false
---

Transportation datasets rarely speak the same language. A city's OpenStreetMap extract might tag a road as "primary" or "secondary," while a government inventory such as the U.S. Federal Highway Administration's (FHWA) Functional Classification sorts the same roads into categories like "Interstate," "Principal Arterial," or "Minor Collector." Point-of-interest catalogs and land-use datasets run into the same mismatch in their own vocabularies. Merging sources like these for infrastructure planning or traffic analysis means mapping one taxonomy onto another, and today that mostly still means manually built lookup tables or brittle keyword-matching rules — approaches that don't scale and break down as soon as a new dataset phrases things slightly differently.

This paper proposes a framework that automates that mapping using two complementary signals instead:

- **Prompt-driven pseudo-labeling.** For each source-taxonomy label, a large language model is queried with several different prompt variants asking which target-taxonomy label it corresponds to; the candidate answers are combined by majority vote into one pseudo-label. This gives the model a starting signal without any hand-built mapping table.
- **Structural embeddings.** In parallel, a DeepWalk embedding is trained directly on the road network graph, so every road segment also carries information about where it sits and how it connects in the network, independent of what it happens to be called.

The two views — an entity's LLM-derived semantic signal (pseudo-label plus its encoded source-taxonomy label) and its structural embedding — are concatenated into one multi-view input and fed to a two-layer classifier.

![Architecture diagram showing the semantic view (LLMs and source-taxonomy label producing pseudo-labels and label embeddings), the structural view (DeepWalk embeddings from the road network), their concatenation, and the two-stage pretraining/fine-tuning training procedure with semantic masking.](fig-architecture.png "Framework overview: semantic features (LLM-generated pseudo-labels plus source-taxonomy label embeddings) and structural features (DeepWalk embeddings from the road network) are concatenated and passed through a two-stage pretrain-then-fine-tune procedure with semantic masking.")

Training happens in two stages. The model first pretrains on the LLM-generated pseudo-labels, using a technique the authors call **semantic masking**: in every batch, a random subset of nodes has its semantic input zeroed out, which forces the model to also lean on the structural embedding rather than just memorizing the pseudo-label mapping. It's then fine-tuned on a small set of human-verified labels to correct whatever noise the pseudo-labels introduced. Tested on mapping real OSM 'highway' tags to FHWA functional classes, the fine-tuned model reached **79.1% accuracy and 81.0% macro-F1**, well ahead of plain string-matching (29.5%/20.9%) and of using the LLM's pseudo-labels directly with no learned model at all (54.3%/51.8%). An ablation confirmed both views pull their weight: a model trained on structural embeddings alone already reached 68.5% accuracy, versus 54.8% for a model with no structural information at all — a sizeable share of the framework's benefit comes from network topology, not just the LLM's semantic guesses.

The more telling result is what happens as human-verified labels become scarce, which is the realistic case for most cross-dataset integration projects. The paper compares the full framework (pseudo-label pretraining + fine-tuning) against a model trained the conventional way — directly and only on whatever labeled data happens to be available.

![Two line charts, accuracy and macro-F1 score, each plotted against the percentage of human-labeled data used for fine-tuning (log scale from 100% down to 0.1%), comparing the LLM-pretrained-then-fine-tuned model against a directly supervised model, with two flat dashed baselines for string-matching and prompt-only mapping.](fig-results.png "Performance as the human-labeled fine-tuning budget shrinks from 100% to 0.1%: the LLM-pretrained-then-fine-tuned model (orange) degrades far more gracefully than a model trained the conventional way, directly supervised on the same shrinking label budget (blue).")

With abundant labels the two approaches land close together (both around 79-81%), but as the labeled fraction shrinks, the directly-supervised model's performance collapses — down to 40.0% accuracy / 33.4% macro-F1 at just 1% of the labels, and below 30% accuracy at 0.1%. The pseudo-label-pretrained model degrades far more gently: still 51.3% accuracy / 50.4% macro-F1 at 1% of the labels, and 47.0% accuracy even at 0.1%. That gap is the practical payoff — real cross-taxonomy alignment problems rarely come with abundant hand-labeled data across every source, and this is exactly where the prompt-driven pretraining earns its keep, giving the model a useful starting point before it ever sees a human annotation.
