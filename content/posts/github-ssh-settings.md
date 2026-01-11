---
date: '2026-01-10T23:40:52+11:00'
draft: false
title: 'GitHub - SSH Settings (ed25519)'
tags: ["Git", "SSH", "Security"]
categories: ["Technology"]
---

## This workflow ensures:

- **Secure key** (with passphrase)
- **Convenient usage** (Keychain remembers passphrase)
- **SSH-only workflow** → no HTTPS credentials required

![](2026-01-10-23-42-49.png)

### 1) Check for existing keys (optional)

```bash
ls -la ~/.ssh
```

- Look for `id_ed25519` / `id_ed25519.pub`
- If you already have a key you want to use, skip key generation

---

### 2) Generate a new ed25519 key

`ed25519` refers to the **Ed25519 elliptic-curve algorithm**, which is the *modern*, *faster*, and *more secure* replacement for older RSA SSH keys. Replace the email with your GitHub email:

```bash
ssh-keygen -t ed25519 -C "nob@example.com"
```

- Press **Enter** to accept default file (`~/.ssh/id_ed25519`)
- Enter a **strong passphrase**

---

### 3) Ensure correct permissions

```bash
# Private key: ~/.ssh/id_ed25519
# Public key: ~/.ssh/id_ed25519.pub
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

---

### 4) Start `ssh-agent` and add the key

```bash
eval "$(ssh-agent -s)"       # start agent in this session
ssh-add -K ~/.ssh/id_ed25519 # -K ensures macOS Keychain remembers the passphrase
```

---

### 5) Copy your public key to clipboard

Show the key and copy it manually:

```bash
cat ~/.ssh/id_ed25519.pub

# Or the command
pbcopy < ~/.ssh/id_ed25519.pub
```

Then select & copy the whole line (starts with `ssh-ed25519 ...`).

---

### 6) Add key to GitHub

1. Open GitHub in your browser → **Settings** → **SSH and GPG keys** → **New SSH key**.
2. Give it a title (e.g., “MacBook”) and paste the public key you copied.
3. Save.

---

### 7) Test the connection

Run the command below. First time it may ask to confirm the host fingerprint → type `yes`.

```bash
ssh -T git@github.com
```

---

### 8) Clone the repo with SSH

Now clone with the SSH URL. No username or token needed.

```bash
# Clone a new repo
git clone git@github.com:metamototomo/IntelliumX.git

# Update existing repo to use SSH
git remote set-url origin git@github.com:username/repo.git

# Verify
git remote -v

# check which key is used
ssh-add -l
```


