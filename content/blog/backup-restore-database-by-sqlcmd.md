---
date: '2025-04-03T16:43:34+11:00'
draft: false
title: 'Backup Restore Database by sqlcmd'
tags: ["Docker", "Container", "Backup", "AWS", "SSM"]
categories: ["Technology"]
---

### **1. Taking Full Backups with `sqlcmd`**


```bash
# Run the commands when you reach an important point in the database configuration
sudo docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Password123' -Q "BACKUP DATABASE [v7.3.1_HUB_511_lab] TO DISK = '/var/opt/mssql/backups/v7.3.1_HUB_511_lab_Stage_3.bak' WITH FORMAT, INIT, NAME = 'Stage3';"
sudo docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Password123' -Q "BACKUP DATABASE [HUB-5.1.1-lab] TO DISK = '/var/opt/mssql/backups/HUB-5.1.1-lab_Stage_3.bak' WITH FORMAT, INIT, NAME = 'Stage3';"

# Check the result
sudo docker exec -it sql1 ls -l /var/opt/mssql/backups/
```

### **2. Restoring a Specific Backup**

```bash
# Restore databases
sudo docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Password123' -Q "RESTORE DATABASE [v7.3.1_HUB_511_lab] FROM DISK = '/var/opt/mssql/backups/v7.3.1_HUB_511_lab_Stage_3.bak' WITH REPLACE, RECOVERY;"
sudo docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Password123' -Q "RESTORE DATABASE [HUB-5.1.1-lab] FROM DISK = '/var/opt/mssql/backups/HUB-5.1.1-lab_Stage_3.bak' WITH REPLACE, RECOVERY;"
```

### **3. Restoring a Specific Backup via SSM**

```bash
# Restore database via SSM
aws ssm send-command \
    --instance-ids "i-0e0df3af14a11b3d1" \
    --document-name "AWS-RunShellScript" \
    --parameters 'commands=[
        "sudo docker exec sql1 /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P '\''Password123'\'' -Q \"RESTORE DATABASE [v7.3.1_HUB_511_lab] FROM DISK = '\''/var/opt/mssql/backups/v7.3.1_HUB_511_lab_Stage_3.bak'\'' WITH REPLACE, RECOVERY;\""
    ]' \
    --region "ap-southeast-2"
```



```bash
# Check the Log in case of failure
aws ssm list-command-invocations --command-id abab87ca-7abb-4746-8666-fa6ebbe67b51 --details
```
---