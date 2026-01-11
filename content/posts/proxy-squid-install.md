---
date: '2026-01-11T10:24:49+11:00'
draft: false
title: 'Proxy Squid Install'
tags: ["proxy", "Linux"]
categories: ["Technology"]
---

![](2026-01-11-11-40-50.png)

## Summary

This guide provides a baseline setup for Squid proxy server. It covers system updates, installing Squid with essential networking tools, configuring a minimal proxy setup that allows local network access.

### 1️⃣ First steps after installation (baseline)

After installing Linux Server and logging in:

```bash
sudo dnf update
sudo dnf upgrade -y
```

Install basic tools (very helpful later):

```bash
sudo dnf install -y \
  squid \
  tcpdump \
  net-tools \
  iproute \
  curl \
  ca-certificates
```

Enable and start Squid:

```bash
sudo systemctl enable squid
sudo systemctl start squid
systemctl status squid
```

You should see **active (running)**

![](2026-01-11-10-30-07.png)


---

### 2️⃣ Baseline Squid config

Backup the original config

```bash
sudo cp /etc/squid/squid.conf /etc/squid/squid.conf.bak
```

Edit the config:

```bash
sudo vi /etc/squid/squid.conf
```

For now, use a **minimal, clean baseline** (this avoids surprises):

```
############################################
# Basic Squid proxy (baseline)
############################################

http_port 3128

# Allow your test network (adjust subnet)
acl localnet src 10.10.0.0/16  # <--- REPLAE WITH YOUR CIDR RANGE
http_access allow localnet
http_access deny all

# Logging
access_log /var/log/squid/access.log

# Conservative defaults
client_idle_pconn_timeout 5 minutes
request_timeout 5 minutes
read_timeout 5 minutes
```

Restart and verify:

```bash
sudo squid -k parse
sudo systemctl restart squid
```

---

### 3️⃣ VMware networking check (important)

#### Connection test

Quick proxy test from Windows:

```powershell
curl-x http://<ubuntu-ip>:3128 https://www.google.com-v
```

#### Confirm Squid sees traffic

On the proxy server:

```bash
sudo tail -f /var/log/squid/access.log
```

#### Block direct HTTPS connection on the machine

This command forces the PC to use the proxy server to access any web pages.

```powershell
# Admin PowerShell
New-NetFirewallRule `
-DisplayName"Block Direct HTTPS" `
-Direction Outbound `
-Protocol TCP `
-RemotePort443 `
-Action Block
```
