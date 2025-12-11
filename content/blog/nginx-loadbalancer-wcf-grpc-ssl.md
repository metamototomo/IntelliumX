---
date: '2025-04-24T23:01:47+10:00'
draft: false
title: 'NGINX Load Balancer - Secure gRPC'
tags: ["NGINX", "WCF", "SSL", "gRPC","Load Balancer"]
categories: ["Technology"]
---

![](2025-04-24-23-10-53.png)

This guide extends our previous blog post on [NGINX Load Balancer for WCF & gRPC]({{< ref "nginx-loadbalancer-wcf-grpc.md" >}}) by adding SSL connections to the gRPC protocol. The steps are similar—just update the config file bpserver-loadbalancer.conf

Configuration File Location:
``/etc/nginx/conf.d/bpserver-loadbalancer.conf``

```bash
# NGINX Load Balancer Configuration for Blue Prism Enterprise
# Defining two upstream blocks for different ports

upstream bpserver_backend_8199 {
    ip_hash;
    server d11-app-bpe02.gcs.cloud:8199 max_fails=3 fail_timeout=30s;
    server d11-app-bpe03.gcs.cloud:8199 max_fails=3 fail_timeout=30s;
    server d11-app-bpe04.gcs.cloud:8199 max_fails=3 fail_timeout=30s;
}

upstream bpserver_backend_10000 {
    ip_hash;
    server d11-app-bpe02.gcs.cloud:10000 max_fails=3 fail_timeout=30s;
    server d11-app-bpe03.gcs.cloud:10000 max_fails=3 fail_timeout=30s;
    server d11-app-bpe04.gcs.cloud:10000 max_fails=3 fail_timeout=30s;
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
        proxy_pass https://bpserver_backend_8199;
        proxy_ssl_verify off;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        proxy_connect_timeout 300s;
        proxy_read_timeout 300s;
        proxy_send_timeout 300s;

        proxy_pass_request_headers on;
        
        proxy_buffer_size 128k;
        proxy_buffers 4 256k;
        proxy_busy_buffers_size 256k;
    }
}

server {
    listen 10000 ssl;  # Add ssl here
    http2 on;
    server_name d11-lnx-alb01.gcs.cloud;
    
    # Add SSL certificate configuration
    ssl_certificate     /etc/nginx/ssl/server_001.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;
    ssl_client_certificate /etc/nginx/ssl/ca-bundle.crt;
    ssl_verify_client off;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    location / {
        grpc_pass grpcs://bpserver_backend_10000;  # Change to grpcs:// for SSL
        
        # gRPC specific settings
        grpc_read_timeout 300s;
        grpc_send_timeout 300s;
        
        # Headers for gRPC
        grpc_set_header Host $host;
        grpc_set_header X-Real-IP $remote_addr;
        grpc_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

```
***
## See also:

[NGINX Load Balancer for WCF & gRPC]({{< ref "nginx-loadbalancer-wcf-grpc.md" >}})

[NGINX Load Balancer - Bare Metal]({{< ref "nginx-loadbalancer.md" >}})

[NGINX Container - Secure Web Page]({{< ref "nginx-container-test-web-page.md" >}})

[NGINX Container - Load Balancer]({{< ref "nginx-container-loadbalancer.md" >}})

[NGINX Load Balancing for WCF Applications]({{< ref "nginx-loadbalance-wcf-application.md" >}})

[Haproxy Container - Load Balancer]({{< ref "haproxy-container-loadbalancer.md" >}})

