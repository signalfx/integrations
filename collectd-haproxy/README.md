---
title: HaProxy Metrics
brief: Metrics collected from HaProxy 1.5 or above
---

# HAProxy collectd Plugin   

_This is a directory consolidate all the metadata associated with the HAProxy collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd-haproxy)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use the [collectd-haproxy](https://github.com/signalfx/collectd-haproxy) collectd plugin to collect metrics about HaProxy. An example config file for collecting data about HaProxy using this plugin can be found in our [collectd configs repo](https://github.com/signalfx/integrations/blob/master/collectd-haproxy/10-haproxy.conf).

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| haproxy  | 1.5 or later |

### INSTALLATION

Follow these steps to install and configure this plugin:

1. Install the plugin.

  **Ubuntu 12.04, 14.04, & 15.04 and Debian 7 & 8:**

  This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

  **RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09**:

  Run the following command to install this plugin:

         yum install collectd-haproxy


1. Download SignalFx's [sample configuration file](./10-haproxy.conf) for this plugin.
1. Modify the sample configuration file as described in [Configuration](#configuration), below.
1. Add the following line to `/etc/collectd.conf`, replacing the example path with the location of the configuration file:

         include '/path/to/10-haproxy.conf'

1. Restart collectd.

### CONFIGURATION

Change the Socket parameter to point to the haproxy socket file. The location of the file is defined in the haproxy config file. Here is the example:

```
global
    daemon
    stats socket /var/run/haproxy.sock
    stats timeout 2m
```

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| Socket | This is the location of the HAProxy socket file | `Socket "/var/run/haproxy.sock"` |
| ProxyMonitor | list all the pxname(s) or svname(s) that you want to monitor | <ui><li>ProxyMonitor "http-in"</li><li>ProxyMonitor "server1"</li><li>ProxyMonitor "backend"</li></ui> |

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This plugin is released under the following [LICENSE](https://github.com/signalfx/collectd-haproxy/blob/master/LICENSE).
