---
date: '2025-04-24T16:52:01+10:00'
draft: false
title: 'OpenSSL (4) - Client Certificate'
tags: ["OpenSSL", "SSL Certificate", "Security"]
categories: ["Technology"]
---

## **Create a Client Certificate**

### 1. Generate a client key file

```bash
openssl genrsa -out server/private/client.key 2048
```

### 2. Generate a client Certificate Signing Request (CSR)

```bash
openssl req -config mid-ca/mid-ca.conf -key server/private/client.key -new -sha256 -out server/csr/client.csr
```

e.g., CN=GCS-Client-Certificate-v0x

### 3. Sign the client CSR using the client_cert extension

```bash
openssl ca -config mid-ca/mid-ca.conf -extensions client_cert -days 3650 -notext -in server/csr/client.csr -out server/client-certs/client.crt
```

### 4. Generate client PFX (if needed)

```bash
openssl pkcs12 -inkey server/private/client.key -in server/client-certs/client.crt -export -out server/client-certs/client.pfx -passout pass:
```

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
