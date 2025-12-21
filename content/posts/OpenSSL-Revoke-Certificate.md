---
date: '2025-04-24T17:19:22+10:00'
draft: false
title: 'OpenSSL - Revoke Certificate'
tags: ["OpenSSL", "SSL Certificate", "Security"]
categories: ["Technology"]
---
***
## Revoke a certificate

```bash
openssl ca -config mid-ca/mid-ca.crt -revoke server/certs/server.crt
cat mid-ca/index
```

![](2025-04-24-18-22-40.png)


***
## See also:

[OpenSSL - Initial Setup]({{< ref "OpenSSL-Intial-Setup.md" >}})

[OpenSSL (1) - Root CA]({{< ref "OpenSSL-CA.md" >}})

[OpenSSL (2) - Intermediate CA]({{< ref "OpenSSL-Intermediate-CA.md" >}})

[OpenSSL (3) - Server Certificate]({{< ref "OpenSSL-Server-Certificate.md" >}})

[OpenSSL (4) - Client Certificate]({{< ref "OpenSSL-Client-Certificate.md" >}})

[OpenSSL - Verify Certificate]({{< ref "OpenSSL-Verify-Certificate.md" >}})

[OpenSSL - Revoke Certificate]({{< ref "OpenSSL-Revoke-Certificate.md" >}})