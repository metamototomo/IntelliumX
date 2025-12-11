---
date: '2025-02-18T21:40:50+11:00'
draft: false
title: 'How to Disable Sounds in vs Code'
tags: ["VS Code"]
categories: ["Technology"]
---
## How to disable sounds in VS Code.

1. Open the **Command Palette** (`Ctrl + Shift + P`).

2. Search for **"Preferences: Open Settings (JSON)"** and select it.

![](2025-02-18-23-41-41.png)

3. Add the following line inside the JSON file:
```json
"editor.accessibilitySupport": "off",
```

![](2025-02-18-23-42-44.png)