"""Build thiran.app/guides from guides/md/*.md into <out>/guides/.

Each guide is a Markdown draft. Screenshot lines (**Screenshot:** ...) are swapped
for the images listed in SHOTS, in order. Images are written as hashed WebP at
800 and 1600 px wide with width/height, srcset, sizes and lazy loading.
"""
import re, os, sys, json, glob, html, hashlib
from PIL import Image

OUT = sys.argv[1]
SITE = 'https://thiran.app'
APP = 'https://my.thiran.app'
A = os.path.join(OUT, 'assets', 'guides'); os.makedirs(A, exist_ok=True)
G = os.path.join(OUT, 'guides'); os.makedirs(G, exist_ok=True)
DATE = '2026-11-03'

# Per guide: category, headline accent (words set in italic orange), card crop,
# and the images for each **Screenshot:** line in order ((files), caption or None).
META = {
 '01': dict(cat='Markup', em='a PDF drawing', thumb=('01-cloud-callout', '47% 40%'), shots=[
   (['uc1-03-arrived-a101'], 'The Lumen House drawing set open in Thiran.'),
   (['01-cloud'], 'The Cloud tool part-way round a door on sheet A-101.'),
   (['01-cloud-callout'], 'A Cloud with Callout: “Door moved 600 mm to clear the riser”.'),
   (['01-stamp-list', '01-stamp'], 'The Stamp list open, then For Construction placed on the title block.'),
   (['01-register'], 'The Register listing the clouds, callouts and stamp from this guide.')]),
 '02': dict(cat='Measure', em='a PDF drawing', thumb=('02-calibrate', '35% 45%'), shots=[
   (['02-status-scale'], 'The scale shown in the status bar on sheet A-101.'),
   (['02-set-scale'], 'The Set scale box with 1:100 picked.'),
   (['02-calibrate'], 'Calibrate between grid lines A and B, with 6000 mm typed.'),
   (['uc1-04-scale-box'], 'A viewport box round one view, ready for its own scale.'),
   (['02-units'], 'The Measurements panel with the units and decimal places.')]),
 '03': dict(cat='Measure', em='on a PDF', thumb=('03-void-depth', '40% 62%'), shots=[
   (['uc1-09-length'], 'A length measured across Lumen House A-101.'),
   (['03-run-length'], 'A run length along an external wall, with each part’s length shown.'),
   (['uc1-08-area-done'], 'A finished area round a room.'),
   (['03-void-depth'], 'An area with a void cut out and the depth filled in.'),
   (['03-quantities'], 'Quantities with this guide’s lengths and areas totalled.')]),
 '04': dict(cat='Revisions', em='drawing revisions', thumb=('04-traced', '35% 45%'), shots=[
   (['04-compare-box'], 'The Compare box with Lumen House Rev A and Rev B picked.'),
   (['04-traced'], 'Rev B with changes traced in blue and orange, and the What changed list.'),
   (['04-keep-dismiss'], 'The What changed list with some changes kept and some dismissed.'),
   (['04-clouded'], 'The newer revision with the kept changes clouded.')]),
 '05': dict(cat='Takeoff', em='to Excel', thumb=('05-quantities', '42% 45%'), shots=[
   (['uc1-10-count'], 'Numbered count dots on the Lumen House lighting plan.'),
   (['uc1-13-find-results'], 'Find Similar has outlined every downlight and counted them.'),
   (['uc1-14-register'], 'The Register grouped by type, with totals.'),
   (['uc1-15-export-menu'], 'The Export menu on the Register.')],
   extra={'Keep a spreadsheet up to date by itself': (['05-live-link'], 'The Live spreadsheet link section.')}),
}

_img = {}
def img(name):
    """Write 800/1600 WebP copies; return (src, srcset, w, h)."""
    if name in _img: return _img[name]
    p = f'guides/shots/{name}.webp'; im = Image.open(p)
    h8 = hashlib.md5(open(p, 'rb').read()).hexdigest()[:8]
    out = {}
    for w in (800, 1600):
        if im.width < w and w == 1600: continue
        fn = f'{name}-{h8}-{w}.webp'
        (im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)).save(os.path.join(A, fn), quality=84, method=6)
        out[w] = f'/assets/guides/{fn}'
    big = out.get(1600) or out[800]
    srcset = ', '.join(f'{u} {w}w' for w, u in out.items()) if im.width >= 1600 else f'{out[800]} 800w'
    r = _img[name] = (big, srcset, im.width, im.height)
    return r

