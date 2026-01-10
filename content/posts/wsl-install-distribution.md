---
date: '2026-01-10T23:27:57+11:00'
draft: false
title: 'WSL - Install a Linux Distribution'
tags: ["WSL", "Linux"]
categories: ["Technology"]
---

## Summary

This guide explains how to install a Linux distribution on Windows Subsystem for Linux (WSL). It covers the installation command using PowerShell, the password setup process, and how to verify the installation by listing all installed distributions.

![](2026-01-10-23-30-09.png)

1. Install a Distribution

```powershell
# for example, install "Ubuntu"
wsl --install -d ubuntu

# set a new password during the step
```

2. Verify the installation

```powershell
# Eixt from the Distribution
exit

# Show the list of Distributions
wsl --list --verbose
```

***
## See also:
[WSL - Install a Linux Distribution]({{< ref "wsl-install-distribution.md" >}})

[WSL - Start up a Distibution]({{< ref "wsl-startup-distibution.md" >}})
