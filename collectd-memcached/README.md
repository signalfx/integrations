---
title: Memcached collectd Plugin
brief: Memcached metrics for collectd.
---

# ![](https://github.com/signalfx/Integrations/blob/master/collectd-memcached/img/integrations_memcached.png) Memcached Plugin

_This is a directory consolidate all the metadata associated with the Memcached collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/memcached.c)_

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

1. Install the collectd plugin.

 ##### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/Integrations/tree/master/collectd).

 ##### RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following command to install this plugin:
 ```
 yum install collectd-memcached
 ```
1. Download SignalFx's [sample memcached configuration file](https://github.com/signalfx/Integrations/blob/master/collectd-memcached/10-memcached.conf)

 Modify the sample configuration file to provide values that make sense for your environment, as described in the header.

1. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file you downloaded in step 2:
 ```
 include '/path/to/10-memcached.conf'
 ```
1. Restart collectd.

Metrics from memcached will begin streaming into SignalFx, and new built-in dashboards will be created for you. Check the status of your new integration on the Integrations page.


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

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/memcached.c)
