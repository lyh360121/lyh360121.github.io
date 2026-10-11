---
title: ""
summary: "AI research and engineering in spatiotemporal learning, generative modeling, and representation learning, with applications in autonomous driving and urban mobility."
date: "2026-10-11"
lastmod: "2026-10-12"
type: landing
design:
  spacing: "4rem"
sections:
  - block: research-profile
    id: about
    content:
      username: me
      eyebrow: "AI Research & Engineering"
      title: "Spatiotemporal AI & Generative Modeling"
      text: |-
        My research spans **spatiotemporal AI, generative modeling, and representation learning**. My published work covers trajectory reconstruction, motion prediction analysis, and road-network representations using **large language models and graph neural networks**. I am currently developing research systems for **controllable traffic simulation and adaptive sensing**, with applications in autonomous driving and urban mobility.

        I am a Ph.D. candidate at **KAIST**, advised by Prof. Inhi Kim in the [TUPA Lab](https://www.inhi.kim/). I received my M.S. from Zhejiang University and previously worked as a software engineer at **Meituan**.
      primary_action:
        label: View Publications
        url: /#papers
      secondary_action:
        label: Explore Projects
        url: /projects/
    design:
      spacing:
        padding: ["4rem", "0", "3rem", "0"]
  - block: research-questions
    id: research
    content:
      eyebrow: Research Areas
      title: Models, methods, and applications
      text: "My work combines sequence modeling, generative models, and representation learning, with published studies and ongoing system projects."
      questions:
        - title: Motion Prediction & Reconstruction
          question: "Understand movement from trajectory data."
          text: "Transformer-based trajectory reconstruction and systematic analysis of forecasting inputs."
          links:
            - label: ProChunkFormer · COMMTR
              url: /publications/2025-liu-enhanced-trajectory-reconstruction/
            - label: SDA · Knowledge-Based Systems
              url: /publications/2025-liu-sda/
        - title: Generative Models & Simulation
          question: "Generate motion in interacting traffic."
          text: "Current work on route-conditioned traffic generation, joint fine-tuning, and closed-loop evaluation."
          links:
            - label: Ongoing simulation project
              url: /projects/route-conditioned-traffic-simulation/
        - title: Representation Learning
          question: "Learn semantic representations of urban networks."
          text: "Language models and graph neural networks for road representations and cross-taxonomy label alignment."
          links:
            - label: Semantic graph learning · IEEE ITSC
              url: /publications/2025-liu-a-generalizable-semantic/
            - label: Label alignment · IEEE ITSC
              url: /publications/2025-liu-cross-taxonomy-label-alignment/
    design:
      spacing:
        padding: ["3rem", "0", "3rem", "0"]
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders: [publications]
        featured_only: true
      archive:
        enable: true
        text: All publications
        link: publications/
    design:
      view: article-grid
      columns: 2
      fill_image: false
      show_read_time: false
  - block: current-systems
    id: systems
    content:
      title: Current Projects
      text: "Putting research into practice through controllable traffic simulation and an adaptive sensing workspace."
    design:
      spacing:
        padding: ["3rem", "0", "3rem", "0"]
  - block: collection
    content:
      title: Other Publications
      filters:
        folders: [publications]
        exclude_featured: true
    design:
      view: citation
  - block: research-contact
    id: contact
    content:
      title: Let’s connect
      text: "I welcome research and engineering conversations on spatiotemporal AI, generative modeling, and representation learning."
    design:
      spacing:
        padding: ["2rem", "0", "2rem", "0"]
---
