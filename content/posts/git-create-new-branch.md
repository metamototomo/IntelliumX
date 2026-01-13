---
date: '2026-01-13T23:27:15+11:00'
draft: false
title: 'GitHuh - Create a New Branch'
tags: ["GitHub", "Git"]
categories: ["Technology"]
---
This is an example to create “develop” branch from copying from “main” branch. We can apply the same steps for creating “feature” branch and “release” branch

![](2026-01-13-23-33-44.png)

---

### **1. Ensure your repository is clean**

```bash
git status
git branch -a
```

---

### **2. Preparation before creating a new branch**

```bash
git checkout {ORIGINAL BRANCH} (e.g, main)
git pull origin {ORIGINAL BRANCH} (e.g, main)
```

### **3. Create the new branch locally**

```bash
git checkout -b {NEW BRANCH} (e.g, develop)

# Sample of feature branch
git checkout -b feature/new_feature_branch_name

# Sample of release branch
git checkout -b release/new_release_branch_name
```

---

### **4. Push the new branch to GitHub**

```bash
git push -u origin {NEW BRANCH} (e.g, develop)
```

---

### **5. Verify both branches exist**

Run:

```bash
git branch -a
```

You should see the new branch

```
* {NEW BRANCH} (e.g, develop)
  main
  remotes/origin/{NEW BRANCH} (e.g, develop)
  remotes/origin/main
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

