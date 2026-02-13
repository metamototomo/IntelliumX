---
date: '2026-02-13T11:49:53+11:00'
draft: false
title: 'Espanso - Installation and Setup'
tags: ["Mac", "Automation"]
categories: ["Technology"]
---

# Install Espanso (macOS) Using Homebrew

Open Terminal and install Espanso

```
brew install espanso
```

```
# Start the espanso service
espanso service register
espanso service start
```

```
# Check the status
~ ❯ espanso service status 
espanso is running
```

```
# Restart the service if required
~ ❯ espanso service restart
espanso started correctly!
```

```
# Unregister and Register the service if required
~ ❯ espanso service unregister
service unregistered correctly!
~ ❯ espanso service register
service registered correctly!
```

* * *

# Enable Accessibility Permission Is Enabled

Go to: `System Settings → Privacy & Security → Accessibility`

Enable: `Espanso` and `Terminal`

![](2026-02-13-11-53-08.png)

* * *

# Configure the file

Espanso config lives here:

```
~/Library/Application Support/espanso/match/base.yml
```

![](2026-02-13-11-53-28.png)

Set the code and save it

```
matches:
  - trigger: ":critq"
    replace: |
      Please respond with critical thinking.
      If something is incorrect, clearly point it out.
      Challenge weak assumptions.
      Be concise and technically precise.

  - trigger: ":arch"
    replace: |
      Act as a senior AWS cloud architect reviewing this design.
      Identify security risks, IAM misconfigurations, scalability issues, 
      cost inefficiencies, and operational weaknesses.
      Do not assume correctness.
      Suggest better alternatives where applicable.

  - trigger: ":sec"
    replace: |
      Perform a strict security review.
      Identify IAM risks, data exposure, injection risks,
      privilege escalation paths, and compliance concerns.
      
  - trigger: ":cost"
    replace: |
      Analyze for cost optimization opportunities.
      Identify unnecessary services, over-provisioning,
      and better pricing models.

  - trigger: ":perf"
    replace: |
      Review for performance and scalability issues.
      Identify bottlenecks, cold start concerns,
      concurrency limits, and caching improvements.
```

Check the contents from the Terminal

```
espanso match list
```

![](2026-02-13-11-53-51.png)

* * *

# Test It

Anywhere on your Mac:

1.  Open Notes, VS Code, or Amazon Q chat
    
2.  Type: `critq`
    
3.  Press space
    
It should expand instantly.