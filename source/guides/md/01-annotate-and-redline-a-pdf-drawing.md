<!--
DRAFT 2 · folds in draft 09 · for gate 1 (Jay's OK) · 18 Nov 2026
Web address: thiran.app/guides/annotate-and-redline-a-pdf-drawing
Search title: How to annotate and redline a PDF drawing | Thiran
Meta description: Mark up a construction drawing with revision clouds, callouts, text and stamps, save the redlines inside the PDF, send a copy that can't be changed, and print it.
Target searches: annotate pdf, pdf annotator, redline drawings, pdf markup, how to redline a pdf, add redline to pdf, how to save redline pdf, how to print redline pdf
Source of steps: in-app Help (markup.ts, measure.ts) on the released app, 0.17.10; added steps from in-app Help on main @ eee0f437 (markup.ts: markup-layers; start.ts: open-files, cloud-drives; documents.ts: flatten, export-print, batch)
-->

# How to annotate and redline a PDF drawing

To redline a PDF drawing, open it in a markup tool, draw a revision cloud round each change, attach a note that says what changed and why, and save. The markups stay inside the PDF, so whoever you send it to sees them in their usual PDF reader. To print the redlines, print the PDF as usual: the markups print with it.

This guide shows each step in Thiran, on the fictional Lumen House drawings.

## What you need

- A PDF drawing. One sheet or a whole combined set both work.
- Thiran on Mac, Windows or the web. The 7-day free trial has every tool.

## 1. Open the drawing

Drag the PDF onto Thiran, or choose it from your computer. You can also open it straight from Google Drive or OneDrive and save it back there when you're done.

**Screenshot:** Lumen House set open on sheet A-101, toolbar visible.

## 2. Cloud the change

1. Choose **Cloud** on the toolbar.
2. Click round the area that changed. Double-click, press Enter or click the first point to close the cloud. To draw a box-shaped cloud instead, switch Shape to Rectangle and drag.
3. In Properties, set the arc size (S, M, L or XL), the colour and the line width.

The Cloud tool stays on after each cloud, so you can cloud change after change. Press Esc to go back to Select.

**Screenshot:** a red cloud half drawn round a door on A-101.

## 3. Say what changed

A cloud on its own doesn't explain anything. Add the reason in one of two ways:

- **Cloud with Callout** draws the cloud and attaches a note in one go. Type the note, then drag its box to where it reads best. The cloud and its note move together.
- **Callout** is a note with an arrow. Click the point the arrow should touch, click where the text box goes, then type.

Click the cloud, the leader line or the text box, and Properties shows a section for each one. That means you can give the cloud, the line and the box their own colour and line.

**Screenshot:** a Cloud with Callout on A-101 reading "Door moved 600 mm to clear the riser".

## 4. Add notes and stamps

- **Text box:** drag a box, or just click for a standard-size box, and type. Press Esc or click away to finish.
- **Sticky note:** a small note icon. Point at it to read it, or open it to see the whole note.
- **Pen and Highlighter:** freehand, as with a pen on paper.
- **Stamp:** choose the arrow beside Stamp and pick one, such as Approved or For Construction. To make your own, choose New text stamp… (for example CHECKED with your name and the date) or New image stamp… for a logo or signature.
- **Highlight, Underline and Strikeout:** for redlining a specification. Drag across the PDF's own words.

**Screenshot:** the Stamp list open, with For Construction placed on the title block.

## 5. Keep each reviewer's redlines apart

If several people are commenting, give each one a markup layer.

1. Choose **Markup layers**. Add a layer and name it, such as "Client comments".
2. Select markups and pick the layer under Properties › Markup › Layer.
3. Use the eye beside a layer to hide its markups, or the lock to stop them being moved.

Layers are saved in the PDF too, so other PDF readers can show and hide them.

**Screenshot:** Layers panel with "Architect" and "Client comments" layers, one hidden

## 6. Check every markup in the Register

The Register is docked at the bottom of the screen. It lists every markup with its page, type, comment, author, date and status.

- Click a row to jump to that markup on the sheet.
- Set a status on each markup to track what's been answered.
- Point at any markup on the sheet to see who made it and when.

**Screenshot:** the Register with the clouds, callouts and stamp from this guide.

## 7. Save the redlined PDF

- **File › Save** (Ctrl+S on Windows, Cmd+S on Mac) writes your markups into the PDF. A dot on the tab means there are unsaved changes.
- **File › Save As…** saves a new copy and leaves the original as it was.
- Opened it from Google Drive or OneDrive? **Save** puts it back over the same file. If someone else saved that file since you opened it, nothing is overwritten: you're offered a copy instead.

Your markups are saved as standard PDF markups, so the person you send it to sees them in their usual PDF reader.

**Screenshot:** File menu open with Save and Save As… highlighted

## 8. Send a copy that can't be changed

Saved markups can still be moved or edited. To fix them in place before you issue a drawing, flatten them on a copy:

1. Choose **Save As…** first, so you keep a copy with live markups.
2. Choose **Flatten all markups**, or select some and choose **Flatten selected markups**.
3. They become part of the drawing straight away. If that was a slip, choose Undo in the message that appears. **Unflatten markups** brings them back while the file is still open.
4. Save.

**Screenshot:** the flattened A-101 copy, with the Undo message showing

## 9. Print the redlines

Choose **File › Print…** (Ctrl+P on Windows, Cmd+P on Mac). The PDF prints with your markups on it.

To print or flatten a whole stack of PDFs in one go, use **File › Batch process files…**, pick the files and choose the job.

**Screenshot:** Print chosen from the File menu with A-101 and its red clouds in view

## Tips

- **Save your favourite styles.** A cloud you've set up just right can be saved as a tool in the Tool Library and reused on every job.
- **Too big to email?** **Reduce file size…** makes the PDF smaller for email or upload.
- **Need a picture instead?** **File › Export pages as images…** saves pages as PNG or JPEG. You choose the pages, the resolution and whether the markups are included.

## Common questions

**What does "redline" mean on a drawing?**
Redlining means marking changes or comments on a drawing, usually in red: clouds round what changed and notes saying why.

**Will my markups show up in other PDF readers?**
Yes. They're saved inside the PDF, so other PDF readers show them.

**How do I print a redlined PDF?**
Choose File › Print… in Thiran. The PDF prints with every markup on it.

**Can I stop people changing my redlines?**
Yes. Flatten them on a copy before you send it (step 8). They become part of the drawing and can't be moved or edited.

**Can I mark up a scanned drawing?**
Yes. Markups work on any PDF page, scanned or not.

---

## Try Thiran free for 7 days

Every markup tool in this guide is in the free trial, on Mac, Windows and the web. No card needed.
**[Start your 7-day free trial]** → my.thiran.app

**Next guide:** [How to set the scale on a PDF drawing](./set-the-scale-on-a-pdf-drawing)

<!--
SCREENSHOTS TO CAPTURE (real app, main 0.17.10, fictional Lumen House set, extend thiran-uc1/capture.mjs)
1. NEED  01-open.png         Lumen House open on A-101 (can reuse thiran-uc1/shots/03-arrived-a101.png)
2. NEED  01-cloud.png        Cloud tool part-way round a door on A-101
3. NEED  01-cloud-callout.png Cloud with Callout with the note typed
4. NEED  01-stamp.png        Stamp list open, For Construction placed
5. NEED  01-register.png     Register listing this guide's markups
All at 1600 px wide WebP for the page; keep the 3840 px PNG originals.
CAPTURED 2 Nov (shots/web/): 01-cloud, 01-cloud-callout, 01-stamp-list, 01-stamp, 01-register. Open shot: reuse thiran-uc1 03-arrived-a101. All done.
NEW (18 Nov, from folded draft 09; take on main, fictional Lumen House set)
6. NEED  01-layers.png       Layers panel with two markup layers, one hidden
7. NEED  01-save-menu.png    File menu with Save / Save As…
8. NEED  01-flatten.png      flattened copy with the Undo message
9. NEED  01-print.png        File › Print… with red clouds in view
CHECK: Save / Save As / Flatten / Print / Batch / Reduce file size / Export pages as images come from Help on main @ eee0f437, not 0.17.10. Confirm they are in the released app (0.17.13) before publishing.
-->
<!--
WEEK 1 BUILD (18 Nov): screens captured on the released app 0.17.13 (tag v0.17.13), fictional Lumen House set, via thiran-social/guides/capture-week1.mjs.
-->