def figure(names, cap, eager=False):
    parts = []
    for n in names:
        src, srcset, w, h = img(n)
        lazy = '' if eager else ' loading="lazy"'
        sizes = '(max-width: 900px) calc(100vw - 32px), 780px'
        parts.append(f'<div class="shot"><img src="{src}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{html.escape(cap.rstrip("."))}"{lazy} decoding="async"></div>')
    return f'<figure>{"".join(parts)}<figcaption class="cap">{html.escape(cap)}</figcaption></figure>'

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    def link(m):
        t, u = m.group(1), m.group(2)
        if u.startswith('./'): u = '/guides/' + u[2:]
        return f'<a href="{u}">{t}</a>'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, s)

def slugify(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

def parse(path):
    raw = open(path).read()
    head = re.search(r'<!--(.*?)-->', raw, re.S).group(1)
    m = lambda k: re.search(k + r':\s*(.+)', head).group(1).strip()
    g = dict(url=m('Web address'), title=m('Search title'), desc=m('Meta description'))
    g['slug'] = g['url'].rsplit('/', 1)[1]
    body = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
    g['h1'] = re.search(r'^# (.+)$', body, re.M).group(1)
    # split into intro + sections by "## "
    parts = re.split(r'^## (.+)$', body, flags=re.M)
    intro = [p.strip() for p in re.split(r'\n\s*\n', parts[0].split('\n', 2)[-1]) if p.strip() and not p.startswith('# ')]
    g['lede'] = intro[0]
    g['intro'] = [p for p in intro[1:] if not p.startswith(('This guide shows each step', 'This guide uses'))]
    g['sections'] = [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]
    return g

def blocks(text, shots, faq=False):
    """Markdown blocks -> HTML. Pops images from shots for each Screenshot line."""
    out = []
    for b in re.split(r'\n\s*\n', text.strip()):
        b = b.strip()
        if not b or b == '---': continue
        if b.startswith('**Screenshot:**'):
            if shots:
                names, cap = shots.pop(0); out.append(figure(names, cap))
            continue
        lines = b.split('\n')
        if all(re.match(r'- ', l) for l in lines):
            out.append('<ul>' + ''.join(f'<li>{inline(l[2:])}</li>' for l in lines) + '</ul>')
        elif all(re.match(r'\d+\. ', l) for l in lines):
            out.append('<ol>' + ''.join('<li>' + inline(re.sub(r'^\d+\. ', '', l)) + '</li>' for l in lines) + '</ol>')
        elif faq and lines[0].startswith('**') and lines[0].endswith('**') and len(lines) > 1:
            out.append(f'<h3>{inline(lines[0][2:-2])}</h3><p>{inline(" ".join(lines[1:]))}</p>')
        else:
            out.append(f'<p>{inline(" ".join(lines))}</p>')
    return '\n'.join(out)

CSS_HASH = None
def write_css():
    """Shared stylesheet for /guides pages (picked look: guides/mockup/mockup.html)."""
    fonts = {}
    for f in ('OpenSans-Light-latin.woff2', 'inter-latin-wght-normal.woff2'):
        p = f'kit/fonts/{f}'; h = hashlib.md5(open(p, 'rb').read()).hexdigest()[:8]
        n = f.replace('.woff2', f'-{h}.woff2'); open(os.path.join(A, n), 'wb').write(open(p, 'rb').read()); fonts[f] = n
    css = open('guides/guides.css').read().replace('__OPENSANS__', fonts['OpenSans-Light-latin.woff2']).replace('__INTER__', fonts['inter-latin-wght-normal.woff2'])
    h = hashlib.md5(css.encode()).hexdigest()[:8]
    open(os.path.join(A, f'guides-{h}.css'), 'w').write(css)
    return f'/assets/guides/guides-{h}.css', fonts

def mark():
    p = 'a/mark-m7-tight.png'; h = hashlib.md5(open(p, 'rb').read()).hexdigest()[:8]
    n = f'mark-{h}.png'; open(os.path.join(A, n), 'wb').write(open(p, 'rb').read())
    im = Image.open(p); return f'/assets/guides/{n}', im.width, im.height

def page(title, desc, path, og, ld, main, css, fonts, mk, active='guides'):
    url = SITE + path
    ldj = '\n'.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<link rel="icon" href="{FAVICON}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Thiran">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{SITE}{og}">
<link rel="preload" href="/assets/guides/{fonts['OpenSans-Light-latin.woff2']}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/guides/{fonts['inter-latin-wght-normal.woff2']}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@1,300&display=swap">
<link rel="stylesheet" href="{css}">
{ldj}
</head>
<body>
<header class="top"><div class="in">
 <a class="lock" href="/"><img src="{mk[0]}" width="{mk[1]}" height="{mk[2]}" alt="">thiran</a>
 <nav><a class="hs" href="/#job">Features</a><a class="hs" href="/#pricing">Pricing</a><a class="on" href="/guides">Guides</a><a class="hs" href="{APP}">Sign in</a><a class="ghost" href="/download">Download</a></nav>
</div></header>
{main}
<footer><div class="in"><span>Thiran by Tensi.ai · © 2026 Tensi Pty Ltd</span><span class="fl"><a href="/#job">Features</a> · <a href="/guides">Guides</a> · <a href="/#pricing">Pricing</a> · <a href="/download">Download</a> · <a href="{APP}/legal/#privacy">Privacy</a> · <a href="{APP}/legal/#terms">Terms</a></span></div></footer>
</body>
</html>
'''

def og_image(name):
    return f'/og/{name}.jpg'

ORG = {'@type': 'Organization', 'name': 'Tensi.ai', 'url': 'https://tensi.ai'}
CTA_BTN = f'<a class="pill" href="{APP}">Start your 7-day free trial</a>'

FAVICON = sys.argv[2] if len(sys.argv) > 2 else '/favicon.png'
css, fonts = write_css(); mk = mark()
guides = []
for path in sorted(glob.glob('guides/md/0*.md')):
    num = os.path.basename(path)[:2]; g = parse(path); g['num'] = num; g.update(META[num]); guides.append(g)

for g in guides:
    shots = list(g['shots']); extra = g.get('extra', {})
    toc, secs, steps, nxt, cta_text = [], [], 0, '', ''
    for i, (h, txt) in enumerate(g['sections']):
        if h.startswith('Try Thiran free'):
            for b in re.split(r'\n\s*\n', txt.strip()):
                b = b.strip()
                if b.startswith('**Next guide:**'):
                    mm = re.search(r'\[(.+?)\]\(\./(.+?)\)', b); nxt = (mm.group(1), mm.group(2))
                elif b and not b.startswith('**[') and not cta_text: cta_text = b
            continue
        sid = slugify(re.sub(r'^\d+\.\s*', '', h))
        if h == 'What you need':
            secs.append(f'<section id="{sid}" class="need"><h2>What you need</h2>{blocks(txt, shots)}</section>')
            toc.append((sid, h)); continue
        mm = re.match(r'(\d+)\.\s*(.+)', h)
        if mm:
            steps += 1
            hh = f'<h2><span class="n">{mm.group(1)}</span>{inline(mm.group(2))}</h2>'
        else:
            hh = f'<h2>{inline(h)}</h2>'
        body = blocks(txt, shots, faq=(h == 'Common questions'))
        if h in extra: body += figure(*extra[h])
        secs.append(f'<section id="{sid}" class="step">{hh}{body}</section>')
        toc.append((sid, h))
    assert not shots, (g['num'], shots)
    # first image on the page loads straight away
    main_html = '\n'.join(secs).replace(' loading="lazy"', '', 1)
    h1 = html.escape(g['h1'])
    if g['h1'].endswith(g['em']): h1 = html.escape(g['h1'][:-len(g['em'])]) + f'<em>{html.escape(g["em"])}</em>'
    chips = ([f'<span>{steps} steps</span>'] if steps else []) + ['<span>Mac, Windows and web</span>', '<span>Shown on the fictional Lumen House drawings</span>']
    if nxt: nb = f'<a class="next" href="/guides/{nxt[1]}"><span>Next guide</span><b>{html.escape(nxt[0])} →</b></a>'
    else: nb = '<a class="next" href="/guides"><span>More guides</span><b>See all guides →</b></a>'
    main = f'''<main>
<div class="crumb in"><a href="/guides">Guides</a> › <b>{html.escape((lambda s: s[0].upper() + s[1:])(g['h1'].replace('How to ', '')))}</b></div>
<div class="ghead in">
 <div class="ey">Guide {g['num']} · {g['cat']}</div>
 <h1>{h1}</h1>
 <p class="lede">{inline(g['lede'])}</p>
 {''.join(f'<p class="lede2">{inline(p)}</p>' for p in g['intro'])}
 <div class="meta">{''.join(chips)}</div>
</div>
<div class="gbody in">
 <aside class="toc"><p class="ey">On this page</p>{''.join(f'<a href="#{s}">{html.escape(t)}</a>' for s, t in toc)}<a class="pill" href="{APP}">Try free for 7 days</a></aside>
 <article>
{main_html}
<div class="cta"><div><h2>Try Thiran free <em>for 7 days</em></h2><p>{inline(cta_text)}</p></div>{CTA_BTN}</div>
{nb}
 </article>
</div>
</main>
<script>
(()=>{{const a=[...document.querySelectorAll('.toc a[href^="#"]')],s=a.map(x=>document.getElementById(x.getAttribute('href').slice(1)));
const f=()=>{{let k=0;s.forEach((e,i)=>{{if(e.getBoundingClientRect().top<140)k=i}});a.forEach((x,i)=>x.classList.toggle('on',i===k))}};addEventListener('scroll',f,{{passive:true}});f()}})();
</script>'''
    path = f'/guides/{g["slug"]}'
    ld = [{'@context': 'https://schema.org', '@type': 'Article', 'headline': g['h1'], 'description': g['desc'],
           'image': SITE + og_image(f'guide-{g["num"]}'), 'datePublished': DATE, 'dateModified': DATE,
           'author': ORG, 'publisher': ORG, 'mainEntityOfPage': SITE + path, 'inLanguage': 'en'},
          {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
           {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
           {'@type': 'ListItem', 'position': 2, 'name': 'Guides', 'item': SITE + '/guides'},
           {'@type': 'ListItem', 'position': 3, 'name': g['h1'], 'item': SITE + path}]}]
    open(os.path.join(G, g['slug'] + '.html'), 'w').write(page(g['title'], g['desc'], path, og_image(f'guide-{g["num"]}'), ld, main, css, fonts, mk))

# /guides index
src, srcset, w, h = img('dark-04-clouded')
cards = []
for g in guides:
    t, pos = g['thumb']; ts, tss, tw, th = img(t)
    cards.append(f'''<a class="card" data-cat="{g['cat']}" href="/guides/{g['slug']}"><div class="th"><img src="{_img[t][1].split(' ')[0]}" width="{tw}" height="{th}" style="object-position:{pos}" alt="" loading="lazy" decoding="async"></div><div class="cb"><div class="ey">{g['num']} · {g['cat']}</div><h3>{html.escape(g['h1'])}</h3><p>{html.escape(g['desc'].replace(' Step-by-step guide.', '').replace(' Step by step.', ''))}</p><div class="go">Read guide →</div></div></a>''')
cats = ['Markup', 'Measure', 'Revisions', 'Takeoff']
idx_desc = 'Step-by-step guides for PDF drawings: mark up, redline, set the scale, measure, compare revisions and count symbols on construction drawings.'
main = f'''<main>
<div class="ihero in">
 <div class="ey">Guides</div>
 <h1>Step-by-step guides for <em>PDF drawings</em></h1>
 <p class="lede">Short how-tos for marking up, measuring and comparing construction drawings. Every step is shown on real Thiran screens.</p>
 {CTA_BTN}
</div>
<div class="dark in"><img src="{src}" srcset="{srcset}" sizes="(max-width: 1280px) calc(100vw - 32px), 1184px" width="{w}" height="{h}" alt="Thiran in dark mode with the changes between two drawing revisions clouded" fetchpriority="high"></div>
<div class="ibody in">
 <div class="row"><h2>All guides</h2><div class="chips" role="group" aria-label="Filter guides"><button class="on" data-f="">All</button>{''.join(f'<button data-f="{c}">{c}</button>' for c in cats)}</div></div>
 <div class="grid">{''.join(cards)}<div class="card soon">More guides on the way</div></div>
</div>
<div class="band in"><div><h2>Try Thiran free <em>for 7 days</em></h2><p>Every tool in these guides, on Mac, Windows and the web.</p></div>{CTA_BTN}</div>
</main>
<script>
document.querySelectorAll('.chips button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.chips button').forEach(x=>x.classList.toggle('on',x===b));
document.querySelectorAll('.grid .card[data-cat]').forEach(c=>c.hidden=!!b.dataset.f&&c.dataset.cat!==b.dataset.f)}});
</script>'''
ld = [{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Thiran guides', 'url': SITE + '/guides', 'description': idx_desc, 'inLanguage': 'en', 'publisher': ORG,
       'hasPart': [{'@type': 'Article', 'headline': g['h1'], 'url': f'{SITE}/guides/{g["slug"]}'} for g in guides]},
      {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
       {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
       {'@type': 'ListItem', 'position': 2, 'name': 'Guides', 'item': SITE + '/guides'}]}]
open(os.path.join(G, 'index.html'), 'w').write(page('Guides to PDF markup and takeoff | Thiran', idx_desc, '/guides', og_image('guides'), ld, main, css, fonts, mk))

# list for sitemap, llms.txt and the OG image maker
json.dump([{'num': g['num'], 'slug': g['slug'], 'h1': g['h1'], 'desc': g['desc'], 'cat': g['cat'], 'thumb': g['thumb'][0]} for g in guides],
          open('.guides.json', 'w'))
print('guides:', len(guides))
