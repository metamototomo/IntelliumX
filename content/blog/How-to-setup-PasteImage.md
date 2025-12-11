---
date: '2025-02-09T08:04:22+11:00'
draft: false
title: 'How to Setup PasteImage'
tags: ["Hugo", "VS Code"]
categories: ["Technology"]
---

## **How to Paste Images into Your Hugo Blog in VS Code on Mac**


### **1. Install the "Paste Image" Extension in VS Code**

- Open **VS Code**
- Press **`Cmd + Shift + X`** to open Extensions
- Search for **"Paste Image"** by *mushanh*
- Click **Install**

### **2. Configure the Extension to Save Images in Your Blog Folder**

- Open **Settings** (`Cmd + ,`)
- Search for **"pasteImage.path"**
- Set it to:This ensures images are saved inside the **same folder** as the Markdown file.
    
    ```
    ${currentFileNameWithoutExt}
    
    ```

![](2025-02-09-13-24-34.png)

### **3. Set a Shortcut for Pasting Images (Optional but Recommended)**

- Open **Keyboard Shortcuts** (`Cmd + K, Cmd + S`)
- Search for **"Paste Image"**
- Assign a shortcut like **`Cmd + Alt + V`**

### **4. Important**
Delete the folder name from the image path.
![](2025-02-09-13-31-48.png)