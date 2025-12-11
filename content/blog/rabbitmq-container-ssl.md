---
date: '2025-03-30T21:40:32+11:00'
draft: false
title: 'RabbitMQ Container - SSL'
tags: ["Docker", "RabbitMQ", "SSL", "Certificate"]
categories: ["Technology"]
---
## Create a container (SSL)

1. First, create a new working directory and prepare your certificate files:

```bash
mkdir gcs-rabbit-ssl
cd gcs-secure-rabbit
mkdir certs
# Copy your certificates to gcs-secure-rabbit/certs:
# - ca.crt
# - mid-ca.crt
# - server-001.crt
# - server-001.key
```

2. Set 644 to these certificate

```bash
chmod 644 certs/*
```

![](2025-03-30-21-52-45.png)

3. Create a ```rabbitmq.conf``` (gcs-secure-rabbit/rabbitmq.conf):

```bash
# RabbitMQ Configuration File
# Disable non-SSL listeners
listeners.tcp = none
listeners.ssl.default = 5671

# SSL configuration
ssl_options.cacertfile = /etc/rabbitmq/ssl/ca-bundle.crt
ssl_options.certfile = /etc/rabbitmq/ssl/server.crt
ssl_options.keyfile = /etc/rabbitmq/ssl/server.key
ssl_options.verify = verify_peer
ssl_options.depth = 2
ssl_options.fail_if_no_peer_cert = true

# Management SSL configuration
management.ssl.port = 15671
management.ssl.cacertfile = /etc/rabbitmq/ssl/ca-bundle.crt
management.ssl.certfile = /etc/rabbitmq/ssl/server.crt
management.ssl.keyfile = /etc/rabbitmq/ssl/server.key
```

4. Create a ```Dockerfile``` (e.g., gcs-secure-rabbit/DockerFile):

```bash
FROM rabbitmq:3.11.10-management

# Create SSL directory
RUN mkdir -p /etc/rabbitmq/ssl

# Copy certificates
COPY ca.crt mid-ca.crt /etc/rabbitmq/ssl/
COPY server-001.crt /etc/rabbitmq/ssl/server.crt
COPY server-001.key /etc/rabbitmq/ssl/server.key

# Create bundle certificate
RUN cat /etc/rabbitmq/ssl/mid-ca.crt /etc/rabbitmq/ssl/ca.crt > /etc/rabbitmq/ssl/ca-bundle.crt

# Copy config file
COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf

# Expose SSL ports
EXPOSE 5671 15671

CMD ["rabbitmq-server"]
```

5. Build and run the container:

```bash
# Build the image
sudo docker build -t gcs-secure-rabbit:latest .

# Run the container
sudo docker run -d --hostname secure-rabbit --name secure-rabbit \
-p 15671:15671 \
-p 5671:5671 \
--restart always \
gcs-secure-rabbit:latest
```

6. Check the container logs after running it:

```bash
sudo docker logs secure-rabbit
```

***
## See also:
[RabbitMQ Container - HTTP]({{< ref "rabbitmq-container-http.md" >}})

[Upload Docker an Image to ECR]({{< ref "upload-docker-image-to-ecr.md" >}})