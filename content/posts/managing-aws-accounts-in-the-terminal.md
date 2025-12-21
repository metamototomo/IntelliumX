---
date: '2025-02-27T22:11:39+11:00'
draft: false
title: 'Managing AWS Accounts in Terminal'
tags: ["AWS", "Terminal"]
categories: ["Technology"]
---

## Register AWS Accounts to the Terminal

1. Set AWS Credential

![](2025-02-27-23-11-55.png)

2. The command to check the Current AWS Credentials

```
aws sts get-caller-identity
```

3. The command to clear the AWS Account from the terminal

```bash
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
```


