from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
)
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_iam as iam
from constructs import Construct


class BasicWebAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC with public and private subnets
        vpc = ec2.Vpc(
            self,
            "WebAppVPC",
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24,
                ),
            ],
        )

        # Create S3 bucket for static assets
        static_assets_bucket = s3.Bucket(
            self,
            "StaticAssets",
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            removal_policy=RemovalPolicy.DESTROY,  # For demo purposes only
            auto_delete_objects=True,  # For demo purposes only
        )

        # Create security group for web server
        web_server_sg = ec2.SecurityGroup(
            self,
            "WebServerSG",
            vpc=vpc,
            description="Security group for web server",
            allow_all_outbound=True,
        )

        web_server_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow HTTP traffic",
        )

        # Create IAM role for EC2 instance
        web_server_role = iam.Role(
            self,
            "WebServerRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )

        # Add permissions to access S3 bucket
        static_assets_bucket.grant_read(web_server_role)

        # Create EC2 instance
        web_server = ec2.Instance(
            self,
            "WebServer",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2,
                ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            security_group=web_server_sg,
            role=web_server_role,
        )

        # Add user data script to install and configure web server
        web_server.add_user_data(
            "yum update -y",
            "yum install -y httpd",
            "systemctl start httpd",
            "systemctl enable httpd",
            'echo "<h1>Hello from AWS!</h1>" > /var/www/html/index.html',
        )

        # Output the public IP of the web server
        CfnOutput(
            self,
            "WebServerIP",
            value=web_server.instance_public_ip,
            description="Public IP address of the web server",
        )

        # Output the S3 bucket name
        CfnOutput(
            self,
            "BucketName",
            value=static_assets_bucket.bucket_name,
            description="Name of the S3 bucket for static assets",
        )
