---
date: '2025-06-15T16:20:16+10:00'
draft: false
title: 'Amazon DynamoDB - Import CSV Data'
tags: ["AWS", "DynamoDB"]
categories: ["Technology"]
---

![](2025-06-17-11-19-21.png)

### 1. Save the CSV file in the same location as the Python code

```
user_id,first_name,last_name,company_name,address,city,state,post,phone1,phone2,email,web
U001,Rebbecca,Didio,"Brandt, Jonathan F Esq",171 E 24th St,Leith,TAS,7315,03-8174-9123,0458-665-290,rebbecca.didio@didio.com.au,http://www.brandtjonathanfesq.com.au
U002,Stevie,Hallo,Landrum Temporary Services,22222 Acoma St,Proston,QLD,4613,07-9997-3366,0497-622-620,stevie.hallo@hotmail.com,http://www.landrumtemporaryservices.com.au
U003,Mariko,Stayer,"Inabinet, Macre Esq",534 Schoenborn St #51,Hamel,WA,6215,08-5558-9019,0427-885-282,mariko_stayer@hotmail.com,http://www.inabinetmacreesq.com.au
U004,Gerardo,Woodka,Morris Downing & Sherred,69206 Jackson Ave,Talmalmo,NSW,2640,02-6044-4682,0443-795-912,gerardo_woodka@hotmail.com,http://www.morrisdowningsherred.com.au
U005,Mayra,Bena,"Buelt, David L Esq",808 Glen Cove Ave,Lane Cove,NSW,1595,02-1455-6085,0453-666-885,mayra.bena@gmail.com,http://www.bueltdavidlesq.com.au
U006,Idella,Scotland,Artesian Ice & Cold Storage Co,373 Lafayette St,Cartmeticup,WA,6316,08-7868-1355,0451-966-921,idella@hotmail.com,http://www.artesianicecoldstorageco.com.au
U007,Sherill,Klar,Midway Hotel,87 Sylvan Ave,Nyamup,WA,6258,08-6522-8931,0427-991-688,sklar@hotmail.com,http://www.midwayhotel.com.au
U008,Ena,Desjardiws,"Selsor, Robert J Esq",60562 Ky Rt 321,Bendick Murrell,NSW,2803,02-5226-9402,0415-961-606,ena_desjardiws@desjardiws.com.au,http://www.selsorrobertjesq.com.au
U009,Vince,Siena,Vincent J Petti & Co,70 S 18th Pl,Purrawunda,QLD,4356,07-3184-9989,0411-732-965,vince_siena@yahoo.com,http://www.vincentjpettico.com.au
U010,Theron,Jarding,"Prentiss, Paul F Esq",8839 Ventura Blvd,Blanchetown,SA,5357,08-6890-4661,0461-862-457,tjarding@hotmail.com,http://www.prentisspaulfesq.com.au
```

### 2. Set a temporary token for VS Code

Reference: [AWS STS - Temporary Access Tokens]({{< ref "aws-sts-temporary-access-tokens.md" >}})

### 3. Execute the Python code

```python
import boto3
import csv

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user_list')

with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        table.put_item(
            Item={
                'user_id': row['user_id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'company_name': row['company_name'],
                'address': row['address'],
                'city': row['city'],
                'state': row['state'],
                'post': row['post'],
                'phone1': row['phone1'],
                'phone2': row['phone2'],
                'email': row['email'],
                'web': row['web']
            }
        )
```

### 4. Check the table contents

AWS CLI:

```bash
aws dynamodb scan --table-name user_list
```

AWS Console:

1. Go to the DynamoDB service
2. In the left navigation pane, click on "Tables"
3. Click on the "user_list" table name
4. Click on the "Explore table items" button or "View items" tab

![](2025-06-15-17-22-41.png)


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
