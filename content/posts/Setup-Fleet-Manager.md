---
date: '2025-02-09T21:55:18+11:00'
draft: false
title: 'Setup Fleet Manager'
tags: ["Freet Manager", "System Manager", "AWS"]
categories: ["Technology"]
---
## How to Enable GUI Access via Fleet Manager

1. Ensure SSM Agent is Installed and Running
    - Windows EC2 instances must have the "SSM Agent" installed and running.
    - Check the status by the powershell command
```powershell
Get-Service AmazonSSMAgent
```
        
2. Attach a Role with the following  policies
    - AmazonSSMManagedInstanceCore
    - AmazonSSMFullAccess (This is required for GUI access via Fleet Manager)

![](2025-02-09-22-09-30.png)

***
## How to access to EC2 via Fleet Manager

1. Go to "Systems Manager" → "Fleet Manager"

2. Select "EC2" → "Node actions" → "Connect" → "Remote Desktop (RDP)"

![](2025-02-09-22-13-36.png)

3. Start the session in the browser

![](2025-02-09-22-12-21.png)