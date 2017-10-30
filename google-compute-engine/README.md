# ![](./img/integration_googlecomputeengine.png) Google Compute Engine

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Google Compute Engine via [Google Stackdriver](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

#### FEATURES

##### Built-in dashboards

- **Compute Instances**: Overview of all data from Google Compute Engine.

  [<img src='./img/compute_instances.png' width=200px>](./img/compute_instances.png)

- **Compute Instance**: Focus on a single EC2 instance.

  [<img src='./img/compute_instance.png' width=200px>](./img/compute_instance.png)

### INSTALLATION

To access this integration, [connect to Stackdriver](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

### USAGE

#### METRICS
| Metric Name | Description |
|-------------|-------------|
| instance/disk/throttled_read_bytes_count | Delta count of bytes in throttled read operations. |
| instance/cpu/reserved_cores | Number of cores reserved on the host of the instance. |
| instance/network/received_packets_count | Delta count of packets received from the network. |
| firewall/dropped_bytes_count | Delta count of incoming bytes dropped by the firewall. |
| instance/cpu/usage_time | Delta CPU usage for all cores, in seconds. To compute the per-core CPU utilization fraction, divide this value by (end-start)*N, where end and start define this value's time interval and N is `compute.googleapis.com/instance/cpu/reserved_cores` at the end of the interval. |
| instance/disk/throttled_read_ops_count | Delta count of throttled read operations. |
| instance/disk/throttled_write_bytes_count | Delta count of bytes in throttled write operations. |
| instance/disk/write_bytes_count | Delta count of bytes written to disk. |
| instance/uptime | How long the VM has been running, in seconds. |
| instance/network/sent_bytes_count | Delta count of bytes sent over the network. |
| firewall/dropped_packets_count | Delta count of incoming packets dropped by the firewall. |
| instance/disk/read_bytes_count | Delta count of bytes read from disk. |
| instance/disk/read_ops_count | Delta count of disk read IO operations. |
| instance/disk/throttled_write_ops_count | Delta count of throttled write operations. |
| instance/network/sent_packets_count | Delta count of packets sent over the network. |
| instance/disk/write_ops_count | Delta count of disk write IO operations. |
| instance/network/received_bytes_count | Delta count of bytes received from the network. |
| instance/cpu/utilization | The fraction of the allocated CPU that is currently in use on the instance. This value can be greater than 1.0 on some machine types that allow bursting. |


For more information about the metrics emitted by Google Compute Engine, visit the service's metric page at https://cloud.google.com/monitoring/api/metrics#gcp-compute

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
