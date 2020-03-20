# ![](./img/integration_cloudwatchevents.png) CloudWatch Events

- [Description](#description)
- [Installation](#installation)

### DESCRIPTION

The SignalFx CloudWatch Lambda function for [CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) transforms CloudWatch Events into SignalFx Custom Events and sends them to [SignalFx](https://www.SignalFx.com).

This enables you to [view CloudWatch events](https://docs.signalfx.com/en/latest/detect-alert/events-intro.html) in SignalFx.

### INSTALLATION

SignalFx Lambda for CloudWatch Events is provided via AWS Serverless Application Repository and as a GitHub repository. For details, see the repository's [README](https://github.com/signalfx/cloudwatch-event-forwarder/blob/master/README.md) or search for "SignalFx CloudWatch" in [AWS Serverless Repository](https://console.aws.amazon.com/serverlessrepo/home#/available-applications).
The application in Serverless Repository is called "signalfx-cloudwatch-event-forwarder".