---
date: '2025-03-29T00:10:31+11:00'
draft: false
title: 'Upload Docker Image to ECR'
tags: ["Docker", "Container", "AWS", "ECR"]
categories: ["Technology"]
---
## Configure in AWS management console

1. Stay in the working directory where Dockerfile is located (e.g., ~/gcs-rabbit)

2. Open Repository page in Amazon ECR

3. Create a repository by the code below

```bash
aws ecr create-repository --repository-name gcs-normal-rabbit --region ap-southeast-2
```

![](2025-03-29-00-16-24.png)


4. Click "View push command" and follow the instruction with `sudo` command

![](2025-03-29-00-30-09.png)

***
## See also:
[RabbitMQ Container - HTTP]({{< ref "rabbitmq-container-http.md" >}})

[RabbitMQ Container - SSL]({{< ref "rabbitmq-container-ssl.md" >}})
