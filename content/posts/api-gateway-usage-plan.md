---
date: '2025-06-15T17:46:05+10:00'
draft: false
title: 'API Gateway - Usage Plan'
tags: ["AWS", "API Gateway"]
categories: ["Technology"]
---

### 1. Create new usage plan

![](2025-06-15-17-51-14.png)

### Rate and Burst

- **Rate:** Set to 10-20 requests per second for development/testing
    - Recommended: Start with 10 req/sec for controlled testing
- **Burst:** Set to 2x your rate (20-40)
    - Recommended: Start with 20 to handle short traffic spikes

### Quota Settings

- **Quota period:** MONTH (most common)
    - Alternative periods: WEEK, DAY
- **Requests per quota period:** Start with 50,000/month
    - This allows approximately 1,600 requests per day
    - Can be adjusted based on actual usage patterns

Recommended Initial Configuration:

- Rate: 10 requests per second
- Burst: 20 requests
- Quota: 50,000 requests per month

These settings provide a good balance between:

- Preventing API abuse
- Allowing legitimate usage
- Managing AWS costs
- Maintaining API performance

Monitor usage patterns through CloudWatch and adjust these values as needed.

### 2. Link to the stage

![](2025-06-15-17-51-33.png)

### 3. Link to API Keys

![](2025-06-15-17-51-51.png)

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
