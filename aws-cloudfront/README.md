---
title: Amazon CloudFront
brief: SignalFx's integration with Amazon CloudFront
---

# Amazon CloudFront

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon CloudFront via [Amazon CloudWatch](../aws)<!-- sfx_link:aws -->. 

#### FEATURES

##### Built-in dashboards

- **CloudFront Distributions**: Overview of all data from CloudFront.
  
  [<img src='./img/dashboard_cloudfront_distributions.png' width=200px>](./img/dashboard_cloudfront_distributions.png)
- **CloudFront Distribution**: Focus on a single CloudFront distribution.
  
  [<img src='./img/dashboard_cloudfront_distribution.png' width=200px>](./img/dashboard_cloudfront_distribution.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](../aws)<!-- sfx_link:aws --> on the SignalFx Integrations page. 

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page. 

### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below. 

![](./img/dashboard_cloudfront_distributions.png)

![](./img/dashboard_cloudfront_distribution.png)

### METRICS

For more information about the metrics emitted by Amazon CloudFront, click here or visit the service's homepage at https://aws.amazon.com/cloudfront/.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
