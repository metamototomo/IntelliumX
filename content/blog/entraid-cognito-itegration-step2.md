---
date: '2025-08-10T11:45:51+10:00'
draft: false
title: 'Entra ID and Cognito Itegration - Step2'
tags: ["Azure AD", "Microsoft Entra ID", "Amazon Cognito User Pool", "federation authentication", "SAML"]
categories: ["Technology"]
---

### Step 2: Configure SAML Parameters

You'll need to retrieve key information from your Cognito User Pool to properly configure the SAML parameters:

1. In the AWS Console, locate your Cognito User Pool and note the **User Pool ID**

![](2025-08-10-15-31-53.png)

2. Record the **Cognito Domain** from your User Pool settings

![](2025-08-10-15-32-16.png)

3. In Azure Portal, configure the following SAML parameters:
    - **Identifier (Entity ID)**: Format as `urn:amazon:cognito:sp:{User pool ID}`
    - **Reply URL (Assertion Consumer Service URL)**: Format as `{Cognito domain}/saml2/idpresponse`
4. Save your configuration changes

![](2025-08-10-15-33-19.png)

5. From the **SAML Certificates** section, download the **Federation Metadata XML** file for use in the next step

![](2025-08-10-15-33-33.png)


***
## See also:

[Entra ID and Cognito Itegration - Guide]({{< ref "entraid-cognito-itegration-overview.md" >}})

[Entra ID and Cognito Itegration - Step1]({{< ref "entraid-cognito-itegration-step1.md" >}})

[Entra ID and Cognito Itegration - Step2]({{< ref "entraid-cognito-itegration-step2.md" >}})

[Entra ID and Cognito Itegration - Step3]({{< ref "entraid-cognito-itegration-step3.md" >}})

[Entra ID and Cognito Itegration - Step4]({{< ref "entraid-cognito-itegration-step4.md" >}})

[Entra ID and Cognito Itegration - Step5]({{< ref "entraid-cognito-itegration-step5.md" >}})

[Entra ID and Cognito - OIDC]({{< ref "entraid-cognito-oidc.md" >}})