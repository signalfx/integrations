---
title: collectd Cassandra Plugin
brief: Cassandra metrics for collectd.
---

# ![](https://github.com/signalfx/Integrations/blob/master/collectd-cassandra/img/integrations_cassandra.png) Cassandra collectd Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Follow these instructions to configure the Java plugin for collectd to monitor Cassandra. This will send data about Cassandra to SignalFx, enabling built-in Cassandra monitoring dashboards.

Use this plugin to monitor the following types of information from Cassandra nodes:

* read/write/range-slice requests
* read/write/range-slice errors (timeouts and unavailable)
* read/write/range-slice latency (median, 99th percentile, maximum)
* compaction activity
* hint activity

### REQUIREMENTS AND DEPENDENCIES

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9+  |
| java collectd plugin | 4.9+ |
| cassandra | 2.0.10+ |


### INSTALLATION

1. Install the [Java plugin](https://collectd.org/wiki/index.php/Plugin:GenericJMX).

 RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following command to install the Java plugin for collectd:

 ```
 yum install collectd-java
 ```
 Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/Integrations/tree/master/collectd).

1. Download SignalFx's sample JMX configuration file and sample Cassandra configuration file from the following URLs:

 [`JMX.conf`](https://github.com/signalfx/Integrations/blob/master/collectd-java/10-jmx.conf)

 [`cassandra.conf`](https://github.com/signalfx/Integrations/blob/master/collectd-cassandra/20-cassandra.conf)

1. Modify [`cassandra.conf`](https://github.com/signalfx/Integrations/blob/master/collectd-cassandra/20-cassandra.conf) to provide values that make sense for your environment, as described in the header.

 Add the following lines to /etc/collectd.conf, replacing the example paths with the locations of the configuration files you downloaded in step 2:
 ```
 include '/path/to/10-jmx.conf'
 include '/path/to/20-cassandra.conf'
 ```
1. Restart collectd.

Metrics from Cassandra will begin streaming into SignalFx, and new built-in dashboards will be created for you. Check the status of your new integration on the Integrations page.

### CONFIGURATION

#### System modifications:

Open the JMX port on your cassandra app. Cassandra will listen for connections on port 8080 (port 7199 starting in 0.8.0-beta1). More information can be found at the [Cassandra Project site](http://wiki.apache.org/cassandra/JmxInterface). There is also a page covering a few [common issues](http://wiki.apache.org/cassandra/JmxGotchas).

#### [`cassandra.conf`](https://github.com/signalfx/Integrations/blob/master/collectd-cassandra/20-cassandra.conf) file modifications:

You must include [10-jmx.conf]() this ensures that the Java collectd plugin will properly run prior to loading the Cassandra specific configuration.

| Value | Description |
|-------|-------------|
| ServiceURL | URL of your JMX application|
| Host | The name of your host (_Please leave the identifier `[hostHasService=cassandra]`) in the host name_|

### USAGE

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

Since this is not an actual _plugin_ but rather a configuration of the `collectd-java plugin` there is no need for a license.
