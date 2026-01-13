---
date: '2026-01-13T23:28:31+11:00'
draft: false
title: 'GitHub - Create a Tag'
tags: ["GitHub", "Git"]
categories: ["Technology"]
---

![](2026-01-13-23-46-57.png)

### 1. Displaying Git Tags

```bash
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git tag
2.0
show
v1.0
v1.0.0
```

---

### 2. Check out the `main` branch

```bash
git checkout main
```

---

### 3. Check the commit hash of main branch (last update)

```powershell
# Show the latest commit on main (from remote)
git fetch origin
git log origin/main -1
```

```powershell
# For example
PS C:\code\Quick-Installer> git log origin/main -1
commit 87b1cfd5fae54d85f9c1a77b134092fb9ed624a3 (origin/main, origin/HEAD)
Merge: ea44cbc 4195693
Author: gituser <gituser@users.noreply.github.com>
Date:   Mon Sep 15 15:59:32 2025 +1000

    Merge pull request #7 from gituser/patch/backward-compatibility

    fixed confi file downlaod issue
```

### 4. Create the tag

```bash
git tag v.3.3.2 87b1cfd5fae54d85f9c1a77b134092fb9ed624a3
```

---

### 5. Push the tag to remote

```bash
git push origin v3.3.2
```

### 6. Verify

```powershell
git show v3.3.2
```

### Display tags with detailed information

```bash
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git ls-remote --tags origin
90e2de33d27de3116195bfe26dde6d750191889d        refs/tags/2.0
6655ed0a66e4b9fa141d5aa87ffd9c10fdfdc603        refs/tags/v1.0
ab35d0488d9e8b0a66502a0e900538449dc7190d        refs/tags/v1.0.0
47ecf4f18119d628cc3f61932c9d81d25690630c        refs/tags/v1.0.0^{}
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

