---
date: '2026-01-18T21:58:22+11:00'
draft: false
title: 'Custom Domain - Cloudfront & Cloudflare'
tags: ["Custom Domain", "CloudFront", "CloudFlare", "SSL"]
categories: ["Technology"]
---

## Step 1: Request ACM Certificate (AWS)

1. Go to **AWS Certificate Manager** in **us-east-1** region
2. Click **Request a public certificate**
3. Add domain names: e.g., `heartbeat.intelliumx.com`
4. Select **DNS validation**
5. Click **Request**

![](2026-01-18-21-59-43.png)

![](2026-01-18-22-00-00.png)

---

## Step 2: Add Validation Records to CloudFlare

1. In ACM, copy the CNAME **name** and **value** shown for validation
2. Go to **CloudFlare DNS** settings
3. Add a new **CNAME record** with the name and value from ACM
4. **Important:** Set proxy status to **DNS only** (grey cloud) for validation
5. Save the record

![](2026-01-18-22-00-23.png)

---

## Step 3: Wait for Certificate Validation

1. Return to ACM console
2. Wait for certificate status to change to **Issued** (usually a few minutes)
3. If it stays pending, double-check the CNAME record in CloudFlare

![](2026-01-18-22-00-41.png)

---

## Step 4: Configure CloudFront Distribution

1. Go to **CloudFront** console
2. Select your distribution and click **Edit**
3. Under **Alternate Domain Names (CNAMEs)**, add: `heartbeat.intelliumx.com`
4. Under **SSL Certificate**, select **Custom SSL certificate**
5. Choose your ACM certificate from the dropdown
6. Save changes and wait for deployment to complete

![](2026-01-18-22-08-52.png)

---

## Step 5: Point Domain to CloudFront (CloudFlare DNS)

1. In CloudFlare DNS, create a **CNAME record**:
    - Type: `CNAME`
    - Name: `heartbeat`
    - Target: `your-distribution.cloudfront.net` (from CloudFront console)
    - Proxy: Choose **Proxied** (orange) or **DNS only** (grey)

![](2026-01-18-22-00-57.png)

---