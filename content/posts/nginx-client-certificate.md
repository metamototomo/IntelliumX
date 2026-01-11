---
date: '2026-01-11T12:10:31+11:00'
draft: false
title: 'NGINX - Client Certificate Authentication'
tags: ["NGINX", "Client Certificate", "SSL Certificate", "Security"]
categories: ["Technology"]
---

## **Summary**

This guide sets up Nginx with client certificate authentication on Amazon Linux 2023, requiring clients to present a valid certificate signed by your CA to access the web server. Key steps include installing Nginx with TLS configuration, uploading server and CA certificates, configuring `ssl_verify_client on` for authentication, and installing client certificates on Windows machines. Common troubleshooting involves temporarily disabling SELinux if it blocks HTTPS traffic.

## **1. Launch EC2 Instance (Example operations)**

```bash
# Amazon Linux 2023, t3.micro, in your VPC
# Security Group: Allow 443 from your network

sh-5.2$ cd ~
sh-5.2$ pwd
/home/ssm-user
sh-5.2$ aws s3 cp s3://gcs-share/certs/certs_v06.zip .
download: s3://gcs-share/certs/certs_v06.zip to ./certs_v06.zip
sh-5.2$ ls
certs_v06.zip
sh-5.2$ pwd
/home/ssm-user
sh-5.2$ sudo dnf install -y unzip tree
sh-5.2$ unzip certs_v06.zip
Archive:  certs_v06.zip
   creating: certs/
  inflating: certs/ca-bundle.crt
  inflating: certs/ca.crt
  inflating: certs/client-006.crt
  inflating: certs/client-006.pfx
  inflating: certs/client.key
  inflating: certs/dual-006.crt
  inflating: certs/dual-006.pfx
  inflating: certs/dual.key
  inflating: certs/mid-ca.crt
  inflating: certs/server-006.crt
  inflating: certs/server-006.pfx
  inflating: certs/server.key
sh-5.2$ tree certs
certs
├── ca-bundle.crt
├── ca.crt
├── client-006.crt
├── client-006.pfx
├── client.key
├── dual-006.crt
├── dual-006.pfx
├── dual.key
├── mid-ca.crt
├── server-006.crt
├── server-006.pfx
└── server.key

0 directories, 12 files
sh-5.2$ ^C
```

## **2. Install and Configure Nginx**

```bash
sudo dnf update -y
sudo dnf install -y nginx
sudo systemctl enable nginx

# Create SSL directory
sudo mkdir -p /etc/nginx/ssl
sudo chmod 700 /etc/nginx/ssl
```

## **3. Upload Your Certificates**

```bash
# Copy these files to /etc/nginx/ssl/:
# - server-006.crt (your server certificate)
# - server.key (your server private key)
# - ca-bundle.crt (mid-ca.crt + ca.crt concatenated)
sudo cp certs/* /etc/nginx/ssl/
sudo chmod 600 /etc/nginx/ssl/server.key
sudo chmod 644 /etc/nginx/ssl/ca-bundle.crt
sudo chmod 644 /etc/nginx/ssl/server-006.crt
sudo ls -l /etc/nginx/ssl/
```

## **4. Configure Nginx (/etc/nginx/nginx.conf)**

```
events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    server {
        listen 443 ssl;
        server_name d11-lnx-web01.gcs.cloud;  # <-- SET THE FQDN OF THE SERVER

        # Server certificates
        ssl_certificate /etc/nginx/ssl/server-006.crt;
        ssl_certificate_key /etc/nginx/ssl/server.key;

        # Client certificate authentication
        ssl_client_certificate /etc/nginx/ssl/ca-bundle.crt;
        ssl_verify_client on;

        # SSL settings
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256;
        ssl_prefer_server_ciphers off;

        location / {
            root /usr/share/nginx/html;
            index index.html;

            # Add client cert info to response
            add_header X-Client-Cert-Subject $ssl_client_s_dn;
            add_header X-Client-Cert-Issuer $ssl_client_i_dn;
        }
    }
}
```

## **6. Create Sample HTML Page (Optional)**

```bash
sudo tee /usr/share/nginx/html/index.html > /dev/null << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Client Certificate Authentication Test</title>
</head>
<body>
    <h1>Welcome! Client Certificate Authentication Successful</h1>
    <p>Your client certificate was verified successfully.</p>
    <p>This page requires a valid client certificate to access.</p>
</body>
</html>
EOF
```

## **7. Start Nginx**

```bash
sudo nginx -t
sudo systemctl start nginx
sudo systemctl status nginx
```

## **9. Client Setup (Windows machines)**

- Install  in "Current User\Personal\Certificates"
    
    ```
    client-006.pfx
    ```
    
![](2026-01-11-12-19-20.png)
    

## **10. Access from Browser**

- Navigate to
    
    ```
    https://d11-lnx-web01.gcs.cloud/
    ```
    
- Browser will show certificate selection popup
- Select your client certificate
- Page will load successfully

This setup will show the certificate selection popup on Windows browsers when accessing the site.

