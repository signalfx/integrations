---
title: Docker Metrics
brief: Metrics collected from docker containers.
---
### Docker Metrics

The
[`docker-collectd-plugin`](https://github.com/lebauce/docker-collectd-plugin)
collects metrics about the Docker containers running on the system using
Docker's stats API. It reports metrics about the CPU utilization of each
container, their memory consumption, and their network and disk
activity.

### Installation

To install the Docker collectd plugin, follow the instructions from its
[README.md](https://github.com/lebauce/docker-collectd-plugin/tree/master/README.md).

### Metric dimensions used by this plugin

All metrics reported by the Docker collectd plugin will contain the
following dimensions:

* `host` will contain the hostname (as known by collectd) of the machine
  reporting the metrics
* `plugin` is always set to `docker`
* `plugin_instance` will contain the name of the container the metrics
  are from. The container name is used because that's usually a more
  stable value than the container ID, which changes on every restart

### Version information

| Software | Version      |
|----------|--------------|
| collectd | 5.x or later |
| Python   | 2.6 or later |
| Docker   | 1.5 or later |
