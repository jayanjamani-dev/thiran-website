<!--
DRAFT 1 · for gate 1 (Jay's OK) · 18 Nov 2026
Web address: thiran.app/guides/annotate-a-pdf-on-a-mac
Search title: How to annotate a PDF on a Mac | Thiran
Meta description: Annotate a PDF on a Mac: add text, notes, callouts, highlights, clouds, stamps and your signature, then save them inside the PDF. Works the same on Windows and the web.
Target searches: annotate pdf on mac, best pdf annotator for mac
Source of steps: in-app Help on main @ eee0f437 (start.ts: open-files, cloud-drives; markup.ts: text, callout, note, text-markup, pen, highlighter, cloud-plus, stamp, signature, markup-properties; documents.ts: flatten)
-->

# How to annotate a PDF on a Mac

To annotate a PDF on a Mac, open it in a PDF markup app, pick a tool such as a text box, note, highlight or cloud, click on the page, and save. In Thiran the annotations are saved inside the PDF as standard annotations, so they show in any PDF reader on a Mac, Windows or a phone.

Thiran runs as an app on Mac and Windows, and in the browser. Every step below is the same on all three. This guide uses the fictional Lumen House drawings.

## What you need

- A PDF: a drawing, a specification or any other document.
- Thiran for Mac, Windows or the web. The 7-day trial has every tool.

## 1. Open the PDF

Drag the PDF onto the Thiran window, or choose **File › Open**. Each file opens in its own tab.

You can also open a PDF straight from Google Drive or OneDrive, and save it back over the same file. Pictures (PNG, JPEG) and DXF drawings open too, turned into a PDF as they open.

**Screenshot:** Thiran on a Mac with Lumen House A-101 open, toolbar visible

## 2. Add text and notes

- **Text box:** choose **Text box**, drag a box (or just click), and type. Press Esc or ⌘+Enter, or click away, to finish.
- **Callout:** choose **Callout**, click the point the arrow should touch, click where the text goes, and type. Move the box and the arrow stays on what it points at.
- **Sticky note:** choose **Sticky note** and click. A small note icon stays on the page; point at it to read who wrote it and when.

**Screenshot:** a callout and a note on A-101

## 3. Highlight, underline or strike out text

For a specification or report, mark the words themselves.

1. Choose **Highlight text**, **Underline text** or **Strike out text**.
2. Press on a word and drag across the text. The mark follows the line of text.

Scanned pages have no words to follow. Run **Recognise text (OCR)** on them first.

**Screenshot:** a page of the Lumen House specification with a highlight and a strike-out

## 4. Draw on the page

- **Pen** draws freehand, as on paper. **Highlighter** draws a see-through stroke over part of a drawing.
- **Line and arrow**, **Rectangle and ellipse** and **Polygon** frame or point at things.
- **Cloud with Callout** draws a revision cloud with a note attached. Click round the area, double-click or press Enter to close it, then type the note.

**Screenshot:** a Cloud+ round a changed door on A-101, with its note

## 5. Stamp and sign

- **Stamps:** choose the arrow beside **Stamp**, pick one such as Approved, and click where it goes. Make your own with **New text stamp…** or **New image stamp…**.
- **Signature:** sign in a small pad with your mouse, trackpad or pen, and place it on the page like a stamp.

**Screenshot:** an Approved stamp and a signature on the title block

## 6. Change how annotations look

Select an annotation and open **Properties** to change its colour, line width, fill, opacity and font. Give it a subject, comment and status there too.

Like a look? Select it and choose **Set as default** in Properties. Every new annotation from that tool comes out the same, in every document.

## 7. Save

Choose **File › Save**. A dot on the tab means there are unsaved changes. **Save As** makes a new copy.

To send a copy nobody can change, choose **Flatten all markups**, then save it as a new file. Keep the original, so you can still edit the annotations.

## Common questions

**Will my annotations show for someone without Thiran?**
Yes. They're saved as standard PDF annotations, so they open in any PDF reader.

**Is it the same on Windows?**
Yes. The tools, panels and steps are the same in the Windows app and in the browser.

**Can I annotate a scanned PDF?**
Yes, with any drawing tool, text box, note or stamp. To highlight its words, run Recognise text (OCR) first.

---

## Try Thiran free for 7 days

Annotate PDFs on Mac, Windows and the web. No card needed.
**[Start your 7-day free trial]** → my.thiran.app

**Next guide:** [How to annotate and redline a PDF drawing](./annotate-and-redline-a-pdf-drawing)

<!--
SCREENSHOTS TO CAPTURE (real Mac app, fictional Lumen House set; show the Mac window frame)
1. NEED 08-mac-open.png        Lumen House A-101 open in the Mac app
2. NEED 08-callout-note.png    callout + note
3. NEED 08-text-markup.png     highlight + strike-out on a Lumen House spec page (needs a fictional spec PDF)
4. NEED 08-cloudplus.png       Cloud+ with note
5. NEED 08-stamp-sign.png      Approved stamp + signature
6. NEED 08-other-reader.png    saved PDF in another reader (don't show that reader's name or logo)
CHECK: "trackpad" in step 5. Help says "mouse, pen or finger". Trackpad is a mouse on a Mac, but change to "mouse or pen" to match Help exactly if preferred.
Flatten all markups: exact label confirmed in src/markup/commands.ts on main.
CHECK: Mac menus. Help names File › Open / File › Save; confirm the Mac app's menu bar uses the same names.
-->
<!--
WEEK 1 BUILD (18 Nov): screens captured on the released app 0.17.13 (tag v0.17.13), fictional Lumen House set, via thiran-social/guides/capture-week1.mjs.
DROPPED (could not be captured honestly): the saved PDF open in another PDF reader, annotations showing
-->
