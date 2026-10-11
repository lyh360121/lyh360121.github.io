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
      text: ""
      headings:
        about: ""
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
