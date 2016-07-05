---
title: Amazon Route 53
brief: SignalFx's integration with Amazon Route 53
---

# Amazon Route 53

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon Route 53 via Amazon CloudWatch. 

#### FEATURES

##### Built-in dashboards

- **Route53**: Overview of all data from Route 53.
  
  [<img src='./img/dashboard_route53.png' width=200px>](./img/dashboard_route53.png)

- **Route53 HealthCheck**: Focus on a single Route 53 health check.
  
  [<img src='./img/dashboard_route53_healthcheck.png' width=200px>](./img/dashboard_route53_healthcheck.png)

### INSTALLATION

To access this integration, connect to CloudWatch on the SignalFx Integrations page. 

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page. 

### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below. 

![](./img/dashboard_route53.png)

![](./img/dashboard_route53_healthcheck.png)

### METRICS

For more information about the metrics emitted by Amazon Route 53, click here or visit the service's homepage at https://aws.amazon.com/route53/.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
