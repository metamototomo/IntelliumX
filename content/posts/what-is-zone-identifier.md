---
date: '2025-12-21T17:13:50+11:00'
draft: false
title: 'What Is Zone Identifier'
tags: ["Git", "Mac"]
categories: ["Technology"]
---
- **What it is**
    
    `Zone.Identifier` is **Windows-only metadata** stored as an **NTFS Alternate Data Stream (ADS)**.
    
- **Why it exists**
    
    Windows uses it to mark files **downloaded from the Internet** for security purposes.
    
- **Why it appears on macOS/Linux**
    
    NTFS ADS is hidden on Windows, but when files are copied, zipped, or committed to Git and then opened on non-Windows systems, the metadata becomes a **visible file**:
    
    ```
    filename:Zone.Identifier
    ```
    
- **Is it dangerous?**
    
    ❌ No.
    
    It contains only text metadata and is safe to delete.
    
- **Should it be in Git?**
    
    ❌ Never.
    
    It has no meaning outside Windows.
    
- **What to do**
    - Delete existing files:
        
        ```bash
        find . -name'*:Zone.Identifier' -delete
        ```
        
    - Prevent future commits:
        
        ```
        *:Zone.Identifier
        ```
        
- **Common cause**
    
    Repos shared between **Windows ↔ macOS/Linux**.
    

