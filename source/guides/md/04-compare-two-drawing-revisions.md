<!--
DRAFT 1 · for gate 1 (Jay's OK) · 2 Nov 2026
Web address: thiran.app/guides/compare-two-drawing-revisions
Search title: How to compare two drawing revisions | Thiran
Meta description: Compare two revisions of a PDF drawing and see every change: added in blue, removed in orange. Keep or dismiss each one, then cloud the changes that matter.
Target searches: compare drawing revisions, compare two pdf drawings, drawing comparison
Source of steps: in-app Help (revisions.ts: compare, what-changed, overlay, slip-sheet) on the released app, 0.17.10
-->

# How to compare two drawing revisions

To compare two revisions of a drawing, open both, run a compare, and go through the differences one by one. Thiran lines the sheets up, traces what was added and removed, and lets you cloud the changes that matter on the newer revision.

This guide uses two revisions of the fictional Lumen House drawings.

## 1. Open both revisions

Open the newer revision. Open the older one too, or leave it on your computer and pick it in the next step.

## 2. Run the compare

1. Choose the **Compare** button on the toolbar.
2. Pick the older and the newer revision. Sheets are matched by sheet number, or by page order if there are no sheet numbers. The swap button trades the two sides.
3. To compare one page with another, pick a page on each side. They can even be two pages of the same document.
4. Leave **Auto-align** on for sheets that have shifted, and choose the sensitivity.

The differences show straight away.

**Screenshot:** the Compare box with Lumen House Rev A and Rev B picked.

## 3. See what changed

The changes are traced on the newer revision: **added in blue, removed in orange**, and the rest of the drawing faded so the changes stand out.

Each change has a numbered pin and a one-line description. Click a pin or its line, and both revisions zoom to the same place, side by side, so you see the before and after together.

Revision letters, dates, initials, issue status and plot stamps in the title block are set aside, so you only see changes to the drawing itself.

**Screenshot:** Lumen House Rev B with changes traced in blue and orange, and the What changed list.

## 4. Keep or dismiss each change

Go down the list and press ✓ to keep a change or ✗ to dismiss it. With the list selected, the keys are quick: N next, P previous, K keep, X dismiss.

Tick **Hide dismissed** to clear the ones you crossed out.

**Screenshot:** the What changed list with some changes kept and some dismissed.

## 5. Cloud the changes that matter

Choose **Cloud kept**. Every change you kept is clouded on the newer revision with a note that says what changed.

**Screenshot:** the newer revision with the kept changes clouded.

## 6. Share the result

Export every change as a spreadsheet (.xlsx) or CSV, or print the change report as a PDF to send to the team.

## Another way: overlay the drawings

To see two drawings on top of each other, in two colours, use **Overlay pages**. Each drawing gets its own colour and is lined up automatically. You can also overlay different trades to check how they fit together.

## Tips

- **Bringing in a new revision?** Slip-sheet it into your drawing set and tick **Cloud what changed on each replaced sheet**. Your markups carry across to the new sheets.
- **Review first, cloud second.** Clouding every change at once is off by default, so you only cloud what you've checked.

## Common questions

**What if the drawing has moved on the new sheet?**
Leave Auto-align on. It lines up sheets that have shifted before comparing them.

**Can I compare a whole set at once?**
Yes. Pick both documents and the sheets are matched by sheet number.

---

## Try Thiran free for 7 days

Find every change between revisions, on Mac, Windows and the web.
**[Start your 7-day free trial]** → my.thiran.app

**Next guide:** [How to count symbols and export quantities to Excel](./count-symbols-and-export-quantities-to-excel)

<!--
SCREENSHOTS TO CAPTURE (real app, main 0.17.10, fictional Lumen House set)
BLOCKER: needs a fictional Lumen House Rev B (a few walls/doors moved, a window added).
Make it with thiran-uc1/make-set.mjs as a second set; never a real project.
1. NEED  04-compare-box.png   Compare box with Rev A / Rev B picked
2. NEED  04-traced.png        changes traced blue/orange + What changed list
3. NEED  04-keep-dismiss.png  list with ✓ and ✗ set
4. NEED  04-clouded.png       Cloud kept result on Rev B
CHECK with Jay: the "one-line description" of each change must not depend on the AI being
signed in. Help says names are written locally when the AI isn't available. Keep the wording
generic; never mention AI on the page.
CAPTURED 2 Nov on Rev A vs fictional Rev B (thiran-uc1/make-set-revb.mjs): 04-compare-box, 04-traced, 04-keep-dismiss, 04-clouded. 04-traced/clouded/keep-dismiss are CROPPED to leave out the compare panel's 'Thiran AI' sign-in note. Never use the uncropped PNGs publicly.
-->
