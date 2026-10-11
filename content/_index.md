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
        I am a Ph.D. candidate at the Cho Chun Shik Graduate School of Mobility, KAIST, advised by Prof. Inhi Kim in the [TUPA Lab](https://www.inhi.kim/).

        My research focuses on **behavior modeling and simulation for autonomous driving**. I build generative models that learn how vehicles and other road users move and interact, and use them for multi-agent trajectory prediction and realistic traffic simulation. Longer term, I am interested in foundation models for mobility. I am also exploring autonomous sensing.

        Previously, I worked on trajectory reconstruction, trajectory forecasting, and LLM-enhanced road network learning. Before my Ph.D., I was a software engineer at Meituan, and I received my M.S. from Zhejiang University.

        Feel free to reach out if you are interested in collaboration.
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
