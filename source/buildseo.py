"""Write sitemap.xml, robots.txt and llms.txt into the built site."""
import os, sys, json
OUT = sys.argv[1]; SITE = 'https://thiran.app'; DATE = '2026-11-03'
here = os.path.dirname(os.path.abspath(__file__))
guides = json.load(open(os.path.join(here, '.guides.json')))
pages = ['/', '/download', '/guides'] + [f'/guides/{g["slug"]}' for g in guides]
urls = ''.join(f'  <url><loc>{SITE}{"" if p == "/" else p}{"/" if p == "/" else ""}</loc><lastmod>{DATE}</lastmod></url>\n' for p in pages)
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
g = '\n'.join(f'- [{x["h1"]}]({SITE}/guides/{x["slug"]}): {x["desc"]}' for x in guides)
open(os.path.join(OUT, 'llms.txt'), 'w').write(f'''# Thiran

> Thiran is PDF markup and takeoff software for construction drawings, made by Tensi.ai (Tensi Pty Ltd). Annotate, redline, measure, compare revisions and count symbols on PDF drawings. It runs on Mac, Windows and the web, with a 7-day free trial.

## Main pages

- [Home]({SITE}/): what Thiran does, features and pricing (USD, one licence per device).
- [Download]({SITE}/download): the desktop app for Windows and Mac.
- [Guides]({SITE}/guides): step-by-step how-tos.
- [Sign in or start a free trial](https://my.thiran.app)

## Guides

{g}
''')
print('seo files:', len(pages), 'pages in sitemap')
