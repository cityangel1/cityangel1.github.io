# cityangel1.github.io

Built with Jekyll + the [Minimal Mistakes](https://mademistakes.com/work/jekyll-themes/minimal-mistakes/) theme (dark skin), loaded via `remote_theme` — no local theme files needed, GitHub Pages builds it for you.

## Deploy

1. In your `cityangel1.github.io` repo, delete the old `index.html` (the standalone terminal page) and upload every file/folder from this bundle in its place, keeping the same structure (`_config.yml`, `_pages/`, `_posts/`, `_data/`, `index.html`, `assets/`).
2. Commit to `main`.
3. Settings → Pages should already show Source: `main` / `/ (root)` from before — no change needed there. GitHub will rebuild automatically (1–2 min).
4. Visit `https://cityangel1.github.io/` — you should see the new layout with sidebar bio and the three sample posts.

## Things to edit before it's really "yours"

- `_config.yml` — email, LinkedIn/X URLs, location
- `assets/images/avatar.jpg` — add a real photo here (any square image works)
- `_pages/about.md` and `_pages/cv.md` — replace placeholder bio/experience
- `assets/files/resume.pdf` — drop your real résumé PDF here; the CV page already links to it
- `_posts/` — replace the three sample write-ups with your own, or add new ones the same way: a new file named `YYYY-MM-DD-title.md` in `_posts/`, with the same front matter format

## Adding a new write-up later

Create `_posts/2026-09-01-my-new-writeup.md`:

```
---
title: "My New Writeup"
categories: [lab]
tags: [whatever, applies]
excerpt: "One or two sentences shown in the feed."
---

Your content in Markdown here.
```

Push it — it appears on the homepage automatically, newest first.
