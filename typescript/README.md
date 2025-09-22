# AWS Blueprints - TypeScript

This directory contains AWS infrastructure blueprints implemented using TypeScript and AWS CDK.

## 🚀 Quick Start

1. Install dependencies:
   ```bash
   npm install
   ```

2. Bootstrap AWS CDK (if you haven't already):
   ```bash
   cdk bootstrap
   ```

3. Deploy a blueprint:
   ```bash
   cd blueprints/basic-web-app
   cdk deploy
   ```

## 📁 Available Blueprints

- **basic-web-app**: A fundamental web application with VPC, EC2, and S3

## 🛠️ Development

### Prerequisites
- Node.js 14.x or later
- AWS CLI configured
- AWS CDK CLI (`npm install -g aws-cdk`)

### Scripts
- `npm run build` - Compile TypeScript
- `npm run watch` - Watch for changes and recompile
- `npm test` - Run tests
- `cdk deploy` - Deploy stack
- `cdk destroy` - Destroy stack
- `cdk diff` - Show differences
- `cdk synth` - Synthesize CloudFormation template

## 📚 Learning Resources
- [AWS CDK TypeScript Documentation](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-typescript.html)
- [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-cdk-lib.aws-ec2-readme.html)
