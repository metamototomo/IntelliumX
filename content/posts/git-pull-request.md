---
date: '2026-01-13T23:27:52+11:00'
draft: false
title: 'GitHub - Pull Request (Azure DevOps)'
tags: ["GitHub", "Git"]
categories: ["Technology"]
---
This guide shows how to push changes from the `feature/script-update-for-multi-regsions` branch to the `develop` branch in Azure DevOps

---

### Step 1: Ensure all the changes are committed to the feature branch.

```bash
# Check the current branch
(.venv) coo:~/Documents/DevOps/GCS-Cloud/base$ git branch
  develop
* feature/script-update-for-multi-regsions
  main
  
# Check the status of the local repository
(.venv) coo:~/Documents/DevOps/GCS-Cloud/base$ git status
On branch feature/script-update-for-multi-regsions
nothing to commit, working tree clean
```

### Step 2: Use Azure DevOps Web UI

1. Go to your Azure DevOps project in the browser.
2. Navigate to **Repos > Branches**.
3. Find your branch `feature/script-update-for-multi-regsions`.
4. Click on the **"..." (More options)** next to it and select **"New pull request"**.
    
    ![](2026-01-13-23-37-34.png)
    
5. Configure the pull request direction:
    - **Source**: `feature/script-update-for-multi-regsions`
    - **Target**: `develop`
6. Add a title, description (optional but helpful), and click **"Create"**.
    
    ![](2026-01-13-23-37-58.png)
    
7. Review and complete the PR when you're ready (or assign reviewers if required).

8. Select options and click Complete

    ![](2026-01-13-23-38-25.png)

9. Check the status

    ![](2026-01-13-23-39-00.png)


***
## See also:

[GitHub - Create a New Repo]({{< ref "git-create-new-repo.md" >}})

[GitHub - Create a New Branch]({{< ref "git-create-new-branch.md" >}})

[GitHub - Pull Latest Change]({{< ref "git-pull-latest-change.md" >}})

[GitHub - Pull Request (Azure DevOps)]({{< ref "git-pull-request.md" >}})

[GitHub - Chean a Branch]({{< ref "git-clean-branches.md" >}})

[GitHub - Delete a Branch]({{< ref "git-delete-branches.md" >}})

[GitHub - Create a Tag]({{< ref "git-create-tag.md" >}})

[GitHub - Delete a Tag]({{< ref "git-delete-tag.md" >}})

