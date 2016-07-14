---
title: Amazon RDS
brief: SignalFx's integration with Amazon Relational Database Service (RDS)
---

# Amazon Relational Database Service (RDS)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon Relational Database Service (RDS) via [Amazon CloudWatch](../aws)<!-- sfx_link:aws -->. 

#### FEATURES

##### Built-in dashboards

- **RDS Instances**: Overview of all data from RDS.
  
  [<img src='./img/dashboard_rds_instances.png' width=200px>](./img/dashboard_rds_instances.png)

- **RDS Instance**: Focus on a single RDS instance.
  
  [<img src='./img/dashboard_rds_instance.png' width=200px>](./img/dashboard_rds_instance.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](../aws)<!-- sfx_link:aws --> on the SignalFx Integrations page. 

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page. 

### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below. 

![](./img/dashboard_rds_instances.png)

![](./img/dashboard_rds_instance.png)

### METRICS

For more information about the metrics emitted by Amazon Relational Database Service, click here or visit the service's homepage at https://aws.amazon.com/rds/.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
