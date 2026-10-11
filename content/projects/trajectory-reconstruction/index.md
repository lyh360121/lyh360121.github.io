---
title: "Intelligent Spatiotemporal Computing"
date: 2026-03-08
draft: false
summary: "A research direction on robust, resource-efficient, and interpretable AI for modeling spatiotemporal dynamics such as trajectories and traffic."
tags:
  - Spatiotemporal AI
  - Urban Computing
  - Data-Centric AI

---

## 1. The Grand Vision

In the era of Cyber-Physical Systems (CPS) and Autonomous Mobility, understanding the physical world through spatiotemporal data (e.g., trajectories, sensor networks, traffic flows) is the cornerstone of urban intelligence. However, the real physical environment is highly dynamic, strictly resource-constrained, and fraught with uncertainty.

This research direction aims to develop **next-generation Intelligent Spatiotemporal Computing paradigms**. The ultimate goal is to bridge the fundamental gap between imperfect physical sensing and the urgent need for highly reliable, real-time, and resource-efficient decision-making in complex urban environments.

## 2. Key Research Questions

As a long-term research agenda, this project seeks to answer three overarching scientific questions in the field of Spatiotemporal AI:

- **RQ1: Robustness against Physical Uncertainty:** How can AI models reliably perceive and reconstruct continuous spatiotemporal dynamics from highly fragmented, sparse, and noise-corrupted sensor streams?
- **RQ2: Efficiency and Scalability under Constraints:** How do we design data-centric computing paradigms (e.g., active sampling, intelligent compression) that dynamically adapt to strict system budgets (bandwidth, edge computing power) without compromising downstream utility?
- **RQ3: Explainable and Causal Spatiotemporal Reasoning:** Beyond black-box forecasting, how can we endow spatiotemporal models with the ability to disentangle complex physical mechanisms and provide causal attributions for safety-critical decisions?

## 3. Current Milestones & Publications

To address these grand challenges, my ongoing research has established several foundational frameworks, serving as the initial milestones for this agenda:

- **Tackling RQ1 (Data Recovery):** We introduced ProChunkFormer, which reconstructs long trajectories from sparse, noisy GPS data as chunks decoded in parallel, conditioned on a semi-high-frequency skeleton. It matches an autoregressive transformer's accuracy while running faster, with the largest gains at long sampling intervals (up to 240 s).
  _([Enhanced trajectory reconstruction from sparse and noisy GPS data](/publications/2025-liu-enhanced-trajectory-reconstruction/), published in Communications in Transportation Research)_
- **Tackling RQ3 (Input Attribution):** We proposed SDA, a model-agnostic evaluation protocol that splits forecasting inputs into Past, Current, and Prior and measures each one's standalone and marginal contribution through controlled input gating. It shows that gains from history saturate after short windows (about 6–8 steps), and that a reliable goal prior helps more than additional history, especially at longer horizons.
  _([Sequential decomposition and attribution for trajectory forecasting](/publications/2025-liu-sda/), published in Knowledge-Based Systems)_

## 4. Future Impact

Looking forward, the methodologies developed in this direction will serve as the algorithmic infrastructure for broader applications, including **Urban Digital Twins**, **Low-Altitude Economy (UAV routing)**, and **Autonomous Fleet Management**, driving the sustainable evolution of future smart cities.
