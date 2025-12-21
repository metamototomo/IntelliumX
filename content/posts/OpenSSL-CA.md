---
date: '2025-02-09T14:32:13+11:00'
draft: false
title: 'OpenSSL (1) - Root CA'
tags: ["OpenSSL", "SSL Certificate", "Security"]
categories: ["Technology"]
---
## Create a “Root CA” certificate

### 1. Generate a key file for “Root CA”

```bash
openssl genrsa –aes256 -out ca/private/ca.key 4096
```
![](2025-02-09-14-48-57.png)

### 2. Change the permission of ca.key

```bash
chmod 400 ca/private/ca.key
```

### 3. Check the content of ca.key
```
openssl rsa -noout -text -in ca/private/ca.key
```

### 4. Generate a certificate file for “Root CA”

```bash
openssl req -config ca/ca.conf -key ca/private/ca.key -new -x509 -days 3650 -sha256 -extensions v3_ca -out ca/certs/ca.crt
```
![](2025-02-09-14-50-06.png)

### 5. Change the permission of ca.crt

```bash
chmod 444 ca/certs/ca.crt 
```

### 6. Check the contents of ca.crt

```
openssl x509 -noout -text -in ca/certs/ca.crt
```

***
## See also:

[OpenSSL - Initial Setup]({{< ref "OpenSSL-Intial-Setup.md" >}})

[OpenSSL (1) - Root CA]({{< ref "OpenSSL-CA.md" >}})

[OpenSSL (2) - Intermediate CA]({{< ref "OpenSSL-Intermediate-CA.md" >}})

[OpenSSL (3) - Server Certificate]({{< ref "OpenSSL-Server-Certificate.md" >}})

[OpenSSL (4) - Client Certificate]({{< ref "OpenSSL-Client-Certificate.md" >}})

[OpenSSL - Verify Certificate]({{< ref "OpenSSL-Verify-Certificate.md" >}})

[OpenSSL - Revoke Certificate]({{< ref "OpenSSL-Revoke-Certificate.md" >}})

