---
date: '2025-04-02T19:20:15+11:00'
draft: false
title: 'Copy Files from a Docker to S3'
tags: ["Docker", "Container", "Backup", "AWS", "S3"]
categories: ["Technology"]
---

## Backup files from Docker Container

1. Login to the machine running the Docker Container
2. Copy back files in Docker container to the current directory

```bash
sudo docker cp sql1:/var/opt/mssql/backups/HUB-5.1.1-lab_Stage_2.bak ./HUB-5.1.1-lab_Stage_2.bak
sudo docker cp sql1:/var/opt/mssql/backups/HUB-5.1.1-lab_Stage_3.bak ./HUB-5.1.1-lab_Stage_3.bak
sudo docker cp sql1:/var/opt/mssql/backups/HUB-5.1.1-lab_Stage_4.bak ./HUB-5.1.1-lab_Stage_4.bak
sudo docker cp sql1:/var/opt/mssql/backups/v7.3.1_HUB_511_lab_Stage_3.bak ./v7.3.1_HUB_511_lab_Stage_3.bak
sudo docker cp sql1:/var/opt/mssql/backups/v7.3.1_HUB_511_lab_Stage_4.bak ./v7.3.1_HUB_511_lab_Stage_4.bak
```

3. Upload them to S3 bucket

```bash
# Change the ownership of the files:
sudo chown ssm-user:ssm-user *.bak

# Create a timestamp variable
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# Upload both files to the timestamped folder
aws s3 cp HUB-5.1.1-lab_Stage_2.bak s3://gcs-share/db-backup/$TIMESTAMP/
aws s3 cp HUB-5.1.1-lab_Stage_3.bak s3://gcs-share/db-backup/$TIMESTAMP/
aws s3 cp HUB-5.1.1-lab_Stage_4.bak s3://gcs-share/db-backup/$TIMESTAMP/
aws s3 cp v7.3.1_HUB_511_lab_Stage_3.bak s3://gcs-share/db-backup/$TIMESTAMP/
aws s3 cp v7.3.1_HUB_511_lab_Stage_4.bak s3://gcs-share/db-backup/$TIMESTAMP/
```