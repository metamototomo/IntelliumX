---
date: '2025-08-10T11:45:59+10:00'
draft: false
title: 'Entra ID and Cognito Itegration - Step4'
tags: ["Azure AD", "Microsoft Entra ID", "Amazon Cognito User Pool", "federation authentication", "SAML"]
categories: ["Technology"]
---

### Step 4: Update Cognito App Client Configuration

Enable the new identity provider in your Cognito App Client settings:

1. Within your Cognito User Pool, navigate to **App integration** and select your app client
2. Under **Hosted UI**, click **Edit** to modify the settings

![](2025-08-10-15-48-15.png)

1. In the **Identity providers** section, select **EntraID** to enable it
2. Save your changes to apply the configuration

![](2025-08-10-15-49-01.png)

![](2025-08-10-15-49-10.png)


***
## See also:

[Entra ID and Cognito Itegration - Guide]({{< ref "entraid-cognito-itegration-overview.md" >}})

[Entra ID and Cognito Itegration - Step1]({{< ref "entraid-cognito-itegration-step1.md" >}})

[Entra ID and Cognito Itegration - Step2]({{< ref "entraid-cognito-itegration-step2.md" >}})

[Entra ID and Cognito Itegration - Step3]({{< ref "entraid-cognito-itegration-step3.md" >}})

[Entra ID and Cognito Itegration - Step4]({{< ref "entraid-cognito-itegration-step4.md" >}})

[Entra ID and Cognito Itegration - Step5]({{< ref "entraid-cognito-itegration-step5.md" >}})

[Entra ID and Cognito - OIDC]({{< ref "entraid-cognito-oidc.md" >}})