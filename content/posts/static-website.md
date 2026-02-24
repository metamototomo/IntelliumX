---
date: '2026-02-24T20:53:00+11:00'
draft: false
title: 'Static Website (VS Code, GitHub, Netlify)'
tags: ["Static Website", "CICD", "GitHub", "VS Code"]
categories: ["Technology"]
---

### Install VS Code and Plugins
Download and install VS Code from https://code.visualstudio.com/download

### Install Plugins
- Live Preview or Live Server (for previewing your website locally)
- Co-Pilot or Amazon Q (for AI-powered coding assistance)

![](2026-02-24-20-55-10.png)


### Prerequisites

Before creating your website, set up GitHub authentication and create a repository:

- [GitHub - SSH Settings (ed25519)]({{< ref "github-ssh-settings.md" >}})
- [GitHub - Create a New Repository]({{< ref "git-create-new-repo.md" >}})

## Create a Website Using AI
Here's a sample prompt you can use with AI assistants like Amazon Q or GitHub Copilot:

```
Create a minimal static website project that can be hosted on Netlify.

Requirements:

1. Project Structure:
- home.html
- dom-reshuffle.html
- /css/style.css
- /js/script.js

2. Technology Constraints:
- Pure static website (HTML, CSS, JavaScript only)
- No backend
- No build tools
- No frameworks except Bootstrap via CDN
- Must work by simply opening home.html

3. UI Requirements:
- Modern clean UI using Bootstrap 5 (via CDN)
- Responsive layout
- Simple navigation bar with links:
  - Home
  - DOM Reshuffle Demo

4. Functional Requirement (Demonstration Feature):
Implement DOM reshuffling behavior in dom-reshuffle.html:

- Display a list of at least 6 items inside a Bootstrap card.
- When the page loads, use JavaScript to randomly reshuffle the order of the list items.
- Use clean, readable JavaScript inside /js/script.js.
- Keep the logic minimal and well commented.

5. Home Page:
- Brief introduction text explaining this is a simple automation resilience demo site.
- Button linking to dom-reshuffle.html.

6. Code Quality:
- Keep everything simple and minimal.
- No unnecessary animations.
- No extra libraries.
- Clean formatting.
- Comment the reshuffle logic clearly.

7. Output:
Provide full code for:
- home.html
- dom-reshuffle.html
- css/style.css
- js/script.js
```


### Preview the Website Locally

![](2026-02-24-21-04-50.png)

![](2026-02-24-21-05-08.png)

### Push to GitHub Repository

```
cd /Users/nob/repo/automation-resilience-lab
git add .
git commit -m "Add static website"
git push origin main
```


## Create a Project in Netlify

1. Navigate to https://app.netlify.com

2. Click "Add new site" → "Import an existing project"

![](2026-02-24-21-07-08.png)

3. Select "Deploy with GitHub"

![](2026-02-24-21-07-47.png)


4. Choose your repository: automation-resilience-lab

![](2026-02-24-21-08-57.png)

![](2026-02-24-21-09-13.png)

![](2026-02-24-21-09-41.png)


## Configure Build Settings:

- Branch to deploy: `main`
- Build command: (leave empty for static sites)
- Publish directory: `/` or `.`
- Click "Deploy site"

![](2026-02-24-21-11-44.png)

![](2026-02-24-21-12-11.png)

![](2026-02-24-21-12-26.png)


### Verify the Deployment

Access the generated Netlify URL to check the deployment status. Initially, you may see a "Page Not Found" error if the repository hasn't been pushed yet.

![](2026-02-24-21-13-04.png)


Push your code to the `main` branch:

![](2026-02-24-21-13-24.png)

Netlify will automatically detect the changes and redeploy your site.

![](2026-02-24-21-13-45.png)

## Congratulations!

You've successfully set up a complete CI/CD pipeline integrating Visual Studio Code, GitHub, and Netlify. Any future changes pushed to your GitHub repository will automatically trigger a new deployment on Netlify!

