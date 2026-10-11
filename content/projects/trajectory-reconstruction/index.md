---
title: "Trajectory Observation–Reconstruction Co-Design"
date: 2026-03-08
lastmod: 2026-10-11
draft: false
project_kind: direction
weight: 30
summary: "Preserving useful mobility information under limited observation resources through the co-design of trajectory selection, reporting, and reconstruction."
tags:
  - Spatiotemporal AI
  - Trajectory Modeling
  - Urban Computing

---

## Research Focus

Urban mobility applications use discrete observations to represent continuous movement. Storage and communication constraints limit the observations that can be retained or reported. Which observations are available, and how they are reconstructed, jointly determine the movement information a system can provide.

My doctoral research, *Compression–Reconstruction Co-Design for Urban Mobility Trajectories*, studies this relationship. The aim is to preserve useful movement information at the resource level a system actually achieves, by considering observation decisions and reconstruction together.

## Complementary Research Settings

- **Completed-trajectory retention:** Once a trip is recorded, which observations should be kept under a fixed retained-point budget? Current work examines reconstruction-aware selection and refinement of retained point sets.
- **Live trajectory reporting:** As a trip unfolds, when should a source report a new observation so that a receiver can maintain an accurate movement state? Current work coordinates reporting decisions with the state propagated at the receiver.
- **Sparse-trajectory reconstruction:** How does recoverability change as gaps between available observations grow? This work studies road-consistent reconstruction and the computational cost of recovering long trajectories.

Completed retention can use the full recorded trip; live reporting makes decisions with information available at the current time. These settings share a co-design perspective and are evaluated under their respective information conditions.

Road-network structure and semantics provide another source of information for mobility models. Related work on [Urban Knowledge and Semantic Intelligence](/projects/urban-knowledge-and-semantic-intelligence/) develops road representations and compatible labels, and examines the value of this context in stated transportation tasks.

## Published Studies

- **Reconstruction capability:** [ProChunkFormer](/publications/2025-liu-enhanced-trajectory-reconstruction/) reconstructs long trajectories from sparse, noisy GPS observations using progressive skeleton generation and parallel chunk completion. It studies the accuracy and efficiency of recovery across increasing observation intervals. Published in *Communications in Transportation Research*.
- **Conditional information value:** [Sequential Decomposition and Attribution (SDA)](/publications/2025-liu-sda/) uses controlled input gating to examine the contributions of historical trajectory, current state, and available goal information to forecasting. It is a supporting information-value study within the wider research program. Published in *Knowledge-Based Systems*.
- **Urban context:** [Semantic graph learning](/publications/2025-liu-a-generalizable-semantic/) and [cross-taxonomy label alignment](/publications/2025-liu-cross-taxonomy-label-alignment/) study road representations and semantic compatibility across datasets. Published in *IEEE ITSC 2025*.

## From Research to Systems

[Autonomous Traffic Sensor Web (ATSW)](/projects/autonomous-traffic-sensor-web/) is a working local prototype for inspecting GPS reporting decisions, receiver estimates, and historical retention. Its recorded-trajectory replay and explicit source–receiver states make the effects of observation decisions visible. The current prototype uses heuristic reporting, Kalman estimation, and a geometric historical baseline; it provides a setting for future evaluation of learned methods.

Across these studies, the shared question is how much useful movement information a reduced observation record can support. Retained-point count and reporting ratio are evaluated alongside movement fidelity, with their resource definitions made explicit.
