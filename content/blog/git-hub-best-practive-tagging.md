---
date: '2025-06-25T20:39:37+10:00'
draft: false
title: 'GitHub - Best Practive Tagging'
tags: ["GitHub", "Git", "Tag"]
categories: ["Technology"]
---

## ✅ **Daily Git Workflow with Tag Strategy**

### 1. Continue to work on the feature branch

```bash
git checkout feature/v3.2.0
git pull origin feature/v3.2.0
```

---

### 2. Commit stable changes

```bash
git add .
git commit -m "Fixed export timeout issue"
```

---

### 3. Tag a stable version (optional, when ready)

```bash
# Use semantic versioning: v3.1.3, v3.1.4, etc.
# Tags point to the most recent commit.
git tag v3.1.2
```

---

### 4. Push your changes and tag to GitHub

```bash
git push origin feature/v3.2.0
git push origin v3.1.2
```

---

### 5. Verify your tag (if needed)

```bash
git tag                         # List local tags
git show v3.1.2                 # Show details of the tag
git branch --contains v3.1.2    # See which branch includes it
```

---

### Bonus (Optional Advanced Commands)

- **List tags sorted by date (most recent first):**
    
    ```bash
    git for-each-ref --sort=-creatordate --format '%(refname:short)' refs/tags
    ```
    
- **Delete a local tag (if needed):**
    
    ```bash
    git tag -d v3.1.2
    ```
    
- **Delete a remote tag:**
    
    ```bash
    git push origin --delete v3.1.2
    ```

***
## See also:

[GitHub - Best Practive Tagging]({{< ref "git-hub-best-practive-tagging.md" >}})

[GitHub - Reset and Start Again]({{< ref "git-hub-reset-and-start-again.md" >}})


