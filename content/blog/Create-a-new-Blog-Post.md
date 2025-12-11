---
date: '2025-02-25T22:21:46+11:00'
draft: false
title: 'Create a New Blog Post'
tags: ["Hugo", "Blog"]
categories: ["Technology"]
---
## Create a new blog post in HUGO

1. Create a new file

```bash
hugo new posts/create-a-new-blog-post.md
```

2. Add `Tag` and `Category` to the header

```markdown
---
date: '2025-02-25T22:21:46+11:00'
draft: false
title: 'Create a New Blog Post'
tags: ["Hugo", "Blog","Homepage"]
categories: ["Technology"]
---
```

3. Edit the blog page
4. Check the page in debugging mode

```bash
hugo server
hugo serve
```

5. Open the page from the browser [http://localhost:1313/](http://localhost:1313/)

![](2025-02-25-22-30-23.png)