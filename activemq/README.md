# ![](./img/integrations_activemq.png) ActiveMQ

Metadata associated with SignalFx's integration with ActiveMQ can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/activemq">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/activemq-integration">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

#### FEATURES

##### Built-in dashboards

- **ActiveMQ Hosts**: Overview of all data from ActiveMQ hosts.

  [<img src='./img/dashboard_activemq_hosts.png' width=200px>](./img/dashboard_activemq_hosts.png)

- **ActiveMQ Host**: Focus on a single ActiveMQ host.

  [<img src='./img/dashboard_activemq_host.png' width=200px>](./img/dashboard_activemq_host.png)

- **ActiveMQ Queue**: Focus on a single ActiveMQ queue.

  [<img src='./img/dashboard_activemq_queue.png' width=200px>](./img/dashboard_activemq_queue.png)

- **ActiveMQ Topic**: Focus on a single ActiveMQ topic.

  [<img src='./img/dashboard_activemq_topic.png' width=200px>](./img/dashboard_activemq_topic.png)

- **ActiveMQ Message Age**: (if enabled) Shows the average age of messages in ActiveMQ queues. See [ActiveMQ message age listener](https://github.com/signalfx/integrations/tree/master/amq-message-age)[](sfx_link:amq-message-age).

  [<img src='./img/dashboard_activemq_messageage.png' width=200px>](./img/dashboard_activemq_messageage.png)

### REQUIREMENTS AND DEPENDENCIES

| Software    | Version        |
|-------------|----------------|
| Smart Agent |       *        |
| ActiveMQ    | 5.8.0 or later |

### USAGE

Sample of built-in dashboard in SignalFx:

![](././img/dashboard_activemq.png)

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
