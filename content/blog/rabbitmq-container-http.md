---
date: '2025-03-28T22:46:51+11:00'
draft: false
title: 'RabbitMQ Container - HTTP'
tags: ["Docker", "RabbitMQ"]
categories: ["Technology"]
---
## Create a container (HTTP)

1. Install Docker

```bash
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
docker --version
sudo docker info
```

2. Create a workiing directory

```bash
mkdir gcs-rabbit
cd gcs-rabbit
```

3. Create “Dockerfile”

```bash
# Use the official RabbitMQ image from the Docker Hub
FROM rabbitmq:3.11.10-management

# Set the default RabbitMQ environment variables
ENV RABBITMQ_DEFAULT_USER=guest
ENV RABBITMQ_DEFAULT_PASS=guest

# Expose ports for RabbitMQ and the management UI
EXPOSE 5672 15672

# Copy rabbitmq.conf if you have additional configurations
COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf

# Start RabbitMQ server
CMD ["rabbitmq-server"]
```

4. Create “rabbitmq.conf”

```bash
# RabbitMQ Configuration File

# Listeners for AMQP (5672) and HTTP management (15672)
listeners.tcp.default = 5672
management.tcp.port = 15672

# Optional: Define a specific IP address to bind to
# (Uncomment the next line to specify a specific IP)
# listeners.tcp.default = 0.0.0.0

# Disable SSL (since you're focusing on HTTP only)
ssl_options.verify = verify_none
ssl_options.fail_if_no_peer_cert = false
```

5. Build a Docker Image

```bash
sudo docker build -t gcs-normal-rabbit:latest .
sudo docker images
```

6. Test the Docker Image locall

```bash
sudo docker run -d --name brown -p 5672:5672 -p 15672:15672 gcs-normal-rabbit
sudo docker logs brown
```

***
## See also:
[RabbitMQ Container - SSL]({{< ref "rabbitmq-container-ssl.md" >}})

[Upload Docker an Image to ECR]({{< ref "upload-docker-image-to-ecr.md" >}})