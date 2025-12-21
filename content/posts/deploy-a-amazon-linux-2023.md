---
date: '2025-02-25T23:16:13+11:00'
draft: false
title: 'Deploy a Amazon Linux 2023'
tags: ["Linux", "Domain", "AWS"]
categories: ["Technology"]
---
## Deploy a Linux machine

1. Update OS

```bash
sudo yum update -y
```

2. Update Hostname and check it

```bash
sudo hostnamectl set-hostname DEV-VAR-OIDC2.apj.cloud
hostnamectl
```

3. Update TimeZone and check it

```bash
sudo timedatectl set-timezone Australia/Sydney
timedatectl
```

4. DNS Settings - Make sure all the DNS servers are registered

```bash
sudo vi /etc/resolv.conf
```

![](2025-02-25-23-38-44.png)

5. Install some components for any Linux OS

```bash
sudo yum install sssd-ad sssd-tools realmd adcli
```

6. Install some components for Amazon Linux 2023.

```bash
sudo yum install oddjob oddjob-mkhomedir
```

7. Check the status of Active Directory

```bash
realm discover apj.cloud
```

![](2025-02-25-23-39-45.png)

8. Join the Active Directory Domain

```bash
sudo realm join apj.cloud -U aus -v
realm list
```

![](2025-02-25-23-58-45.png)

***
## See also:
[NGINX Container - Secure Web Page]({{< ref "nginx-container-test-web-page.md" >}})

[Change hostname - Linux]({{< ref "change-hostname-linux.md" >}})
