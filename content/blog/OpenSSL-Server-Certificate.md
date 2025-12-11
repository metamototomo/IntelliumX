---
date: '2025-02-09T14:43:00+11:00'
draft: false
title: 'OpenSSL (3) - Server Certificate'
tags: ["OpenSSL", "SSL Certificate", "Security"]
categories: ["Technology"]
---
## Create a Server Certificate

### 1. Generate a key file  (It can be one-off operation)

```bash
openssl genrsa -out server/private/server.key 2048
```

### 2. Generate a Certificate Signing Request (CSR)

```bash
openssl req -config mid-ca/mid-ca.conf -key server/private/server.key -new -sha256 -out server/csr/server.csr
```

e.g., CN=GCS-Server-Certificate-v0x

### 3. Sign the request (CSR) by Sub-CA

```bash
openssl ca -config mid-ca/mid-ca.conf -extensions server_cert -days 3650 -notext -in server/csr/server.csr -out server/certs/server.crt
```

### 4. Generate PFX with NO password

```bash
openssl pkcs12 -inkey server/private/server.key -in server/certs/server.crt -export -out server/certs/server.pfx -passout pass:
```

### 5. Result

![](2025-03-10-21-41-44.png)


***
## See also:
[Download from CloudShell]({{< ref "Download-from-CloudShell.md" >}})

[OpenSSL - Initial Setup]({{< ref "OpenSSL-Intial-Setup.md" >}})

[OpenSSL (1) - Root CA]({{< ref "OpenSSL-CA.md" >}})

[OpenSSL (2) - Intermediate CA]({{< ref "OpenSSL-Intermediate-CA.md" >}})

[OpenSSL (3) - Server Certificate]({{< ref "OpenSSL-Server-Certificate.md" >}})

[OpenSSL (4) - Client Certificate]({{< ref "OpenSSL-Client-Certificate.md" >}})

[OpenSSL - Verify Certificate]({{< ref "OpenSSL-Verify-Certificate.md" >}})

[OpenSSL - Revoke Certificate]({{< ref "OpenSSL-Revoke-Certificate.md" >}})