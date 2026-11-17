<!--
DRAFT 1 · for gate 1 (Jay's OK) · 18 Nov 2026
Web address: thiran.app/guides/open-and-edit-a-pdf-from-google-drive
Search title: How to open and edit a PDF from Google Drive | Thiran
Meta description: Open a PDF drawing straight from Google Drive, mark it up, and save it back over the same file or as a new copy in a Drive folder. Works with OneDrive too.
Target searches: can i edit a pdf from google drive, edit a pdf from google drive
Source of steps: in-app Help on main @ eee0f437 (start.ts: cloud-drives, recent-files, open-files; collab.ts: storage)
-->

# How to open and edit a PDF from Google Drive

Yes, you can edit a PDF that lives in Google Drive. Open it from Drive in a PDF markup app, make your changes, and save. The file is saved back over the same file in Drive, so your team sees the marked-up version without anyone downloading and re-uploading it.

This guide shows how in Thiran, using the fictional Lumen House drawings kept in a shared Drive folder.

## What you need

- A Google account with the PDF in its Drive.
- Thiran on Windows, Mac or the web.

## 1. Open the PDF from Google Drive

1. Choose **File › Open from…** and pick **Google Drive**.
2. Choose the Google account to use. The first time, sign in to it. In the desktop app, this happens in your web browser.
3. Browse to the PDF and open it.

The drawing opens in its own tab, with a cloud mark on the tab so you know it came from a drive.


## 2. Pick the right account

If you have more than one Google account, say a work one and a personal one, Thiran asks which to use each time you open a drive. The account you used last is already picked:

- Press **Enter** to keep it.
- Pick another account from the list.
- Choose **Use another account** to sign in with a different email address.

Each email address has its own drive, so pick the one the file is in.

## 3. Mark it up

Everything works the same as on a file from your computer: clouds, notes, text, stamps, measurements and counts. For the tools themselves, see [How to annotate and redline a PDF drawing](./annotate-and-redline-a-pdf-drawing).

**Screenshot:** a cloud with callout on A-101 reading "Check window head height"

## 4. Save it back to Google Drive

Choose **File › Save** (Ctrl+S, or ⌘S on a Mac). The PDF is saved back over the same file in Google Drive, with your markups inside it.

Because the markups are saved as standard PDF markups, anyone who opens the file from Drive sees them, whatever PDF reader they use.

**If someone else saved it first:** if a colleague saved the file in Drive after you opened it, nothing is overwritten. You're offered **Save as copy** instead, so neither of you loses work.

## 5. Or save a copy to a Drive folder

To keep the original untouched, or to put a file from your computer into Drive:

1. Choose **File › Save to…**.
2. Pick **Google Drive** and the folder.

The document is saved there as a new file.

## 6. Reopen it later

Open the **File** menu and point to **Open recent**. Files from Google Drive show the drive after their name and reopen from Drive, as the account they came from. You may be asked to sign in again.

Only the file's name and where it came from are remembered. No copy of a Drive file is kept in the browser.

## Keep your drives in one panel

If you open lots of files from the same places, the **Connected storage** panel keeps Google Drive, OneDrive and a folder on your computer side by side. For Google Drive, choose **Open…** to pick a PDF, or **Save to…** to put the document you're viewing there.

## OneDrive works the same way

Choose **File › Open from…** and pick **OneDrive**, then sign in to your Microsoft account. Opening, saving back, saving a copy and switching accounts all work as above. The OneDrive browser shows the account in use, and **Switch account** changes it.

## Stop using an account on this computer

In the drive's account list, choose **Sign out** next to the account. You stay signed in to Thiran.

## Common questions

**Can I edit a PDF in Google Drive without downloading it?**
Yes. Open it with **File › Open from… › Google Drive**, mark it up and save. It's saved back to Drive, with no download and re-upload.

**Will my team see my markups?**
Yes. They're saved inside the PDF in Drive, so anyone with access sees them in their PDF reader.

**What if Google Drive says "Set up by your administrator"?**
Your organisation hasn't switched that drive on yet. Ask your IT team.

**Does it work on the web as well as the desktop app?**
Yes, on Windows, Mac and the web. In the desktop app, you sign in to Google in your web browser the first time.

---

## Try Thiran free for 7 days, no card needed

Open drawings from Google Drive or OneDrive, mark them up and save them back, on Windows, Mac and the web.
**[Start your 7-day free trial]** → my.thiran.app

**Related guides:** [How to annotate and redline a PDF drawing](./annotate-and-redline-a-pdf-drawing) · [How to rotate a PDF drawing and save it](./rotate-a-pdf-drawing-and-save-it)

<!--
SCREENS TO CAPTURE (real app, main, fictional Lumen House set, test Google account only)
1. 12-open-from.png     File › Open from… menu
2. 12-account.png       account picker with two fictional accounts
3. 12-drive-tab.png     A-101 open with the cloud mark on its tab
4. 12-markup.png        cloud with callout on A-101
5. 12-storage.png       Connected storage panel
-->
<!--
WEEK 1 BUILD (18 Nov): screens captured on the released app 0.17.13 (tag v0.17.13), fictional Lumen House set, via thiran-social/guides/capture-week1.mjs.
DROPPED (could not be captured honestly): File › Open from… with Google Drive and OneDrive listed | Lumen House A-101 open, cloud mark on its tab | Connected storage panel with Google Drive, OneDrive and Local drive
-->
