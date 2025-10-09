# URL Shortener Blueprint (Python)

A serverless URL shortener service built with AWS CDK, perfect for learning serverless architecture and API design.

## 📋 Architecture Overview

This blueprint creates:

1. **DynamoDB Table**
   - Stores URL mappings (shortCode → originalUrl)
   - Pay-per-request billing
   - Global Secondary Index for analytics

2. **Lambda Functions**
   - **Shorten Function**: Creates short URLs
   - **Redirect Function**: Redirects to original URLs
   - **Analytics Function**: Provides click statistics

3. **API Gateway**
   - RESTful API endpoints
   - CORS enabled
   - Lambda integration

4. **CloudFront Distribution**
   - Global CDN for fast access
   - Custom domain support
   - Caching optimization

5. **S3 Bucket**
   - Static website hosting
   - Public read access

## 🎯 Learning Objectives

This blueprint helps you understand:
- Serverless architecture patterns
- DynamoDB NoSQL database design
- Lambda function development
- API Gateway REST API creation
- CloudFront CDN configuration
- CORS and security best practices

## 🚀 Deployment

1. **Navigate to the blueprint directory**:
   ```bash
   cd python/blueprints/url_shortener
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

4. **Deploy the stack**:
   ```bash
   cdk deploy
   ```

5. **After deployment, note the outputs**:
   - **ApiUrl**: API Gateway URL for the service
   - **DistributionUrl**: CloudFront URL for the website
   - **WebsiteBucketName**: S3 bucket name for static files

## 📡 API Endpoints

### Create Short URL
```bash
POST {ApiUrl}/shorten
Content-Type: application/json

{
  "originalUrl": "https://example.com/very-long-url"
}
```

**Response:**
```json
{
  "shortCode": "a1b2c3d4",
  "shortUrl": "https://api.example.com/a1b2c3d4",
  "originalUrl": "https://example.com/very-long-url"
}
```

### Redirect to Original URL
```bash
GET {DistributionUrl}/a1b2c3d4
```
Returns HTTP 302 redirect to original URL.

### Get Analytics
```bash
GET {ApiUrl}/analytics/a1b2c3d4
```

**Response:**
```json
{
  "shortCode": "a1b2c3d4",
  "originalUrl": "https://example.com/very-long-url",
  "clickCount": 42,
  "createdAt": "2024-01-15T10:30:00.000Z"
}
```

## 💡 Cost Considerations

This blueprint uses:
- **DynamoDB**: Pay-per-request (very low cost for small usage)
- **Lambda**: Pay-per-request (1M free requests/month)
- **API Gateway**: Pay-per-request (1M free requests/month)
- **CloudFront**: Pay-per-request (1TB free data transfer/month)
- **S3**: Pay-per-request (very low cost)

**Estimated monthly cost for light usage**: $0-5

## 🧹 Cleanup

To remove all resources:
```bash
cdk destroy
```

## 🔧 Customization Ideas

1. **Custom Domain**: Add Route 53 hosted zone and certificate
2. **Authentication**: Add Cognito for user management
3. **Rate Limiting**: Add API Gateway throttling
4. **Analytics Dashboard**: Add QuickSight for visual analytics
5. **Bulk Import**: Add CSV import functionality
6. **QR Code Generation**: Add QR code generation for short URLs

## 📚 Related AWS Services

Learn more about the services used:
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [Amazon S3](https://aws.amazon.com/s3/)
