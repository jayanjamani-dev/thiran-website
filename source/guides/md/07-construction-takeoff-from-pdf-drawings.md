<!--
DRAFT 1 · for gate 1 (Jay's OK) · 18 Nov 2026
Web address: thiran.app/guides/construction-takeoff-from-pdf-drawings
Search title: How to do a construction takeoff from PDF drawings | Thiran
Meta description: Do a construction takeoff from PDF drawings: set the scale, measure areas and lengths, count items, add your prices and export the quantities to Excel. Step-by-step guide.
Target searches: how to do construction takeoffs, how to create a construction takeoff, construction drawing takeoff software
Source of steps: in-app Help on main @ eee0f437 (measure.ts: calibrate, area, volume, void, fill-area, length, polylength, count, measurements-panel, markup-register, register-takeoff, export-takeoff; library.ts: find-similar; start.ts: open-files)
-->

# How to do a construction takeoff from PDF drawings

A construction takeoff is the list of quantities you price a job from: areas, lengths, volumes and counts, measured off the drawings. To do one from PDFs, set each sheet's scale, measure and count everything by name, check the totals, add your rates, and export to a spreadsheet.

This guide takes off part of the fictional Lumen House set in Thiran.

## What you need

- The PDF drawings. One combined set or separate sheets both work.
- Thiran on Windows, Mac or the web. The 7-day trial has every tool.

## 1. Open the drawings and set the scale

1. Choose **File › Open…** or drag the PDFs onto the window. Each opens in its own tab.
2. Check the scale in the status bar. If it says Not scaled, click it and choose **Set scale…**, pick the scale (such as 1:100), say if an A1 sheet was printed at A3, and choose the pages it applies to.
3. Or calibrate: choose **Calibrate**, click two points a known distance apart, such as two grid lines, and type the real distance (6000 mm or 6 m).
4. Measure a length you already know before you start. If it's right, the sheet is ready.

More detail: [How to set the scale on a PDF drawing](./set-the-scale-on-a-pdf-drawing).

**Screenshot:** A-101 with Set scale… open at 1:100

## 2. Measure areas and volumes

1. Choose **Area**. Choose Polygon or Rectangle in the status bar.
2. Click each corner, then double-click, press Enter or click the first point to close it.
3. To take out a hole, such as a stair void or a column, press **Void** and draw it inside the area.
4. For a slab or screed, give the area a depth under Properties › Measurement › Depth. You get its volume in m³ as well.

Area stays on, so you can measure room after room. Press Esc to stop. For rooms with closed walls, **Fill Area** is quicker: click inside the room and its outline is traced and measured.

**Screenshot:** three room areas on A-101 with their m² showing, one with a void

## 3. Measure lengths

- **Length** measures a straight distance: drag, or click two points.
- **Run length** measures a run with several parts, such as a wall, pipe or cable route. Click each point and double-click to finish. Each part and the total are listed.
- **Perimeter** measures round a closed outline, such as a room for skirting. Add a height as the depth to get the wall surface area too.

More detail: [How to measure areas and lengths on a PDF](./measure-areas-and-lengths-on-a-pdf).

**Screenshot:** a Polylength along the external wall of A-101 with each part listed in Properties

## 4. Count items

- **Count**: click each item and each click adds a numbered dot. The running total shows beside the last dot.
- **Find Similar**: for lots of one symbol, box one copy and every copy on the sheet, the document or all open documents is outlined. Untick any that are wrong, then **Add to takeoff**.

More detail: [How to count symbols and export quantities to Excel](./count-symbols-and-export-quantities-to-excel).

**Screenshot:** ceiling downlights on the Lumen House lighting plan, all outlined, with the count

## 5. Name everything as you price it

A takeoff only helps if the totals group the way you price. Give each measurement a clear subject, such as "Floor tiles – wet areas" or "Wall type A". Totals are then grouped by that name.

At the top of the Register, **Pick item…** gets the right tool ready for a named item, so the next thing you measure lands under that name.

## 6. Check the totals

- **Measurements › Quantities** totals every length, area, volume and count by subject, for this page or the whole document.
- **The Register**, docked at the bottom, lists every measurement. Use Group by, Filter and Totals to check it. Click a row to jump to that measurement on the sheet.

**Screenshot:** the Register grouped by subject with Totals showing

## 7. Add your rates and formulas

The Register works like a spreadsheet:

- Add your own columns with the **+** at the end of the headings: text, number, money, measured, choice, date, tick box or formula.
- Formulas start with =, for example **= Quantity * Unit price**. SUM, AVERAGE, ROUND, IF, MIN, MAX and CONVERT are there as you type.
- Unit prices (under **⋯**) are typed by you, once per heading, and fill every row with that heading.
- **Profiles** saves your columns, prices, currency and units for the next project.

**Screenshot:** the Register with Unit price and a Total formula column filled in

## 8. Export to Excel

1. In the Register, set the columns, filters and grouping you want.
2. Choose **Export › Spreadsheet (.xlsx)…** or **CSV…** for the rows shown.
3. Or choose **Export › Takeoff with formulas**: the columns shown, with working formulas, subtotals and grand totals.
4. For a printable report, choose **Export › PDF summary with thumbnails…**

To keep an estimating spreadsheet in step as you work, use **Live spreadsheet link** in the Measurements panel. Thiran keeps that .xlsx or CSV file up to date with the takeoff.

## Common questions

**What should a construction takeoff include?**
Every quantity you'll price: areas (floors, ceilings, walls), lengths (walls, pipes, skirting), volumes (slabs, excavation) and counts (doors, fittings, lights), each under a name that matches your estimate.

**Can I take off a whole drawing set?**
Yes. Set the scale for each page, then switch Quantities to Whole document.

**Does it work in metric?**
Yes. Measure in mm, m, m² and m³, or in feet and inches.

---

## Try Thiran free for 7 days, no card needed

Measure, count and export your takeoff on Windows, Mac and the web.
**[Start your 7-day free trial]** → my.thiran.app

**Next guide:** [How to compare two drawing revisions](./compare-two-drawing-revisions)

<!--
SCREENS TO CAPTURE (real app, main, fictional Lumen House set)
1. 10-set-scale.png     Set scale… dialog at 1:100 (may reuse guide 02 shot)
2. 10-areas.png         room areas with a void
3. 10-polylength.png    wall run with parts listed
4. 10-find-similar.png  reuse thiran-uc1/shots/13-find-results.png
5. 10-register.png      grouped by subject with Totals
6. 10-rates.png         Unit price + formula column
7. 10-export.png        exported takeoff open in Numbers or Excel
-->
<!--
WEEK 1 BUILD (18 Nov): screens captured on the released app 0.17.13 (tag v0.17.13), fictional Lumen House set, via thiran-social/guides/capture-week1.mjs.
DROPPED (could not be captured honestly): the exported takeoff open in a spreadsheet, subtotals visible
-->
