---
title: "Autonomous Traffic Sensor Web (ATSW)"
date: 2026-10-11
lastmod: 2026-10-11
draft: false
project_kind: system
current: true
status: "Working research prototype"
preview_alt: "Conceptual illustration of selected source observations and a receiver trajectory estimate"
weight: 20
summary: "A replay-based web prototype for adaptive GPS reporting, receiver-state estimation, and historical trajectory reconstruction."
tags:
  - Autonomous Sensing
  - Trajectory Modeling
  - Urban Computing
---

## Overview

ATSW is a working local research prototype for exploring how GPS observation decisions affect the movement state available to a receiver. Independent sources replay recorded trajectories and decide when to report a new observation. A web workspace shows the received evidence, movement estimates, forecasts, and reporting decisions as playback advances.

The prototype connects to my research on [trajectory observation–reconstruction co-design](/projects/trajectory-reconstruction/): selecting or reporting an observation changes the information available for recovering movement. It provides an inspectable setting for studying that relationship.

## Implemented

- **Adaptive reporting:** Each source compares its current GPS observation with a local replica of the receiver's predicted state. A heuristic policy reports significant deviations and periodically refreshes the receiver. Periodic and all-observation policies provide comparison modes.
- **Receiver-state maintenance:** Constant-velocity Kalman prediction and updates, implemented with Stone Soup, maintain each receiver's position estimate. Delivered GPS observations update the estimate; between reports, the receiver advances by prediction.
- **Live inspection:** The workspace supports playback, pause and single-step controls, per-source decision logs, forecasts, and requests for a source's next recorded observation.
- **Historical comparison:** An elapsed recorded window can be reduced to selected original observations and reconstructed between them. This branch currently uses a geometric retention baseline and linear interpolation.
- **Run evidence:** A local journal and JSON export record received observations, estimates, and diagnostic events for inspection.

## What the Prototype Evaluates

Replay comparisons pair position error with the ratio of delivered GPS observations. The ratio measures report count; network bytes and device energy require separate measurement. Received GPS evidence and predicted or updated state estimates remain distinct in the workspace.

The live receiver uses reported observations. The History view separately accesses an elapsed source recording for retrospective retention and reconstruction comparisons. These two views examine different information conditions.

Recorded sources and their independent receiver states run in one local process. The implemented version uses heuristic reporting, Kalman estimation, and geometric historical reconstruction. Its current scope is recorded GPS replay.

## Next Steps

The next stage is to integrate and evaluate compatible learned reporting and recovery modules while preserving the source–receiver information boundary. Live device connections and coordination across sources are further development directions, supported by the observation and command interfaces.
