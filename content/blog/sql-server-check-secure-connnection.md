---
date: '2025-03-27T14:01:38+11:00'
draft: false
title: 'SQL Server - Check Secure Connnection'
tags: ["SQLCMD", "SQL Server", "SSL"]
categories: ["Technology"]
---
```bash
 sqlcmd -S d11-sql-db001.gcs.cloud -U sa -P Password123
 1 >
 2 >
 3 < exit
```

```bash
sqlcmd -S d11-sql-db001.gcs.cloud -U sa -P Password123 -Q "SELECT session_id, encrypt_option FROM sys.dm_exec_connections WHERE session_id = @@SPID;"

session_id  encrypt_option
				53  FALSE
```
---