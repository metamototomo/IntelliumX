---
date: '2025-05-19T18:37:55+10:00'
draft: false
title: 'Memory Dump Anaylsis - WinDbg'
tags: ["Windows", "Memory Dump"]
categories: ["Technology"]
---

WinDbg is the primary tool from Microsoft to analyze memory dump files.

This is the Step-by-Step guide to Analyze Memory Dump with WinDbg.

### 1. Install WinDbg Preview

- Open Microsoft Store and search for WinDbg Preview.

- Or download it from [WinDbg Preview](https://apps.microsoft.com/detail/9pgjgd53tn86?hl=en-US&gl=AU)

![](2025-05-19-18-58-10.png)

### 2. Open Your Dump File

- Launch WinDbg Preview.

- Click File > Open dump file.

- Select your .dmp file (e.g., C:\Windows\MEMORY.DMP, C:\Windows\Minidump\).

![](2025-05-19-18-56-40.png)

### 3. Use Basic Commands

- After opening the file, type the following in the command window:

```
!analyze -v
```

![](2025-05-19-19-00-22.png)

This gives a detailed analysis: crash cause, likely driver, stack trace, etc.

