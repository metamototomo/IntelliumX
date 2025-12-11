---
date: '2025-06-15T17:07:00+10:00'
draft: false
title: 'AWS Credentials for CLI'
tags: ["AWS", "Security"]
categories: ["Technology"]
---

![](2025-06-15-17-10-26.png)

### 1. Using AWS CLI Configuration

```bash
aws configure
```

This will prompt you to enter:

- AWS Access Key ID
- AWS Secret Access Key
- Default region name
- Default output format

### 2. Environment Variables

```bash
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
export AWS_DEFAULT_REGION="your_region"
```

### 3. Credentials File

Create or edit ~/.aws/credentials:

```
[default]
aws_access_key_id = your_access_key
aws_secret_access_key = your_secret_key
```

### 4. Clear AWS CLI Configuration (OPTIONAL)

To clear your AWS CLI credentials, you have several options:

- Delete the credentials file: `rm ~/.aws/credentials`
- Delete the config file: `rm ~/.aws/config`
- Clear specific profile: `aws configure --profile your_profile_name` and press Enter without entering values

```bash
# Remove both credentials and config files
rm ~/.aws/credentials ~/.aws/config
```

After clearing the credentials, you can reconfigure them using any of the methods described above.

***
## See also:

[AWS Credentials for CLI]({{< ref "aws-credentials-for-cli.md" >}})

[AWS STS - Temporary Access Tokens]({{< ref "aws-sts-temporary-access-tokens.md" >}})

[Amazon DynamoDB - Create a Table]({{< ref "dynamodb-create-a-table.md" >}})

[Amazon DynamoDB - Import CSV Data]({{< ref "dynamodb-import-data-from-csv.md" >}})

[AWS Lambda - Create a Function]({{< ref "lambda-create-a-function.md" >}})

[AWS Lambda - Grant Access]({{< ref "lambda-set-access-to-dynamodb.md" >}})

[API Gateway - Usage Plan]({{< ref "api-gateway-usage-plan.md" >}})

[API Gateway - API Key]({{< ref "api-gateway-api-key.md" >}})

[API Gateway - Configuration]({{< ref "api-gateway-configuration.md" >}})
