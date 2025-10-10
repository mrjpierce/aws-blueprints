import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_apigateway as apigateway,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3 as s3,
)
from constructs import Construct


class UrlShortenerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB table for storing URL mappings
        url_table = dynamodb.Table(
            self, "UrlTable",
            table_name="url-shortener",
            partition_key=dynamodb.Attribute(
                name="shortCode", 
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        # Add GSI for original URL lookups
        url_table.add_global_secondary_index(
            index_name="originalUrl-index",
            partition_key=dynamodb.Attribute(
                name="originalUrl", 
                type=dynamodb.AttributeType.STRING
            ),
        )

        # Lambda function for URL shortening
        shorten_function = _lambda.Function(
            self, "ShortenFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambda/shorten"),
            environment={
                'TABLE_NAME': url_table.table_name,
            },
        )

        # Lambda function for URL redirection
        redirect_function = _lambda.Function(
            self, "RedirectFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambda/redirect"),
            environment={
                'TABLE_NAME': url_table.table_name,
            },
        )

        # Lambda function for analytics
        analytics_function = _lambda.Function(
            self, "AnalyticsFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambda/analytics"),
            environment={
                'TABLE_NAME': url_table.table_name,
            },
        )

        # Grant DynamoDB permissions
        url_table.grant_read_write_data(shorten_function)
        url_table.grant_read_write_data(redirect_function)
        url_table.grant_read_data(analytics_function)

        # API Gateway
        api = apigateway.RestApi(
            self, "UrlShortenerApi",
            rest_api_name="URL Shortener Service",
            description="API for URL shortening service",
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=apigateway.Cors.ALL_METHODS,
                allow_headers=["Content-Type", "X-Amz-Date", "Authorization", "X-Api-Key"],
            ),
        )

        # API routes
        shorten_integration = apigateway.LambdaIntegration(shorten_function)
        redirect_integration = apigateway.LambdaIntegration(redirect_function)
        analytics_integration = apigateway.LambdaIntegration(analytics_function)

        # POST /shorten - Create short URL
        api.root.add_resource("shorten").add_method("POST", shorten_integration)

        # GET /{shortCode} - Redirect to original URL
        short_code_resource = api.root.add_resource("{shortCode}")
        short_code_resource.add_method("GET", redirect_integration)

        # GET /analytics/{shortCode} - Get analytics for short URL
        analytics_resource = api.root.add_resource("analytics").add_resource("{shortCode}")
        analytics_resource.add_method("GET", analytics_integration)

        # S3 bucket for static website
        website_bucket = s3.Bucket(
            self, "WebsiteBucket",
            website_index_document="index.html",
            website_error_document="error.html",
            public_read_access=True,
            block_public_access=s3.BlockPublicAccess(
                block_public_acls=False,
                block_public_policy=False,
                ignore_public_acls=False,
                restrict_public_buckets=False,
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        # CloudFront distribution
        distribution = cloudfront.Distribution(
            self, "Distribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.HttpOrigin(website_bucket.bucket_website_domain_name),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            additional_behaviors={
                "/api/*": cloudfront.BehaviorOptions(
                    origin=origins.RestApiOrigin(api),
                    viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                    cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                ),
            },
        )

        # Outputs
        cdk.CfnOutput(
            self, "ApiUrl",
            value=api.url,
            description="API Gateway URL",
        )

        cdk.CfnOutput(
            self, "DistributionUrl",
            value=f"https://{distribution.distribution_domain_name}",
            description="CloudFront Distribution URL",
        )

        cdk.CfnOutput(
            self, "WebsiteBucketName",
            value=website_bucket.bucket_name,
            description="S3 Website Bucket Name",
        )
