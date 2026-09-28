---
title: Sequential decomposition and attribution for trajectory forecasting
authors:
  - me
  - Inhi Kim
date: 2025-12-23
publishDate: "2026-03-08T06:40:20.973Z"
publication_types:
  - article-journal
publication: Knowledge-Based Systems
publication_short: KBS
abstract: |
  Trajectory forecasting is fundamental to intelligent mobility systems. A prevailing assumption is that longer historical inputs consistently help, which has motivated the design of models with extended observation windows. Yet empirical results often show diminishing returns, higher computational cost, and increased sensitivity to noise. Despite extensive architectural innovation, there is still no unified framework for systematically attributing forecasting performance to different temporal inputs. Rather than introducing a new forecasting model, we present the Sequential Decomposition and Attribution (SDA) protocol, a model-agnostic evaluation paradigm that decomposes inputs into Past (historical trajectory), Current (present state), and Prior (i.e., destination or goal, when available) and quantifies their standalone utility, marginal contributions, and interactions through controlled input gating. Instantiated on trajectory forecasting on two real-world datasets (Porto taxi and ETH pedestrian) with two representative backbones (LSTM and Transformer), SDA shows that accuracy gains from history saturate with short sequences, the most recent state alone is highly informative at short horizons, and reliable priors yield substantial improvements with greater value at longer horizons. Interaction analyses further reveal conditional complementarity among sources. These findings highlight the importance of input-aware designs that prioritize efficient use of the latest state and goal-conditioning over indiscriminate history accumulation. While demonstrated on trajectories, SDA offers a general lens for sequential information attribution.
summary: A model-agnostic protocol that decomposes trajectory forecasting
  inputs into Past, Current, and Prior to quantify each one's standalone and
  marginal contribution.
tags:
  - Trajectory forecasting
  - Sequential decomposition
  - Input attribution
  - Temporal dependence
  - Goal-conditioned prediction
  - Intelligent transportation systems
  - Model interpretability
featured: true
hugoblox:
  ids:
    doi: 10.1016/j.knosys.2025.115204
links:
  - type: source
    url: "https://dx.doi.org/10.1016/j.knosys.2025.115204"
  - type: pdf
    url: paper.pdf
image:
  caption: "The SDA protocol: inputs are split into Past, Current, and Prior
    streams, combined through controlled gating, then fed to the forecasting
    model and evaluator to attribute each stream's contribution."
  focal_point: ""
  preview_only: false
projects: []
slides: ""
draft: false

---

Trajectory forecasting models keep getting longer input windows on the assumption that more history means better predictions. In practice that assumption often breaks down: accuracy gains taper off quickly, extra history adds compute cost, and longer windows pull in more noise. SDA is not another forecasting model — it is an evaluation protocol for measuring *why* a model performs the way it does.

SDA splits any trajectory forecasting input into three interpretable streams and gates them on/off in controlled combinations to measure each one's standalone value, its marginal contribution on top of the others, and how the streams interact:

- **Past** — the historical trajectory before the current step
- **Current** — the most recent observed state
- **Prior** — an optional destination or goal, when available

Running this protocol on two real-world datasets (Porto taxi, ETH pedestrian) with both an LSTM and a Transformer backbone gives a consistent picture:

![History-length ablation on the Porto taxi dataset: absolute error (ADE, left) and improvement over the no-history baseline (Δ%, right) for LSTM (top) and Transformer (bottom) backbones, across prediction horizons H. Accuracy gains saturate around L*≈6 (LSTM) and L*≈8 (Transformer) — feeding in more history beyond that yields almost no further improvement.](result_1.png "Accuracy sensitivity to history length L, across horizons H and both backbones.")

- Accuracy gains from history **saturate after a short window** (L*≈6–8 steps) regardless of backbone or prediction horizon.
- The **Current** state alone is already highly informative at short horizons.
- A reliable **Prior** (goal/destination) gives a bigger boost than piling on more history, especially at longer horizons.
- Past, Current, and Prior show **conditional complementarity** — their combined value is not simply additive.

The takeaway for model design: prioritize making good use of the latest state and any available goal information, rather than defaulting to ever-longer observation windows.
