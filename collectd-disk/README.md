---
title: collectd disk Plugin
brief: Disk metrics for collectd.
---

# Disk Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Disk):

The Disk plugin collects performance statistics of hard-disks and, where supported, partitions. While the “octets” and “operations” are quite straight forward, the other two datasets need a little explanation:
 * `merged` are the number of operations, that could be merged into other, already queued operations, i. e. one physical disk access served two or more logical operations. Of course, the higher that number, the better.
 * `time` is the average time an I/O-operation took to complete. Since this is a little messy to calculate take the actual values with a grain of salt.
Since 5.5 there are also additional metrics on the Linux platform:
 * `io_time` - time spent doing I/Os (ms). You can treat this metric as a device load percentage (Value of 1 sec time spent matches 100% of load).
 * `weighted_io_time` - measure of both I/O completion time and the backlog that may be accumulating.
 * `pending_operations` - shows queue size of pending I/O operations.
For details about these metrics you can also read [kernel documentation](https://www.kernel.org/doc/Documentation/iostats.txt) (Explanations of fields "Field 9", "Field 10" and "Field 11").

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

- collectd 1.5+

### INSTALLATION

This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

### CONFIGURATION

#### Optional configuration

The following configuration options are *optional*. You may specify them in the configuration file in order to override default values provided by the plugin.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| Disk | Include specific Disk(s) | "sda" "/^hd/" |
| IgnoreSelected  | Ignore the designation of specific Disks | false |

### USAGE

The primary use of this plugin is to track the available space on the systems filesystems. This can be used to set alerts and thresholds to avoid a filesystem from being filled to capacity.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This plugin is released under the Apache 2.0 license as part of collectd
