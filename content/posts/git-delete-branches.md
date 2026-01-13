---
date: '2026-01-13T23:28:19+11:00'
draft: false
title: 'GitHub - Delete a Branch'
tags: ["GitHub", "Git"]
categories: ["Technology"]
---

1. Delete the feature branch locally

```bash
git branch -D feature/multi-users
```

---

2. Delete the feature branch from remote

If you already pushed the branch to remote and want to remove it there too:

```bash
git push origin --delete feature/multi-users
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

