---
date: '2025-02-09T15:49:44+11:00'
draft: false
title: 'Download From CloudShell'
tags: ["CloudShell", "Shell", "AWS"]
categories: ["Technology"]
---
## Copy certificate CloudShell

1. Copy directory

```bash
cp -r wildcard-v6 wildcard-v7
```

2. ZIP the directory

```bash
zip -r wildcard-v7.zip wildcard-v7
```

3. Download from CloudShell

![](2025-02-09-15-51-02.png)

***
## See also:

[OpenSSL (3) - Server Certificate]({{< ref "OpenSSL-Server-Certificate.md" >}})

[OpenSSL (4) - Client Certificate]({{< ref "OpenSSL-Client-Certificate.md" >}})
