---
title: Memory collectd Plugin
brief: Memory plugin for collectd.
---

#![](https://github.com/signalfx/Integrations/blob/master/collectd/img/integrations_collectd.png) Memory collectd Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Memory):

> The Memory plugin collects physical memory utilization.
The values are reported by their use by the operating system. Under Linux, the categories are:

> * Used
 * Buffered
 * Cached
 * Free

> Free memory is memory you paid for, that's using power and that doesn't do anything useful. It is normal that the operating system puts that memory to use, for example by caching files it has accessed (reported as Cached under Linux).

> Virtual memory statistics can be collected with the [vmem plugin](https://github.com/signalfx/Integrations/tree/master/collectd-vmem) under Linux.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd |  1.0+ |

### INSTALLATION

This plugin is included with [SignalFx collectd](https://github.com/signalfx/Integrations/tree/master/collectd).

### CONFIGURATION

No configuration is required for this plugin.

### USAGE

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/memory.c)
