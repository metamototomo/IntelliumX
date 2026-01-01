---
date: '2025-06-15T17:12:59+10:00'
draft: false
title: 'AWS STS - Temporary Access Tokens'
tags: ["AWS", "Security"]
categories: ["Technology"]
---

![](2025-06-15-17-14-28.png)

### 1. Generate Temporary Credentials

First, use the AWS STS (Security Token Service) to generate temporary credentials:

```bash
# 3600 x 5 = 18000 (5 hours)
aws sts get-session-token --duration-seconds 18000
```

This will return something like:

```json
{
    "Credentials": {
        "AccessKeyId": "ASIA...",
        "SecretAccessKey": "...",
        "SessionToken": "...",
        "Expiration": "2025-06-13T..."
    }
}
```

### 2. Set Environment Variables

Then set these environment variables:

```bash
# Replace the values with your actual credentials from the previous step.
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
export AWS_SESSION_TOKEN="your_session_token"
export AWS_DEFAULT_REGION="ap-southeast-2"  # Sydney region
```

### 3. Verify the environment variables

```bash
env | grep AWS
```

After setting these variables, try running your Python script again. The credentials will be automatically picked up by the AWS SDK.

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
