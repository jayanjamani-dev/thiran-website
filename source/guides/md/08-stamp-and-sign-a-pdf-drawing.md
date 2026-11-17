<!--
DRAFT 1 · for gate 1 (Jay's OK) · 18 Nov 2026
Web address: thiran.app/guides/stamp-and-sign-a-pdf-drawing
Search title: How to stamp and sign a PDF drawing | Thiran
Meta description: Add an approval stamp, a custom stamp or your signature to a PDF drawing, sign it with a digital ID if you need to, and send it back. Step-by-step guide.
Target searches: how to add stamp on pdf document, how to add stamp pdf, how to sign a pdf file and send it back, how to sign a pdf file on a computer
Source of steps: in-app Help on main @ eee0f437 (markup.ts: stamp, approval, signature; documents.ts: digital-signatures, flatten, export-print; collab.ts: email; start.ts: open-files)
-->

# How to stamp and sign a PDF drawing

To stamp and sign a PDF drawing, open it in a markup tool, place a stamp such as Approved on the sheet, add your signature, save, and send the PDF back. The stamp and signature are saved inside the PDF, so the person who gets it sees them in their usual PDF reader.

This guide shows four ways to sign off a drawing in Thiran, on the fictional Lumen House set, from a quick stamp to a certified digital signature.

## What you need

- The PDF drawing or document to sign.
- Thiran on Windows, Mac or the web, on your computer.
- For a certified digital signature only: a digital ID. You can make one in Thiran (step 5).

## 1. Open the drawing

Drag the PDF onto Thiran, or choose **File › Open**. If it came to you in Google Drive or OneDrive, open it from there with **File › Open from…** and save it straight back.

**Screenshot:** Lumen House shop drawing M-301 open, title block in view

## 2. Place a stamp

1. Choose the arrow beside **Stamp** on the toolbar and pick a stamp, such as Approved or For Construction.
2. Click where it goes, or drag to size it.
3. To place the same stamp again later, press the Stamp key.

**Screenshot:** Stamp list open, Approved placed beside the title block

## 3. Make your own stamp

Choose the arrow beside **Stamp**, then:

- **New text stamp…** Give it a label name and the stamp text. You can fill in your name and the date by themselves, for example CHECKED {author} {date}.
- **New image stamp…** Use a picture, such as your company logo or a scanned signature.

The page tells you when the stamp is ready to place. To remove one of your own stamps, choose **Delete custom stamp** from the same arrow.

Signed in to your account, your stamps follow you to every computer you use Thiran on.

## 4. Use an approval stamp for review sign-off

A plain stamp says one thing. An **Approval** stamp records the review: a status, your name, your title, the date and your signature.

1. Choose **Approval stamp** on the toolbar.
2. Click where the stamp goes, or drag to set its width.
3. Choose the status (Approved, Approved as noted, Revise and resubmit or Rejected), check your name, title and date, and sign: type your name, draw it, or use your saved signature.
4. Place it.

Once placed, you can move the stamp but you can't edit what it says. To change the decision, select it and choose **Replace** in Properties. The old stamp is kept on record, so there's a trail of who approved what. Deleting one asks you first.

You can design your own approval stamp from the arrow beside the button, with your logo, colours, fields and the statuses your office uses, such as Approved, Approved as noted, Revise and resubmit or Rejected.

**Screenshot:** Approval stamp dialog with status chosen and a drawn signature

## 5. Add a signature

**A hand signature on the sheet**

1. Choose **Signature** on the toolbar (or **Annotate › Insert › Signature**).
2. Sign above the line in the pad with your mouse, pen or finger, or choose your saved signature. Tick **Save my signature on this device** to use it next time.
3. Choose **Place signature**, then click where it goes.

You can move or resize it like a stamp. It's a picture of your signature on the drawing, saved as a standard PDF stamp.

**A certified digital signature**

When the document needs a signature that can be checked, sign it with a digital ID instead:

1. If you don't have a digital ID yet, choose **Pages › Security › Create digital ID…**.
2. Choose **Sign document…**, pick your digital ID file, add a reason and location, and choose a visible signature box or an invisible one.
3. Anyone can use **Validate signatures** to check every signature and whether the file changed after signing.

Sign last. Any change after signing shows as a change to the signed document.

**Screenshot:** Sign document dialog with reason "Reviewed for construction" and location "Brisbane"

## 6. Save and send it back

1. Choose **File › Save**. Stamps and signatures are saved inside the PDF.
2. To stop anyone moving your stamps, flatten them on a copy: they become part of the page.
3. To send it, signed in, choose **Email document…**, type up to 10 addresses, a subject and a message, and leave **Attach the PDF with its markups** ticked. Replies come to you. Attachments can be up to 25 MB.

Or print it with **File › Print…**. Your stamps and signature print with it.

## Common questions

**Is a signature stamp the same as a digital signature?**
No. A hand signature or approval stamp is a picture on the drawing. For a certified digital signature, use **Sign document…** with a digital ID.

**Can I stamp every sheet in a set at once?**
Yes. The batch tools can stamp every page of many PDFs, for example FOR CONSTRUCTION.

**Will the stamp show in other PDF readers?**
Yes. Stamps are saved as standard PDF markups, so they show in other readers.

**Can I sign on my computer without printing?**
Yes. Sign in the pad with your mouse, trackpad or pen, place it, save and send.

---

## Try Thiran free for 7 days, no card needed

Stamp, sign and send drawings on Windows, Mac and the web.
**[Start your 7-day free trial]** → my.thiran.app

**Related guides:** [How to annotate and redline a PDF drawing](./annotate-and-redline-a-pdf-drawing) · [How to annotate a PDF on a Mac](./annotate-a-pdf-on-a-mac)

<!--
SCREENS TO CAPTURE (real app, main, fictional Lumen House set)
1. 11-open.png           M-301 open, title block in view
2. 11-stamp.png          can reuse shots/web/01-stamp-list.png
3. 11-approval.png       Approval dialog: status chosen, drawn signature
4. 11-signature-pad.png  Signature pad with Save my signature ticked
5. 11-sign-document.png  Sign document dialog, visible box
6. 11-email.png          Email a document dialog, fictional addresses
-->
<!--
WEEK 1 BUILD (18 Nov): screens captured on the released app 0.17.13 (tag v0.17.13), fictional Lumen House set, via thiran-social/guides/capture-week1.mjs.
-->
