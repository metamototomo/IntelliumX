---
date: '2026-01-11T11:48:35+11:00'
draft: false
title: 'Setting Up Proxy Using WinHTTP in Windows'
tags: ["Proxy", "WinHTTP"]
categories: ["Technology"]
---

## Summary
WinHTTP (Windows HTTP Services) allows you to configure proxy settings for applications that use the WinHTTP API. This is useful when you need to route HTTP traffic through a proxy server. Here's a simple guide on how to manage proxy settings using the `netsh winhttp` command.

![](2026-01-11-11-50-25.png)

### 1. Check Current Proxy Settings

To view your current WinHTTP proxy configuration, use:

```powershell
netsh winhttp show proxy
```

### 2. Set Proxy Server

To configure a proxy server, use the following syntax:

```powershell
netsh winhttp set proxy [proxy-server] [bypass-list]
```

For example, to set a proxy server at `10.10.2.107` and bypass it for `google.com`:

```powershell
netsh winhttp set proxy 10.10.2.107 google.com
```

### 3. Reset Proxy Settings

This will clear all proxy settings and configure WinHTTP to connect directly to the internet.

```powershell
netsh winhttp reset proxy
```