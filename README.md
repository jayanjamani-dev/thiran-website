# thiran.app website

Marketing site for Thiran (PDF markup and takeoff for construction), served by Vercel from the `site/` folder.

## Folders
- `site/`: the built website exactly as served (home page, `/download`, assets, `vercel.json`). Vercel's Root Directory should be `site`.
- `source/`: what you edit.
  - `v8.tpl.html` is the home page template.
  - `buildsite.py` builds it into `site/`, compressing images and giving them hashed names.
  - `download/index.html` is the download page. The release details (version, date, sizes, file names, SHA-256) live in one `THIRAN_RELEASE` block at the top.

## Making a change
1. Edit files in `source/`.
2. Run `./build.sh` (needs Python 3 and Pillow).
3. Commit and push. Vercel deploys `site/` automatically once the repo is connected.

For a download-page-only change, you can edit `source/download/index.html`, then copy it to `site/download/index.html` (or run `./build.sh`).

## Links the site points to
- App, sign in, trial and buy: https://my.thiran.app
- Installers (always the newest): https://my.thiran.app/download/windows and https://my.thiran.app/download/mac
- Legal: https://my.thiran.app/legal/
