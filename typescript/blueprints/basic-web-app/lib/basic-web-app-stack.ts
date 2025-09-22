import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class BasicWebAppStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create VPC with public and private subnets
    const vpc = new ec2.Vpc(this, 'WebAppVPC', {
      maxAzs: 2,
      natGateways: 1,
      subnetConfiguration: [
        {
          name: 'Public',
          subnetType: ec2.SubnetType.PUBLIC,
          cidrMask: 24,
        },
        {
          name: 'Private',
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
          cidrMask: 24,
        },
      ],
    });

    // Create S3 bucket for static assets
    const staticAssetsBucket = new s3.Bucket(this, 'StaticAssets', {
      versioned: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // For demo purposes only
      autoDeleteObjects: true, // For demo purposes only
    });

    // Create security group for web server
    const webServerSG = new ec2.SecurityGroup(this, 'WebServerSG', {
      vpc,
      description: 'Security group for web server',
      allowAllOutbound: true,
    });

    webServerSG.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(80),
      'Allow HTTP traffic'
    );

    // Create IAM role for EC2 instance
    const webServerRole = new iam.Role(this, 'WebServerRole', {
      assumedBy: new iam.ServicePrincipal('ec2.amazonaws.com'),
    });

    // Add permissions to access S3 bucket
    staticAssetsBucket.grantRead(webServerRole);

    // Create EC2 instance
    const webServer = new ec2.Instance(this, 'WebServer', {
      vpc,
      vpcSubnets: {
        subnetType: ec2.SubnetType.PUBLIC,
      },
      instanceType: ec2.InstanceType.of(
        ec2.InstanceClass.T2,
        ec2.InstanceSize.MICRO
      ),
      machineImage: new ec2.AmazonLinuxImage({
        generation: ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
      }),
      securityGroup: webServerSG,
      role: webServerRole,
    });

    // Add user data script to install and configure web server
    webServer.addUserData(
      'yum update -y',
      'yum install -y httpd',
      'systemctl start httpd',
      'systemctl enable httpd',
      'echo "<h1>Hello from AWS!</h1>" > /var/www/html/index.html'
    );

    // Output the public IP of the web server
    new cdk.CfnOutput(this, 'WebServerIP', {
      value: webServer.instancePublicIp,
      description: 'Public IP address of the web server',
    });

    // Output the S3 bucket name
    new cdk.CfnOutput(this, 'BucketName', {
      value: staticAssetsBucket.bucketName,
      description: 'Name of the S3 bucket for static assets',
    });
  }
}
