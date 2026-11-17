<!--
DRAFT 1 · for gate 1 (Jay's OK) · 18 Nov 2026
Web address: thiran.app/guides/rotate-a-pdf-drawing-and-save-it
Search title: How to rotate a PDF drawing and save it | Thiran
Meta description: Turn sideways or upside-down pages in a PDF drawing so they open the right way round everywhere, then save or print. Plus how to turn only your view.
Target searches: how to rotate a pdf file and save, how to rotate pdf file and print
Source of steps: in-app Help on main @ eee0f437 (documents.ts: rotate-pages, page-thumbnails, export-print; start.ts: rotate-view, open-files, cloud-drives)
-->

# How to rotate a PDF drawing and save it

To rotate a PDF drawing and keep it that way, select the pages, rotate them clockwise, anticlockwise or 180°, and save the file. The rotation is saved in the PDF, so the pages open the right way round for everyone, in any PDF reader.

This guide shows how in Thiran, on the fictional Lumen House set, where a few sheets were scanned sideways.

## What you need

- The PDF with the sideways or upside-down pages.
- Thiran on Windows, Mac or the web.

## First: rotate the page, or just your view?

Thiran can turn a drawing in two ways, and only one is saved:

| | Rotate pages | Rotate view |
|---|---|---|
| What turns | The pages in the file | Only what you see on screen |
| Saved in the PDF | Yes | No |
| Others see it | Yes | No |
| Use it for | Scans or sheets that are the wrong way round | A drawing plotted sideways that you just want to read |

If the page is wrong in the file, rotate the pages. If the page is fine but easier to read turned round, rotate the view.

## 1. Open the drawing

Drag the PDF onto Thiran, or choose **File › Open**. If it's in Google Drive or OneDrive, open it with **File › Open from…** and you can save it straight back.

**Screenshot:** Lumen House set open with sheet A-201 lying on its side

## 2. Select the pages to turn

1. Open the **Thumbnails** panel.
2. Click the page to turn. For several, Shift-click a run of pages, or Ctrl-click (⌘-click on a Mac) to pick them one by one.

Or just go to the page, if it's only the one you're on.

**Screenshot:** Thumbnails panel with three sideways sheets selected

## 3. Rotate them

Choose one of these from the **Pages** menu, or use the rotate buttons at the top of the Thumbnails panel:

- **Rotate pages clockwise:** a quarter turn to the right.
- **Rotate pages counter-clockwise:** a quarter turn to the left.
- **Rotate pages 180°:** turns an upside-down page the right way up.

Any markups already on the page turn with it, so your clouds and notes stay where they belong.

Changed your mind? Every page operation can be undone with Undo.

**Screenshot:** the Pages menu with the three rotate commands

## 4. Save the rotation

Choose **File › Save** to save the rotation into the PDF, or **File › Save As…** to keep the original and save a new copy.

If you opened the file from Google Drive or OneDrive, **File › Save** saves it back over the same file there.

## 5. Print it

Once the pages are the right way round, choose **File › Print…**. Your markups print with the drawing.

## Just want to turn the view?

To read a drawing that was plotted sideways, without changing the file:

1. Choose **Rotate view clockwise** from the **View** menu (Shift+Alt+R), or the rotate buttons on the toolbar.
2. Choose **Rotate view counter-clockwise** to turn it the other way.

New markups are drawn upright for the way you're looking at the sheet. The view rotation isn't saved, so the file is unchanged.

## Other page jobs

While the Thumbnails panel is open, you can also:

- Drag pages up or down to put them in order.
- Right-click to insert a blank page, insert pages from another file, duplicate, extract or delete pages.
- Use **Replace with pages from file…** to swap in a reissued sheet.

## Common questions

**Why does my PDF go back to sideways when I reopen it?**
You probably turned the view, not the page. Rotate view isn't saved. Use Rotate pages, then save.

**Can I rotate just one page in a drawing set?**
Yes. Select only that page in Thumbnails and rotate it. The other pages stay as they are.

**Will my markups end up in the wrong place?**
No. Markups turn with the page.

**Can I rotate pages in a PDF from Google Drive?**
Yes. Open it with **File › Open from… › Google Drive**, rotate the pages, and save it back.

---

## Try Thiran free for 7 days, no card needed

Rotate, reorder and mark up drawing sets on Windows, Mac and the web.
**[Start your 7-day free trial]** → my.thiran.app

**Related guides:** [How to annotate and redline a PDF drawing](./annotate-and-redline-a-pdf-drawing) · [How to open and edit a PDF from Google Drive](./open-and-edit-a-pdf-from-google-drive)

<!--
SCREENS TO CAPTURE (real app, main, fictional Lumen House set; make a copy with A-201 to A-203 turned sideways first)
1. 14-sideways.png     A-201 lying on its side
2. 14-thumbs.png       Thumbnails with three pages selected
3. 14-pages-menu.png   Pages menu showing the three rotate commands
4. 14-fixed.png        the same sheets upright, with clouds turned with them
-->
<!--
WEEK 1 BUILD (18 Nov): screens captured on the released app 0.17.13 (tag v0.17.13), fictional Lumen House set, via thiran-social/guides/capture-week1.mjs.
-->
