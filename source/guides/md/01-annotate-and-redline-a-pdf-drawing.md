<!--
DRAFT 1 · for gate 1 (Jay's OK) · 2 Nov 2026
Web address: thiran.app/guides/annotate-and-redline-a-pdf-drawing
Search title: How to annotate and redline a PDF drawing | Thiran
Meta description: Mark up a construction drawing in a few clicks: revision clouds, callouts, text and stamps, saved inside the PDF so anyone can open them. Step-by-step guide.
Target searches: annotate pdf, pdf annotator, redline drawings, pdf markup
Source of steps: in-app Help (markup.ts, measure.ts) on the released app, 0.17.10
-->

# How to annotate and redline a PDF drawing

To redline a PDF drawing, open it in a markup tool, draw a revision cloud round each change, attach a note that says what changed and why, and save. The markups stay inside the PDF, so whoever you send it to sees them in their usual PDF reader.

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

**Screenshot:** the Stamp list open, with For Construction placed on the title block.

## 5. Check every markup in the Register

The Register is docked at the bottom of the screen. It lists every markup with its page, type, comment, author, date and status.

- Click a row to jump to that markup on the sheet.
- Set a status on each markup to track what's been answered.
- Point at any markup on the sheet to see who made it and when.

**Screenshot:** the Register with the clouds, callouts and stamp from this guide.

## 6. Save and send

Save the PDF. Your markups are saved inside it, so the person you send it to sees them in their usual PDF reader.

## Tips

- **Keep trades apart with layers.** Put each trade's or reviewer's markups on their own layer, then hide or lock a layer with one click.
- **Mark the text itself.** On specifications, use highlight, underline or strikethrough on the PDF's own words.
- **Save your favourite styles.** A cloud you've set up just right can be saved as a tool in the Tool Library and reused on every job.

## Common questions

**What does "redline" mean on a drawing?**
Redlining means marking changes or comments on a drawing, usually in red: clouds round what changed and notes saying why.

**Will my markups show up in other PDF readers?**
Yes. They're saved inside the PDF, so other PDF readers show them.

**Can I mark up a scanned drawing?**
Yes. Markups work on any PDF page, scanned or not.

---

## Try Thiran free for 7 days

Every markup tool in this guide is in the free trial, on Mac, Windows and the web.
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
-->
