---
date: '2025-06-15T17:10:13+10:00'
draft: false
title: 'AWS Lambda - Create a Function'
tags: ["AWS", "Lambda", "Python"]
categories: ["Technology"]
---

1. Navigate to Lambda in AWS Console
2. Click "Create function"
    - Choose "Author from scratch"
    - Runtime: Python 3.x
    - Name: e.g., "get-user-list"

![](2025-06-15-17-31-16.png)

Paste the Python code into “Code” page and click “Deploy” button

```python
import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user_list')

def create_nested_structure(data, current_level, max_level):
    if current_level >= max_level:
        return data
    
    return {
        f"level_{current_level}": {
            "data": data,
            "nested": create_nested_structure(data, current_level + 1, max_level),
            "metadata": {
                "level_info": f"This is level {current_level}",
                "timestamp": datetime.now().isoformat(),
                "metrics": {
                    "depth": current_level,
                    "remaining_levels": max_level - current_level,
                    "complexity_score": max_level * current_level
                }
            }
        }
    }

def create_complex_response(user_data, nested_level):
    base_data = {
        "id": f"user_{user_data['user_id']}",
        "timestamp": datetime.now().isoformat(),
        "category": "Personnel",
        "details": {
            "name": {
                "first": user_data['first_name'],
                "last": user_data['last_name']
            },
            "company": {
                "name": user_data['company_name'],
                "web": user_data['web']
            },
            "contact_info": {
                "address": {
                    "street": user_data['address'],
                    "city": user_data['city'],
                    "state": user_data['state'],
                    "postcode": user_data['post']
                },
                "communication": {
                    "phones": [
                        {
                            "type": "primary",
                            "number": user_data['phone1']
                        },
                        {
                            "type": "secondary",
                            "number": user_data['phone2']
                        }
                    ],
                    "email": user_data['email']
                }
            }
        }
    }
    
    return create_nested_structure(base_data, 1, nested_level)

def lambda_handler(event, context):
    try:
        # Get parameters from event body
        limit = int(event.get('limit', 10) if event.get('limit') else 10)
        nested_level = int(event.get('nested_level', 1) if event.get('nested_level') else 1)
        
        # Validate nested_level
        if nested_level < 1:
            nested_level = 1
        elif nested_level > 30:  # Set a reasonable maximum 
            nested_level = 30    # 29 nested is the limit on Blue Prism
            
        # Scan DynamoDB table with limit
        response = table.scan(
            Limit=limit
        )
        items = response.get('Items', [])
        
        # Transform items into complex nested structure
        transformed_data = [create_complex_response(item, nested_level) for item in items]
        
        # Create final response
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "total_records": len(transformed_data),
            "limit_applied": limit,
            "nesting_level": nested_level,
            "data": transformed_data,
            "metadata": {
                "api_version": "1.0",
                "service": "user-data-api",
                "complexity_info": {
                    "max_depth": nested_level,
                    "structure_type": "recursive",
                    "total_nodes": len(transformed_data) * nested_level
                }
            }
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "success": False,
            "message": "Error processing request",
            "error": str(e)
        }
```

![](2025-06-15-17-30-50.png)

### 6. IAM Roles and Permissions

Reference: [AWS Lambda - Grant Access]({{< ref "lambda-set-access-to-dynamodb.md" >}})

### 7. Run some tests

Event JSON

```json
{
  "limit": "10",
  "nested_level": "1"
}
```

![](2025-06-15-17-28-56.png)

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

