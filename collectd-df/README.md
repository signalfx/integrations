---
title: collectd df Plugin
brief: Disk Free metrics for collectd.
---

# DF (Disk Free) Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:DF):

The DF plugin collects file system usage information, i. e. basically how much space on a mounted partition is used and how much is available. It's named after and very similar to the df(1) UNIX command that's been around forever.
However, not all "partitions" are of interest. For example /proc and /dev usually don't get filled and their "size" doesn't make a lot of sense. That's why the DF plugin offers to select only specific devices, mount points or filesystem types.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

- collectd 3.6+

### INSTALLATION

This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

### CONFIGURATION

#### Optional configuration

The following configuration options are *optional*. You may specify them in the configuration file in order to override default values provided by the plugin.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| FSType | Include specific filesystem types | "ext3" |
| IgnoreSelected  | Ignore the designation of specific filesystem types | false |

### USAGE

The primary use of this plugin is to track the available space on the systems filesystems. This can be used to set alerts and thresholds to avoid a filesystem from being filled to capacity.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This plugin is released under the Apache 2.0 license. See LICENSE for more details.
