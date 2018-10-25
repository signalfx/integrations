# ![](././img/integrations_pivotalcloudfoundry.png) Pivotal Cloud Foundry

Metadata associated with the **Pivotal Cloud Foundry Integration** can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/cloudfoundry-pivotal">here</a>. The relevant code for the integration can be found <a target="_blank" href="https://github.com/signalfx/cloudfoundry-integration">here</a>.

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

- **Infrastructure Navigator**: On the Infrastructure page in SignalFx, the
    Infrastructure Navigator visualizes Cloud Foundry instances as squares,
    colored by metrics including CPU, disk, and network. Additional views are
    provided for focus on the health and performance of specific Cloud Foundry
    services, as well as Garden Containers. <a target="_blank" href="https://docs.signalfx.com/en/latest/built-in-content/infra-nav.html">Click here to read more about the
    Infrastructure
    Page</a>.

  You can quickly see the status of all of the VMs in your Cloud Foundry cluster:

  [<img src='./img/arch-infra.png' width=200px>](./img/arch-infra.png)

  Here is a sample of the view for Garden Containers:

  [<img src='./img/garden-infra.png' width=200px>](./img/garden-infra.png)

##### Built-in dashboards

This integration includes built-in dashboards listed under **Cloud Foundry** on the Dashboards page in SignalFx. Here are some examples:

- **Key Capacity Scaling Indicators**: Helps you figure out whether you need to
    add resources to your cluster.

  [<img src='./img/key-cap-dashboard.png' width=200px>](./img/key-cap-dashboard.png)

- **Diego**: Metrics around Diego, including many KPIs

  [<img src='./img/diego-dashboard.png' width=200px>](./img/diego-dashboard.png)

- **Garden Containers**: High-level look at the Garden container system

  [<img src='./img/garden-containers-dashboard.png' width=200px>](./img/garden-containers-dashboard.png)

  And many more...

### REQUIREMENTS AND DEPENDENCIES

This integration requires administrative access to a Pivotal Cloud Foundry deployment. Pivotal Web Services is not supported. Versions known to work are:

| Software                | Version        |
|-------------------------|----------------|
| Pivotal Ops Manager     | 1.9.1+ |
| Pivotal Elastic Runtime | 1.9.0+ |

### INSTALLATION

Follow these steps to enable this integration:

1. Download the product file from <a target="_blank" href="https://network.pivotal.io/products/signalfx-monitoring-alerting/">Pivotal Network</a>.

2. Follow the <a target="_blank" href="http://docs.pivotal.io/partners/signalfx/installing.html">installation instructions for the tile</a>.

Metrics from Pivotal Cloud Foundry should begin streaming into SignalFx.

To monitor services running within **Garden containers** (e.g. webservers) you will
need to use <a target="_blank" href="https://github.com/signalfx/signalfx-cloudfoundry-buildpack-decorator">our buildpack decorator</a>
along with the CF meta-buildpack.

To get our agent on to your own **BOSH deployments**, you can use <a target="_blank" href="https://github.com/signalfx/agent-boshrelease">our BOSH
release</a>.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/collectd-example/blob/master/LICENSE) for more details.
