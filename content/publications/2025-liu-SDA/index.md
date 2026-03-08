---
title: 2025-liu-SDA
authors:
  - me
  - Inhi Kim
author_notes:
  - ""
date: 2025-12-23
publishDate: 2026-03-08T06:40:20.973Z
publication_types:
  - article-journal
publication: Knowledge-Based Systems
publication_short: KBS
abstract: |
  Trajectory forecasting is fundamental to intelligent mobility systems. A prevailing assumption is that longer historical inputs consistently help, which has motivated the design of models with extended observation windows. Yet empirical results often show diminishing returns, higher computational cost, and increased sensitivity to noise. Despite extensive architectural innovation, there is still no unified framework for systematically attributing forecasting performance to different temporal inputs. Rather than introducing a new forecasting model, we present the Sequential Decomposition and Attribution (SDA) protocol, a model-agnostic evaluation paradigm that decomposes inputs into Past ( ), Current ( ), and Prior ( , i.e., destination or goal when available) and quantifies their standalone utility, marginal contributions, and interactions through controlled input gating. Instantiated on trajectory forecasting on two real-world datasets (Porto taxi and ETH pedestrian) with two representative backbones (LSTM and Transformer), SDA shows that accuracy gains from history saturate with short sequences, the most recent state alone is highly informative at short horizons, and reliable priors yield substantial improvements with greater value at longer horizons. Interaction analyses further reveal conditional complementarity among sources. These findings highlight the importance of input-aware designs that prioritize efficient use of the latest state and goal-conditioning over indiscriminate history accumulation. While demonstrated on trajectories, SDA offers a general lens for sequential information attribution.
summary: One-line takeaway for readers skimming listings.
tags:
  - Trajectory forecasting
  - Sequential decomposition
  - Input attribution
  - Temporal dependence
  - Goal-conditioned prediction
  - Intelligent transportation systems
  - Model interpretability
featured: false
hugoblox:
  ids:
    doi: 10.1016/j.knosys.2025.115204
links:
  - type: source
    url: https://dx.doi.org/10.1016/j.knosys.2025.115204
image:
  caption: ""
  focal_point: ""
  preview_only: false
projects: []
slides: ""
draft: false

---

<!-- Add the paper text or supplementary notes. Markdown, math, and code are supported. -->
