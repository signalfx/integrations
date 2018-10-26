# ![](./img/integration_googlebigtable.png) Google Cloud Bigtable

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Google Cloud Bigtable via [Google Cloud Platform](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

#### FEATURES

##### Built-in dashboards

- **Bigtable Overview**: Overview of project level metrics for Google Cloud Bigtable.

  [<img src='./img/bigtable_overview.png' width=200px>](./img/bigtable_overview.png)

- **Bigtable Cluster**: Overview of a cluster metrics for Google Cloud Bigtable.

  [<img src='./img/bigtable_cluster.png' width=200px>](./img/bigtable_cluster.png)

- **Bigtable Table**: A table level look at metrics for Google Cloud Bigtable.

  [<img src='./img/bigtable_table.png' width=200px>](./img/bigtable_table.png)

### INSTALLATION

To access this integration, [connect to Google Cloud Platform](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

### USAGE

**BigTable Cluster**

- **Node Count** - Number of nodes in the cluster.

  [<img src='./img/cluster-node-count.png' width=200px>](./img/cluster-node-count.png)

- **Cluster Disk Bytes Used** - Amount of compressed data stored in a cluster.

  [<img src='./img/cluster-disk-bytes-used.png' width=200px>](./img/cluster-disk-bytes-used.png)

- **Cluster Disk Load** - Utilization of HDD disks in a cluster.

  [<img src='./img/cluster-disk-load.png' width=200px>](./img/cluster-disk-load.png)

- **Server Error Count per Table** - Number of server requests for a table that failed with an error aggregated by Table.

  [<img src='./img/cluster-error-count-per-table.png' width=200px>](./img/cluster-error-count-per-table.png)

- **Server Latency(ms) per Table** - Distribution of server request latencies aggregated by Table.

  [<img src='./img/cluster-server-latency-per-table.png' width=200px>](./img/cluster-server-latency-per-table.png)

- **Cluster CPU Load** - CPU load of the cluster.

  [<img src='./img/cluster-cpu-load.png' width=200px>](./img/cluster-cpu-load.png)

- **Modified Rows / min per Table** - Rate at which rows are modified aggregated by table.

  [<img src='./img/cluster-modified-rows-per-table.png' width=200px>](./img/cluster-modified-rows-per-table.png)

- **Returned Rows / min per Table** - Rate at which rows are returned by server requests aggregated by table.

  [<img src='./img/cluster-returned-rows-per-table.png' width=200px>](./img/cluster-returned-rows-per-table.png)

- **Requests / min per Table** - Rate at which server makes requests aggregated by table.

  [<img src='./img/cluster-reqs-table.png' width=200px>](./img/cluster-reqs-table.png)

- **Received Bytes per Table** - Rate of uncompressed bytes of response data received by servers.

  [<img src='./img/cluster-received-bytes-table.png' width=200px>](./img/cluster-received-bytes-table.png)

- **Sent Bytes per Table** - Rate of uncompressed bytes of response data sent by servers.

  [<img src='./img/cluster-sent-bytes-table.png' width=200px>](./img/cluster-sent-bytes-table.png)

**BigTable Overview**

- **Number of Clusters** - Number of clusters.

  [<img src='./img/overview-number-of-clusters.png' width=200px>](./img/overview-number-of-clusters.png)

- **Nodes per Cluster** - Number of nodes aggregated by cluster.

  [<img src='./img/overview-nodes-per-cluster.png' width=200px>](./img/overview-nodes-per-cluster.png)

- **Top Cluster CPU Load** - Top 5 clusters based on CPU load.

  [<img src='./img/overview-top-cluster-cpu-load.png' width=200px>](./img/overview-top-cluster-cpu-load.png)

- **Top Disk Bytes Used Per Cluster** - Top 5 clusters based on disk bytes used.

  [<img src='./img/overview-top-disk-per-cluster.png' width=200px>](./img/overview-top-disk-per-cluster.png)

- **Average Server Latency(ms) Per Cluster** - Average server latency aggregated by cluster.

  [<img src='./img/overview-avg-server-latency-cluster.png' width=200px>](./img/overview-avg-server-latency-cluster.png)

- **Error Counts per Cluster** - Error counts aggregated by cluster.

  [<img src='./img/overview-error-counts-per-cluster.png' width=200px>](./img/overview-error-counts-per-cluster.png)

- **Top Number of Requests / min per Cluster** - Clusters with top 5 rate of requests.

  [<img src='./img/overview-number-of-reqs-per-cluster.png' width=200px>](./img/overview-number-of-reqs-per-cluster.png)

- **Top Number of Rows Returned / min per Cluster** - Clusters with top 5 rate of rows returned by server requests.

  [<img src='./img/overview-rows-per-cluster.png' width=200px>](./img/overview-rows-per-cluster.png)

- **Top Number of Rows Modified / min per Cluster** - Clusters with top 5 rate of rows modified by server requests.

  [<img src='./img/overview-rows-modified-per-cluster.png' width=200px>](./img/overview-rows-modified-per-cluster.png)

- **Bytes Received per Cluster** - Rate of uncompressed bytes of response data received by servers aggregated by cluster.

  [<img src='./img/overview-bytes-received-cluster.png' width=200px>](./img/cluster-received-bytes-table.png)

- **Bytes Sent per Table** - Rate of uncompressed bytes of response data sent by servers aggregated by cluster.

  [<img src='./img/overview-bytes-sent-cluster.png' width=200px>](./img/overview-bytes-sent-cluster.png)

**BigTable Table**

- **Average Request Latency (ms)** - Average latency of server requests for a table.

  [<img src='./img/table-avg-req-latency.png' width=200px>](./img/table-avg-req-latency.png)

- **Average Request Latency (ms) Trend** - Trend of average latency of server requests for a table.

  [<img src='./img/table-req-latency-trend.png' width=200px>](./img/table-req-latency-trend.png)

- **Requests / min per Method** - Rate of server requests aggregated by method for the table.

  [<img src='./img/table-req-per-method.png' width=200px>](./img/table-req-per-method.png)

- **Rows Returned / min by Resquest** - Rate at which rows are returned by server requests aggregated by request.

  [<img src='./img/table-rows-returned-by-request.png' width=200px>](./img/table-rows-returned-by-request.png)

- **Modified Rows / min by Resquest** - Rate at which rows are modified by server requests aggregated by request.

  [<img src='./img/table-modified-rows-by-request.png' width=200px>](./img/table-modified-rows-by-request.png)

- **Server Bytes Received** - Rate of uncompressed bytes of response data received by servers.

  [<img src='./img/table-server-bytes-received.png' width=200px>](./img/table-server-bytes-received.png)

- **Server Bytes Sent** - Rate of uncompressed bytes of response data sent by servers.

  [<img src='./img/table-server-bytes-sent.png' width=200px>](./img/table-server-bytes-sent.png)

- **Server Errors** - Number of server requests for the table that failed with an error.

  [<img src='./img/table-server-errors.png' width=200px>](./img/table-server-errors.png)

- **Disk Bytes Used** - Amount of disk used by the table

### METRICS

For more information about the metrics emitted by Google Cloud Bigtable, visit the service's metric page at <a target="_blank" href="https://cloud.google.com/monitoring/api/metrics#gcp-bigtable">https://cloud.google.com/monitoring/api/metrics#gcp-bigtable</a>

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
