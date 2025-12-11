---
date: '2025-04-13T13:54:12+10:00'
draft: false
title: 'NGINX Load Balancer - Bare Metal'
tags: ["NGINX", "Docker", "Container", "SSL"]
categories: ["Technology"]
---

1. Install NGINX:

```bash
sudo apt update
sudo apt install nginx -y
```

2. Set SSL Certificates
```bash
sh-5.2$ sudo mkdir -p /etc/nginx/ssl
sh-5.2$ sudo cp certs/* /etc/nginx/ssl/
sh-5.2$ sudo ls -l /etc/nginx/ssl/
total 32
-rw-r--r--. 1 root root 3830 Apr 13 15:08 ca-bundle.crt
-r--r--r--. 1 root root 1911 Apr 13 15:08 ca.crt
-r--r--r--. 1 root root 1919 Apr 13 15:08 mid-ca.crt
-rw-r--r--. 1 root root 6082 Apr 13 15:08 server-bundle.crt
-rw-------. 1 root root 1704 Apr 13 15:08 server.key
-rw-r--r--. 1 root root 2252 Apr 13 15:08 server_001.crt
-rw-------. 1 root root 3363 Apr 13 15:08 server_001.pfx
sh-5.2$
```

3. Create the NGINX Load Balancing Config

Edit `/etc/nginx/nginx.conf` or (preferably) add a new file in `/etc/nginx/conf.d/iis-loadbalancer.conf`:

```bash
upstream iis_backend {
    server d11-api-demo1.gcs.cloud:443;
    server d11-api-demo2.gcs.cloud:443;
}

server {
    listen 443 ssl;
    server_name d11-alb-ngx01.gcs.cloud;

    ssl_certificate     /etc/nginx/ssl/server-bundle.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;

    location / {
        proxy_pass https://iis_backend;  # Preserves the full URI path
        proxy_ssl_verify off;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 80;
    server_name d11-alb-ngx01.gcs.cloud;
    return 301 https://$host$request_uri;
}

```

4. Restart NGINX

```bash
sudo nginx -t   # test config
sudo systemctl restart nginx
```

5. TIPS, if the backend servers are IIS, set the Load Balancer's FQDN

![](2025-04-13-15-11-40.png)

***
## See also:
[Deploy a Amazon Linux 2023]({{< ref "deploy-a-amazon-linux-2023.md" >}})

[NGINX Container - Secure Web Page]({{< ref "nginx-container-test-web-page.md" >}})

[NGINX Container - Load Balancer]({{< ref "nginx-container-loadbalancer.md" >}})

[NGINX Load Balancer for WCF App]({{< ref "nginx-loadbalance-wcf-application.md" >}})

[Haproxy Container - Load Balancer]({{< ref "haproxy-container-loadbalancer.md" >}})