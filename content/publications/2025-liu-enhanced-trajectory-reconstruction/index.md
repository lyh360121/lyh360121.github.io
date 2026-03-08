---
title: |
  Enhanced trajectory reconstruction from sparse and noisy GPS data: A
    progressive chunked transformer approach
authors:
  - Yonghui Liu
  - Qian Li
  - Inhi Kim
date: "2025-12-01T00:00:00Z"
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
    url: "http://dx.doi.org/10.1016/j.commtr.2025.100200"
featured: true
tags:
  - Trajectory reconstruction
  - Transformer
  - Chunked processing
  - Heuristic-informed
  - Parallel computing

---

