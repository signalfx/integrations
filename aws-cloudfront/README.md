# ![](./img/integration_awscloudfront.png) Amazon CloudFront

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon CloudFront via [Amazon CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws). 

#### FEATURES

##### Built-in dashboards

- **CloudFront Distributions**: Overview of all data from CloudFront.
  
  [<img src='./img/dashboard_cloudfront_distributions.png' width=200px>](./img/dashboard_cloudfront_distributions.png)
- **CloudFront Distribution**: Focus on a single CloudFront distribution.
  
  [<img src='./img/dashboard_cloudfront_distribution.png' width=200px>](./img/dashboard_cloudfront_distribution.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws) on the SignalFx Integrations page. 

Note that CloudWatch metrics for CloudFront are reported only from region `us-east-1` (US East/N. Virginia). To import metrics for CloudFront, ensure that your CloudWatch configuration includes metrics from `us-east-1`. 

### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below. 

![](./img/dashboard_cloudfront_distributions.png)

![](./img/dashboard_cloudfront_distribution.png)

### METRICS

For more information about the metrics emitted by Amazon CloudFront, click here or visit the service's homepage at https://aws.amazon.com/cloudfront/.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
