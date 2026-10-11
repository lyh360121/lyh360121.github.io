---
title: ""
summary: ""
date: "2022-10-24"
type: "landing"
design:
  spacing: "6rem"
sections:
  - block: "resume-biography-3"
    content:
      username: "me"
      text: |-
        I am a PhD candidate at the Cho Chun Shik Graduate School of Mobility, KAIST, advised by Prof. Inhi Kim in the [TUPA Lab](https://www.inhi.kim/) (Transport and Urban Planning with AI). My research develops machine learning methods for spatiotemporal and mobility data, turning imperfect urban sensing into reliable inputs for transportation decisions.

        My recent work spans two threads. On **trajectory modeling**, I proposed [ProChunkFormer](/publications/2025-liu-enhanced-trajectory-reconstruction/) for reconstructing trajectories from sparse, noisy GPS data, and [SDA](/publications/2025-liu-sda/), an evaluation protocol that measures how much past, current, and goal information each contributes to forecasting accuracy. On **urban semantics**, I combine large language models with graph learning to [represent road networks](/publications/2025-liu-a-generalizable-semantic/) and to [align labels across heterogeneous transportation datasets](/publications/2025-liu-cross-taxonomy-label-alignment/).

        Before KAIST, I worked as a software engineer at Meituan (2021–2023) and received my M.S. from Zhejiang University, where I contributed to physics-based modeling of sediment transport and wireless power transfer.
      headings:
        about: "Biography"
        education: ""
        interests: ""
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: "md"
      avatar:
        size: "medium"
        shape: "circle"
    ue: "section-caa3d29d"
    As: "section-a36cf2c6"
  - block: "collection"
    content:
      title: "Featured Publications"
      filters:
        folders:
          - "publications"
        featured_only: true
        kinds:
          - ""
    design:
      view: "article-grid"
      columns: 2
      fill_image: false
      show_read_time: false
    ue: "section-papers"
    id: "papers"
    As: "section-fd535fe4"
  - block: "collection"
    content:
      title: "Other Publications"
      text: ""
      filters:
        folders:
          - "publications"
        exclude_featured: true
      archive:
        enable: true
    design:
      view: "citation"
    ue: "section-0d686be2"
    As: "section-1ff93fd6"
---
