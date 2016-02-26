---
title: plugin_instance
brief: Plugin Instance Dimension
---
### plugin_instance

> Plugin Instance

This dimension is sent in with most metrics from collectd.  Its meaning is
varied between each plugin but generally indicates what source the metric is
referring to.  e.g. each mount point for the df plugin.  You can also use it
to encode other dimensions in.  More Information can be found [here](https://support.signalfx.com/hc/en-us/articles/203773189-Recognize-collectd-metrics-in-SignalFx).

This plugin simply sends "example" after all decodings is done.
