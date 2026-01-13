---
date: '2026-01-13T23:27:39+11:00'
draft: false
title: 'GitHub - Pull Latest Change'
tags: ["GitHub", "Git"]
categories: ["Technology"]
---

### ✅ **Option 1: Stash your changes (temporarily save)**

If you're not ready to commit, but want to pull the latest code:

```powershell
git stash
git pull
git stash pop
```

- `git stash` temporarily saves your changes
- `git pull` fetches and merges the latest version
- `git stash pop` restores your changes

---

### ❌ **Option 2: Discard your changes**

⚠️ Only do this if you're okay with **losing your local changes**:

```powershell
git reset --hard origin/develop
git pull
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

