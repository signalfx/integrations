# ![](./img/integration_awsecs.png) Amazon EC2 Container Service (ECS)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon EC2 Container Service (ECS) via [Amazon CloudWatch](https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.amazon.cloudwatch.html).

#### FEATURES

##### Built-in dashboards

- **ECS**: Overview of all data from ECS.

  [<img src='./img/dashboard_ecs_overview.png' width=200px>](./img/dashboard_ecs_overview.png)

- **ECS Cluster**: Focus on a single ECS cluster.

  [<img src='./img/dashboard_ecs_cluster.png' width=200px>](./img/dashboard_ecs_cluster.png)

- **ECS Service**: Focus on a single ECS service.

  [<img src='./img/dashboard_ecs_service.png' width=200px>](./img/dashboard_ecs_service.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.amazon.cloudwatch.html). 

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page.

### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below.

![](./img/dashboard_ecs_overview.png)

![](./img/dashboard_ecs_cluster.png)

![](./img/dashboard_ecs_service.png)

### METRICS

For more information about the metrics emitted by Amazon EC2 Container Service, visit the service's homepage at https://aws.amazon.com/ecs/.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
