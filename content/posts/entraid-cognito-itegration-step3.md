---
date: '2025-08-10T11:45:55+10:00'
draft: false
title: 'Entra ID and Cognito Itegration - Step3'
tags: ["Azure AD", "Microsoft Entra ID", "Amazon Cognito User Pool", "federation authentication", "SAML"]
categories: ["Technology"]
---

### Step 3: Integrate Identity Provider with Amazon Cognito

Now, configure Amazon Cognito to recognize Microsoft Entra ID as a federated identity provider:

1. In the AWS Console, navigate to **Amazon Cognito** and select your User Pool
2. Go to **Sign-in experience** and locate the **Federated identity provider sign-in** section
3. Select **Add identity provider** and choose **SAML** as the provider type

![](2025-08-10-15-24-59.png)

4. Configure the identity provider with these settings:
    - **Provider name**: "EntraID" (this name will appear on your login screen)
    - **Metadata document**: Upload the Federation Metadata XML file downloaded in the previous step
    - **SAML attribute mapping**: Configure the following essential attribute mappings:
        
        email → http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
        
        given_name → http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname
        
        family_name → http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname

![](2025-08-10-15-25-30.png)

![](2025-08-10-15-25-50.png)


***
## See also:

[Entra ID and Cognito Itegration - Guide]({{< ref "entraid-cognito-itegration-overview.md" >}})

[Entra ID and Cognito Itegration - Step1]({{< ref "entraid-cognito-itegration-step1.md" >}})

[Entra ID and Cognito Itegration - Step2]({{< ref "entraid-cognito-itegration-step2.md" >}})

[Entra ID and Cognito Itegration - Step3]({{< ref "entraid-cognito-itegration-step3.md" >}})

[Entra ID and Cognito Itegration - Step4]({{< ref "entraid-cognito-itegration-step4.md" >}})

[Entra ID and Cognito Itegration - Step5]({{< ref "entraid-cognito-itegration-step5.md" >}})

[Entra ID and Cognito - OIDC]({{< ref "entraid-cognito-oidc.md" >}})
