---
date: '2025-06-15T17:00:19+10:00'
draft: false
title: 'AWS Lambda - Grant Access'
tags: ["AWS", "Lambda", "IAM"]
categories: ["Technology"]
---
1. Go to AWS IAM Console
2. Find your Lambda's role
    - Click on the role name
    - Click "Add permissions" → "Create inline policy"
3. In the JSON editor, paste this policy:
    
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:Scan",
                    "dynamodb:GetItem",
                    "dynamodb:Query"
                ],
                "Resource": "arn:aws:dynamodb:ap-southeast-2:6850********:table/user_list"
            }
        ]
    }
    ```
    
4. Click "Review policy"
    - Name it something like "DynamoDBScanPolicy"
    - Click "Create policy"

After adding this policy, wait a few seconds and try your Lambda function again. The error should be resolved.

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
