---
date: '2026-01-13T23:28:06+11:00'
draft: false
title: 'GitHub - Clean a Branch'
tags: ["GitHub", "Git"]
categories: ["Technology"]
---

After merging, we may still see the release branch like this

```bash
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git branch -a
  develop
* main
  release/2.0
  remotes/origin/HEAD -> origin/main
  remotes/origin/develop
  remotes/origin/feature/witt_test
  remotes/origin/main
  remotes/origin/release/2.0
```

After running "git fetch --prune", the remote branch was updated but the local branch remained unchanged.

```bash
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git fetch --prune
From https://dev.azure.com/nobuops/GCS-Cloud/_git/GCS-Cloud
 - [deleted]         (none)     -> origin/release/2.0
remote: Azure Repos
remote: Found 1 objects to send. (0 ms)
Unpacking objects: 100% (1/1), 328 bytes | 82.00 KiB/s, done.
   47ecf4f..90e2de3  main       -> origin/main
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git branch -a
  develop
* main
  release/2.0
  remotes/origin/HEAD -> origin/main
  remotes/origin/develop
  remotes/origin/feature/witt_test
  remotes/origin/main
```

To clean up the repository completely, manually delete the local branch

```bash
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git branch -d release/2.0 
Deleted branch release/2.0 (was e4f13e0).
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git branch -a
  develop
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/develop
  remotes/origin/feature/witt_test
  remotes/origin/main
```

Deleting Unneeded Remote Branches

```bash
PS C:\Code\repo\BloodPresure> git branch -a
* develop
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/develop
  remotes/origin/feature/additional_attributes
  remotes/origin/hotfix/update_page
  remotes/origin/main
```

To delete the remote branch "feature/additional_attributes"

```bash
git push origin --delete feature/additional_attributes

# Update Local references to match the remote repository
git fetch --prune
```

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

