---
date: '2026-01-11T10:42:59+11:00'
draft: false
title: 'SSH Connection in Linux'
tags: ["SSH", "Linux"]
categories: ["Technology"]
---

## 1️⃣ Setup SSH service

Install OpenSSH server

```bash
sudo apt update
sudo apt install -y openssh-server
```

Enable and start the SSH service

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

Check status:

```bash
systemctl status ssh
```

---

## 2️⃣ Allow SSH through the firewall (if enabled)

Ubuntu Server often has **ufw disabled by default**, but check:

```bash
sudo ufw status
```

If it’s active:

```bash
sudo ufw allow ssh
sudo ufw reload
```

---

## 3️⃣ Connect from Windows

From **PowerShell** on Windows:

```powershell
ssh username@<ubuntu-ip>
```

Example:

```powershell
ssh nob@192.168.1.50
```

---