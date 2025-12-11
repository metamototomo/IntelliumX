---
date: '2025-05-20T08:27:35+10:00'
draft: false
title: 'Azure DevOps - Pull Request'
tags: ["Azure DevOps", "Git"]
categories: ["Technology"]
---
## Use Azure DevOps Web UI

### Scenario:

This guide shows how to push changes from the `release/v1.0-america` branch to the `master` branch in Azure DevOps (or any Git repository).

---

### Steps:
1. Go to your Azure DevOps project in the browser.
2. Navigate to **Repos > Branches**.
3. Find your branch `release/v1.0-america`
4. Click on the **"..." (More options)** next to it and select **"New pull request"**

![](2025-05-20-08-37-28.png)

2. Set:
    - **Source**: `release/v1.0-america`
    - **Target**: `master`

3. Add a title, description (optional but helpful), and click **"Create"**

![](2025-05-20-08-40-15.png)

4. Review and complete the PR when you're ready (or assign reviewers if required)

![](2025-05-20-08-43-04.png)

***
## See also:

[Azure DevOps - Pull Request]({{< ref "azure-devops-pull-request.md" >}})

[Azure DevOps - Approve]({{< ref "azure-devops-approve.md" >}})

[Azure DevOps - Complete (Merge)]({{< ref "azure-devops-complete.md" >}})
