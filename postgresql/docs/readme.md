---
title: Postgresql Metrics
brief: Metrics collected from Postgresql
---
### Postgresql Metrics

This document describes the Postgresql metrics as reported by SignalFx.

collectd-postgresql is preconfigured with basic postgresql statistics query [(postgresql_default.conf)](https://github.com/signalfx/collectd/blob/master/src/postgresql_default.conf) which utilizes the statistics available in postgres documented [here](http://www.postgresql.org/docs/9.3/static/monitoring-stats.html).

### Requirements

This plugin needs `postgresql` collectd plugin.  You need to configure and enable it as documented in [collectd plugin manual](https://collectd.org/wiki/index.php/Plugin:PostgreSQL).

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.5 or later  |
| Redis     |  9.3           |
