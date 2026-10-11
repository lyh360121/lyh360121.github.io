---
title: "Urban Knowledge and Semantic Intelligence"
date: 2026-03-08
lastmod: 2026-10-11
project_kind: direction
weight: 40
draft: false
summary: "A research direction bridging large language models and graph learning to give road networks generalizable urban semantics."
tags:
  - Large Language Models
  - Graph Learning
  - Urban Computing
  - Data Fusion

---

## Motivation

Trajectories describe movement through a city; urban semantics add context to those movements. Road networks sit within rich information about points of interest, land use, functional zones, and road classes. Much of this context exists as unstructured text, or in datasets that use incompatible category systems. Many road graph models emphasize topology and numeric attributes. Integrating heterogeneous semantic context reliably remains a challenge.

This direction combines large language models, which can read and compare unstructured descriptions, with graph learning, which captures network structure, to build road network representations that carry urban semantics and transfer across cities and datasets.

## Research Questions

- **RQ1: Cross-taxonomy alignment.** Datasets from different cities and platforms use different category systems, for example for POIs or road classes. How can LLMs help align these labels automatically, with little human annotation?
- **RQ2: Transferable road representations.** How can a semantic graph learning framework learn road network representations that transfer to cities it was not trained on?
- **RQ3: Selective knowledge integration.** Adding large amounts of text-derived context to a road graph can introduce noise or negative transfer. How can a model decide which semantic context is relevant for a given road and task?

## Work So Far

- **RQ1 (Semantic alignment):** We combined LLM prompt-based pseudo-labels with DeepWalk structural embeddings to align road labels across taxonomies (OpenStreetMap highway tags to FHWA functional classes). The method reaches 79.1% accuracy versus 54.3% for prompt-only mapping, and degrades far more gracefully than direct supervision when labels are scarce (51.3% vs. 40.0% accuracy with 1% of labels).
  _([Cross-Taxonomy Label Alignment in Transportation Networks With Prompt-Driven Large Language Models](/publications/2025-liu-cross-taxonomy-label-alignment/), published in IEEE ITSC 2025)_
- **RQ2 (Transferable representations):** We proposed HetSemNet + SaRNSAGE, which fuses LLM-encoded POI context with road topology in a heterogeneous graph. It outperforms GCN, GAT, GraphSAGE, and a heterogeneous graph-attention baseline on road type classification (best F1 0.7296), and a model trained on Porto transfers unchanged to Lisbon with only a 4.71% F1 drop.
  _([A Generalizable Semantic Graph Learning Framework for Road Network Representation](/publications/2025-liu-a-generalizable-semantic/), published in IEEE ITSC 2025)_
- **RQ3 (Selective integration):** Ongoing work on gating mechanisms that control which urban semantics are fused into road-centric graph representations.
  _(Under review)_

## Outlook

Road network representations that carry semantic context could support applications such as LLM-assisted urban planning, semantic map generation for autonomous driving, and context-aware traffic management.
