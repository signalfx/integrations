---
title: plugin_instance
brief: Plugin Instance Dimension
---
### plugin_instance

> Plugin Instance

This dimension is sent in with most metrics from collectd.  Its meaning varies between plugins, but generally indicates which specific data source the metric is
referring to. For example, the plugin `df` uses `plugin_instance` to encode each mount point.  You can also use it to encode additional dimensions, as demonstrated by [dimension.frequency](./dimension.frequency.md).  More information can be found [here](https://support.signalfx.com/hc/en-us/articles/203773189-Recognize-collectd-metrics-in-SignalFx).

After all decoding is complete, the value of `plugin_instance` for this plugin is just "example".
