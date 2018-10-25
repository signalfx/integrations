# ![](./img/integration_awssqs.png) Amazon Simple Queue Service (SQS)

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Amazon Simple Queue Service (SQS) via [Amazon Web Services](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

#### FEATURES

##### Built-in dashboards

- **SQS Queues**: Overview of all data from SQS.

  [<img src='./img/dashboard_sqs_queues.png' width=200px>](./img/dashboard_sqs_queues.png)

- **SQS Queue**: Focus on a single SQS queue.

  [<img src='./img/dashboard_sqs_queue.png' width=200px>](./img/dashboard_sqs_queue.png)

### INSTALLATION

To access this integration, [connect to CloudWatch](https://github.com/signalfx/integrations/tree/master/aws)[](sfx_link:aws).

By default, SignalFx will import all CloudWatch metrics that are available in your account. To retrieve metrics for a subset of available services or regions, modify the connection on the Integrations page.

### USAGE

SignalFx provides built-in dashboards for this service. Examples are shown below.

![](./img/dashboard_sqs_queues.png)

![](./img/dashboard_sqs_queue.png)

### METRICS

For more information about the metrics emitted by Amazon Simple Queue Service, visit the service's homepage at <a target="_blank" href="https://aws.amazon.com/sqs/">https://aws.amazon.com/sqs/</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
