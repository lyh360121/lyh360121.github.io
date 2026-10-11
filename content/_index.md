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

        My research is in **spatiotemporal AI for mobility**. Much of my work models how people and vehicles move, covering trajectory reconstruction from sparse GPS data, trajectory forecasting, and more recently multi-agent trajectory generation for autonomous-driving simulation. I have also worked on using large language models and graph learning to learn semantic representations of road networks. In the long run, I hope to contribute to foundation models for mobility. I am currently exploring autonomous sensing as well.

        I received my M.S. from Zhejiang University and worked as a software engineer at Meituan before starting my Ph.D.

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
