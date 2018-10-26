# ![](./img/integration_awsalb.png) Amazon Application Load Balancing (ALB)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Application Load Balancing (ALB) via [Amazon Web Services](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

#### FEATURES

##### Built-in dashboards

- **ApplicationELB Instances**: Overview of all data from ALB.

  [<img src='./img/dashboard_alb_instances.png' width=200px>](./img/dashboard_alb_instances.png)

- **ApplicationELB Instance**: Focus on a single ALB load balancer.

  [<img src='./img/dashboard_alb_instance.png' width=200px>](./img/dashboard_alb_instance.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page.

### USAGE

#### Uniquely identifying ALBs

SignalFx synthesizes a unique ID for each ALB in the dimension `AWSUniqueId`.

### METRICS

For more information about the metrics emitted by Application Load Balancing, visit the service's homepage at <a target="_blank" href="https://aws.amazon.com/elasticloadbalancing/">https://aws.amazon.com/elasticloadbalancing/</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
