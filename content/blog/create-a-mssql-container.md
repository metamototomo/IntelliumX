---
date: '2025-04-04T20:40:37+11:00'
draft: false
title: 'Create a MS SQL Server Container'
tags: ["Docker", "Container", "AWS"]
categories: ["Technology"]
---


```bash
# This is the current folder structure
sh-5.2$ tree
.
├── Dockerfile
├── backups
│   ├── APP-6.3.2-lab_Stage_2.bak
│   ├── APP-6.3.2-lab_Stage_3.bak
│   ├── APP-6.3.2-lab_Stage_4.bak
│   ├── v9.1.23_APP_632_lab_Stage_3.bak
│   └── v9.1.23_APP_632_lab_Stage_4.bak
├── certs
│   ├── server-bundle.crt
│   └── server.key
├── containers
│   └── sql1
│       ├── data [error opening dir]
│       ├── log [error opening dir]
│       └── secrets [error opening dir]
└── mssql.conf
```

1. Create `Dockerfile` file

```bash
FROM mcr.microsoft.com/mssql/server:2022-latest

USER root

# Install required dependencies
RUN apt-get update && \
    apt-get install -y curl apt-transport-https gnupg2 && \
    mkdir -p /etc/apt/keyrings && \
    curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/keyrings/microsoft.gpg && \
    chmod 644 /etc/apt/keyrings/microsoft.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/ubuntu/22.04/prod jammy main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools unixodbc-dev && \
    ln -s /opt/mssql-tools/bin/sqlcmd /usr/bin/sqlcmd && \
    ln -s /opt/mssql-tools/bin/bcp /usr/bin/bcp && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch back to default user
USER mssql
```

2. Create `mssql.conf` file

```bash
[network]
tlscert = /var/opt/mssql/secrets/server-bundle.crt
tlskey = /var/opt/mssql/secrets/server.key
tlsprotocols = 1.2
forceencryption = 1
```

3. Build an image

```bash
# Build new image
sudo docker build -t mssql-with-tools .
```

4. Test locally
```bash
# Run new container
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=Password123' \
-p 1433:1433 \
-v /data/containers/sql1/data:/var/opt/mssql/data \
-v /data/containers/sql1/log:/var/opt/mssql/log \
-v sql-certs:/var/opt/mssql/secrets:ro \
-v /data/mssql.conf:/var/opt/mssql/mssql.conf:ro \
-v /data/backups:/var/opt/mssql/backups \
--restart always \
--name sql1 \
-d mssql-with-tools
```

5. Build a custom container and push into ECR in AWS.

```bash
# The container URI is below
ACCOUNTID.dkr.ecr.ap-southeast-2.amazonaws.com/gcs-sql-server:latest
```

6. Then run the script to deploy a MS SQL Container

```bash
#=============================================================================
# The following approach successfully copy "server.key"
#=============================================================================
# Create a Docker volume for the certificates
sudo docker volume create sql-certs

# Copy the necessary certificate files into the volume
sudo cp /data/certs/server-bundle.crt /var/lib/docker/volumes/sql-certs/_data/
sudo cp /data/certs/server.key /var/lib/docker/volumes/sql-certs/_data

# Change the ownership
sudo chown -R 10001:0 /var/lib/docker/volumes/sql-certs/_data/
sudo chmod -R 600 /var/lib/docker/volumes/sql-certs/_data/

# Retrieve an authentication token and authenticate your Docker client to your registry. Use the AWS CLI:
aws ecr get-login-password --region ap-southeast-2 | sudo docker login --username AWS --password-stdin ACCOUNTID.dkr.ecr.ap-southeast-2.amazonaws.com

# Deploy MS SQL Server container
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=Password123' \
-p 1433:1433 \
-v /data/containers/sql1/data:/var/opt/mssql/data \
-v /data/containers/sql1/log:/var/opt/mssql/log \
-v sql-certs:/var/opt/mssql/secrets:ro \
-v /data/mssql.conf:/var/opt/mssql/mssql.conf:ro \
-v /data/backups:/var/opt/mssql/backups \
--restart always \
--name sql1 \
-d ACCOUNTID.dkr.ecr.ap-southeast-2.amazonaws.com/gcs-sql-server:latest

```

7. After the deployment, check the status of the container

```bash
# Check the login
sudo docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 'Password123'

#Check the files
sudo docker exec -it sql1 ls -l /var/opt/mssql/backups
```

---