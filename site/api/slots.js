// GET /api/slots -> { len, slots: [ISO start times, UTC], siteKey }
const { RULES, freeSlots, limited, ipOf, send } = require('./_lib/demo');

module.exports = async (req, res) => {
  if (req.method !== 'GET') return send(res, 405, { error: 'method' });
  if (limited('s:' + ipOf(req), 30, 60e3)) return send(res, 429, { error: 'busy' });
  try {
    const s = await freeSlots();
    send(res, 200, { len: RULES.len, slots: s.map(d => d.toISOString()), siteKey: process.env.TURNSTILE_SITE_KEY || '' });
  } catch (e) {
    console.error('slots', e.message);
    send(res, 502, { error: 'calendar' });
  }
};
