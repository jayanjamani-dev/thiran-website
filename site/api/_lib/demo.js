// Shared code for the Book a demo functions. Secrets come only from Vercel env:
// GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN (we@tensi.ai),
// TURNSTILE_SITE_KEY + TURNSTILE_SECRET (optional), CRON_SECRET, DEMO_CALENDAR_ID (default primary).

const HOST_TZ = 'Australia/Sydney';
const RULES = {
  days: [0, 1, 2, 3, 4, 5, 6],  // every day, weekends too (Jay, 13 Nov)
  windows: [[9 * 60, 17 * 60], [18 * 60, 21 * 60]], // 9am–5pm and 6–9pm Sydney (evening suits Europe), in minutes
  len: 20, gap: 10,             // 20-minute call, 10 minutes clear either side
  step: 30,                     // a start every 30 minutes
  notice: 12 * 60,              // earliest booking: 12 hours from now
  ahead: 21,                    // up to 3 weeks ahead
};
const CAL = () => process.env.DEMO_CALENDAR_ID || 'primary';

// ---- time helpers (no libraries) ----
function tzOffset(tz, d) {
  const o = {};
  new Intl.DateTimeFormat('en-US', { timeZone: tz, hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' })
    .formatToParts(d).forEach(p => (o[p.type] = p.value));
  return Date.UTC(+o.year, o.month - 1, +o.day, +o.hour % 24, +o.minute, +o.second) - d.getTime();
}
// a wall-clock time in Sydney -> real Date
function hostTime(y, m, d, min) {
  const g = Date.UTC(y, m, d, 0, min);
  let t = g - tzOffset(HOST_TZ, new Date(g));
  return new Date(g - tzOffset(HOST_TZ, new Date(t))); // second pass settles DST edges
}
function hostDate(d) { // {y,m,d,wd} of a Date in Sydney
  const p = {};
  new Intl.DateTimeFormat('en-US', { timeZone: HOST_TZ, year: 'numeric', month: 'numeric', day: 'numeric', weekday: 'short' })
    .formatToParts(d).forEach(x => (p[x.type] = x.value));
  return { y: +p.year, m: +p.month - 1, d: +p.day, wd: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(p.weekday) };
}

// every start time the rules allow, before checking the calendar
function candidateSlots(now = new Date()) {
  const out = [], first = now.getTime() + RULES.notice * 6e4, last = now.getTime() + RULES.ahead * 864e5;
  const t = hostDate(now);
  for (let i = 0; i <= RULES.ahead + 1; i++) {
    const day = new Date(Date.UTC(t.y, t.m, t.d + i, 12));
    const y = day.getUTCFullYear(), m = day.getUTCMonth(), d = day.getUTCDate();
    if (!RULES.days.includes(day.getUTCDay())) continue;
    for (const [ws, we] of RULES.windows) for (let min = ws; min + RULES.len <= we; min += RULES.step) {
      const s = hostTime(y, m, d, min);
      if (s.getTime() >= first && s.getTime() <= last) out.push(s);
    }
  }
  return out;
}

// ---- Google ----
let tok = { v: null, exp: 0 };
async function accessToken() {
  if (tok.v && Date.now() < tok.exp - 60e3) return tok.v;
  const r = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST', headers: { 'content-type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ client_id: process.env.GOOGLE_CLIENT_ID, client_secret: process.env.GOOGLE_CLIENT_SECRET, refresh_token: process.env.GOOGLE_REFRESH_TOKEN, grant_type: 'refresh_token' }),
  });
  const j = await r.json();
  if (!r.ok) throw new Error('google token ' + r.status + ' ' + (j.error || ''));
  tok = { v: j.access_token, exp: Date.now() + j.expires_in * 1000 };
  return tok.v;
}
async function g(path, { method = 'GET', body, query } = {}) {
  const u = new URL(path.startsWith('http') ? path : 'https://www.googleapis.com/calendar/v3' + path);
  if (query) Object.entries(query).forEach(([k, v]) => [].concat(v).forEach(x => u.searchParams.append(k, x)));
  const r = await fetch(u, { method, headers: { authorization: 'Bearer ' + (await accessToken()), 'content-type': 'application/json' }, body: body && JSON.stringify(body) });
  const j = r.status === 204 ? {} : await r.json();
  if (!r.ok) throw new Error(`google ${method} ${u.pathname} ${r.status} ${j.error?.message || ''}`);
  return j;
}
async function busy(from, to) {
  const j = await g('/freeBusy', { method: 'POST', body: { timeMin: from.toISOString(), timeMax: to.toISOString(), timeZone: 'UTC', items: [{ id: CAL() }] } });
  return Object.values(j.calendars || {}).flatMap(c => c.busy || []).map(b => [Date.parse(b.start), Date.parse(b.end)]);
}
// free slots = candidates with nothing busy within the call plus the gap either side
async function freeSlots(now = new Date()) {
  const c = candidateSlots(now);
  if (!c.length) return [];
  const pad = RULES.gap * 6e4, len = RULES.len * 6e4;
  const b = await busy(new Date(c[0].getTime() - pad), new Date(c[c.length - 1].getTime() + len + pad));
  return c.filter(s => { const a = s.getTime() - pad, z = s.getTime() + len + pad; return !b.some(([bs, be]) => bs < z && be > a); });
}

// ---- small guards ----
const hits = new Map(); // per-instance rate limit (Fluid Compute reuses instances)
function limited(key, max, windowMs) {
  const now = Date.now(), h = (hits.get(key) || []).filter(t => now - t < windowMs);
  h.push(now); hits.set(key, h);
  if (hits.size > 5000) hits.clear();
  return h.length > max;
}
const ipOf = req => String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'x';

async function turnstileOk(token, ip) {
  if (!process.env.TURNSTILE_SECRET) return true; // not switched on yet
  if (!token) return false;
  const r = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', { method: 'POST', body: new URLSearchParams({ secret: process.env.TURNSTILE_SECRET, response: token, remoteip: ip }) });
  return !!(await r.json()).success;
}

function send(res, code, obj) {
  res.statusCode = code;
  res.setHeader('content-type', 'application/json; charset=utf-8');
  res.setHeader('cache-control', 'no-store');
  res.end(JSON.stringify(obj));
}

module.exports = { HOST_TZ, RULES, CAL, freeSlots, g, accessToken, limited, ipOf, turnstileOk, send };
