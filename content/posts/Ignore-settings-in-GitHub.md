---
date: '2025-02-25T22:48:12+11:00'
draft: false
title: 'Git - Ignore Settings'
tags: ["Git","GitHub", "Azure DevOps"]
categories: ["Technology"]
---

## How to Ignore Uploading Folders and Files to GitHub

For example `.venv` folder

1. Open your project folder in **VS Code**.
2. Open `.gitignore` file in the root of the project
3. Add the following line to `.gitignore`:
    
    ```
    .venv/
    ```
    
4. Save the file. then Git will ignore the `.venv` folder, and it won’t be tracked in your repository. 

If `.venv` was already committed before, you’ll need to remove it from Git history using:

```
git rm -r --cached .venv
git commit -m "Removed .venv from repository"
git push origin main  # or your current branch
```

You can check if `.venv` is ignored by Git using the following command

```bash
git check-ignore -v .venv
```


***
## See also:

[Git - Useful Commands]({{< ref "git-useful-commands.md" >}})

[Git - Move Branch]({{< ref "git-move-branch.md" >}})

[Git - Ignore Settings]({{< ref "Ignore-settings-in-GitHub.md" >}})
