---
date: '2026-01-13T23:28:39+11:00'
draft: false
title: 'GitHub - Delete a Tag'
tags: ["GitHub", "Git"]
categories: ["Technology"]
---
### To delete a tag from the LOCAL:

```bash
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git tag -d v1.0
Deleted tag 'v1.0' (was 6655ed0)
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git tag -d v1.0.0 
Deleted tag 'v1.0.0' (was ab35d04)
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git tag      
2.0
show
```

### To delete a tag from the REMOTE:

```bash
# For example, to delete the v1.0 and v1.0.0 tags from remote:
git push origin --delete v1.0
git push origin --delete v1.0.0

# Check the remote tags again
git ls-remote --tags origin
```

Note that while the tags were deleted locally, they still appear in the remote repository when using "git ls-remote --tags origin". The "git tag" command only displays tags that exist in your local repository.

```bash
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git ls-remote --tags origin
90e2de33d27de3116195bfe26dde6d750191889d        refs/tags/2.0
6655ed0a66e4b9fa141d5aa87ffd9c10fdfdc603        refs/tags/v1.0
ab35d0488d9e8b0a66502a0e900538449dc7190d        refs/tags/v1.0.0
47ecf4f18119d628cc3f61932c9d81d25690630c        refs/tags/v1.0.0^{}
```

### View tag details and associated commit information using "git show {TAG}"

```bash
(.venv) coo:~/Documents/DevOps/GCS-Cloud$ git show 2.0
commit 90e2de33d27de3116195bfe26dde6d750191889d (HEAD -> main, tag: 2.0, origin/main, origin/HEAD)
Merge: 47ecf4f e4f13e0
Author: Nobuhiro Tokushige <nobuhiro.tokushige@sscinc.com>
Date:   Sun Jul 13 12:07:32 2025 +0000

    Merged PR 5: The first multi-region support version
    
    This is the first version that supports multiple regions (EMEA, AMER and APJ). It serves as a solid starting point for collaborative work across regions.

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

