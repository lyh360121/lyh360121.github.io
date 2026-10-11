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
        I'm a PhD candidate at KAIST, working with Prof. Inhi Kim in the [TUPA Lab](https://www.inhi.kim/). I'm interested in teaching machines how a city moves.

        Lately that means generative models of traffic, which learn how vehicles and people move together and can simulate realistic traffic for autonomous driving. I see this as a step toward foundation models for mobility. I'm also starting to explore autonomous sensing.

        Earlier, I worked on recovering trajectories from sparse GPS data, on what trajectory prediction models actually rely on, and on using LLMs to help models understand road networks. Before my PhD, I spent two years as a software engineer at Meituan.
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
