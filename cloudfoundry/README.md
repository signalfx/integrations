# ![](././img/integrations_cloudfoundry.png) Pivotal Cloud Foundry

_This directory consolidates all the metadata associated with the **Pivotal Cloud Foundry Integration**. The relevant code for the integration can be found [here](https://github.com/signalfx/cloudfoundry-integration)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use this integration to monitor a Pivotal Cloud Foundry deployment. This integration provides metrics about the performance of the various components that make up Pivotal Cloud Foundry.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires administrative access to a Pivotal Cloud Foundry deployment with the JMX Bridge installed. Pivotal Web Services is not supported. Versions known to work are:

| Software                | Version        |
|-------------------------|----------------|
| Pivotal Ops Manager     |    1.9.1+      |
| Pivotal Elastic Runtime |    1.9.0+      |
| Pivotal JMX Bridge      |    1.8.11+     |

### INSTALLATION

Follow these steps to enable this integration:

1. Install the [JMX Bridge](https://network.pivotal.io/products/ops-metrics/) tile on your Pivotal Cloud Foundry instance and configure it by following the [Pivotal documentation](https://docs.pivotal.io/jmx-bridge/index.html).
2. If you just installed JMX Bridge for the first time apply your changes in Ops Manager before continuing so that you will know the IP address of the deployed JMX Bridge for later use.
3. Install the SignalFx Agent tile:
    1. Download the [SignalFx Agent tile](https://github.com/signalfx/cloudfoundry-integration/releases/download/v1.0.0/signalfx-agent-1.0.0.pivotal) to your local machine.
    2. Log into your Ops Manager instance.
    3. Click **Import a Product** and select the SignalFx Agent tile previously downloaded.
4. Configure the SignalFx Agent as described [below](#configuration).
5. Apply changes in Ops Manager to deploy and configure the SignalFx Agent.

### CONFIGURATION

Configure the SignalFx Agent by logging into Ops Manager and clicking the **SignalFx Agent** tile. There are two sections that must be configured before deploying.

Under the **SignalFx** section enter your SignalFx access key. The ingestion URL should be left as the default.

Under the **Pivotal JMX Bridge** section configure the IP of the deployed JMX Bridge. You can find the IP address of your JMX Bridge instance by selecting the **JMX Bridge** tile in Ops Manager and then selecting the **Status** tab. Use the IP from the **JMX Provider** job. Configure the remaining options by entering the configuration values you used when you configured JMX Bridge.

### USAGE

Sample of pre-built dashboard in SignalFx:
![](././img/example_dashboard.png)

#### TROUBLESHOOTING

If after deploying data is not appearing in SignalFx check the logs of the deployed SignalFx Agent. You can do this by logging into **Pivotal Apps Manager**. Inside the space named signalfx-agent-space there will be an app named signalfx-agent. Ensure that it is in the running state. Next examine the logs for clues, such as connection issues to the JMX Bridge, SSL certificate errors with the JMX Bridge, or errors reporting metrics to SignalFx. Check that the JMX configuration in SignalFx matches the JMX Bridge configuration.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/collectd-example/blob/master/LICENSE) for more details.
