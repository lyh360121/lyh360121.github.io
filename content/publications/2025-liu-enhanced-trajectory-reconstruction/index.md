---
title: |
  Enhanced trajectory reconstruction from sparse and noisy GPS data: A
    progressive chunked transformer approach
authors:
  - me
  - Qian Li
  - Inhi Kim
date: 2025-12-01T00:00:00Z
hugoblox:
  ids:
    doi: 10.1016/j.commtr.2025.100200
publication_types:
  - article-journal
publication: Communications in Transportation Research
publication_short: COMMTR
abstract: >
  Trajectory reconstruction from sparse and noisy GPS data is critical for
  applications such as urban mobility analysis, transportation planning, and
  navigation systems. However, large sampling intervals and the typically long
  output sequences required to reconstruct coherent travel trajectories
  significantly increase computational complexity, particularly in the presence
  of noise. To address these challenges, we propose a progressive chunked
  transformer (ProChunkFormer), which is a deep learning method for trajectory
  reconstruction that employs self-attention mechanisms and chunked processing
  to balance efficiency with accuracy. ProChunkFormer first generates
  intermediate trajectories at a semi-high frequency from low-frequency sampled
  data, and then the remaining trajectory is divided into manageable blocks and
  reconstructed parallelly in the condition of the semi-high-frequency
  trajectory. By combining progressive reconstruction with chunk processing,
  ProChunkFormer not only mitigates the cumulative errors commonly observed in
  autoregressive models but also alleviates the rapid increase in complexity
  associated with reconstructing ultralong trajectories. Specifically, our
  approach achieves quadratic optimization in time and space for attention
  modules, with cubic time savings compared with autoregressive decoding. A case
  study using an open-source taxi trajectory dataset confirms the effectiveness
  of our approach. The performance of ProChunkFormer is comparable to that of
  autoregressive transformers while offering better running efficiency. It
  improves the accuracy, F1 score (F1), mean absolute error (MAE), and road
  network mean absolute error (MAE_RN) by 23.1%, 18.6%, 22.3%, and 25.1%,
  respectively, for trajectories with a long interval time of up to 240 ​s.
  Furthermore, we investigate incorporating heuristic information to guide
  trajectory reconstruction for each block. The experimental results indicate an
  improvement in both the overall performance and convergence speed of the
  model.
links:
  - type: source
    url: http://dx.doi.org/10.1016/j.commtr.2025.100200
  - type: pdf
    url: paper.pdf
featured: true
tags:
  - Trajectory reconstruction
  - Transformer
  - Chunked processing
  - Heuristic-informed
  - Parallel computing
summary: ProChunkFormer, a progressive chunked transformer that reconstructs
  trajectories from sparse, noisy GPS data with better accuracy and
  efficiency than autoregressive baselines.
image:
  caption: "ProChunkFormer overview. Phase 1 (Skeleton Generation): the
    sparse, noisy GPS trajectory and the road network are encoded and
    decoded into a semi-high-frequency skeleton, MM-Semi. Phase 2
    (Trajectory Completion): conditioned on that skeleton and a heuristic
    shortest-path estimate, the remaining trajectory is split into chunks
    and reconstructed in parallel; concatenating the chunks gives the final
    reconstructed trajectory, MM-Full."
  focal_point: ""
  preview_only: false

---

GPS traces collected in the wild are sparse and noisy — long gaps between fixes are the norm, not the exception. Reconstructing a coherent, road-consistent trajectory from such data matters for mobility analysis, transportation planning, and navigation, but the long output sequences involved make it computationally expensive, and autoregressive models tend to accumulate error step by step over a long reconstruction.

ProChunkFormer tackles this with a two-phase, divide-and-conquer strategy instead of decoding the full trajectory one point at a time:

1. **Phase 1 — Skeleton generation.** The sparse, low-frequency GPS input and the road network are encoded and decoded into an intermediate, semi-high-frequency "skeleton" of the trajectory (`MM-Semi`) that already follows the road network.
2. **Phase 2 — Trajectory completion.** Conditioned on that skeleton — and optionally on a heuristic shortest-path estimate (`Heuristic`) computed between each pair of consecutive skeleton points — the remaining trajectory is divided into chunks and reconstructed **in parallel** with self-attention, rather than autoregressively. Concatenating all the reconstructed chunks gives the final, complete trajectory (`MM-Full`).

Self-attention is quadratic in the length of the sequence it looks at, but standard autoregressive decoding still ends up cubic in the length of the whole trajectory, because each of its output steps has to attend over an ever-growing context. ProChunkFormer avoids this by sizing each attention pass to a chunk rather than the full trajectory and generating chunks in parallel; the paper's complexity analysis shows this cuts decoding time by roughly the cube of the number of chunks used, compared with standard autoregressive decoding. On an open-source taxi trajectory dataset, this lets ProChunkFormer match the accuracy of autoregressive transformer baselines while running faster — 13.9%, 16.5%, and 20.7% faster at sampling intervals of 60, 120, and 240 seconds, respectively — with the largest accuracy gains showing up on the hardest cases: long sampling intervals of up to 240 seconds, where it improves accuracy by 23.1%, F1 score by 18.6%, mean absolute error by 22.3%, and road-network error by 25.1% over a standard transformer baseline.

![Three side-by-side street maps comparing a reconstructed taxi trip: (a) the ground-truth route as a continuous line, (b) points reconstructed by a standard autoregressive transformer, several of which are wrongly bunched on top of each other in one spot, and (c) points reconstructed by ProChunkFormer, generated in two independent chunks (Block 1 and Block 2) and correctly spread out along the true route.](fig-reconstruction-comparison.png "Ground truth versus reconstructed GPS points for the same trip: the standard transformer's points collapse together in the circled area, while ProChunkFormer — which reconstructs the trajectory in independent, parallel chunks — keeps them spread out along the real route. Map data © OpenStreetMap contributors, licensed under CC BY-SA 2.0.")

Adding heuristic guidance — using the shortest path between consecutive skeleton points to help condition each chunk's reconstruction — speeds up convergence during training and improves accuracy and error metrics in most configurations, though the paper reports a few cases (for example, accuracy at a 120-second sampling interval) where it produces a small decline instead.

