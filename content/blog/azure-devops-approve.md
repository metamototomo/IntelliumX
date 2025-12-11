---
date: '2025-05-20T08:49:12+10:00'
draft: false
title: 'Azure DevOps - Approve'
tags: ["Azure DevOps", "Git"]
categories: ["Technology"]
---

## Use Azure DevOps Web UI

### Scenario:

This guide demonstrates how to approve a pull request from the `release/v1.0-america` branch into the `master` branch in Azure DevOps or any Git repository.

### Steps (Approve the Pull Request):

1. Go to Azure DevOps in your browser
2. Navigate to **Repos > Pull Requests**

![](2025-05-20-08-54-53.png)

3. Find the Pull request (from `release/v1.0-america` to `master`)
4. Click on the PR to open it.
5. On the right-hand side, you’ll see the **"Reviewers"** section

![](2025-05-20-08-58-10.png)

6. If you're not listed, click **"Add"** and select yourself

![](2025-05-20-08-59-02.png)

6. Once you're added as a reviewer, click the **"Approve"** button near the top
    - You may also leave an optional comment

![](2025-05-20-09-01-00.png)


***
## See also:

[Azure DevOps - Pull Request]({{< ref "azure-devops-pull-request.md" >}})

[Azure DevOps - Approve]({{< ref "azure-devops-approve.md" >}})

[Azure DevOps - Complete (Merge)]({{< ref "azure-devops-complete.md" >}})


