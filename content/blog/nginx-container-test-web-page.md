---
date: '2025-04-10T23:21:17+10:00'
draft: false
title: 'NGINX Container - Secure Web Page'
tags: ["NGINX", "Docker", "Container", "SSL"]
categories: ["Technology"]
---
Why Choose NGINX for Your Web Server?

- It's lightweight and high-performance
- Excellent for serving static content and as a reverse proxy
- Simple configuration syntax
- Very popular in containerized environments

So, let’s create a Docker container with Nginx and SSL!

1. First, create a directory structure:

```bash
cd ~
aws s3 cp s3://BUCKET NAME/ . --recursive
sudo yum install unzip tree -y

mkdir nginx-ssl
unzip certs.zip
mv certs nginx-ssl/
unzip html.zip
mv html nginx-ssl/

cd nginx-ssl
mkdir conf

```

2. Create `nginx.conf` in the conf directory: **Change server_name.**

```bash
server {
    listen 443 ssl;
    server_name d11-vdi-lin04.gcs.cloud;
    
    root /usr/share/nginx/html;
	    location / {
		    index index.html;
		    }
		    
    ssl_certificate /etc/nginx/certs/server_001.crt;
    ssl_certificate_key /etc/nginx/certs/server.key;
    ssl_trusted_certificate /etc/nginx/certs/ca-bundle.crt;
    ssl_protocols TLSv1.2 TLSv1.3;
}
```

3. Create the full certificate chain by concatenating the certificates in the correct order:

```bash
cd certs
cat mid-ca.crt ca.crt > ca-bundle.crt
cat server_001.crt mid-ca.crt ca.crt > server-bundle.crt
```

4. Create `Dockerfile`:

```bash
FROM nginx:alpine

RUN mkdir -p /etc/nginx/certs

# Copy SSL certificates
COPY certs/ca-bundle.crt /etc/nginx/certs/
COPY certs/server_001.crt /etc/nginx/certs/
COPY certs/server.key /etc/nginx/certs/

COPY conf/nginx.conf /etc/nginx/conf.d/default.conf
COPY html /usr/share/nginx/html

EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]
```

5. Make sure your HTML content is organized in a directory structure like this:
```bash
 .
└── nginx-ssl
    ├── Dockerfile
    ├── certs
    │   ├── ca-bundle.crt
    │   ├── ca.crt
    │   ├── mid-ca.crt
    │   ├── server-bundle.crt
    │   ├── server.key
    │   ├── server_001.crt
    │   └── server_001.pfx
    ├── conf
    │   └── nginx.conf
    └── html
        ├── colour.conf
        ├── img
        │   └── GCS-AWS-logo_32_v02.png
        ├── index.html
        └── swagger
            └── ui
                └── index
                    ├── img
                    │   └── Tech-Task-v07.png
                    └── index.html
                    
```


6. Build and run the container:

```bash
# Build the image
sudo docker build -t my-secure-nginx:latest .

# Run the container
sudo docker run -d --name secure-nginx \
-p 443:443 \
--restart always \
my-secure-nginx:latest

```

7. Check the status using `curl` command. 

```bash
# -k flag to allow insecure connections
curl -k https://localhost
# Or specify your domain
curl -k https://your-domain.com
# To get more detailed with -v (verbose) flag
curl -kv https://localhost
```

***
## See also:
[Deploy a Amazon Linux 2023]({{< ref "deploy-a-amazon-linux-2023.md" >}})

[NGINX Load Balancer - Bare Metal]({{< ref "nginx-loadbalancer.md" >}})

[NGINX Load Balancer for WCF & gRPC]({{< ref "nginx-loadbalancer-wcf-grpc.md" >}})

[NGINX Container - Load Balancer]({{< ref "nginx-container-loadbalancer.md" >}})

[NGINX Load Balancer for WCF App]({{< ref "nginx-loadbalance-wcf-application.md" >}})

[Haproxy Container - Load Balancer]({{< ref "haproxy-container-loadbalancer.md" >}})

