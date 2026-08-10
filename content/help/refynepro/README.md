# RefynePro User Manual — authoring guide

Source files for the customer help pages published at
`https://www.intelliumx.com/help/refynepro/`.

These source files are maintained directly in the IntelliumX repository and published to the
RefynePro Help Center. Nothing in this folder is rendered by the RefynePro app itself.

---

## Frontmatter

Every page carries exactly these four fields.

```yaml
---
title: "Subscription"
description: "View and manage your RefynePro subscription plan."
category: "Account & Billing"
weight: 30
---
```

- **title** — verb-first where it reads naturally ("Create a folder", "Move documents").
  Noun titles are fine for reference pages such as "Subscription".
- **description** — one sentence, under 160 characters, used for search results and link previews.
- **category** — exactly one of the three below. Copy the string verbatim, including the ampersand.
- **weight** — controls order within the category. Numbered in tens so pages can be inserted later
  without renumbering everything.

### Categories

| Category | Blurb for the category index |
|---|---|
| `Getting Started` | New to RefynePro? Start here to learn the core interface and essential operations. |
| `Daily Operations` | Organise and navigate your documents efficiently every day. |
| `Account & Billing` | Manage your account security, credits, and subscription. |

Filenames are clean slugs with no number prefix — `create-a-folder.md` — because `weight`
handles ordering. This keeps the published URL as `/help/refynepro/create-a-folder/`.

---

## Page format

```markdown
---
title: "Create a folder"
description: "One sentence, under 160 characters."
category: "Daily Operations"
weight: 10
---

One or two sentences saying what this does and when you would want it.

## Steps

1. First action.
2. Second action.

   ![Alt text describing what the reader should look at](2026-08-09-14-26-08.png)

3. Third action.

**Other ways to do this:** the alternative path, in one sentence.

> **Tip:** One short, genuinely useful note. Omit if there is nothing to say.

## Related

- [Create a document](/help/refynepro/create-a-document/)
```

### Rules

- **Three to five steps.** If a task needs more, it is two pages.
- **Bold for anything the user reads on screen.** Button labels, menu items, field names,
  keyboard keys. Never bold for emphasis — that makes real labels ambiguous.
- **Quote labels exactly as the app shows them**, including British spellings
  (**Favourite**, **Summarise**) and existing casing (**Insert Below**, not "insert below").
- **150–250 words per page.** The AI and billing pages run slightly longer; that is the ceiling,
  not the target.
- **Use screenshots where they help.** Prefer one or two focused images, but include more when each
  one explains a distinct action or prevents confusion.
- **Pick one path for the numbered steps.** Most tasks can be done from the Document Tree and from the
  folder view. Do not branch the steps — choose the primary path and put the other in the
  single-sentence "Other ways to do this" line. This is what keeps pages at three to five steps.
- **Screenshots inside a numbered list must be indented three spaces**, otherwise the numbering
  restarts after the image.
- **No "Before you start" or "Tip" block unless it earns its place.** Empty sections add pressure.
- When tutorial videos exist, a single line goes directly under the intro:
  `**Watch instead:** [Create a folder (1:20)](url)`.

**One exception:** `get-to-know-the-refynepro-editor.md` is an orientation page, not a task, so it
uses short labelled sections instead of numbered steps. Every other page follows the format above.

---

## Screenshots

- Live in a directory with the same slug as the page — for example, screenshots referenced by
  `create-a-folder.md` live in `create-a-folder/`.
- Reference each screenshot by its filename, such as `2026-08-09-14-26-08.png`.
- Crop to the relevant region when possible. Keep enough surrounding context for the reader to
  recognise where the control appears.
- Light mode only for the first pass. Dark mode duplicates double the maintenance for little
  gain; revisit only if support questions justify it.
- Realistic but neutral sample content. No personal data, no real customer names.
- Alt text describes what to look at, not what the image is. Write "The New Folder option in the
  Document Tree right-click menu", not "Screenshot of the Document Panel".

---

## Pages

### Getting Started

