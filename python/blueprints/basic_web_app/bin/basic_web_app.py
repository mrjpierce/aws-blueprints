#!/usr/bin/env python3
import aws_cdk as cdk
from basic_web_app_stack import BasicWebAppStack

app = cdk.App()
BasicWebAppStack(app, "BasicWebAppStack",
    env=cdk.Environment(
        account=app.node.try_get_context("account") or cdk.Aws.ACCOUNT_ID,
        region=app.node.try_get_context("region") or cdk.Aws.REGION,
    )
)

app.synth()
