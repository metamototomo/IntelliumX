---
date: '2025-08-10T10:45:47+10:00'
draft: false
title: 'Entra ID and Cognito Itegration - Step1'
tags: ["Azure AD", "Microsoft Entra ID", "Amazon Cognito User Pool", "federation authentication", "SAML"]
categories: ["Technology"]
---

### Step 1: Configure SAML in Microsoft Entra ID

Begin by setting up a SAML application in Microsoft Entra ID to establish the identity provider side of the federation:

1. In **Azure Portal**, access **Microsoft Entra ID**, then select **Enterprise applications**
2. Select **New application** to create a custom application integration

![](2025-08-10-11-51-45.png)

3. Click **Create your own application** to configure a custom SAML provider

![](2025-08-10-11-52-25.png)

4. Configure the application with the following parameters:
    - **Application name**: (your preferred application name)
    - Select **Integrate any other application you don't find in the gallery (Non-gallery)**
5. Click **Create** to generate the application
![](2025-08-10-11-53-13.png)

1. Within your new Enterprise application, navigate to **Single sign-on**
2. Select **SAML** as your authentication method

![](2025-08-10-11-54-18.png)

8. Click **Edit** in the **Basic SAML Configuration** section

![](2025-08-10-11-54-47.png)

__Note: Keep this page open and proceed to Step 2. We will return to this configuraiton in Step 2.__


***
## See also:

[Entra ID and Cognito Itegration - Guide]({{< ref "entraid-cognito-itegration-overview.md" >}})

[Entra ID and Cognito Itegration - Step1]({{< ref "entraid-cognito-itegration-step1.md" >}})

[Entra ID and Cognito Itegration - Step2]({{< ref "entraid-cognito-itegration-step2.md" >}})

[Entra ID and Cognito Itegration - Step3]({{< ref "entraid-cognito-itegration-step3.md" >}})

[Entra ID and Cognito Itegration - Step4]({{< ref "entraid-cognito-itegration-step4.md" >}})

[Entra ID and Cognito Itegration - Step5]({{< ref "entraid-cognito-itegration-step5.md" >}})

[Entra ID and Cognito - OIDC]({{< ref "entraid-cognito-oidc.md" >}})
