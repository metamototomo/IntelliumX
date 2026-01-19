---
date: '2026-01-19T18:57:17+11:00'
draft: false
title: 'Python - Check Version'
tags: ["python"]
categories: ["Technology"]
related:
    - python-enable-virtual-environment
---

### Check default Python versions in Mac OS

```bash
python3 --version
```

### Check where Python is coming from

```bash
which python3
```

### List all Python versions on your system

```bash
ls -l /usr/bin/python*
```

### If you use Homebrew (very common)

```bash
brew list | grep python
brew info python
```