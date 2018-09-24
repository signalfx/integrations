---
title: plugin_instance
brief: Plugin Instance Dimension
---
### plugin_instance

> Plugin Instance

This dimension is sent in with most metrics from collectd.  Its meaning varies between plugins, but generally indicates which specific data source the metric is
referring to. For example, the plugin `df` uses `plugin_instance` to encode each mount point.  You can also use it to encode additional dimensions, as demonstrated by [dimension.frequency](./dimension.frequency.md).  More information can be found [here](http://docs.signalfx.com/en/latest/integrations/collectd-info.html#using-collectd-metrics).

After all decoding is complete, the value of `plugin_instance` for this plugin is just "example".
