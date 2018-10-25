# ![](./img/integration_awsopsworks.png) AWS OpsWorks

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor AWS OpsWorks via [Amazon Web Services](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

#### FEATURES

##### Built-in dashboards

- **OpsWorks (a)**: Overview of all data from OpsWorks.

  [<img src='./img/dashboard_opsworks_a.png' width=200px>](./img/dashboard_opsworks_a.png)

- **OpsWorks**: Focus on a single OpsWorks instance, layer or stack.

  [<img src='./img/dashboard_opsworks_instance.png' width=200px>](./img/dashboard_opsworks_instance.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page.

### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below.

![](./img/dashboard_opsworks_a.png)

![](./img/dashboard_opsworks_instance.png)

### METRICS

For more information about the metrics emitted by AWS OpsWorks, visit the service's homepage at <a target="_blank" href="https://aws.amazon.com/opsworks/">https://aws.amazon.com/opsworks/</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
