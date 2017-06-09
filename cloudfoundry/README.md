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

- **Cloud Foundry Architecture**: Focus on a single Cloud Foundry instance.
  
  [<img src='./img/dashboard_cloud_foundry_instance.png' width=200px>](./img/dashboard_cloud_foundry_instance.png)

### REQUIREMENTS AND DEPENDENCIES

This integration requires administrative access to a Pivotal Cloud Foundry deployment. Pivotal Web Services is not supported. Versions known to work are:

| Software                | Version        |
|-------------------------|----------------|
| Pivotal Ops Manager     | 1.9.1+ |
| Pivotal Elastic Runtime | 1.9.0+ |

### INSTALLATION

Follow these steps to enable this integration:

1. Download the product file from [Pivotal Network](https://network.pivotal.io/products/signalfx-monitoring-alerting/).

1. Follow the [installation instructions for the tile](http://docs.pivotal.io/partners/signalfx/installing.html).

Metrics from Pivotal Cloud Foundry should begin streaming into SignalFx.

To monitor services running within **Garden containers** (e.g. webservers) you will
need to use [our buildpack
decorator](https://github.com/signalfx/signalfx-cloudfoundry-buildpack-decorator)
along with the CF meta-buildpack.

To get our agent on to your own **BOSH deployments**, you can use [our BOSH
release](https://github.com/signalfx/agent-boshrelease).

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/collectd-example/blob/master/LICENSE) for more details.
