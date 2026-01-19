---
date: '2026-01-19T19:01:12+11:00'
draft: false
title: 'Python - Enable Virtual Environment'
tags: ["Python"]
categories: ["Technology"]
related:
    - python-check-version
---
### Open your repo in VS Code

```bash
cd your-new-repo
code .
```

### Create a virtual environment

```bash
# MacOS / Linux
python3 -m venv .venv

# Windows
python-m venv .venv
```

### Activate the virtual environment

```powershell
# MacOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\Activate.ps1
```

### Install packages

```bash
pip install requests boto3
```

### Freeze dependencies

```bash
pip freeze > requirements.txt
```

Later, anyone can recreate the env with:

```bash
pip install -r requirements.txt
```