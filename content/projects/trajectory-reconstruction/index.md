---
title: "Intelligent Spatiotemporal Computing"
date: 2026-03-08
draft: false
summary: "A research direction on robust, resource-efficient, and interpretable AI for modeling spatiotemporal dynamics such as trajectories and traffic."
tags:
  - Spatiotemporal AI
  - Trajectory Modeling
  - Urban Computing

---

## Motivation

Trajectories, sensor streams, and traffic flows are the main record of how people and vehicles move through a city, but the data that reaches a model is rarely clean. GPS fixes are sparse and noisy, sensing and communication budgets are limited, and forecasting models are often deployed without a clear account of which inputs their predictions depend on.

This direction develops methods that remain reliable under these conditions: recovering continuous movement from imperfect observations, making efficient use of limited sensing and computing budgets, and making transparent what information a spatiotemporal model actually relies on.

## Research Questions

- **RQ1: Robustness to imperfect data.** How can models reconstruct continuous spatiotemporal dynamics from fragmented, sparse, and noisy sensor streams?
- **RQ2: Efficiency under constraints.** How can data collection and processing (for example, active sampling or compression) adapt to bandwidth and computing budgets without degrading downstream tasks?
- **RQ3: Interpretability.** How can we attribute a spatiotemporal model's predictions to the inputs it uses, and move toward causal explanations for safety-critical decisions?

## Work So Far

- **RQ1 (Data recovery):** We introduced ProChunkFormer, which reconstructs long trajectories from sparse, noisy GPS data as chunks decoded in parallel, conditioned on a semi-high-frequency skeleton. It matches an autoregressive transformer's accuracy while running faster, with the largest gains at long sampling intervals (up to 240 s).
  _([Enhanced trajectory reconstruction from sparse and noisy GPS data](/publications/2025-liu-enhanced-trajectory-reconstruction/), published in Communications in Transportation Research)_
- **RQ3 (Input attribution):** We proposed SDA, a model-agnostic evaluation protocol that splits forecasting inputs into Past, Current, and Prior and measures each one's standalone and marginal contribution through controlled input gating. It shows that gains from history saturate after short windows (about 6–8 steps), and that a reliable goal prior helps more than additional history, especially at longer horizons.
  _([Sequential decomposition and attribution for trajectory forecasting](/publications/2025-liu-sda/), published in Knowledge-Based Systems)_

## Outlook

Methods for recovering, sampling, and interpreting spatiotemporal data are relevant to applications that depend on reliable movement data, such as urban digital twins, drone routing, and autonomous fleet management.
