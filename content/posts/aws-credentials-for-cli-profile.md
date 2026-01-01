---
date: '2025-12-23T23:19:52+11:00'
draft: false
title: 'AWS Credentials for CLI (Profile)'
tags: ["AWS", "Security"]
categories: ["Technology"]
---

![](2025-12-23-23-21-32.png)

# 🚀 **Quick Start Guide**

- Create a named profile using **`aws configure --profile [name]`**
- Never set a default profile permanently
- This avoids accidental operations on the wrong AWS account
- Activate profiles temporarily per session using `$env:AWS_PROFILE`
- Or activate per command using `--profile`
- Always clear the active profile when done to prevent unintended AWS operations

---

## ✅ **1. Create the profile (once only)**

In PowerShell:

```powershell
aws configure --profile nob
```

This creates:

- `~\.aws\credentials`
- `~\.aws\config`

---

## ✅ **2. Use the profile *temporarily* in PowerShell**

Option A — **Set environment variable only for the current session**

```powershell
$env:AWS_PROFILE = "nob"
```

---

Option B — **Use profile for one command**

```powershell
aws s3 ls --profile nob
```

---

## ✅ **3. Detach / remove / clear the temporary profile**

**Remove**

```powershell
Remove-Item Env:AWS_PROFILE
```

Check

```powershell
Get-ChildItem Env:AWS_PROFILE
```

***
## See also:

[AWS Credentials for CLI]({{< ref "aws-credentials-for-cli.md" >}})

[AWS Credentials for CLI (Profile)]({{< ref "aws-credentials-for-cli-profile.md" >}})

[AWS STS - Temporary Access Tokens]({{< ref "aws-sts-temporary-access-tokens.md" >}})

[Amazon DynamoDB - Create a Table]({{< ref "dynamodb-create-a-table.md" >}})

[Amazon DynamoDB - Import CSV Data]({{< ref "dynamodb-import-data-from-csv.md" >}})

[AWS Lambda - Create a Function]({{< ref "lambda-create-a-function.md" >}})

[AWS Lambda - Grant Access]({{< ref "lambda-set-access-to-dynamodb.md" >}})

[API Gateway - Usage Plan]({{< ref "api-gateway-usage-plan.md" >}})

[API Gateway - API Key]({{< ref "api-gateway-api-key.md" >}})

[API Gateway - Configuration]({{< ref "api-gateway-configuration.md" >}})