| Weight | Page | File |
|---|---|---|
| 10 | Get to know the RefynePro Editor | `get-to-know-the-refynepro-editor.md` |
| 20 | Create your first document | `create-your-first-document.md` |
| 30 | Add content to a document | `add-content-to-a-document.md` |
| 40 | Use a built-in AI action | `use-a-built-in-ai-action.md` |
| 50 | Write a custom AI prompt | `write-a-custom-ai-prompt.md` |
| 60 | Choose an AI model | `choose-an-ai-model.md` |
| 70 | Format text | `format-text.md` |
| 80 | Add images | `add-images.md` |
| 90 | Save your work | `save-your-work.md` |


### Daily Operations

| Weight | Page | File |
|---|---|---|
| 10 | Create a folder | `create-a-folder.md` |
| 20 | Create a document | `create-a-document.md` |
| 30 | Move documents | `move-documents.md` |
| 40 | Move folders | `move-folders.md` |
| 50 | Rename and delete items | `rename-and-delete-items.md` |
| 60 | Restore items from trash | `restore-items-from-trash.md` |
| 70 | Find your documents | `find-your-documents.md` |
| 80 | Organise with tags | `organise-with-tags.md` |
| 90 | Favourite a document | `favourite-a-document.md` |
| 100 | Pin a folder to the Document Panel | `pin-a-folder-to-the-document-panel.md` |
| 110 | Insert tables, code and quotes | `insert-tables-code-and-quotes.md` |
| 120 | Lock and unlock a document | `lock-and-unlock-a-document.md` |


### Account & Billing

| Weight | Page | File |
|---|---|---|
| 10 | Set up two-factor authentication | `set-up-two-factor-authentication.md` |
| 20 | Credits and token usage | `credits-and-token-usage.md` |
| 30 | Subscription | `subscription.md` |
| 40 | Delete your account | `delete-your-account.md` |

---

## Accuracy notes

Checked against the code. These are easy to get wrong and must not drift.

**Editor and AI**

- Right-clicking text does **not** open a RefynePro menu. Selecting text shows a floating
  formatting toolbar after roughly one second. **Cmd+K** / **Ctrl+K** shows it immediately.
- **Cmd+K does two different things.** On a blank line it opens the insert menu
  (Table, Code Block, Quote, Bullet List, Numbered List, Divider, Clear Format). With text
  selected it opens the formatting toolbar, which contains **AI Tools**.
- The result buttons are **Discard**, **Insert Below**, **Replace**. There is no
  "Paste under the text", no "Try again", no copy button.
- **Discard still consumes credits.** The AI call completes before the result window appears.
- **Custom is a one-off prompt, not a saved action.** There is no prompt library, despite what
  the marketing page suggests.
- There is **no Cmd+S**. Autosave runs five seconds after you stop typing.
- The browser close warning is the **browser's own dialog**. Do not quote wording for it.
- Images can only be **pasted**, not dragged in. 4 MB limit, JPEG/PNG/WebP/GIF.
- There is **no version history** for edits.

**Files and folders**

- Drag and drop works in the **Document Tree only**, not in the folder contents shown in the Workspace.
- Moving has **no dialog**. Choosing **Move** puts the Document Tree into a mode where valid
  destinations show "← Click to move here".
- **Lock** and **Favourite** live in the Document Header, not in any right-click menu.
- The folder contents shown in the Workspace have a right-click menu with only **Rename** and **Delete**.
- There is **no duplicate** command.
- Search matches **titles and tags**, not document content.
- Trash retention is **7 days**.

**Stored in the browser, not the account.** These reset on a different computer or browser, and
that surprises people: pinned folders, Document Tree sort order, and AI model and parameter settings.

**Do not document — exists in code but users cannot reach it**

- `/analytics` page — no navigation link, placeholder data, "Charts Coming Soon".
- MFA backup or recovery codes — the function is a stub and never runs.
- SMS MFA, "remember this device", login history — described in internal docs only.
- Changing your password while signed in — only the forgotten-password flow at sign-in exists.
- Member-since date or display name in the Account Panel.

---

## Before deployment

- [ ] Finalise each page's category and weight, then synchronize the catalogue above.
- [ ] Confirm slugs derive from filenames and every internal `/help/refynepro/` link resolves.
- [ ] Confirm every referenced screenshot exists, has useful alt text and matches the shipped UI.
- [ ] Confirm **RefynePro** is used consistently in page content and site metadata.
- [ ] Recheck volatile product and billing facts against the release being documented.
- [ ] Preview the built Help Center and check navigation, tables, lists and screenshots.
