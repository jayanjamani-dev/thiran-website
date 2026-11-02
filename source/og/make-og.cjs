// Makes the 1200x630 link preview pictures in source/og/ from real Thiran screens.
// Run after ./build.sh:  node source/og/make-og.cjs   (needs Playwright; uses the one in ../tensi-markup)
const path = require('path'), fs = require('fs');
const { chromium } = require(process.env.PW || path.resolve(__dirname, '../../../tensi-markup/node_modules/playwright'));
const SRC = path.resolve(__dirname, '..'), OUT = __dirname;
const guides = JSON.parse(fs.readFileSync(path.join(SRC, '.guides.json')));
const f = p => 'file://' + path.join(SRC, p);
const cards = [
  { name: 'home', ey: 'PDF markup and takeoff', title: 'PDF markup software for <em>construction drawings</em>', shot: 'guides/shots/01-cloud-callout.webp', pos: '47% 42%', zoom: 1.7 },
  { name: 'guides', ey: 'Guides', title: 'Step-by-step guides for <em>PDF drawings</em>', shot: 'guides/shots/dark-04-clouded.webp', pos: '30% 40%', zoom: 1.5 },
  ...guides.map(g => ({ name: 'guide-' + g.num, ey: `Guide ${g.num} · ${g.cat}`, title: g.h1, shot: `guides/shots/${g.thumb}.webp`, pos: '45% 45%', zoom: 1.7 })),
];
const html = c => `<!doctype html><html><head><style>
@font-face{font-family:T;src:url(${f('kit/fonts/OpenSans-Light-latin.woff2')})}
@font-face{font-family:I;src:url(${f('kit/fonts/inter-latin-wght-normal.woff2')});font-weight:100 900}
*{margin:0;box-sizing:border-box}body{width:1200px;height:630px;background:#F7F4EF;font-family:I;color:#2A1D14;display:flex;overflow:hidden}
.l{width:520px;padding:56px 40px 56px 64px;display:flex;flex-direction:column;justify-content:space-between}
.lock{display:flex;align-items:center;gap:12px;font:300 34px T}.lock img{height:36px}
.ey{font:600 15px I;letter-spacing:.14em;text-transform:uppercase;color:#B8511A;margin-bottom:18px}
h1{font:300 50px/1.12 T;letter-spacing:-.01em}em{font-style:italic;color:#B8511A}
.u{font:500 18px I;color:#6E6158}
.r{flex:1;padding:56px 0 56px 0;position:relative}
.s{position:absolute;left:0;top:56px;bottom:56px;right:-40px;border-radius:18px 0 0 18px;overflow:hidden;box-shadow:0 30px 60px rgba(42,29,20,.25);background:#fff}
.s img{width:100%;height:100%;object-fit:cover;object-position:${c.pos};transform:scale(${c.zoom});transform-origin:${c.pos}}
</style></head><body><div class="l"><div class="lock"><img src="${f('a/mark-m7-tight.png')}">thiran</div>
<div><div class="ey">${c.ey}</div><h1>${c.title}</h1></div><div class="u">thiran.app · Mac, Windows and web</div></div>
<div class="r"><div class="s"><img src="${f(c.shot)}"></div></div></body></html>`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  for (const c of cards) {
    const tmp = path.join(OUT, '.tmp.html'); fs.writeFileSync(tmp, html(c));
    await p.goto('file://' + tmp); await p.waitForTimeout(300);
    await p.screenshot({ path: path.join(OUT, c.name + '.jpg'), type: 'jpeg', quality: 88 });
    fs.unlinkSync(tmp); console.log('og', c.name);
  }
  await b.close();
})();
