# Book a demo: our own build (no paid tools)

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
