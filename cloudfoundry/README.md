# ![](././img/integrations_cloudfoundry.png) Pivotal Cloud Foundry

_This directory consolidates all the metadata associated with the **Pivotal Cloud Foundry Integration**. The relevant code for the integration can be found [here](https://github.com/signalfx/cloudfoundry-integration)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use this integration to monitor a Pivotal Cloud Foundry deployment. This integration provides metrics about the performance of the various components that make up Pivotal Cloud Foundry.

#### FEATURES

##### Infrastructure Page

- **Infrastructure Navigator**: On the Infrastructure page in SignalFx, the Infrastructure Navigator visualizes Cloud Foundry instances as squares, colored by metrics including CPU, disk, and network. Additional views are provided for focus on the health and performance of specific Cloud Foundry services. [Click here to read more about the Infrastructure Page](http://docs.signalfx.com/en/latest/built-in-content/host-nav.html). 

  [<img src='./img/infra_pcf_instances.png' width=200px>](./img/infra_pcf_instances.png)

##### Built-in dashboards

This integration includes built-in dashboards listed under **Pivotal Cloud Foundry** on the Dashboards page in SignalFx. A sample include:

- **Cloud Foundry Overview**: Overview of all activity in your Cloud Foundry environment.
  
  [<img src='./img/dashboard_cloud_foundry_overview.png' width=200px>](./img/dashboard_cloud_foundry_overview.png)

- **Cloud Foundry Instance**: Focus on a single Cloud Foundry instance.
  
  [<img src='./img/dashboard_cloud_foundry_instance.png' width=200px>](./img/dashboard_cloud_foundry_instance.png)

### REQUIREMENTS AND DEPENDENCIES

This integration requires administrative access to a Pivotal Cloud Foundry deployment with the JMX Bridge installed. Pivotal Web Services is not supported. Versions known to work are:

| Software                | Version        |
|-------------------------|----------------|
| Pivotal Ops Manager     | 1.9.1+ |
| Pivotal Elastic Runtime | 1.9.0+ |
| Pivotal JMX Bridge      | 1.8.11+ |

### INSTALLATION

Follow these steps to enable this integration:

1. Download the product file from [Pivotal Network](https://network.pivotal.io) or from [SignalFx's Github repository](https://github.com/signalfx/cloudfoundry-integration/releases/download/v0.9.0/signalfx-agent-0.9.0.pivotal).

1. Navigate to the Ops Manager Installation Dashboard and click "Import a Product" to upload the product file. 

1. Under "Import a Product", click "+" next to the version number of SignalFx Monitoring and Alerting for PCF. This adds the tile to your staging area.

1. Click the newly added SignalFx Monitoring and Alerting for PCF tile.

1. In the SignalFx section, enter your SignalFx [access token](http://docs.signalfx.com/en/latest/admin-guide/tokens.html#tokens). Leave the SignalFx ingestion URL unchanged.

1. In the Pivotal JMX Bridge section, copy configuration values from the JMX Bridge tile. 

  1. To find the JMX IP Address, select the JMX Bridge tile in PCF Ops Manager and choose the Status tab. Copy the IP address from the job called "JMX Provider". 

  1. To find JMX username, JMX password, and (if applicable) JMX SSL certificate, select the JMX Bridge tile in PCF Ops Manager and choose the "Settings" tab. Select the "JMX Provider" section, then copy over the JMX credentials and SSL certificate. 

1. Click Save.

1. Return to the Ops Manager Installation Dashboard and click "Apply Changes" to install the SignalFx Monitoring and Alerting for PCF tile.

Metrics from Pivotal Cloud Foundry will begin streaming into SignalFx. 

#### Troubleshooting

If metrics from Pivotal Cloud Foundry don't appear in SignalFx after more than a few minutes, check the following:

* Verify that the values in the Pivotal JMX Bridge settings section of the SignalFx tile match the settings of the JMX Bridge tile.

* Check the logs of the deployed SignalFx Agent for errors, such as connection issues to the JMX Bridge, SSL certificate errors with the JMX Bridge, or errors reporting metrics to SignalFx. 

* Ensure that the app called signalfx-agent is running. 
  1. Log into [Pivotal Apps Manager](https://docs.pivotal.io/pivotalcf/1-9/customizing/console-login.html). 
  1. Inside the space signalfx-agent-space there will be an app named `signalfx-agent`. 
  1. Ensure that `signalfx-agent` is in the "running" state. 

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/collectd-example/blob/master/LICENSE) for more details.
