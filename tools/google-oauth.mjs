// One-time: get a Google refresh token for we@tensi.ai and store it (with the OAuth client)
// in Vercel env for project thiran-website. Google secrets are never printed or written to disk.
// Usage: node tools/google-oauth.mjs ~/Downloads/client_secret_XXXX.json
import http from 'node:http';
import { readFileSync, writeFileSync } from 'node:fs';
import { spawnSync, execFileSync } from 'node:child_process';
import { randomBytes } from 'node:crypto';

const SITE = new URL('../site', import.meta.url).pathname;
const file = process.argv[2];
if (!file) { console.error('Give the downloaded client JSON file.'); process.exit(1); }
const c = JSON.parse(readFileSync(file, 'utf8')).installed;
if (!c) { console.error('That file is not a "Desktop app" OAuth client.'); process.exit(1); }

const PORT = 53682, REDIRECT = `http://127.0.0.1:${PORT}`;
const SCOPES = ['https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar.freebusy', 'https://www.googleapis.com/auth/gmail.send'];
const state = randomBytes(12).toString('hex');
const auth = 'https://accounts.google.com/o/oauth2/v2/auth?' + new URLSearchParams({
  client_id: c.client_id, redirect_uri: REDIRECT, response_type: 'code', scope: SCOPES.join(' '),
  access_type: 'offline', prompt: 'consent', login_hint: 'we@tensi.ai', state,
});

function envAdd(name, value) {
  for (const target of ['production', 'preview']) {
    const r = spawnSync('vercel', ['env', 'add', name, target, ...(target === 'preview' ? [''] : []), '--force', '--yes', '--scope', 'tensi'], { cwd: SITE, input: value, encoding: 'utf8' });
    if (r.status !== 0) { console.error(`Could not save ${name} (${target}):`, (r.stderr || '').split('\n').filter(l => !l.includes(value)).slice(-3).join(' ')); process.exit(1); }
  }
  console.log('Saved', name);
}

const srv = http.createServer(async (req, res) => {
  const u = new URL(req.url, REDIRECT);
  if (!u.searchParams.has('code') && !u.searchParams.has('error')) { res.end(); return; }
  if (u.searchParams.get('state') !== state || u.searchParams.get('error')) {
    res.end('Something went wrong (' + (u.searchParams.get('error') || 'state') + '). You can close this tab.'); console.error('Sign-in failed:', u.searchParams.get('error') || 'state mismatch'); srv.close(); return;
  }
  try {
    const t = await (await fetch('https://oauth2.googleapis.com/token', { method: 'POST', body: new URLSearchParams({ code: u.searchParams.get('code'), client_id: c.client_id, client_secret: c.client_secret, redirect_uri: REDIRECT, grant_type: 'authorization_code' }) })).json();
    if (!t.refresh_token) throw new Error('no refresh token (' + (t.error || 'unknown') + ')');
    const granted = (t.scope || '').split(' ');
    const missing = SCOPES.filter(s => !granted.includes(s));
    if (missing.length) throw new Error('these permissions were not ticked: ' + missing.map(s => s.split('/').pop()).join(', '));
    // check it is really we@tensi.ai, via the calendar it can see
    const cal = await (await fetch('https://www.googleapis.com/calendar/v3/calendars/primary/events?maxResults=1', { headers: { authorization: 'Bearer ' + t.access_token } })).json();
    const who = cal.summary || '?';
    if (who.toLowerCase() !== 'we@tensi.ai') throw new Error('signed in as ' + who + ', not we@tensi.ai');
    res.end('Done. Thiran can now see free times and book demos in the we@tensi.ai calendar. You can close this tab.');
    console.log('Signed in as', who);
    envAdd('GOOGLE_CLIENT_ID', c.client_id);
    envAdd('GOOGLE_CLIENT_SECRET', c.client_secret);
    envAdd('GOOGLE_REFRESH_TOKEN', t.refresh_token);
    const cron = randomBytes(24).toString('hex'); envAdd('CRON_SECRET', cron);
    if (process.env.CRON_COPY) writeFileSync(process.env.CRON_COPY, cron, { mode: 0o600 }); // our own random value, for testing the reminder
    console.log('All saved.');
  } catch (e) {
    res.end('Something went wrong: ' + e.message + '. You can close this tab.'); console.error('Failed:', e.message);
  }
  srv.close();
});
srv.listen(PORT, '127.0.0.1', () => {
  console.log('Opening the Google sign-in page…');
  execFileSync('open', [auth]);
});
