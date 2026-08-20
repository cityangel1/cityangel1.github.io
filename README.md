# Brian Karaba Wachira — Offensive Security Portfolio

A static, dependency-free HTML/CSS/JS portfolio. No build step, no Jekyll — just plain files, ready for GitHub Pages.

## Structure
- `index.html` — the main one-page site (About, Skills, Experience, Write-ups, Beyond, Contact)
- `writeups/*.html` — one page per write-up, linked from the Write-ups section
- `assets/css/style.css` — all styling (light/dark theme via CSS variables)
- `assets/js/main.js` — theme toggle, mobile nav, scroll reveal, terminal typing effect, write-up filter
- `assets/images/` — headshot
- `assets/files/resume.pdf` — downloadable CV
- `.nojekyll` — tells GitHub Pages to skip Jekyll processing and serve the files as-is

## Deploying to GitHub Pages
1. Push the contents of this folder to the root of your `<username>.github.io` repository (or to a repo and enable Pages on the `main` branch, root folder).
2. Make sure `.nojekyll` is included in the push (it's a hidden file — check `git status` if it seems missing).
3. Visit `https://<username>.github.io` — it should be live within a minute or two.

## Editing content
- Bio, skills, experience, and project copy live directly in `index.html`.
- Write-ups are generated from `build_writeups.py` — edit the `POSTS` list there and re-run `python3 build_writeups.py` to regenerate `writeups/*.html` and the card list on the homepage. (You can also hand-edit the generated `writeups/*.html` files directly if you don't want to touch the script.)
- Colors live as CSS variables at the top of `assets/css/style.css` under `:root` (light) and `html[data-theme="dark"]`.
