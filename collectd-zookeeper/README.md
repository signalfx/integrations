---
title: Zookeeper Plugin
brief: Zookeeper plugin for collectd.
---

# ![](https://github.com/signalfx/Integrations/blob/master/collectd-zookeeper/img/integrations_zookeeper.png) Zookeeper collectd Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is a collectd plugin for getting metrics and information from
[ZooKeeper](http://zookeeper.apache.org) servers. Based off the ZooKeeper monitoring script
[check_zookeeper.py](https://svn.apache.org/repos/asf/zookeeper/trunk/src/contrib/monitoring/check_zookeeper.py).

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

- collectd 4.9+
- Python plugin for collectd (included with SignalFx collectd)
- Python 2.6+
- Zookeeper 3.4.0+

 #### Note:
 - Requires ZooKeeper 3.4.0 or greater in order to use the `mntr` [four letter word command](http://zookeeper.apache.org/doc/trunk/zookeeperAdmin.html#sc_zkCommands).
 - If support for earlier versions is needed, add `srvr` command, available in since 3.3.0, or `stat` (fetches extra uneeded data but available pre-3.3).


### INSTALLATION

1. Install the Python plugin for collectd.

 ##### RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following command to install the Python plugin for collectd:
 ```
 yum install collectd-python
 ```
 ##### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

1. Download the Python module from the following URL:

 https://github.com/signalfx/collectd-zookeeper

1. Download SignalFx’s [sample configuration file](https://github.com/signalfx/Integrations/collectd-elasticsearch/20-zookeeper.conf).

1. Modify the configuration file as follows:

 1. Modify the fields “TypesDB and “ModulePath” to point to the location on disk where you downloaded the Python module in step 2.

 1. Provide values that make sense for your environment, as described [below](#configuration).

1. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file you downloaded in step 4:
 ```
 include '/path/to/20-zookeeper.conf'
 ```
1. Restart collectd.

collectd will begin emitting metrics from Zookeeper.

### CONFIGURATION

| Setting            | Description     | Default|
|--------------------|-----------------|-----------|
|Hosts | host name where Zookeeper is running| `"localhost"`|
|Port| port number for Zookeeper  | `2181`|
|Instance | Specify a cluster name | none (commented out)|


### USAGE


### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This plugin is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/collectd-zookeeper/blob/master/LICENSE) for more details.
