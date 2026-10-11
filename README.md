# Yonghui Liu — personal academic website

Source for <https://lyh360121.github.io/>, the homepage of Yonghui Liu, PhD candidate at KAIST and former software engineer at Meituan, working on spatiotemporal AI, generative modeling, and representation learning for autonomous driving and urban mobility.

## Structure

- `content/publications/` — one folder per paper (`index.md`, `cite.bib`, figures, and the PDF where the license allows it)
- `content/projects/` — research directions and current system projects
- `data/authors/me.yaml` — profile, education, experience, and links
- `config/_default/` — site configuration
- `layouts/` — local overrides of theme templates

## Local development

Requires [Hugo](https://gohugo.io/) extended (version pinned in `hugoblox.yaml`) and Go.

```bash
hugo server
```

## Deployment

Every push to `main` builds the site and deploys it to GitHub Pages via `.github/workflows/deploy.yml`.

## Credits

Built with [HugoBlox Kit](https://github.com/HugoBlox/kit) (MIT License, see `LICENSE.md`). The MIT license covers the template code only; site content (text, publication figures, and photos) is © Yonghui Liu unless noted otherwise.
