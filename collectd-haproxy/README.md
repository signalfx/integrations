# HAProxy

_This directory consolidates all the metadata associated with the HAProxy collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd-haproxy)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use the [collectd-haproxy](https://github.com/signalfx/collectd-haproxy) collectd plugin to collect metrics about HaProxy. 

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| haproxy  | 1.5 or later |

### INSTALLATION

1. On RHEL/CentOS and Amazon Linux systems, run the following command to install this plugin:

         yum install collectd-haproxy
         
   On Ubuntu and Debian systems, this plugin is included by default with the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd). 
1. Download SignalFx's [sample configuration file](./10-haproxy.conf) for this plugin to `/etc/collectd/managed_config`.
1. Modify the sample configuration file as described in [Configuration](#configuration), below.
1. Restart collectd.

### CONFIGURATION

Using the example configuration file [`10-haproxy.conf`](././10-haproxy.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the HAProxy instance to be monitored.

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| Socket | Location of the HAProxy socket file | Socket "/var/run/haproxy.sock" |
| ProxyMonitor | A list of all the pxname(s) or svname(s) that you want to monitor | <ui><li>ProxyMonitor "http-in"</li><li>ProxyMonitor "server1"</li><li>ProxyMonitor "backend"</li></ui> |

The location of the HAProxy socket file is defined in the HAProxy config file, as in the following example:

```
global
    daemon
    stats socket /var/run/haproxy.sock
    stats timeout 2m
```


### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
