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
│   ├── blueprints/
│   ├── package.json
│   └── tsconfig.json
├── python/          # Python CDK implementations
│   ├── blueprints/
│   ├── requirements.txt
│   └── pyproject.toml
└── docs/            # Shared documentation and guides
```

## 🔧 Available Blueprints

Each blueprint is available in both TypeScript and Python, contained in their respective language directories with their own README and deployment instructions.

### Current Blueprints:
1. **Basic Web Application** (EC2 + VPC + S3)
   - TypeScript: `typescript/blueprints/basic-web-app/`
   - Python: `python/blueprints/basic_web_app/`

### Coming Soon:
2. Serverless API (API Gateway + Lambda + DynamoDB)
3. Static Website Hosting (S3 + CloudFront)
4. Container Application (ECS + Fargate)
5. Microservices Architecture (ECS + API Gateway + Lambda)

## 🚀 Getting Started

### Prerequisites

- AWS Account and configured AWS CLI
- AWS CDK CLI (`npm install -g aws-cdk`)

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