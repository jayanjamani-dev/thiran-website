<!--
DRAFT 2 · folds in draft 07 · for gate 1 (Jay's OK) · 18 Nov 2026
Web address: thiran.app/guides/compare-two-drawing-revisions
Search title: How to compare two drawing revisions | Thiran
Meta description: Compare two PDF files for differences: trace every change between drawing revisions (added in blue, removed in orange), overlay two drawing revisions in two colours, or view them side by side.
Target searches: compare drawing revisions, compare two pdf drawings, drawing comparison, compare two pdf files for differences, compare pdf drawings, overlay two drawing revisions, compare pdf mac, compare pdf windows
Source of steps: in-app Help (revisions.ts: compare, what-changed, overlay, slip-sheet) on the released app, 0.17.10; overlay detail and split screen from in-app Help on main @ eee0f437 (revisions.ts: overlay; start.ts: page-display)
-->

# How to compare two drawing revisions

To compare two revisions of a drawing, open both, run a compare, and go through the differences one by one. Thiran lines the sheets up, traces what was added and removed, and lets you cloud the changes that matter on the newer revision.

The same steps work whenever you need to compare two PDF files for differences. You can also overlay two drawing revisions in two colours, or look at them side by side.

| You want to… | Use |
|---|---|
| Find and check every change, one by one | **Compare** (steps 1 to 6) |
| See two drawings on top of each other | **Overlay pages** |
| Look at two sheets next to each other | **Split screen** |

This guide uses two revisions of the fictional Lumen House drawings.

## 1. Open both revisions

Open the newer revision. Open the older one too, or leave it on your computer and pick it in the next step.

## 2. Run the compare

1. Choose the **Compare** button on the toolbar.
2. Pick the older and the newer revision. Sheets are matched by sheet number, or by page order if there are no sheet numbers. The swap button trades the two sides.
3. To compare one page with another, pick a page on each side. They can even be two pages of the same file.
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

## Another way: overlay two drawing revisions

To see two drawings on top of each other, each in its own colour, use **Overlay pages**.

1. With the newer drawing open, choose **Overlay pages**. A panel opens, and the open drawing is Drawing 1.
2. Under **Add a drawing**, choose the older revision (or **Choose file…** for one on your computer), pick its sheet, pick a colour, then **Add drawing**.
3. The drawings are lined up for you, on the gridlines and walls. The preview says how well they match, such as "Aligned · 85% of linework matches".
4. Drag the top drawing, or use the arrow keys, to nudge it. **Reset position** puts it back.
5. Lower the opacity of a busy drawing so the other shows through.
6. Choose **Apply**. The overlay opens as a new document, each drawing on its own layer.

Where the two colours sit on top of each other, nothing changed. Where you see only one colour, something moved, was added or was taken away.

You can also overlay different trades to check how they fit together.

**Screenshot:** Lumen House Rev A and Rev B overlaid in two colours, with the Overlay panel and its match preview

## Or look at them side by side

For a quick look, split the screen into two columns, open one file in each, and turn on **Sync panes**. Both scroll to the same place, each at its own zoom.

**Screenshot:** Rev A and Rev B in two panes, Sync panes on

## Tips

- **Bringing in a new revision?** Slip-sheet it into your drawing set and tick **Cloud what changed on each replaced sheet**. Your markups carry across to the new sheets.
- **Review first, cloud second.** Clouding every change at once is off by default, so you only cloud what you've checked.

## Common questions

**How do I compare two PDF files for differences?**
Open both and choose Compare (steps 1 to 6). Every change is traced and listed, so you can go through them one by one. For a quick visual check, overlay them instead.

**What if the drawing has moved on the new sheet?**
Leave Auto-align on. It lines up sheets that have shifted before comparing them. Overlay lines the drawings up by itself, and you can drag to adjust.

**Can I compare a whole set at once?**
Yes. Pick both documents and the sheets are matched by sheet number.

**Can I compare drawings without an internet connection?**
Yes. Compare and Overlay pages run on your own computer. The Windows and Mac apps keep working without an internet connection for up to 30 days on your device licence, then need to check in once.

**Can I compare PDFs on a Mac or Windows?**
Yes. Compare and Overlay pages work the same in the Mac and Windows apps and on the web.

---

## Try Thiran free for 7 days

Find every change between revisions, on Mac, Windows and the web. No card needed.
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
NEW (18 Nov, from folded draft 07; take on main, fictional Lumen House Rev A / Rev B)
5. NEED  04-overlay.png       overlay in two colours + Overlay panel with match preview
6. NEED  04-split-sync.png    two panes, Sync panes on
CHECK: the overlay reading ("Where the two colours sit on top of each other, nothing changed") is plain explanation of a two-colour overlay, not a Help step.
CHECK: the overlay steps and split screen come from Help on main @ eee0f437, not 0.17.10. Confirm they are in the released app (0.17.13).
CHECK: "compare two PDF files for differences" can bring in people comparing text documents (contracts). Help only describes drawings; the page never promises text comparison.
NEVER mention the AI sign-in note in the compare panel; use cropped shots only.
-->
<!--
WEEK 1 BUILD (18 Nov): screens captured on the released app 0.17.13 (tag v0.17.13), fictional Lumen House set, via thiran-social/guides/capture-week1.mjs.
-->
