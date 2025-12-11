---
date: '2025-02-09T14:42:31+11:00'
draft: false
title: 'OpenSSL (2) - Intermediate CA'
tags: ["OpenSSL", "SSL Certificate", "Security"]
categories: ["Technology"]
---

## Create a “Intermediate CA” certificate

### 1. Generate a key file for “Intermediate CA”

```bash
openssl genrsa -aes256 -out mid-ca/private/mid-ca.key 4096
```

### 2. Change the permission of mid-ca.key

```
chmod 400 mid-ca/private/mid-ca.key
```

### 3. Generate a Certificate Signing Request (CSR)

```bash
openssl req -config ca/ca.conf -new -key mid-ca/private/mid-ca.key -sha256 -out mid-ca/csr/mid-ca.csr
```

![](2025-03-09-23-28-23.png)

### 4. Sign the request file by Root-CA

```bash
openssl ca -config ca/ca.conf -extensions v3_mid_ca -days 3650 -notext -in mid-ca/csr/mid-ca.csr -out mid-ca/certs/mid-ca.crt
```

### 5. Change the permission of mid-ca.crt
```
chmod 444 mid-ca/certs/mid-ca.crt
```

### 6. Check a backup file created in newcerts dirctory

![](2025-02-09-15-06-00.png)


### 7. Verify the content

```bash
openssl x509 -noout -text -in mid-ca/certs/mid-ca.crt 
```

### 8. CHECK ca/index.txt

![](2025-03-09-23-41-21.png)


***
## See also:

[OpenSSL - Initial Setup]({{< ref "OpenSSL-Intial-Setup.md" >}})

[OpenSSL (1) - Root CA]({{< ref "OpenSSL-CA.md" >}})

[OpenSSL (2) - Intermediate CA]({{< ref "OpenSSL-Intermediate-CA.md" >}})

[OpenSSL (3) - Server Certificate]({{< ref "OpenSSL-Server-Certificate.md" >}})

[OpenSSL (4) - Client Certificate]({{< ref "OpenSSL-Client-Certificate.md" >}})

[OpenSSL - Verify Certificate]({{< ref "OpenSSL-Verify-Certificate.md" >}})

[OpenSSL - Revoke Certificate]({{< ref "OpenSSL-Revoke-Certificate.md" >}})