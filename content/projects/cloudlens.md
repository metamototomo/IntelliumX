---
title: "Serverless AWS Cost Monitoring"
date: 2025-01-30
draft: false
tags: ["AWS", "Serverless", "Cost Optimization", "Dashboard", "DynamoDB", "Lambda"]
categories: ["Cloud Projects"]
description: "A serverless AWS cost monitoring dashboard with real-time visibility, enterprise-grade security, and 97% cost optimization through intelligent caching."
---

# CloudLens

**Live Application:** <a href="https://cloudlens.intelliumx.com/" target="_blank" rel="noopener">cloudlens.intelliumx.com</a>

![](2026-01-04-10-58-11.png)

## Overview

CloudLens is a serverless AWS cost monitoring dashboard that quickly detects unexpected cost increases. Built with AWS-native services, CloudLens delivers real-time cost visibility through simple charts and time-based filtering while maintaining enterprise-grade security and minimal operational overhead.

## Background

I used to check AWS costs through Cost Explorer in the AWS Management Console. This was tedious—I had to log in, open Cost Explorer, and filter the data each time. I wanted quick access whenever I needed to check costs, ideally from my mobile device.

When developing systems, I sometimes encountered higher costs than expected. I wanted to catch any unexpected cost increases by checking costs regularly, which required a quick and easy access method.

So I developed CloudLens to quickly check costs with enterprise-level security protection.

## Key Features

- **Real-time Cost Visibility** - Monitor AWS costs across all services with up-to-date data
- **Service Breakdown Analysis** - Identify top cost drivers by service
- **Flexible Time Filtering** - Toggle between 7, 30, or 90-day views
- **Secure Authentication** - OAuth 2.0 with Amazon Cognito and PKCE
- **Cost Optimized** - ~$7/month operational cost with 97% API savings
- **Zero Maintenance** - Fully serverless architecture
- **Mobile Responsive** - Access from any device, anywhere

## Architecture

CloudLens is built on a 100% serverless AWS architecture:

![CloudLens Architecture](/images/projects/cloudlens/architecture-diagram.png)

**Components:**
- **Frontend:** S3 + CloudFront with Origin Access Control (OAC)
- **Authentication:** Amazon Cognito with Authorization Code + PKCE flow
- **Backend:** API Gateway (REST) + Lambda (Python)
- **Caching:** DynamoDB with 6-hour TTL
- **Data Source:** AWS Cost Explorer API

## The Cost Optimization Story

During development, I ran many API calls from the UI for testing. Then I noticed a cost surge because of the API calls to Cost Explorer. I was shocked—I had been so careful about costs.

**The Problem:**
- Cost Explorer API: $0.01 per request
- Development testing: ~160 page loads/day
- Each page load: 6 API calls
- Daily cost: $9.60 → **$288/month**

**The Solution:**
I implemented a caching layer using DynamoDB with a 6-hour TTL. The results were dramatic:
- API calls reduced from 960/day to 24/day
- Cost dropped from $288/month to $7.45/month
- **97% cost reduction**

I've been actively using the application for testing over the last few days, and I no longer see unexpected cost increases. This is crucial when developing any application or system in a cloud environment. I'm very happy with this application and will keep using it while improving usability and maintaining simple UI operations.

**Total: ~$7/month** (after free tier)

## Conclusion

CloudLens demonstrates that powerful, production-ready applications can be built entirely on serverless AWS services while maintaining low costs and high security. The project showcases practical cloud architecture patterns, cost optimization techniques, and the importance of monitoring in cloud environments.

Most importantly, it solves a real problem: making AWS cost monitoring quick, easy, and accessible from anywhere.

---

**Project Status:** Production (Active Development)  
**Live Demo:** <a href="https://cloudlens.intelliumx.com/" target="_blank" rel="noopener">cloudlens.intelliumx.com</a>  
**Last Updated:** January 2026
