// One-time: connect Microsoft Teams for Book a demo. Jay runs this in their own Terminal and
// types the answers; the secret is hidden while typing and is never printed or saved on disk.
// It checks the details by making (and deleting) a test Teams meeting, then saves to Vercel env.
// Usage: node tools/ms-setup.mjs
import readline from 'node:readline';
import { spawnSync } from 'node:child_process';

const SITE = new URL('../site', import.meta.url).pathname;
const rl = readline.createInterface({ input: process.stdin, output: process.stdout, terminal: true });
let mute = false;
rl._writeToOutput = s => { if (!mute || s.includes('\n')) rl.output.write(mute ? '\n' : s); };
const ask = (q, hidden) => new Promise(r => { rl.output.write(q); mute = !!hidden; rl.question('', a => { mute = false; r(a.trim()); }); });

const tenant = await ask('Directory (tenant) ID: ');
const client = await ask('Application (client) ID: ');
const secret = await ask('Client secret VALUE (hidden while you paste): ', true);
const mailbox = (await ask('Teams account email (e.g. we@tensi.com.au): ')).toLowerCase();
rl.close();

try {
  const t = await (await fetch(`https://login.microsoftonline.com/${encodeURIComponent(tenant)}/oauth2/v2.0/token`, { method: 'POST', body: new URLSearchParams({ client_id: client, client_secret: secret, scope: 'https://graph.microsoft.com/.default', grant_type: 'client_credentials' }) })).json();
  if (!t.access_token) throw new Error('sign-in refused: ' + (t.error_description || t.error || '').split('\n')[0]);
  const h = { authorization: 'Bearer ' + t.access_token, 'content-type': 'application/json' };
  const start = new Date(Date.now() + 30 * 864e5);
  const r = await fetch(`https://graph.microsoft.com/v1.0/users/${encodeURIComponent(mailbox)}/events`, { method: 'POST', headers: h, body: JSON.stringify({ subject: 'Thiran setup test (deleting)', start: { dateTime: start.toISOString().slice(0, 19), timeZone: 'UTC' }, end: { dateTime: new Date(+start + 20 * 6e4).toISOString().slice(0, 19), timeZone: 'UTC' }, isOnlineMeeting: true, onlineMeetingProvider: 'teamsForBusiness', showAs: 'free', isReminderOn: false }) });
  const ev = await r.json();
  if (!r.ok) throw new Error('could not make a test meeting: ' + (ev.error?.message || r.status));
  await fetch(`https://graph.microsoft.com/v1.0/users/${encodeURIComponent(mailbox)}/events/${ev.id}`, { method: 'DELETE', headers: h });
  if (!ev.onlineMeeting?.joinUrl) throw new Error('the test meeting had no Teams link. Does ' + mailbox + ' have a Teams licence?');
  console.log('Test Teams meeting made and deleted. Saving to Vercel…');
  for (const [k, v] of [['MS_TENANT_ID', tenant], ['MS_CLIENT_ID', client], ['MS_CLIENT_SECRET', secret], ['MS_TEAMS_MAILBOX', mailbox]]) {
    for (const target of ['production', 'preview']) {
      const s = spawnSync('vercel', ['env', 'add', k, target, ...(target === 'preview' ? [''] : []), '--force', '--yes', '--scope', 'tensi'], { cwd: SITE, input: v, encoding: 'utf8' });
      if (s.status !== 0) throw new Error('could not save ' + k + ' to Vercel');
    }
    console.log('Saved', k);
  }
  console.log('All done. Tell Claude "Teams is connected".');
} catch (e) {
  console.error('Stopped:', e.message);
  process.exit(1);
}
