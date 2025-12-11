---
date: '2025-04-13T22:30:23+10:00'
draft: false
title: 'HAProxy Container - Load Balancer'
tags: ["HAProxy", "Docker", "Container", "SSL", "Load Balancer"]
categories: ["Technology"]
---

## HAProxy Load Balancer with SSL Termination



### 1. Install Docker

```bash
sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
```

### 2. Install Docker Compose

```bash
# Download Docker Compose binary
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Make it executable
sudo chmod +x /usr/local/bin/docker-compose

# Verify the installation
docker-compose --version
```

### 3. Create a Docker Compose file (docker-compose.yml):

```yaml
version: '3'
services:
  haproxy:
    image: haproxy:latest
    ports:
      - "443:443"
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
      - ./certs:/etc/ssl/certs:ro
    restart: always
```

### 4. Create SSL certificates directory and copy certificates:

```bash
mkdir certs
cp ~/certs/server-bundle.crt certs/
cp ~/certs/server.key certs/
cat certs/server.key certs/server-bundle.crt > certs/server.pem
```

### 5. Create HAProxy configuration file (haproxy.cfg):

```bash
global
    log /dev/log local0
    log /dev/log local1 notice
    daemon
    maxconn 2000

defaults
    log global
    mode http
    option httplog
    option forwardfor
    timeout connect 5000
    timeout client  50000
    timeout server  50000

frontend https_front
    bind *:443 ssl crt /etc/ssl/certs/server.pem
    mode http

    # Add URL path rule for Swagger
    use_backend servers if { path_beg /swagger }
    default_backend servers

backend servers
    mode http
    balance roundrobin
    server win1 d11-api-demo1.gcs.cloud:443 ssl verify none check
    server win2 d11-api-demo2.gcs.cloud:443 ssl verify none check

```

This configuration will route any requests starting with /swagger to your backend servers. The only change needed is adding the path rule in the frontend section.

### 6. Deploy using Docker Compose

```bash
sudo docker-compose down
sudo docker-compose up -d
```

### 7. Verify the deployment:

```bash
sudo docker-compose ps
sudo docker-compose logs
```

***
## See also:

[NGINX Load Balancer - Bare Metal]({{< ref "nginx-loadbalancer.md" >}})

[NGINX Container - Secure Web Page]({{< ref "nginx-container-test-web-page.md" >}})

[NGINX Container - Load Balancer]({{< ref "nginx-container-loadbalancer.md" >}})

[NGINX Load Balancer for WCF App]({{< ref "nginx-loadbalance-wcf-application.md" >}})

[NGINX Load Balancer for WCF & gRPC]({{< ref "nginx-loadbalancer-wcf-grpc.md" >}})

[Deploy a Amazon Linux 2023]({{< ref "deploy-a-amazon-linux-2023.md" >}})