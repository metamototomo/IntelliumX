---
date: '2026-01-10T23:31:42+11:00'
draft: false
title: 'WSL - Start up a Distibution'
tags: ["WSL", "Linux"]
categories: ["Technology"]
---

## Summary

This guide explains how to manage and start up Linux distributions in Windows Subsystem for Linux (WSL). 

![](2026-01-10-23-32-51.png)

1. Check Available Linux Distributions

```powershell
# Check which distribution is set as default (marked with *)
wsl --list --verbose
```

2. Start Up a Distribution

```powershell
# case insenstive
wsl -d fedoralinux-42
```

3. Verify the Distribution (Optional)

```powershell
cat /etc/os-release
```

4. Set a Distribution as Default (Optional)

```powershell
# Set a specific distribution as the default
wsl --set-default Ubuntu
```

***
## See also:
[WSL - Install a Linux Distribution]({{< ref "wsl-install-distribution.md" >}})

[WSL - Start up a Distibution]({{< ref "wsl-startup-distibution.md" >}})
