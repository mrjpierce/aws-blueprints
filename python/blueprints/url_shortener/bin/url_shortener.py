#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import aws_cdk as cdk
from url_shortener_stack import UrlShortenerStack

app = cdk.App()
UrlShortenerStack(app, "UrlShortenerStack",
    env=cdk.Environment(
        account=app.node.try_get_context("account") or cdk.Aws.ACCOUNT_ID,
        region=app.node.try_get_context("region") or cdk.Aws.REGION,
    )
)

app.synth()
