# ![](./img/integration_googlecloudspanner.png) Google Cloud Spanner

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Google Cloud Spanner via [Google Cloud Platform](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

#### FEATURES

##### Built-in dashboards

- **Spanner Overview**: Overview of project level metrics for Google Cloud Spanner

  [<img src='./img/spanner_overview.png' width=200px>](./img/spanner_overview.png)

- **Spanner Instance**: Metrics for a single instance of Google Cloud Spanner

  [<img src='./img/spanner_instance.png' width=200px>](./img/spanner_instance.png)


### INSTALLATION

To access this integration, [connect to Google Cloud Platform](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

### USAGE

#### Interpreting Built-in dashboards

**Spanner Instance**

- **API Sent Bytes by Method** - Rate at which uncompressed response bytes sent by Cloud Spanner grouped by method.

  [<img src='./img/instance-api-sent.png' width=200px>](./img/instance-api-sent.png)

- **API Received Bytes by Method** - Rate at which uncompressed response bytes received by Cloud Spanner grouped by method.

  [<img src='./img/instance-api-received.png' width=200px>](./img/instance-api-received.png)

- **Instance CPU Utilization** - CPU utilization of the instance.

  [<img src='./img/instance-cpu-utilization.png' width=200px>](./img/instance-cpu-utilization.png)

- **API Request Count by Method** - Rate of Cloud Spanner API requests grouped by method.

  [<img src='./img/instance-api-req-count.png' width=200px>](./img/instance-api-req-count.png)

- **Storage Used** - Storage used in bytes by the instance.

**Spanner Overview**

- **Node Count** - Total number nodes in the project.

  [<img src='./img/overview-node-count.png' width=200px>](./img/overview-node-count.png)

- **CPU Utilization** - Utilization of provisioned CPU by all instances.

  [<img src='./img/overview-cpu-utilization.png' width=200px>](./img/overview-cpu-utilization.png)

- **Sent Bytes** - Rate at which uncompressed response bytes are sent by Cloud Spanner.

  [<img src='./img/overview-sent-bytes.png' width=200px>](./img/overview-sent-bytes.png)

- **Received Bytes** - Rate at which uncompressed response bytes are received by Cloud Spanner.

  [<img src='./img/overview-received-bytes.png' width=200px>](./img/overview-received-bytes.png)

- **Request Count** - Rate of Cloud Spanner API requests.

  [<img src='./img/overview-req-count.png' width=200px>](./img/overview-req-count.png)

- **Storage Used** - Storage used in bytes by Cloud Spanner.

  [<img src='./img/overview-storage-used.png' width=200px>](./img/overview-storage-used.png)


### METRICS

For more information about the metrics emitted by Google Cloud Spanner, visit the service's metric page at <a target="_blank" href="https://cloud.google.com/monitoring/api/metrics#gcp-spanner">https://cloud.google.com/monitoring/api/metrics#gcp-spanner</a>

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
