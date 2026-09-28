---
title: Unified Model of Sediment Transport Threshold and Rate Across Weak and
  Intense Subaqueous Bedload, Windblown Sand, and Windblown Snow
authors:
  - Thomas Pähtz
  - me
  - Yuezhang Xia
  - Peng Hu
  - Zhiguo He
  - Katharina Tholen
date: "2021-04-01T00:00:00Z"
hugoblox:
  ids:
    doi: 10.1029/2020jf005859
publication_types:
  - article-journal
publication: "Journal of Geophysical Research: Earth Surface"
publication_short: JGR Earth Surface
abstract: "Nonsuspended sediment transport (NST) refers to the sediment transport regime in which the flow turbulence is unable to support the weight of transported grains. It occurs in fluvial environments (i.e., driven by a stream of liquid) and in aeolian environments (i.e., wind-blown) and plays a key role in shaping sedimentary landscapes of planetary bodies. NST is a highly fluctuating physical process because of turbulence, surface inhomogeneities, and variations of grain size and shape and packing geometry. Furthermore, the energy of transported grains varies strongly due to variations of their flow exposure duration since their entrainment from the bed. In spite of such variability, we here propose a deterministic model that represents the entire grain motion, including grains that roll and/or slide along the bed, by a periodic saltation motion with rebound laws that describe an average rebound of a grain after colliding with the bed. The model simultaneously captures laboratory and field measurements and discrete element method (DEM)-based numerical simulations of the threshold and rate of equilibrium NST within a factor of about 2, unifying weak and intense transport conditions in oil, water, and air (oil only for threshold). The model parameters have not been adjusted to these measurements but determined from independent data sets. Recent DEM-based numerical simulations (Comola, Gaume, et al., 2019; https://doi.org/10.1029/2019GL082195) suggest that equilibrium aeolian NST on Earth is insensitive to the strength of cohesive bonds between bed grains. Consistently, the model captures cohesive windblown sand and windblown snow conditions despite not explicitly accounting for cohesion."
summary: A deterministic model unifying the threshold and rate of nonsuspended
  sediment transport across subaqueous bedload, windblown sand, and windblown
  snow.
tags:
  - Sediment Transport
  - Aeolian Transport
  - Bedload
  - Discrete Element Method
links:
  - type: source
    url: "http://dx.doi.org/10.1029/2020JF005859"
  - type: pdf
    url: paper.pdf
featured: false

---

Grains get pushed along a riverbed, blown across a desert dune, or carried over a snowfield by very different physical processes — yet in each case, a grain that isn't fully suspended in the fluid moves the same basic way: it hops, rolls, or slides along the bed in a sequence of collisions. This is called nonsuspended sediment transport (NST), and it shapes sedimentary landscapes on Earth and other planetary bodies alike. In reality NST is messy: turbulence, an uneven bed surface, and grain-to-grain variability make individual grain trajectories highly erratic. This paper asks whether, despite that mess, one single deterministic model can still predict *both* when transport starts (the threshold) and *how much* material moves once it does (the rate) — across fluvial settings (grains driven by a stream of liquid) and aeolian settings (grains driven by wind) at once.

The model's key idea is to represent the entire population of grains — including ones that mostly roll or slide rather than hop — by a single, repeating (periodic) saltation trajectory: a grain leaves the bed, follows a ballistic-like path shaped by the mean turbulent flow profile above the bed, and comes back down, where an empirical "rebound law" (fit to grain-bed collision experiments and simulations) sets its average rebound velocity as a function of how it hit the bed. The transport threshold is then defined as the weakest flow for which such a self-sustaining periodic trajectory can still exist, with an extra criterion checking whether a grain has enough energy to roll itself out of the most stable pockets of the bed surface.

![Sketch of the model's core mechanism: a grain bounces in a periodic saltation trajectory just above a granular bed, driven by the mean streamwise flow velocity profile u_x(z); the bed's virtual zero level and crest level are marked below.](fig-saltation-mechanism.png "The model reduces the entire fluctuating grain motion to a single periodic bouncing trajectory driven by the mean flow profile above the bed (Figure 1).")

What makes the result notable is that none of the model's parameters were tuned to the data it is then tested against — they were fixed beforehand from independent experiments and simulations (grain-bed rebound measurements, earlier discrete-element-method simulations of transport, and separate studies of bed yielding). With those parameters locked in, the model reproduces laboratory measurements and field data of both the transport threshold and the transport rate to within about a factor of two, across density ratios between grain and fluid spanning roughly 2.65 (mineral grains in water) up to around 2000 (mineral grains or snow in air) — that is, across subaqueous bedload, windblown sand, and windblown snow together.

![Two log-log plots: on the left, the model's predicted transport-threshold curves (solid lines, one per density ratio) plotted against experimental threshold data points across a range of Galileo numbers; on the right, the model's predicted dimensionless transport rate plotted directly against the measured transport rate, with points clustering close to the 1:1 line — both panels showing separate data series for fluvial transport of minerals, aeolian transport of minerals, and aeolian transport of snow.](fig-model-vs-data.png "Left: predicted transport-threshold curves versus Galileo number compared with measured threshold data. Right: predicted versus measured dimensionless transport rate. Both panels combine fluvial mineral, aeolian mineral, and aeolian snow data sets (Figure 5c-d).")

A striking side finding concerns cohesion. Windblown sand and snow grains are known to stick together via cohesive bonds, yet the model captures their behavior without ever explicitly representing cohesion. This lines up with independent DEM simulations showing that equilibrium aeolian transport is nearly unaffected by how strong those cohesive bonds are — a fairly counterintuitive result that this model helps explain: in the model's picture, cohesion only matters while a grain is in contact with the bed, and for grains that are mostly saltating (as opposed to rolling), those contacts are so brief that cohesion barely gets a chance to act. The model also yields a simple, physically grounded way to tell apart "bedload" (where a significant fraction of grains roll or slide in sustained contact with the bed) from "saltation" (where that fraction is negligible) — consistent with an independent criterion from the authors' earlier work — and it further separates viscous from turbulent transport regimes based on how the grain's hop height compares to the flow's viscous sublayer thickness.
