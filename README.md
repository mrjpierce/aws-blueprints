# AWS Blueprints

A collection of ready-to-deploy AWS infrastructure patterns and solutions using AWS CDK in multiple programming languages. This repository serves as a learning resource for AWS Cloud Practitioner certification preparation and provides practical, production-ready infrastructure templates.

## 🎯 Purpose

- Provide practical, hands-on examples of AWS infrastructure patterns
- Serve as a learning resource for AWS certification preparation
- Offer ready-to-use templates for common cloud architecture scenarios
- Demonstrate AWS best practices and well-architected framework principles
- Support multiple programming languages for different developer preferences

## 📁 Repository Structure

```
aws-blueprints/
├── typescript/       # TypeScript CDK implementations
│   └── blueprints/   # Self-contained blueprint directories
├── python/          # Python CDK implementations
│   └── blueprints/   # Self-contained blueprint directories
└── dev/             # Development workspace (not committed)
```

## 🔧 Available Blueprints

Each blueprint is completely self-contained and available in both TypeScript and Python:

### Current Blueprints:
1. **Basic Web Application** (EC2 + VPC + S3)
   - TypeScript: `typescript/blueprints/basic-web-app/`
   - Python: `python/blueprints/basic_web_app/`

2. **URL Shortener** (Lambda + DynamoDB + API Gateway + CloudFront)
   - TypeScript: `typescript/blueprints/url-shortener/`
   - Python: `python/blueprints/url_shortener/`

### Coming Soon:
3. Serverless API (API Gateway + Lambda + DynamoDB)
4. Static Website Hosting (S3 + CloudFront)
5. Container Application (ECS + Fargate)
6. Microservices Architecture (ECS + API Gateway + Lambda)

## 🚀 Getting Started

### Prerequisites

- AWS Account and configured AWS CLI
- AWS CDK CLI (`npm install -g aws-cdk`)

## 🔧 Initial Setup for Beginners

### 1. AWS Account Setup

If you don't have an AWS account yet:
1. Go to [AWS Console](https://aws.amazon.com/console/)
2. Click "Create an AWS Account"
3. Follow the registration process
4. **Important**: Set up billing alerts to avoid unexpected charges

### 2. AWS CLI Installation and Configuration

#### Install AWS CLI
```bash
# On macOS with Homebrew
brew install awscli

# On Ubuntu/Debian
sudo apt update
sudo apt install awscli

# On Windows with Chocolatey
choco install awscli

# Or download from: https://aws.amazon.com/cli/
```

#### Configure AWS CLI
```bash
aws configure
```
You'll need:
- **AWS Access Key ID**: Get from AWS Console → IAM → Users → Security credentials
- **AWS Secret Access Key**: Generated when you create access keys
- **Default region**: e.g., `us-east-1`, `us-west-2`, `eu-west-1`
- **Default output format**: `json` (recommended)

#### Verify AWS CLI Setup
```bash
aws sts get-caller-identity
```
This should return your AWS account details.

### 3. CDK CLI Installation

#### Install Node.js (if not already installed)
```bash
# On macOS with Homebrew
brew install node

# On Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Or download from: https://nodejs.org/
```

#### Install CDK CLI
```bash
npm install -g aws-cdk
```

#### Verify CDK Installation
```bash
cdk --version
```

### 4. Required AWS Permissions

Your AWS user/role needs the following permissions for CDK deployment:

#### Essential Permissions
- `cloudformation:*` (CloudFormation management)
- `s3:*` (S3 bucket operations)
- `iam:*` (IAM role and policy management)
- `ec2:*` (EC2 instance and networking)
- `ssm:*` (Systems Manager Parameter Store)

#### Quick Setup with AWS Managed Policies
For learning purposes, you can attach these managed policies to your user:
- `PowerUserAccess` (provides most permissions except IAM)
- `IAMFullAccess` (for IAM operations)

**⚠️ Security Note**: For production environments, create custom policies with minimal required permissions.

### 5. Bootstrap CDK (First Time Only)

CDK needs to bootstrap your AWS environment:
```bash
cdk bootstrap
```

This creates:
- S3 bucket for CDK assets
- IAM roles for CDK operations
- CloudFormation stack for CDK toolkit

### Language-Specific Prerequisites

**For TypeScript:**
- Node.js 14.x or later
- TypeScript (`npm install -g typescript`)

**For Python:**
- Python 3.8 or later
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/aws-blueprints.git
   cd aws-blueprints
   ```

2. Choose your preferred language and follow the setup instructions:
   - [TypeScript Setup](typescript/README.md)
   - [Python Setup](python/README.md)

3. Bootstrap AWS CDK (if you haven't already):
   ```bash
   cdk bootstrap
   ```

## 🛠️ Usage

Each blueprint contains its own README with specific instructions. Choose your preferred language:

### TypeScript
```bash
cd typescript/blueprints/[blueprint-name]
cdk deploy
```

### Python
```bash
cd python/blueprints/[blueprint_name]
cdk deploy
```

## 📚 Learning Resources

- [AWS Cloud Practitioner Certification](https://aws.amazon.com/certification/certified-cloud-practitioner/)
- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

The blueprints provided are examples and should be reviewed and modified according to your specific requirements before using in a production environment. Always follow AWS best practices and security guidelines.