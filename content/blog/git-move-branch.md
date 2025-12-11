---
date: '2025-05-20T09:30:14+10:00'
draft: false
title: 'Git - Move Branch'
tags: ["Azure DevOps", "GitHub", "Git"]
categories: ["Technology"]
---
### Move to "master"

Open the terminal (press Ctrl+`) and run:

``` bash
git checkout master
```

If master isn’t checked out locally yet, do:

``` bash
git fetch origin
git checkout master
```

---

### If "master" was not updated in the local branch
If the branch switched successfully to master, but the files in your working directory didn’t update as expected, it could be one of these cases:

1. Confirm You’re on the Correct Branch
Run this to verify:

```bash
git branch
```

You should see something like this. The asterisk * indicates your current branch.

```arduino
* master
  release/v1.0-america
```



2. Ensure You Pulled the Latest Changes. Fetching doesn’t update your local branch.

```bash
# That will update your local master branch with the latest from the remote.
git pull origin master
```



3. Check for Local Changes Preventing Switch

```bash
# If you had local changes, Git might have silently blocked switching some files.
git status
```

If you see uncommitted changes, you can:

 - Stash them: git stash

 - Or discard them: git reset --hard

Then try switching branches again:

```bash
git checkout master
git pull origin master
```

![](2025-05-20-10-11-05.png)


***
## See also:

[Git - Useful Commands]({{< ref "git-useful-commands.md" >}})

[Git - Move Branch]({{< ref "git-move-branch.md" >}})

[Git - Ignore Settings]({{< ref "Ignore-settings-in-GitHub.md" >}})
