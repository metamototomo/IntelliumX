---
date: '2025-02-18T22:31:44+11:00'
draft: false
title: 'Terraform Link to "tfvars" File'
tags: ["tfvars", "Symbolic link", "Terraform"]
categories: ["Technology"]
---
## Terraform tfvars file

When a tfvars file is in a different location, you must specify it using the "-var-file" option. However, creating a symbolic link can simplify the command operation.

1. Create a symbolic link
```bash
ln -s ../common.tfvars terraform.tfvars
```

2. Run a simple terraform command without option
```bash
terraform plan
```

3. Screenshot of the process

![](2025-02-18-23-35-39.png)