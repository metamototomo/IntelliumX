---
date: '2025-04-02T19:41:08+11:00'
draft: false
title: 'SQL Server Container with Tools'
tags: ["SQLCMD", "SQL Server", "SSL", "Docker", "Container"]
categories: ["Technology"]
---

## File and Folder Structure at the end

![](2025-04-02-19-53-47.png)

1. Create ```mssql.conf```

```bash
[network]
tlscert = /var/opt/mssql/secrets/server-bundle.crt
tlskey = /var/opt/mssql/secrets/server.key
tlsprotocols = 1.2
forceencryption = 1
```

2. Create ```Dockerfile```:

```bash
# Use the official Microsoft SQL Server 2022 image as base
FROM mcr.microsoft.com/mssql/server:2022-latest

# Switch to root to install packages
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

# Switch back to mssql user
USER mssql
```

3. Build an image

```bash
# Build new image
sudo docker build -t mssql-with-tools .
```

4. Run commands

```bash
# Run new container
sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=Password123' \
-p 1433:1433 \
-v /data/containers/sql1/data:/var/opt/mssql/data \
-v /data/containers/sql1/log:/var/opt/mssql/log \
-v sql-certs:/var/opt/mssql/secrets:ro \
-v /data/mssql.conf:/var/opt/mssql/mssql.conf:ro \
--restart always \
--name sql1 \
-d mssql-with-tools
```

5. Verify installation:

```bash
# Test sqlcmd
sudo docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -?
```