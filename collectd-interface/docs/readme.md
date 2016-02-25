---
title: Network Interface Metrics
brief: Metrics collected from physical and virtual network interfaces.
---
### Network Interface Metrics

Use the [collectd:Interface plugin](https://collectd.org/wiki/index.php/Plugin:Interface) to collect 
the following types of metrics from physical and virtual network interfaces on the host.

* Bytes (octets) transmitted and received (total, or per second)
* Packets transmitted and received (total, or per second)
* Interface errors (total, or per second)

### Dimensions associated with plugin:interface metrics
* **host**: host/server from which this metric is being collected, e.g. 'i-1234abcd' or 'myappserver'.
* **plugin_instance**: represents the interface name, e.g. 'eth0'. If there are multiple network
interfaces on the host, there will be multiple values of plugin_instance for the same host (one for each
network interface).
