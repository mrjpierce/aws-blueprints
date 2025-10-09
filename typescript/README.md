# AWS Blueprints - TypeScript

This directory contains self-contained AWS infrastructure blueprints implemented using TypeScript and AWS CDK.

## 🚀 TypeScript Setup

### Prerequisites
- Node.js 18.x or later
- AWS CLI configured (see main README for setup)
- AWS CDK CLI (`npm install -g aws-cdk`)

### Quick Start

1. **Navigate to a blueprint directory**:
   ```bash
   cd blueprints/[blueprint-name]
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Bootstrap CDK (first time only)**:
   ```bash
   cdk bootstrap
   ```

4. **Deploy the blueprint**:
   ```bash
   cdk deploy
   ```

5. **Destroy when done**:
   ```bash
   cdk destroy
   ```

## 📁 Available Blueprints

### 1. **Basic Web Application** (`blueprints/basic-web-app/`)
- **Services**: VPC, EC2, S3, IAM
- **Purpose**: Learn fundamental AWS services

### 2. **URL Shortener** (`blueprints/url-shortener/`)
- **Services**: Lambda, DynamoDB, API Gateway, CloudFront, S3
- **Purpose**: Learn serverless architecture

## 🏗️ Blueprint Structure

Each blueprint is completely independent with its own:
- **Dependencies** (`package.json`)
- **TypeScript Configuration** (`tsconfig.json`)
- **CDK Configuration** (`cdk.json`)
- **App Entry Point** (`bin/blueprint-name.ts`)
- **Stack Implementation** (`lib/blueprint-name-stack.ts`)
- **Documentation** (`README.md`)

## 📚 Learning Resources
- [AWS CDK TypeScript Documentation](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-typescript.html)
- [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-cdk-lib.aws-ec2-readme.html)
