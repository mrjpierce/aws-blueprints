#!/usr/bin/env python3
import os
import aws_cdk as cdk
from blueprints.basic_web_app.basic_web_app_stack import BasicWebAppStack

app = cdk.App()
BasicWebAppStack(
    app,
    "BasicWebAppStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION"),
    ),
)

app.synth()
