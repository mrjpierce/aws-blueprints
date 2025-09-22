# Basic Web Application Blueprint

This blueprint demonstrates a fundamental web application architecture in AWS, perfect for learning core AWS services covered in the Cloud Practitioner exam.

## 📋 Architecture Overview

This blueprint creates:

1. **VPC (Virtual Private Cloud)**
   - 2 Availability Zones
   - Public and Private subnets
   - NAT Gateway for private subnet internet access
   - Internet Gateway for public subnet

2. **EC2 Instance**
   - t2.micro instance (free tier eligible)
   - Apache web server
   - Located in public subnet
   - Security group allowing HTTP traffic

3. **S3 Bucket**
   - Versioning enabled
   - Server-side encryption
   - Used for static assets storage

4. **IAM Role**
   - Allows EC2 instance to access S3 bucket
   - Follows principle of least privilege

## 🎯 Learning Objectives

This blueprint helps you understand:

- VPC networking and subnets
- EC2 instance deployment and configuration
- Security Groups and network access control
- S3 bucket creation and permissions
- IAM roles and policies
- Infrastructure as Code using AWS CDK

## 🚀 Deployment Instructions

1. Navigate to the blueprint directory:
   ```bash
   cd blueprints/basic-web-app
   ```

2. Deploy the stack:
   ```bash
   cdk deploy
   ```

3. After deployment, note the outputs:
   - WebServerIP: Public IP of your web server
   - BucketName: Name of your S3 bucket

4. Access your web application:
   ```
   http://<WebServerIP>
   ```

## 💡 Cost Considerations

This blueprint uses:
- t2.micro EC2 instance (Free Tier eligible)
- S3 bucket (Free Tier eligible for first 12 months)
- NAT Gateway (NOT Free Tier eligible - approximately $0.045/hour)

To minimize costs:
- Destroy the stack when not in use
- Consider removing the NAT Gateway if not needed
- Monitor AWS Cost Explorer

## 🧹 Cleanup

To remove all resources:
```bash
cdk destroy
```

## 📚 Related AWS Services

Learn more about the services used:
- [Amazon VPC](https://aws.amazon.com/vpc/)
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [AWS IAM](https://aws.amazon.com/iam/)
