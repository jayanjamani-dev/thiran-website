<!--
DRAFT 1 · for gate 1 (Jay's OK) · 2 Nov 2026
Web address: thiran.app/guides/count-symbols-and-export-quantities-to-excel
Search title: How to count symbols and export quantities to Excel | Thiran
Meta description: Count symbols on a PDF drawing with a click each, or find every copy at once, then export your quantities to an Excel spreadsheet or CSV. Step-by-step guide.
Target searches: count symbols on pdf, export quantities to excel, pdf takeoff
Source of steps: in-app Help (measure.ts: count, measurements-panel, markup-register, export-takeoff; library.ts: find-similar) on the released app, 0.17.10
-->

# How to count symbols and export quantities to Excel

To count symbols on a PDF drawing, click each one with a count tool, or box one example and let the software find every copy. Then export the totals to a spreadsheet. In Thiran you do both without leaving the drawing.

This guide counts ceiling downlights on the fictional Lumen House lighting plan.

## Count by hand: one click per item

Best for a handful of items.

1. Choose **Count**. Pick the symbol and numbering under Properties › Count.
2. Click each item on the drawing. Each click adds a numbered dot.
3. The running total shows beside the last dot and in the status bar.
4. Press Enter or Esc to finish. Start a new count for the next kind of item.

**Screenshot:** numbered count dots on Lumen House. (Have: thiran-uc1/shots/10-count.png)

## Find every copy at once: Find Similar

Best for lots of the same symbol: lights, outlets, diffusers, sprinkler heads.

1. Choose **Find Similar** on the toolbar.
2. Drag a box tightly round one copy of the symbol, with little else inside it.
3. Give it a name, such as "Ceiling downlight", and choose where to look: this sheet, the whole document, or all open documents. Choose **Search**.
4. Every copy is outlined on the drawing and listed in the panel. If a symbol is in the sheet's legend, its name is read from there.
5. Untick any that are wrong.
6. Choose **Add to takeoff**. They become one count, with the symbol's picture, in Quantities and the Register. Adding again updates the count. It doesn't double it.

**Screenshot:** box round one downlight, then every downlight outlined with the count. (Have: thiran-uc1/shots/12-find-box.png, 13-find-results.png, 13b-added.png)

Find Similar works best on clean PDFs exported from design software. Always check the list before adding: symbols that look alike can match.

## Check the totals

- **Measurements › Quantities** totals every count, length, area and volume by subject, for this page or the whole document.
- **The Register** at the bottom lists every item. Use Group by, Filter and Totals to check it the way you'll price it.

**Screenshot:** the Register grouped by type, with totals. (Have: thiran-uc1/shots/14-register.png)

## Export to Excel

1. In the Register, set the columns, filters and grouping you want.
2. Choose **Export › Spreadsheet (.xlsx)…**, or CSV…
3. The spreadsheet has the rows you see in the Register, ready for your estimate.

For a printable report, choose **Export › PDF summary with thumbnails…** instead.

**Screenshot:** the Export menu, then the exported spreadsheet open. (Have: thiran-uc1/shots/15-export-menu.png, 16-exported.png)

## Keep a spreadsheet up to date by itself

In the Measurements panel, under **Live spreadsheet link**, choose **Link to spreadsheet…** Thiran keeps that .xlsx or CSV file up to date with your takeoff, so your estimating spreadsheet can read from it as you work.

## Common questions

**Can I count across a whole drawing set?**
Yes. In Find Similar, choose the whole document or all open documents.

**Does the export include measurements as well as counts?**
Yes. Lengths, areas, volumes and counts all go to the spreadsheet.

**Does it work with Excel and Google Sheets?**
The export is a standard .xlsx or CSV file, so it opens in Excel, Numbers or Google Sheets.

---

## Try Thiran free for 7 days

Count, measure and export your takeoff on Mac, Windows and the web.
**[Start your 7-day free trial]** → my.thiran.app

**Back to the start:** [How to annotate and redline a PDF drawing](./annotate-and-redline-a-pdf-drawing)

<!--
SCREENSHOTS TO CAPTURE (real app, main 0.17.10, fictional Lumen House set)
1. HAVE  10-count, 12-find-box, 13-find-results, 13b-added, 14-register, 15-export-menu, 16-exported (thiran-uc1/shots)
2. NEED  05-quantities.png    Measurements › Quantities with the downlight count and picture
3. NEED  05-spreadsheet.png   the real exported .xlsx open in Excel or Numbers (Excel access
                               wasn't granted last time; Numbers or Jay's Excel works)
4. NEED  05-live-link.png     Live spreadsheet link section
CAPTURED 2 Nov (shots/web/): 05-quantities (64 downlights found), 05-live-link. STILL NEEDED: the exported .xlsx open in Numbers or Excel.
-->
