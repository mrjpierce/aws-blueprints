# AWS Blueprints - Python

This directory contains self-contained AWS infrastructure blueprints implemented using Python and AWS CDK.

## 🚀 Python Setup

### Prerequisites
- Python 3.8 or later
- AWS CLI configured (see main README for setup)
- AWS CDK CLI (`npm install -g aws-cdk`)

### Quick Start

1. **Navigate to a blueprint directory**:
   ```bash
   cd blueprints/[blueprint_name]
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Bootstrap CDK (first time only)**:
   ```bash
   cdk bootstrap
   ```

5. **Deploy the blueprint**:
   ```bash
   cdk deploy
   ```

6. **Destroy when done**:
   ```bash
   cdk destroy
   ```

## 📁 Available Blueprints

### 1. **Basic Web Application** (`blueprints/basic_web_app/`)
- **Services**: VPC, EC2, S3, IAM
- **Purpose**: Learn fundamental AWS services

### 2. **URL Shortener** (`blueprints/url_shortener/`)
- **Services**: Lambda, DynamoDB, API Gateway, CloudFront, S3
- **Purpose**: Learn serverless architecture

## 🏗️ Blueprint Structure

Each blueprint is completely independent with its own:
- **Dependencies** (`requirements.txt` and `pyproject.toml`)
- **CDK Configuration** (`cdk.json`)
- **App Entry Point** (`bin/blueprint_name.py`)
- **Stack Implementation** (`blueprint_name_stack.py`)
- **Documentation** (`README.md`)

## 📚 Learning Resources
- [AWS CDK Python Documentation](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)
- [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-cdk-lib.aws-ec2-readme.html)