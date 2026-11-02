<!--
DRAFT 1 · for gate 1 (Jay's OK) · 2 Nov 2026
Web address: thiran.app/guides/measure-areas-and-lengths-on-a-pdf
Search title: How to measure areas and lengths on a PDF drawing | Thiran
Meta description: Measure lengths, wall runs and floor areas on a PDF drawing to scale. Take out voids, add a depth for volume, and see the totals as you go. Step by step.
Target searches: pdf measuring tool, measure pdf, measure area on pdf
Source of steps: in-app Help (measure.ts: length, polylength, area, void, measurements-panel) on the released app, 0.17.10
-->

# How to measure areas and lengths on a PDF

To measure a PDF drawing, set its scale, then click the points you want to measure: two points for a length, or every corner for an area. Thiran shows the result on the sheet as you draw and adds it to the totals.

This guide uses the fictional Lumen House plans.

## Before you start: check the scale

Look at the scale in the status bar. If it says **Not scaled**, set it first. See [How to set the scale on a PDF drawing](./set-the-scale-on-a-pdf-drawing).

## Measure a length

1. Choose **Length**.
2. Click the two points, or drag between them. Hold Shift to keep the line at 45° steps.
3. The length shows on the sheet and in the Register.

In Properties you can measure along the line (Aligned), or only its Horizontal or Vertical part, and choose the unit it's written in.

**Screenshot:** a length across Lumen House A-101. (Have: thiran-uc1/shots/09-length.png)

## Measure a run: walls, pipes and cables

For anything with bends, use **Run length**.

1. Choose **Run length**.
2. Click each point along the run. Backspace takes back the last point.
3. For a curved part, press A. Press L to go back to straight lines.
4. Double-click or press Enter to finish.

The total shows on the sheet. Properties lists the length of each part, and you can tick Show on the drawing to write them along the run.

**Screenshot:** a run length along an external wall with each part's length shown.

## Measure an area

1. Choose **Area**, then Polygon or Rectangle in the status bar.
2. Polygon: click each corner, then double-click, press Enter or click the first point to close it. Rectangle: drag from corner to corner.
3. The area shows on the sheet. The Area tool stays on, so you can measure room after room. Press Esc to stop.

**Screenshot:** an area being drawn round a room, then the finished area. (Have: thiran-uc1/shots/07-area-drawing.png, 08-area-done.png)

### Take out holes

To take out a shaft or a column, press **Void** in the status bar and draw the hole inside the area. It's taken off the total.

### Get a volume

Type a depth under Properties › Measurement › Depth, such as a slab thickness. You get the volume as well as the area.

**Screenshot:** an area with a void cut out, and the depth filled in.

## Click exactly on the drawing

Snap catches the ends, middles and corners of the linework as you click, so your points land on the drawing, not near it. Turn it on or off with the one Snap switch.

## See the totals

Open the **Measurements** panel and look under **Quantities**. Choose This page or Whole document. Lengths, areas, volumes and counts are totalled by subject.

Give each measurement a clear subject, such as "Wall type A" or "Floor tiles", so the totals group the way you price them.

**Screenshot:** Quantities with this guide's lengths and areas totalled.

## Common questions

**Can I measure in feet and inches?**
Yes. Choose the unit in the Measurements panel for the sheet, or in Properties for one line.

**My measurement crosses two scales. What happens?**
A measurement uses one scale for all of it. Measure each part inside its own scale area.

**Can I send the measurements to a spreadsheet?**
Yes. See [How to count symbols and export quantities to Excel](./count-symbols-and-export-quantities-to-excel).

---

## Try Thiran free for 7 days

Measure lengths, areas and volumes to scale on Mac, Windows and the web.
**[Start your 7-day free trial]** → my.thiran.app

**Next guide:** [How to compare two drawing revisions](./compare-two-drawing-revisions)

<!--
SCREENSHOTS TO CAPTURE (real app, main 0.17.10, fictional Lumen House set)
1. HAVE  09-length.png, 07-area-drawing.png, 08-area-done.png (thiran-uc1/shots)
2. NEED  03-run-length.png   run length along a wall, segment lengths shown
3. NEED  03-void-depth.png   area with a void, Properties showing Depth
4. NEED  03-quantities.png   Measurements › Quantities totals
CAPTURED 2 Nov (shots/web/): 03-run-length, 03-quantities, 03-void-depth (Workshop 1: 32.61 m² with one void, depth 0.15 m = 4.89 m³). All done. Note: Depth is typed in metres here.
-->
