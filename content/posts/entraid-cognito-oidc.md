---
date: '2025-08-11T08:26:23+10:00'
draft: false
title: 'Entra ID and Cognito - OIDC'
tags: ["Azure AD", "Microsoft Entra ID", "Amazon Cognito User Pool", "federation authentication", "OIDC"]
categories: ["Technology"]
---

## Overview

This guide walks through setting up Microsoft Entra ID (formerly Azure AD) as an OpenID Connect (OIDC) identity provider for AWS Cognito User Pools. This integration allows users to sign in to your applications using their Microsoft credentials.

## **Steps**

### **1. Sign in to Azure Portal**

Navigate to https://portal.azure.com and access **Microsoft Entra ID** (formerly "Azure AD") from the main services menu.

### **2. Register a New Application**

1. In **Microsoft Entra ID**, select **App registrations** → **New registration**.

![](2025-08-11-08-30-37.png)

1. Configure the following settings: 
    - **Name:** Choose a descriptive name like `CognitoOIDC`
    - **Supported account types:** Select based on your requirements:
        - For internal use: *Accounts in this organizational directory only*
        - For broader access: *Accounts in any organisational directory and personal Microsoft accounts*
    - **Redirect URI:**
        - Platform: **Web**
        - URI: `https://<your-cognito-domain>/oauth2/idpresponse`
        
        Example: `https://myapp.auth.ap-southeast-2.amazoncognito.com/oauth2/idpresponse`
        
2. Click **Register** to create the application.

![](2025-08-11-08-32-00.png)

### **3. Collect OIDC Metadata**

After registration, from your new app's **Overview** page, note these important values:

- **Application (client) ID** - This becomes your `client_id` for Cognito
- **Directory (tenant) ID** - Required for constructing the issuer URL
- **OIDC Metadata URL:** `https://login.microsoftonline.com/&lt;tenant-id&gt;/v2.0/.well-known/openid-configuration`

![](2025-08-11-08-46-53.png)

### **4. Create a Client Secret**

1. Navigate to **Certificates & secrets** → **New client secret**
2. Add a meaningful description and select an appropriate expiration period
3. Click **Add** and immediately copy the generated **Value** - this is your `client_secret`

![](2025-08-11-08-48-25.png)

### **5. Configure Token Generation**

1. In your user pool, go to **App integration** → **Hosted UI**
2. Under **ID token**, enable the attributes (email, family_name, given_name)
3. Click **Save changes**

![](2025-08-11-08-33-43.png)

### **6. Configure API Permissions**

To ensure proper user attribute access:

1. Go to **API permissions** → **Add a permission** → **Microsoft Graph**
2. Add these permissions (email, family_name, given_name)
3. Click **Add permissions** and then **Grant admin consent**

![](2025-08-11-08-34-17.png)

### **7. Add OIDC Provider in Cognito**

In the AWS Console:

1. Navigate to **Cognito** → **User Pools** → select your user pool
2. Go to **Identity providers** → **Add identity provider** → **OpenID Connect**
    
![](2025-08-11-08-35-13.png)
    

1. Configure the provider: 
    - **Provider name:** `entra` (use a simple name without spaces)
    - **Client ID:** Paste the Application (client) ID from Entra ID
    - **Client secret:** Paste the secret value you created earlier
    - **Authorize scopes:** `openid profile email`
    - **Attributes request method:** Select `POST` (recommended)
    - **Issuer URL:** `https://login.microsoftonline.com/<tenant-id>/v2.0`

![](2025-08-11-08-36-04.png)

![](2025-08-11-08-36-21.png)

### **8. Configure Attribute Mapping**

In the same identity provider settings:

1. Under **Attribute mapping**, map these important attributes: 
    - **email** → `email`
    - **family_name** → `family_name`
    - **given_name** → `given_name`
2. Click **Save changes**

![](2025-08-11-08-36-46.png)

### **9. Enable Provider for Your App Client**

1. Go to **App integration** → **App clients** → select your app client
2. Under **Hosted UI** settings: 
    - Ensure your app client has appropriate **Callback URLs** configured
    - Under **Identity providers**, enable `OpenID Connect (entra)`
    - Verify **OAuth 2.0 grant types** includes `Authorization code grant`
    - Set **OpenID Connect scopes** to include `openid`, `profile`, `email`
3. Click **Save changes**

![](2025-08-11-08-37-07.png)

![](2025-08-11-08-37-22.png)

### **10. Test the Integration**

Test your integration by accessing:

```
https://<your-cognito-domain>/login?response_type=code&client_id=<cognito-app-client-id>&redirect_uri=<your-redirect-uri>
```

## See also:

[Entra ID and Cognito Itegration - Guide]({{< ref "entraid-cognito-itegration-overview.md" >}})

[Entra ID and Cognito Itegration - Step1]({{< ref "entraid-cognito-itegration-step1.md" >}})

[Entra ID and Cognito Itegration - Step2]({{< ref "entraid-cognito-itegration-step2.md" >}})

[Entra ID and Cognito Itegration - Step3]({{< ref "entraid-cognito-itegration-step3.md" >}})

[Entra ID and Cognito Itegration - Step4]({{< ref "entraid-cognito-itegration-step4.md" >}})

[Entra ID and Cognito Itegration - Step5]({{< ref "entraid-cognito-itegration-step5.md" >}})
