---
title: collectd HBase Plugin
brief: HBase metrics for collectd
---

# ![](https://github.com/signalfx/integrations/blob/master/collectd-hbase/img/integrations_hbase.png) HBase collectd Plugin

 _This is a directory consolidate all the metadata associated with the HBase collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/java.c)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION


### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9+  |
| java collectd plugin | 4.9+ |
| HBase | XXXXXXXXXXXX |


### INSTALLATION

1. Install the [Java plugin](https://collectd.org/wiki/index.php/Plugin:GenericJMX).

 RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following command to install the Java plugin for collectd:

 ```
 yum install collectd-java
 ```
 Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/integrations/tree/master/collectd).

1. Download SignalFx's sample JMX configuration file and sample Cassandra configuration file from the following URLs:

 [`JMX.conf`](https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf)

 [`hbase.conf`](https://github.com/signalfx/integrations/blob/master/collectd-hbase/20-hbase.conf)

1. Modify [`hbase.conf`](https://github.com/signalfx/integrations/blob/master/collectd-hbase/20-hbase.conf) to provide values that make sense for your environment, as described in the header.

 Add the following lines to /etc/collectd.conf, replacing the example paths with the locations of the configuration files you downloaded in step 2:
 ```
 include '/path/to/10-jmx.conf'
 include '/path/to/20-hbase.conf'
 ```
1. Restart collectd.

Metrics from HBase will begin streaming into SignalFx.

### CONFIGURATION

#### System modifications:



You must include [`JMX.conf`](https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf) this ensures that the Java collectd plugin will properly run prior to loading the Cassandra specific configuration.

| Value | Description |
|-------|-------------|
| ServiceURL | URL of your JMX application|
| Host | The name of your host (_Please leave the identifier `[hostHasService=hbase]`) in the host name_|

### USAGE


### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

Since this is not an actual _plugin_ but rather a configuration of the `collectd-java plugin` there is no need for a license.
