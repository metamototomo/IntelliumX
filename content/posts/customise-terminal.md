---
date: '2025-12-21T16:49:48+11:00'
draft: false
title: 'Customise Terminal'
tags: ["Terminal", "Mac"]
categories: ["Technology"]
---

![](2025-12-21-17-04-44.png)

### 🎯 Goal

- Hide `@computername`
- Use a clean, professional prompt
- Reload config safely

---

### ✅ Step 1: Open zsh config with vi

```bash
vi ~/.zshrc
```

---

### ✅ Step 2: Add the custom prompt

```bash
# --- Custom prompt ---

# Colors
BLUE="%F{blue}"
RESET="%f"

# Prompt with color
PROMPT="${BLUE}%1~${RESET} ❯ "
```

---

### ✅ Step 4: Save and exit vi

--- 

### ✅ Step 5: Reload the config

```bash
source ~/.zshrc
```

Your prompt updates immediately.

---

### 🔁 Do I always need to run `source ~/.zshrc`?

- ✅ Yes → to apply changes **now**
- ❌ No → if you open a new Terminal window

