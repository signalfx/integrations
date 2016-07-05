---
title: Amazon ELB
brief: SignalFx's integration with Elastic Load Balancing (ELB)
---

# Elastic Load Balancing (ELB)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Elastic Load Balancing (ELB) via Amazon CloudWatch. 

#### FEATURES

##### Built-in dashboards

- **ELB Instances**: Overview of all data from ELB.
  
  [<img src='./img/dashboard_elb_instances.png' width=200px>](./img/dashboard_elb_instances.png)

- **ELB Instance**: Focus on a single ELB load balancer.
  
  [<img src='./img/dashboard_elb_instance.png' width=200px>](./img/dashboard_elb_instance.png)

### INSTALLATION

To access this integration, connect to CloudWatch on the SignalFx Integrations page. 

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page. 

### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below. 

![](./img/dashboard_elb_instances.png)

![](./img/dashboard_elb_instance.png)

### METRICS

For more information about the metrics emitted by Elastic Load Balancing, click here or visit the service's homepage at https://aws.amazon.com/elasticloadbalancing/.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
