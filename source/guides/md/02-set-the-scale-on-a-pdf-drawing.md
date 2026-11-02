<!--
DRAFT 1 · for gate 1 (Jay's OK) · 2 Nov 2026
Web address: thiran.app/guides/set-the-scale-on-a-pdf-drawing
Search title: How to set the scale on a PDF drawing | Thiran
Meta description: Set the scale on a PDF drawing so every measurement is right: pick it from a list, calibrate from a known distance, or give each detail its own scale.
Target searches: set scale pdf, change measurement units on a pdf drawing
Source of steps: in-app Help (measure.ts: calibrate, viewport, measurements-panel) on the released app, 0.17.10
-->

# How to set the scale on a PDF drawing

To set the scale on a PDF drawing, pick the drawing's scale (such as 1:100) from a list, or calibrate by clicking two points a known distance apart and typing that distance. After that, every length and area you measure is in real units.

In Thiran you often don't need to do anything: the scale written on the drawing is read when it opens. This guide shows how to check it, set it, and fix it when a sheet was printed at the wrong size.

## 1. Check the scale first

Open the drawing and look at the scale in the status bar at the bottom of the screen.

- If it shows a scale, such as 1:100, it was read from the drawing. Check it matches the title block.
- If it says **Not scaled**, set it using step 2 or 3.

**Screenshot:** status bar close-up showing the scale on Lumen House A-101.

## 2. Pick the scale from a list

Use this when you know the scale and the sheet was printed at its proper size.

1. Click the scale in the status bar and choose **Set scale…**
2. Pick the scale, such as 1:100.
3. If an A1 sheet was printed at A3, say so here. Thiran works out the difference.
4. Choose the pages it applies to.

**Screenshot:** the Set scale box with 1:100 picked.

## 3. Or calibrate from a known distance

Use this when the scale isn't written down, or the sheet was printed or scanned at an unknown size.

1. Choose **Calibrate**.
2. Click two points a known distance apart, such as two grid lines.
3. Type the real distance, for example 6000 mm or 6 m.

The sheet now measures to scale.

**Screenshot:** Calibrate between grid lines A and B on A-101, with 6000 mm typed.

## 4. Give a detail its own scale

Many sheets mix scales: a 1:100 plan with a 1:20 detail beside it. Give the detail its own scale area, called a viewport.

1. Choose **Viewport (region scale)**.
2. Drag a box round the detail. If a scale is written inside the box, it's already filled in.
3. Type the ratio (20 for 1:20) and press Enter.

Measurements inside the box now use that scale. The rest of the sheet keeps the page scale. Views titled with their scale, such as SCALE 1:50, get a viewport automatically when the drawing opens.

**Screenshot:** a viewport box dragged round one view, with its scale typed in. (Have: thiran-uc1/shots/04-scale-box.png, 05-scale-set.png)

## 5. Use the same scale on every page

Open the Measurements panel and choose **All pages** to copy this page's scale to every page.

## 6. Check before you measure

Measure a length you already know, such as a grid spacing, before you start your takeoff. If it's out, set the scale again. Anything you've already measured updates straight away.

## Change the measurement units

- **For one sheet:** in the Measurements panel, choose the units and the number of decimal places.
- **For everything:** Preferences › Decimal places sets one number of decimals for every measurement and total. Preferences › Takeoff lengths totals lengths in m or cm.
- **For one line:** select it, then pick its unit in Properties: mm, cm, m, in, ft, or feet and inches.

Metric is the default. Imperial sheets show feet and inches.

**Screenshot:** the Measurements panel with the units and decimal places.

## Common questions

**Why are my measurements wrong?**
Usually the sheet was printed at a different size from the one in the title block, such as an A1 drawing printed at A3. Calibrate from a known distance (step 3), or say the printed size in Set scale (step 2).

**Can one sheet have more than one scale?**
Yes. Draw a viewport round each part that has its own scale (step 4).

**Do I have to set the scale again when a new revision comes in?**
If the new revision has its scale written on it, it's read when it opens. Check the status bar as in step 1.

---

## Try Thiran free for 7 days

Set the scale once and measure in real units, on Mac, Windows and the web.
**[Start your 7-day free trial]** → my.thiran.app

**Next guide:** [How to measure areas and lengths on a PDF](./measure-areas-and-lengths-on-a-pdf)

<!--
SCREENSHOTS TO CAPTURE (real app, main 0.17.10, fictional Lumen House set)
1. NEED  02-status-scale.png  status bar scale close-up, then the menu that opens from it
2. NEED  02-set-scale.png     Set scale box, 1:100 picked
3. NEED  02-calibrate.png     Calibrate between two grid lines, 6000 mm typed
4. HAVE  04-scale-box.png / 05-scale-set.png / 06-scale-done.png (thiran-uc1/shots)
5. NEED  02-units.png         Measurements panel: units and decimals
CAPTURED 2 Nov (shots/web/): 02-status-scale, 02-set-scale, 02-calibrate (6000 mm typed), 02-units. Viewport: thiran-uc1 04/05/06. All done.
-->
