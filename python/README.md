# AWS Blueprints - Python

This directory contains AWS infrastructure blueprints implemented using Python and AWS CDK.

## 🚀 Quick Start

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Bootstrap AWS CDK (if you haven't already):
   ```bash
   cdk bootstrap
   ```

4. Deploy a blueprint:
   ```bash
   cd blueprints/basic_web_app
   cdk deploy
   ```

## 📁 Available Blueprints

- **basic_web_app**: A fundamental web application with VPC, EC2, and S3

## 🛠️ Development

### Prerequisites
- Python 3.8 or later
- AWS CLI configured
- AWS CDK CLI (`npm install -g aws-cdk`)

### Development Setup
```bash
# Install development dependencies
pip install -e ".[dev]"

# Format code
black .
isort .

# Type checking
mypy .

# Run tests
pytest
```

### CDK Commands
- `cdk deploy` - Deploy stack
- `cdk destroy` - Destroy stack
- `cdk diff` - Show differences
- `cdk synth` - Synthesize CloudFormation template

## 📚 Learning Resources
- [AWS CDK Python Documentation](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)
- [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-cdk-lib.aws-ec2-readme.html)
