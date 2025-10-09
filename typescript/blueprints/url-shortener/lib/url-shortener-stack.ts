import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class UrlShortenerStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // DynamoDB table for storing URL mappings
    const urlTable = new dynamodb.Table(this, 'UrlTable', {
      tableName: 'url-shortener',
      partitionKey: { name: 'shortCode', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Add GSI for original URL lookups
    urlTable.addGlobalSecondaryIndex({
      indexName: 'originalUrl-index',
      partitionKey: { name: 'originalUrl', type: dynamodb.AttributeType.STRING },
    });

    // Lambda function for URL shortening
    const shortenFunction = new lambda.Function(this, 'ShortenFunction', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('lambda/shorten'),
      environment: {
        TABLE_NAME: urlTable.tableName,
      },
    });

    // Lambda function for URL redirection
    const redirectFunction = new lambda.Function(this, 'RedirectFunction', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('lambda/redirect'),
      environment: {
        TABLE_NAME: urlTable.tableName,
      },
    });

    // Lambda function for analytics
    const analyticsFunction = new lambda.Function(this, 'AnalyticsFunction', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('lambda/analytics'),
      environment: {
        TABLE_NAME: urlTable.tableName,
      },
    });

    // Grant DynamoDB permissions
    urlTable.grantReadWriteData(shortenFunction);
    urlTable.grantReadWriteData(redirectFunction);
    urlTable.grantReadData(analyticsFunction);

    // API Gateway
    const api = new apigateway.RestApi(this, 'UrlShortenerApi', {
      restApiName: 'URL Shortener Service',
      description: 'API for URL shortening service',
      defaultCorsPreflightOptions: {
        allowOrigins: apigateway.Cors.ALL_ORIGINS,
        allowMethods: apigateway.Cors.ALL_METHODS,
        allowHeaders: ['Content-Type', 'X-Amz-Date', 'Authorization', 'X-Api-Key'],
      },
    });

    // API routes
    const shortenIntegration = new apigateway.LambdaIntegration(shortenFunction);
    const redirectIntegration = new apigateway.LambdaIntegration(redirectFunction);
    const analyticsIntegration = new apigateway.LambdaIntegration(analyticsFunction);

    // POST /shorten - Create short URL
    api.root.addResource('shorten').addMethod('POST', shortenIntegration);

    // GET /{shortCode} - Redirect to original URL
    const shortCodeResource = api.root.addResource('{shortCode}');
    shortCodeResource.addMethod('GET', redirectIntegration);

    // GET /analytics/{shortCode} - Get analytics for short URL
    const analyticsResource = api.root.addResource('analytics').addResource('{shortCode}');
    analyticsResource.addMethod('GET', analyticsIntegration);

    // S3 bucket for static website
    const websiteBucket = new s3.Bucket(this, 'WebsiteBucket', {
      websiteIndexDocument: 'index.html',
      websiteErrorDocument: 'error.html',
      publicReadAccess: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // CloudFront distribution
    const distribution = new cloudfront.Distribution(this, 'Distribution', {
      defaultBehavior: {
        origin: new origins.S3Origin(websiteBucket),
        viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
      },
      additionalBehaviors: {
        '/api/*': {
          origin: new origins.RestApiOrigin(api),
          viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
          cachePolicy: cloudfront.CachePolicy.CACHING_DISABLED,
        },
      },
    });

    // Outputs
    new cdk.CfnOutput(this, 'ApiUrl', {
      value: api.url,
      description: 'API Gateway URL',
    });

    new cdk.CfnOutput(this, 'DistributionUrl', {
      value: `https://${distribution.distributionDomainName}`,
      description: 'CloudFront Distribution URL',
    });

    new cdk.CfnOutput(this, 'WebsiteBucketName', {
      value: websiteBucket.bucketName,
      description: 'S3 Website Bucket Name',
    });
  }
}
