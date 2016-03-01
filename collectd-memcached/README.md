---
title: collectd Memcached Plugin
brief: Memcached metrics for collectd.
---

# Memcached Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx Memcached plugin. Follow these instructions to install the Memcached plugin for collectd. This will send data about Memcached to SignalFx, enabling built-in Memcached monitoring dashboards.

Use this plugin to monitor the following types of information from a Memcached node:

* request information (including hits, misses & evictions)
* current connections
* net input/output bytes
* number of items cached

Original Memcached Documentation https://code.google.com/p/memcached/wiki/NewStart

### REQUIREMENTS AND DEPENDENCIES


#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.2 or later  |
| memcached |  1.1 or later  |

### INSTALLATION

1. Install the Java plugin.

 RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following command to install the Java plugin for collectd:

 ```
 yum install collectd-java
 ```
 Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

1. Download SignalFx's sample JMX configuration file and sample Kafka configuration file from the following URLs:

 [JMX.conf](https://github.com/signalfx/Integrations/collectd-jmx/10-jmx.conf)
 [kafka-conf](https://github.com/signalfx/Integrations/collectd-kafka/20-kafka.conf)

 *Note: If you're using Kafka v0.8.2, download this sample Kafka configuration file instead:*
 [kafka.conf](https://github.com/signalfx/Integrations/collectd-kafka/20-kafka_82.conf)

1. Modify the configuration file providing values that make sense for your environment, as described [below](#configuration).

1. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file you downloaded in step 3:
 ```
 include '/path/to/10-jmx.conf'
  include '/path/to/20-kafka.conf'
 ```
or
 ```
 include '/path/to/10-jmx.conf'
  include '/path/to/20-kafka_82.conf'
 ```

1. Restart collectd.

collectd will begin emitting metrics from elasticsearch.

### CONFIGURATION

* Make sure ServiceURL points to your jmx app.
* Modify the "Host" parameter to what you want your source name to be.
* Please leave the identifier [hostHasService=kafka] in the hostname.

### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Chart images demonstrating each important condition or failure mode

### METRICS

For full documentation of the metrics and dimensions emitted by this plugin, see the `docs` directory in this repository.

### LICENSE

This plugin is released under the Apache 2.0 license. See LICENSE for more details.
