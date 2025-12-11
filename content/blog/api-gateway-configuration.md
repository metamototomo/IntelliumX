---
date: '2025-06-15T17:49:13+10:00'
draft: false
title: 'API Gateway - Configuration'
tags: ["AWS", "API Gateway"]
categories: ["Technology"]
---

### 1. Create REST API

1. Go to API Gateway console
2. Create new REST API

![](2025-06-15-17-54-16.png)

3. Create new resource and method
    - Add resource: e.g., "/user-list"
    - Add GET method
    - Integration type: Lambda Function
    - Select your Lambda function
4. Enable CORS if needed
    - Actions → Enable CORS
    - Accept default settings for testing

### 2. Update “Method request”

![](2025-06-15-17-54-36.png)

### 3. Update “Integration request”

![](2025-06-15-17-54-51.png)

```json
{
    "limit": "$input.params('limit')"
}
```

### 4. Deploy and Test

1. Deploy API

![](2025-06-15-17-55-17.png)

2. Note the API endpoint URL

![](2025-06-15-17-55-34.png)

3. Test using curl or Postman:
    
    ```bash
    curl -X GET 'https://your-api-id.execute-api.region.amazonaws.com/stage/data' \
    -H 'x-api-key: your-api-key-here'
    ```


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
