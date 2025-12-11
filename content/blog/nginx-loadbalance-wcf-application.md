---
date: '2025-04-21T20:23:55+10:00'
draft: false
title: 'NGINX Load Balancer for WCF App'
tags: ["NGINX", "WCF", "SSL", "Load Balancer"]
categories: ["Technology"]
---

![](2025-04-21-23-29-03.png)

This guide demonstrates how to implement a high-performance NGINX load balancer for WCF applications with the following features:

- Enhanced security through SSL/TLS encryption
- Reliable session management using IP-based persistence
- Custom-tuned configurations for WCF service optimisation
- Advanced timeout and buffer settings to handle complex WCF payloads

The configuration ensures reliable, secure, and efficient load balancing specifically optimised for WCF service applications, with built-in session persistence and performance tuning.

**1. Install required packages and SSL certificates**

```bash
# Update the operating system packages to latest versions
sudo yum update -y

# Install NGINX (web server/load balancer), unzip (for certificate extraction), 
# and tree (for directory visualization)
sudo yum install nginx unzip tree -y

# Start the NGINX service and configure it to start on boot
sudo systemctl start nginx
sudo systemctl enable nginx

# Change to home directory and download SSL certificates from S3
cd ~
aws s3 cp s3://{BUCKET NAME}/certs_v04.zip .
unzip certs_v04.zip

# Combine intermediate and root CA certificates into a bundle
# This creates the certificate chain needed for SSL verification
cat certs/mid-ca.crt certs/ca.crt > certs/ca-bundle.crt

# Create SSL directory in NGINX and copy all certificates there
sudo mkdir -p /etc/nginx/ssl
sudo cp certs/* /etc/nginx/ssl/
```

**2. Create the NGINX load balancer configuration file at ``/etc/nginx/conf.d/bpserver-loadbalancer.conf`` with the following settings**

```bash
upstream bpserver_backend {
    ip_hash;  # Makes the client’s session “sticky” or “persistent” in terms of always trying to select a particular server
    server d11-app-bpe02.gcs.cloud:8199 max_fails=3 fail_timeout=30s;
    server d11-app-bpe03.gcs.cloud:8199 max_fails=3 fail_timeout=30s;
    server d11-app-bpe04.gcs.cloud:8199 max_fails=3 fail_timeout=30s;
}

server {
    listen 8199 ssl;
    server_name d11-lnx-alb01.gcs.cloud;
    
    ssl_certificate     /etc/nginx/ssl/server_001.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;
    ssl_client_certificate /etc/nginx/ssl/ca-bundle.crt;
    ssl_verify_client off;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    location / {
        proxy_pass https://bpserver_backend;
        proxy_ssl_verify off;

        # Additional headers for WCF
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Increase timeouts for WCF operations
        proxy_connect_timeout 300s;
        proxy_read_timeout 300s;
        proxy_send_timeout 300s;

        # Preserve WCF headers
        proxy_pass_request_headers on;
        
        # Buffer settings for larger messages
        proxy_buffer_size 128k;
        proxy_buffers 4 256k;
        proxy_busy_buffers_size 256k;
    }
}
```

**3. Validate the NGINX configuration and restarting the service**

```bash
# Test the NGINX configuration for syntax errors
sudo nginx -t

# Restart NGINX service to apply new configuration
sudo systemctl restart nginx
```

**4. Verify ports established connections to the load balancer**

```bash
netstat -nao | findstr 8199
```

**5. Check Log Files (error log and access log)**

```bash
# View error log in real-time
sudo tail -f /var/log/nginx/error.log

# View access log in real-time
sudo tail -f /var/log/nginx/access.log

# View last 100 lines of error log
sudo tail -n 100 /var/log/nginx/error.log

# Search for specific errors
sudo grep "error" /var/log/nginx/error.log
```

**6. Adjust the logging level**

```
error_log /var/log/nginx/error.log warn;  # Levels: debug, info, notice, warn, error, crit, alert, emerg
```

**Reference:**

https://www.f5.com/glossary/ssl-load-balancer

https://nginx.org/en/docs/http/load_balancing.html

***
## See also:

[Deploy a Amazon Linux 2023]({{< ref "deploy-a-amazon-linux-2023.md" >}})

[NGINX Load Balancer - Bare Metal]({{< ref "nginx-loadbalancer.md" >}})

[NGINX Load Balancer for WCF & gRPC]({{< ref "nginx-loadbalancer-wcf-grpc.md" >}})

[NGINX Container - Secure Web Page]({{< ref "nginx-container-test-web-page.md" >}})

[NGINX Container - Load Balancer]({{< ref "nginx-container-loadbalancer.md" >}})

[Haproxy Container - Load Balancer]({{< ref "haproxy-container-loadbalancer.md" >}})
