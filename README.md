# AWS Blueprints

A collection of ready-to-deploy AWS infrastructure patterns and solutions using AWS CDK. This repository serves as a learning resource for AWS Cloud Practitioner certification preparation and provides practical, production-ready infrastructure templates.

## 🎯 Purpose

- Provide practical, hands-on examples of AWS infrastructure patterns
- Serve as a learning resource for AWS certification preparation
- Offer ready-to-use templates for common cloud architecture scenarios
- Demonstrate AWS best practices and well-architected framework principles

## 📁 Repository Structure

```
aws-blueprints/
├── blueprints/       # Individual blueprint implementations
├── lib/             # Shared constructs and utilities
├── test/            # Test cases for blueprints
└── docs/            # Documentation and guides
```

## 🔧 Available Blueprints

Each blueprint is contained in its own directory under `blueprints/` with its own README and deployment instructions.

Coming soon:
1. Basic Web Application (EC2 + VPC + S3)
2. Serverless API (API Gateway + Lambda + DynamoDB)
3. Static Website Hosting (S3 + CloudFront)
4. Container Application (ECS + Fargate)
5. Microservices Architecture (ECS + API Gateway + Lambda)

## 🚀 Getting Started

### Prerequisites

- AWS Account and configured AWS CLI
- Node.js 14.x or later
- AWS CDK CLI (`npm install -g aws-cdk`)
- TypeScript (`npm install -g typescript`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/aws-blueprints.git
   cd aws-blueprints
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Bootstrap AWS CDK (if you haven't already):
   ```bash
   cdk bootstrap
   ```

## 🛠️ Usage

Each blueprint contains its own README with specific instructions, but generally:

1. Navigate to the blueprint directory:
   ```bash
   cd blueprints/[blueprint-name]
   ```

2. Deploy the blueprint:
   ```bash
   cdk deploy
   ```

3. To destroy the resources:
   ```bash
   cdk destroy
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