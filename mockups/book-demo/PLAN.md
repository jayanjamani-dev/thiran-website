# Book a demo: our own build (no paid tools)

## LIVE 13 Nov 2026 (Jay: "yes put it live")
- Production deploy thiran-website-64vxwc2u1-tensi.vercel.app, aliased to https://thiran.app. book-demo merged into main (fast-forward to 512f694) and pushed.
- Live check: /api/slots gave 447 free times (every day, 9-5 plus 6-9pm Sydney); booker, fixed frosted menu and the world time zone list (406) show in light and dark mode; reminder refuses without the secret (401); honeypot refused (400). The daily reminder runs at 8am Sydney from now on.
- Still for Jay: confirm the test invites/reminder reached jay@tensi.com.au, then cancel "Jay Test" and "Jay Teams Test" (Fri 4 Dec 11:00 and 11:30). Optional later: Turnstile, Gmail "Send mail as" we@tensi.ai.

## (earlier) STATUS 13 Nov 2026: built, on a test link, waiting for Jay to try it
- **Branch `book-demo`** in ~/motion_graphics/thiran-website (commits d57df55, 3393845). Not merged and not live.
- **Test link:** https://thiran-website-d5htjpz8h-tensi.vercel.app/#demo (behind the Vercel sign-in).
- **Hours (updated 13 Nov):** every day, 9–5 and 6–9pm Sydney, 20-minute calls, 10 minutes clear either side, up to 3 weeks ahead, earliest booking 12 hours from now. These are set in `source/api/_lib/demo.js` (RULES).
- **Code:** `source/book-demo.part.html` holds the booker (the picked interactive.html look, scoped under #demo, with dark mode). `buildsite.py` puts it in place of `__BOOKDEMO__` above Pricing, and the nav has a "Book a demo" outline button (hidden on phones). Functions are in `source/api/`: `slots.js`, `book.js` and `remind.js`, with a daily cron at 21:00 UTC (8am Sydney). `build.sh` copies them to site/api.
- **Google:** project "thiran-demos" in the tensi.com.au organisation, Internal audience, Desktop client. **we@tensi.ai is an alias of the mailbox we@tensi.com.au**, so invites show we@tensi.com.au as organiser. Reminders say From "Thiran <we@tensi.ai>" (Gmail keeps that only if it's set up under "Send mail as"), with Reply-To we@tensi.ai. Vercel env (Production + Preview): GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN, CRON_SECRET. To redo the sign-in: `node tools/google-oauth.mjs <client json>`.
- **Spam:** honeypot, a per-visitor try limit, and at most 2 upcoming demos per email. Cloudflare Turnstile is built in but off; set TURNSTILE_SITE_KEY + TURNSTILE_SECRET in Vercel env to turn it on (needs a free Cloudflare account, Jay's call).
- **Tested 13 Nov:** /api/slots returned real free times (229, busy times removed). A test booking for jay@tensi.com.au on Fri 4 Dec, 11:00 Sydney, came back with a Meet link, and that time disappeared. The reminder sent once and not twice. The bot trap is refused, and the cron is refused without the secret. The UI flow was checked locally with pretend times. **Jay to confirm** that the invite and reminder arrived in jay@tensi.com.au and that the Meet link opens, then cancel the test event.
- **13 Nov, round 2:** dark-mode time zone list fixed. **Meet or Teams choice** added to the form (Jay's pick): a Teams booking gets no Meet link, the event is titled "Thiran demo (TEAMS: send link): Name", and Jay emails a Teams link from their personal Hotmail account by hand. There's no Microsoft connection, because Teams is on a personal account. **Top menu option A** (Jay's pick, mockups/nav-menu/menu-options.png): links centred; Sign in, a "Book a demo" text link and an orange "Start free trial" on the right, then the theme icon. The hero keeps "Start your 7-day free trial" and adds Download beside it. Test link: https://thiran-website-pmdyc0y8o-tensi.vercel.app. A Teams test booking (jay+teams@tensi.com.au, 4 Dec 11:30 Sydney) came back with no Meet link, and that time disappeared.
- **Top menu, final pick (H, 13 Nov; mockups/nav-menu/menu-layout-h.png):** left has Features, Pricing, Guides and Download (as a link); right has Sign in, a "Book a demo" outline button and the theme icon. There's no trial button in the menu: the hero keeps one centred "Start your 7-day free trial", and Download is gone from the hero. Test link: https://thiran-website-d5htjpz8h-tensi.vercel.app
- **13 Nov, round 3:** the menu stays fixed at the top as you scroll (frosted bar after scrolling) and is the same width as the other pages, with even space above and below the hero text. The time zone list now has every zone grouped by region, with the visitor's own zone first. **Hours are now every day, weekends included, 9am–5pm plus 6–9pm Sydney** (the evening suits Europe). Test link: https://thiran-website-8ksallktf-tensi.vercel.app
- **Go live (only on Jay's yes):** `PATH=/usr/bin:$PATH ./build.sh && cd site && vercel link --yes --project thiran-website --scope tensi && rm -f .gitignore && vercel deploy --prod --scope tensi`, then merge book-demo into main and push. The cron runs only on production.

## HANDOVER (12 Nov 2026): start here
- **Look PICKED:** `interactive.html` (built from `interactive.src.html`, which has placeholders for the fonts and logo; the pictures are in steps.png). It takes Cal.com's layout as inspiration only. Jay wants booking to feel exciting, so keep every animation. The older still `mockup.html`/`mockup.png` is superseded.
- **Demos go to `we@tensi.ai`.** tensi.ai is on Google Workspace (its mail runs through Google), so use Google OAuth for that account. Make an internal OAuth consent screen if Jay is a Workspace admin, so the token doesn't expire after 7 days the way a test-mode one does. Scopes: calendar.events, calendar.freebusy (or calendar.readonly), gmail.send.
- **No paid tools.** No Calendly, no Cal.com cloud, and no self-hosted Cal.com (AGPL).
- **Still to confirm with Jay:** working hours (assumed Mon–Fri 9–5 Sydney), call length (20 min), how far ahead people can book (assumed 3 weeks), and the gap between calls.
- **Repo:** ~/motion_graphics/thiran-website, branch from main. The site is static, built with `PATH=/usr/bin:$PATH ./build.sh` into site/. Vercel project tensi/thiran-website deploys from site/ by CLI, and a function needs an `api/` folder inside site/. See the deploy notes in thiran-social/NEXT-SESSION-GUIDES.md.
- **Placement:** a "Book a demo" outline button in the nav, the section above Pricing on the home page, and maybe a /demo page as well.
- Keep the marketing board and progress board current. Nothing goes live without Jay's "yes".

Jay's decision, 12 Nov 2026: no Calendly or Cal.com cloud. Build it ourselves with free, open pieces.
The look is the mockup in this folder (mockup.png): a menu button, a section above Pricing, a short form, and a "booked" screen.

## How it works
- **Booking card on thiran.app.** Plain HTML and JS in the site's look. The site stays static.
- **Two small Vercel functions** in the thiran-website project:
  - `GET /api/slots` reads Jay's Google Calendar free/busy for the next 3 weeks. It applies the working hours (to be confirmed, e.g. Mon–Fri 9–5 Sydney), takes out busy times and returns the open 20-minute times in the visitor's time zone.
  - `POST /api/book` checks the time is still free. It then creates the event in a "Thiran demos" calendar with the visitor as a guest and a Google Meet link, using `sendUpdates=all`, so Google emails the invite. The event description holds the form answers.
- **Reminders.** The guest's own calendar reminds them. A free Vercel cron sends our own email reminder 24 h before, through Gmail from Jay's account.
- **Change or cancel.** v1: the guest declines in the Google invite, or replies. v2: our own change/cancel link.
- **Organising on our end.** Everything sits in the "Thiran demos" Google calendar. Optional: a Google Sheet log, or a row in the free Supabase tier.
- **Spam.** A hidden honeypot field, a per-IP rate limit, and the free Cloudflare Turnstile check.
- **Secrets.** The Google OAuth refresh token and client secret go in Vercel env vars only, never in the repo.

## Why not self-host Cal.com
It's a heavy app (Next.js plus Postgres, run on our own server). It's also AGPL, so changing it would mean publishing our changes (see the open-pdf-studio licence note). Building our own is smaller and fully ours.

## What Jay does (guided; Claude never types passwords or keys)
1. Say which Google account gets the demos: a tensi.ai Workspace account or a personal Gmail.
2. In Google Cloud: make a project, turn on the Calendar API (and Gmail API for reminders), and create an OAuth client. Claude walks through it.
3. Sign in once to approve. The token is saved in Vercel env.

## Build order (fresh session)
1. Functions, tested against the calendar on a preview.
2. Booking card from mockup.html, wired up.
3. Book a test demo end to end: invite arrives, Meet link works, the slot disappears.
4. Preview to Jay, then live on Jay's yes.
