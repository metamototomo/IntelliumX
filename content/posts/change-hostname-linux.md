---
date: '2025-04-13T07:25:43+10:00'
draft: false
title: 'Change hostname - Linux'
tags: ["Active Directory", "Linux", "hostname"]
categories: ["Technology"]
---

## Change the hostname of a Linux machine that's already joined to Active Directory


1. First, leave the Active Directory domain:

```bash
sudo realm leave gcs.cloud
```

2. Change the hostname using hostnamectl:

```bash
sudo hostnamectl set-hostname new-hostname.gcs.cloud
```

3. Rejoin the Active Directory domain:

```bash
realm join gcs.cloud
```

***
## See also:
[Deploy a Amazon Linux 2023]({{< ref "deploy-a-amazon-linux-2023.md" >}})

