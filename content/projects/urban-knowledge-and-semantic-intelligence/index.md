---
title: "Urban Knowledge and Semantic Intelligence"
date: 2026-03-08
draft: false
summary: "A research direction bridging large language models and graph learning to give road networks generalizable urban semantics."
tags:
  - Large Language Models
  - Graph Learning
  - Urban Computing
  - Semantic Alignment

---

## 1. The Grand Vision

While trajectory coordinates (longitude/latitude) describe _how_ things move in a city, they lack the context of _why_ they move. Real-world urban spaces are not just empty geometric networks; they are profoundly rich in semantics (e.g., points of interest, functional zones, road properties). However, existing spatial graph learning paradigms often struggle to ingest highly heterogeneous, unstructured, and cross-domain urban knowledge.

This research direction aims to build **Foundation Models for Urban Spaces**. By elegantly bridging the reasoning capabilities of **Large Language Models (LLMs)** with the structural modeling power of **Graph Learning**, we seek to create a unified, generalizable semantic representation of urban road networks. This will transform rigid transportation graphs into "knowledge-aware" spatial cognitive systems.

## 2. Key Research Questions

To realize this vision, my research investigates three critical scientific challenges at the intersection of AI and Urban Computing:

- **RQ1: Cross-Domain Semantic Alignment:** Urban data across different cities or platforms often follow completely different taxonomies (e.g., varying POI categorization standards). How can we leverage the zero-shot reasoning of LLMs to automatically align and unify these heterogeneous labels across disjoint spatial networks?
- **RQ2: Generalizable Spatial Representation:** How do we design a unified semantic graph learning framework that transcends specific local datasets, learning universal road network representations that are highly transferable to new, unseen cities?
- **RQ3: Regulated Knowledge Integration:** Injecting massive textual semantics into geometric graphs can cause "negative transfer" or semantic noise. How can we develop regulated, context-aware gating mechanisms to ensure that only task-relevant urban semantics are fused into road-centric graph representations?

## 3. Current Milestones & Publications

My recent work has laid the theoretical and methodological groundwork for this agenda:

- **Tackling RQ1 (Semantic Alignment):** We combined LLM prompt-based pseudo-labels with DeepWalk structural embeddings to align road labels across taxonomies (OpenStreetMap highway tags to FHWA functional classes). The method reaches 79.1% accuracy versus 54.3% for prompt-only mapping, and degrades far more gracefully than direct supervision when labels are scarce (51.3% vs. 40.0% accuracy with 1% of labels).
  _([Cross-Taxonomy Label Alignment in Transportation Networks With Prompt-Driven Large Language Models](/publications/2025-liu-cross-taxonomy-label-alignment/), published in IEEE ITSC 2025)_
- **Tackling RQ2 (Generalizable Frameworks):** We proposed HetSemNet + SaRNSAGE, which fuses LLM-encoded POI context with road topology in a heterogeneous graph. It outperforms GCN, GAT, GraphSAGE, and a heterogeneous graph-attention baseline on road type classification (best F1 0.7296), and a model trained on Porto transfers unchanged to Lisbon with only a 4.71% F1 drop.
  _([A Generalizable Semantic Graph Learning Framework for Road Network Representation](/publications/2025-liu-a-generalizable-semantic/), published in IEEE ITSC 2025)_
- **Tackling RQ3 (Regulated Access):** We are currently exploring advanced regulated access mechanisms to intelligently filter and integrate urban semantics into road-centric graphs, ensuring high signal-to-noise ratios in downstream spatial tasks.
  _(Under Review)_

## 4. Future Impact

This agenda pushes the boundaries of Science in the urban domain. The resulting semantic intelligence will empower a wide array of high-level applications, including **LLM-driven Urban Planning**, **Semantic HD Map Generation for Autonomous Driving**, and **Context-Aware Traffic Management**, aligning perfectly with the strategic goals of next-generation smart city governance.
