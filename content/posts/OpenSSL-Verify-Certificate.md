---
date: '2025-04-24T17:41:29+10:00'
draft: false
title: 'OpenSSL - Verify Certificate'
tags: ["OpenSSL", "SSL Certificate", "Security"]
categories: ["Technology"]
---

### Verify the certificate

```bash
openssl x509 -in server/certs/client.crt -text -noout
openssl x509 -in server/certs/server.crt -text -noout
```

### Verify the certificate chain

```bash
# First, concatenate the CA certificates (leaf to root)
cat mid-ca.crt ca.cert > ca-bundle.crt

# Then verify using the chain file
openssl verify -CAfile ca-bundle.crt server/certs/client.crt
openssl verify -CAfile ca-bundle.crt server/certs/server.crt
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