<!--
DRAFT 1 · for gate 1 (Jay's OK) · 18 Nov 2026
Web address: thiran.app/guides/construction-drawing-review-checklist
Search title: Construction drawing review checklist | Thiran
Meta description: A practical checklist for reviewing a construction or architectural drawing set: sheet index, scale, dimensions, cross-references, coordination and revisions, with tips for marking up as you go.
Target searches: construction drawing review checklist, architectural drawing review checklist
Source of "In Thiran" lines: in-app Help on main @ eee0f437 (revisions.ts: drawing-register, compare, what-changed, slip-sheet; measure.ts: calibrate, markup-register; markup.ts: cloud, cloud-plus, markup-layers, markup-properties, approval; start.ts: navigation, pdf-layers; documents.ts: flatten)
-->

# Construction drawing review checklist

A good drawing review goes through the set in a fixed order: is the set complete, is each sheet to scale, do the dimensions add up, do the references point to the right place, do the trades agree, and what changed since last time. Mark every issue on the sheet as you find it, with a note saying what's wrong.

Use it on architectural, structural or services drawings. Each step ends with how to do it in Thiran, on the fictional Lumen House set.

## Before you start

- [ ] You have the latest issue of every sheet, and you know which revision you're reviewing.
- [ ] You know what the review is for: design check, tender, for-construction sign-off or shop drawing approval.

**In Thiran:** put each reviewer on their own markup layer, such as Structure or Client comments. Anyone can then hide or lock a reviewer's comments with one click.

## 1. The set is complete

- [ ] The sheet index matches the sheets you were sent: nothing missing, nothing extra.
- [ ] Sheet numbers and titles in the title blocks match the index.
- [ ] Revision letters and dates are filled in and agree with the transmittal.

**In Thiran:** the Drawing Register groups the job's PDFs into one set with a sheet index you can filter and click through, and export as a spreadsheet to check against the transmittal.

## 2. Every sheet is to scale

- [ ] The scale in the title block is right for each plan, section and detail.
- [ ] Details at a different scale are labelled with their own scale.
- [ ] A known dimension measures correctly. Check one on every sheet, not just the first.
- [ ] Sheets printed smaller than their original size (say an A1 sheet at A3) are marked as reduced.

**In Thiran:** check the scale in the status bar, or calibrate from two points a known distance apart, such as two grid lines. See [How to set the scale on a PDF drawing](./set-the-scale-on-a-pdf-drawing).

## 3. Dimensions and levels add up

- [ ] Running dimensions add up to the overall dimension.
- [ ] Grid lines and their spacing match on plans, sections and elevations.
- [ ] Floor, ceiling and roof levels agree between sections and elevations.

**In Thiran:** measure lengths and areas to check the numbers. See [How to measure areas and lengths on a PDF](./measure-areas-and-lengths-on-a-pdf).

## 4. References point to the right place

- [ ] Every section, detail and elevation marker points to a sheet that exists.
- [ ] The detail on that sheet is the one the marker shows.
- [ ] Door, window and finish tags appear in their schedules, and the schedules don't list tags that aren't on the plans.

**In Thiran:** in a combined set, click a sheet reference such as 3/A-102 to go to that sheet.

## 5. The trades agree with each other

- [ ] Structure doesn't clash with openings, ducts or pipes on the architectural plans.
- [ ] Ceiling space is big enough for the services shown above it.
- [ ] Risers, shafts and penetrations line up from floor to floor.

**In Thiran:** overlay two trades' drawings in different colours, with each drawing on its own layer, and lower the opacity of the busier one. If the PDF was plotted with CAD layers, hide the ones you don't need, such as furniture.

**Screenshot:** Lumen House architectural and mechanical level 1 overlaid in two colours

## 6. What changed since the last issue

- [ ] Every change is clouded and has a revision note.
- [ ] Nothing changed that isn't clouded.
- [ ] Comments from the last review have been answered.

**In Thiran:** compare the two revisions to find every difference, keep or dismiss each one, and cloud the ones that matter. See [How to compare two drawing revisions](./compare-two-drawing-revisions).

## 7. Mark up and track each issue

- [ ] Each issue has a cloud round it and a note that says what's wrong and what's needed.
- [ ] Every issue has a status, so the next reviewer knows what's still open.

**In Thiran:** use **Cloud with Callout** so the cloud and its note move together. The Register lists every markup with its page, author, date and status; filter it to see what's still open, and click a row to go to it on the sheet.

**Screenshot:** Register filtered to open comments on the Lumen House set

## 8. Sign off and issue

- [ ] The reviewer has signed off, with a status and date.
- [ ] The marked-up set goes back to the designer in a form they can open.

**In Thiran:** place an Approval stamp with your status, name, date and signature. Flatten a copy for issue so the markups can't be moved, and keep the marked-up original.

## Common questions

**What should a drawing review check first?**
That the set is complete and to scale. A missing sheet or a wrong scale makes every later check unreliable.

**How do several reviewers mark up one set without mixing comments?**
Give each reviewer their own markup layer, and record who made each markup.

---

## Try Thiran free for 7 days, no card needed

Review drawing sets on Windows, Mac and the web.
**[Start your 7-day free trial]** → my.thiran.app

**Related guides:** [How to annotate and redline a PDF drawing](./annotate-and-redline-a-pdf-drawing) · [How to compare two drawing revisions](./compare-two-drawing-revisions)

<!--
SCREENS TO CAPTURE (real app, main, fictional Lumen House set)
1. 13-register-set.png   Drawing Register sheet index
2. 13-overlay.png        architectural + mechanical overlay, two colours
3. 13-register-open.png  Register filtered to open comments
4. 13-approval.png       can reuse 11-approval.png
-->
<!--
WEEK 1 BUILD (18 Nov): screens captured on the released app 0.17.13 (tag v0.17.13), fictional Lumen House set, via thiran-social/guides/capture-week1.mjs.
DROPPED (could not be captured honestly): Drawing Register for Lumen House, sheet index listing A-001 to A-301
-->
