// POST /api/book  { start, name, email, company, role, notes, tz, hp, token }
// Re-checks the time is free, then creates the event in we@tensi.ai's calendar with a Meet
// link and the visitor as guest. Google emails the invite (sendUpdates=all).
const { RULES, CAL, freeSlots, g, limited, ipOf, turnstileOk, send } = require('./_lib/demo');

const clean = (v, n) => String(v ?? '').replace(/[\u0000-\u001f\u007f<>]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, n);
const ROLES = ['Estimating and takeoff', 'Drawing review', 'Site and supervision', 'HVAC', 'Something else'];

async function readBody(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  let raw = '';
  for await (const c of req) { raw += c; if (raw.length > 8000) throw new Error('big'); }
  return JSON.parse(raw || '{}');
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') return send(res, 405, { error: 'method' });
  const ip = ipOf(req);
  if (limited('b:' + ip, 5, 10 * 60e3)) return send(res, 429, { error: 'busy', msg: 'Too many tries. Please wait a few minutes.' });
  let b;
  try { b = await readBody(req); } catch { return send(res, 400, { error: 'body' }); }

  // honeypot: bots fill the hidden field. Say nothing useful.
  if (b.hp) return send(res, 400, { error: 'check' });

  const name = clean(b.name, 80), email = clean(b.email, 120).toLowerCase(), company = clean(b.company, 120);
  const role = ROLES.includes(b.role) ? b.role : '', notes = String(b.notes ?? '').replace(/[\u0000-\u0008\u000b-\u001f\u007f<>]/g, ' ').trim().slice(0, 1000);
  let tz = clean(b.tz, 60);
  try { new Intl.DateTimeFormat('en', { timeZone: tz }); } catch { tz = 'Australia/Sydney'; }
  const teams = b.via === 'teams';
  const start = Date.parse(b.start);
  if (name.length < 2 || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || !Number.isFinite(start))
    return send(res, 400, { error: 'fields', msg: 'Please check your name and email.' });

  if (!(await turnstileOk(b.token, ip))) return send(res, 400, { error: 'check', msg: 'The spam check didn’t pass. Please try again.' });

  try {
    // at most 2 upcoming demos per email
    const mine = await g(`/calendars/${encodeURIComponent(CAL())}/events`, { query: { privateExtendedProperty: ['thiranDemo=1', 'email=' + email], timeMin: new Date().toISOString(), singleEvents: 'true', maxResults: '5' } });
    if ((mine.items || []).filter(e => e.status !== 'cancelled').length >= 2)
      return send(res, 409, { error: 'limit', msg: 'You already have demos booked. Reply to your invite to change one.' });

    // still free?
    const free = await freeSlots();
    if (!free.some(s => s.getTime() === start)) return send(res, 409, { error: 'taken', msg: 'Sorry, that time was just taken. Please pick another.' });

    const s = new Date(start), e = new Date(start + RULES.len * 6e4);
    const desc = [
      'Booked on thiran.app.', '',
      'Name: ' + name, 'Email: ' + email,
      company && 'Company: ' + company,
      role && 'Works on: ' + role,
      'Meeting: ' + (teams ? 'MICROSOFT TEAMS. Please email them a Teams link before the call.' : 'Google Meet (link in this invite)'),
      'Their time zone: ' + tz,
      notes && '\nNotes:\n' + notes,
    ].filter(Boolean).join('\n');
    const ev = await g(`/calendars/${encodeURIComponent(CAL())}/events`, {
      method: 'POST',
      query: { conferenceDataVersion: '1', sendUpdates: 'all' },
      body: {
        summary: `Thiran demo${teams ? ' (TEAMS: send link)' : ''}: ${name}${company ? ' (' + company + ')' : ''}`,
        description: desc,
        start: { dateTime: s.toISOString(), timeZone: 'Australia/Sydney' },
        end: { dateTime: e.toISOString(), timeZone: 'Australia/Sydney' },
        attendees: [{ email, displayName: name }],
        guestsCanSeeOtherGuests: false, guestsCanInviteOthers: false,
        ...(teams ? { location: 'Microsoft Teams (we will email you the link)' } : {}),
        ...(teams ? {} : { conferenceData: { createRequest: { requestId: 'thiran-' + start + '-' + Math.random().toString(36).slice(2, 10), conferenceSolutionKey: { type: 'hangoutsMeet' } } } }),
        extendedProperties: { private: { thiranDemo: '1', email, tz, reminded: '0', via: teams ? 'teams' : 'meet' } },
        reminders: { useDefault: true },
      },
    });
    send(res, 200, { ok: true, start: s.toISOString(), end: e.toISOString(), meet: !!ev.hangoutLink, via: teams ? 'teams' : 'meet' });
  } catch (err) {
    console.error('book', err.message);
    send(res, 502, { error: 'calendar', msg: 'We couldn’t book that just now. Please try again in a minute.' });
  }
};
