---
title: Marathon Metrics API
brief: Metrics reported by the Marathon Metrics API
metric_type: gauge
---
### Marathon Metrics API

> Metrics reported by the Marathon Metrics API

The Marathon API offers a set of metrics that are reported by this plugin.
API Endpoint: `/metrics`

#### Counters
This plugin reports all "counters" as `gauge.<metric name>`.  The api does the counting for so the plugin is only reads and reports the counts as type "counter".

#### Gauges
This plugin reports all gauge metrics as `gauge.<metric name>`.

#### Meters
This plugin reports all metrics listed under "meters" as
`gauge.<metric name>.<unit>.per.<unit>`.
