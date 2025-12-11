---
date: '2025-03-10T21:36:31+09:00'
draft: false
title: 'OpenSSL - Initial Setup'
tags: ["OpenSSL", "SSL Certificate", "Security"]
categories: ["Technology"]
---

## OpenSSL Initial Setup

### 1. Create a folder structure

```bash
mkdir -p certs/{ca,mid-ca,server}/{private,certs,newcerts,crl,csr}
```

![](2025-03-10-21-48-33.png)

### 2. Change the permissions

```bash
chmod -v 700 certs/{ca,mid-ca,server}/private
```

![](2025-03-10-21-49-06.png)

### 3. Create index files

```bash
touch certs/{ca,mid-ca}/index
```

![](2025-03-10-21-49-25.png)

### 4. Set a serial number

```bash
openssl rand -hex 16 > certs/ca/serial
openssl rand -hex 16 > certs/mid-ca/serial
```

![](2025-03-10-21-49-55.png)

### 5. Copy and place the configuration files

[ca.conf](ca.conf) - [mid-ca.conf](mid-ca.conf)

![](2025-03-10-21-50-13.png)


***
## See also:

[OpenSSL - Initial Setup]({{< ref "OpenSSL-Intial-Setup.md" >}})

[OpenSSL (1) - Root CA]({{< ref "OpenSSL-CA.md" >}})

[OpenSSL (2) - Intermediate CA]({{< ref "OpenSSL-Intermediate-CA.md" >}})

[OpenSSL (3) - Server Certificate]({{< ref "OpenSSL-Server-Certificate.md" >}})

[OpenSSL (4) - Client Certificate]({{< ref "OpenSSL-Client-Certificate.md" >}})

[OpenSSL - Verify Certificate]({{< ref "OpenSSL-Verify-Certificate.md" >}})

[OpenSSL - Revoke Certificate]({{< ref "OpenSSL-Revoke-Certificate.md" >}})