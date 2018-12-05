# ![](./img/integration_googleclouddatastore.png) Google Cloud Datastore

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Google Cloud Datastore via [Google Cloud Platform](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

#### FEATURES

##### Built-in dashboards

- **Datastore Overview**: Overview of project level metrics for Google Datastore

  [<img src='./img/datastore_overview.png' width=200px>](./img/datastore_overview.png)


### INSTALLATION

To access this integration, [connect to Google Cloud Platform](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

### USAGE

#### Interpreting Built-in dashboards

**Datastore Overview**

- **Read Sizes by Type of Read** - Average sizes of read entities by type.

  [<img src='./img/datastore-overview-read-sizes-type.png' width=200px>](./img/datastore-overview-read-sizes-type.png)

- **Number of Requests per API Method Call** - Number of requests made by method.

  [<img src='./img/datastore-overview-number-of-requests-per-method.png' width=200px>](./img/datastore-overview-number-of-requests-per-method.png)

- **Number of Writes** - Number of Datastore index writes.

  [<img src='./img/datastore-overview-number-of-writes.png' width=200px>](./img/datastore-overview-number-of-writes.png)

- **Write Sizes by Operation Type** - Average size of written entites by operation.

  [<img src='./img/datastore-overview-read-sizes-type.png' width=200px>](./img/datastore-overview-read-sizes-type.png)

### METRICS

For more information about the metrics emitted by Google Cloud Datastore, visit the service's metric page at <a target="_blank" href="https://cloud.google.com/monitoring/api/metrics#gcp-datastore">https://cloud.google.com/monitoring/api/metrics#gcp-datastore</a>

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
