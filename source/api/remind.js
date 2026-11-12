// Daily cron (vercel.json): emails each guest a reminder about their demo in the next ~26 hours,
// sent from we@tensi.ai through Gmail. Vercel calls it with "Authorization: Bearer CRON_SECRET".
const { CAL, g, send } = require('./_lib/demo');

const b64url = s => Buffer.from(s, 'utf8').toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const hdr = s => /^[\x20-\x7e]*$/.test(s) ? s : '=?UTF-8?B?' + Buffer.from(s, 'utf8').toString('base64') + '?=';

module.exports = async (req, res) => {
  if (!process.env.CRON_SECRET || req.headers.authorization !== 'Bearer ' + process.env.CRON_SECRET) return send(res, 401, { error: 'auth' });
  const now = Date.now(), sent = [];
  try {
    const list = await g(`/calendars/${encodeURIComponent(CAL())}/events`, { query: { privateExtendedProperty: ['thiranDemo=1', 'reminded=0'], timeMin: new Date(now + 60 * 6e4).toISOString(), timeMax: new Date(now + 26 * 36e5).toISOString(), singleEvents: 'true', maxResults: '50' } });
    for (const ev of list.items || []) {
      const p = ev.extendedProperties?.private || {}, guest = (ev.attendees || []).find(a => a.email === p.email);
      if (ev.status === 'cancelled' || !guest || guest.responseStatus === 'declined') continue;
      const tz = p.tz || 'Australia/Sydney', s = new Date(ev.start.dateTime), e = new Date(ev.end.dateTime);
      const day = s.toLocaleDateString('en-AU', { timeZone: tz, weekday: 'long', day: 'numeric', month: 'long' });
      const t = d => d.toLocaleTimeString('en-AU', { timeZone: tz, hour: 'numeric', minute: '2-digit' });
      const first = (guest.displayName || '').split(' ')[0];
      const body = [
        `Hi${first ? ' ' + first : ''},`, '',
        `A quick reminder of your Thiran demo:`, '',
        `${day}, ${t(s)} – ${t(e)} (${tz.replace(/_/g, ' ')})`,
        ev.hangoutLink ? `Join with Google Meet: ${ev.hangoutLink}` : '', '',
        `Bring a PDF drawing you work with and we'll mark up, measure and count on it together.`,
        `Need another time? Just reply to this email.`, '',
        `The Thiran team`, `https://thiran.app`,
      ].join('\r\n');
      const mime = [`To: ${guest.email}`, `Subject: ${hdr(`Reminder: your Thiran demo, ${day}`)}`, 'MIME-Version: 1.0', 'Content-Type: text/plain; charset=UTF-8', 'Content-Transfer-Encoding: 8bit', '', body].join('\r\n');
      await g('https://gmail.googleapis.com/gmail/v1/users/me/messages/send', { method: 'POST', body: { raw: b64url(mime) } });
      await g(`/calendars/${encodeURIComponent(CAL())}/events/${ev.id}`, { method: 'PATCH', query: { sendUpdates: 'none' }, body: { extendedProperties: { private: { ...p, reminded: '1' } } } });
      sent.push(ev.id);
    }
    send(res, 200, { ok: true, sent: sent.length });
  } catch (err) {
    console.error('remind', err.message);
    send(res, 502, { error: 'failed' });
  }
};
