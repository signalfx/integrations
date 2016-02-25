---
title: Varnish Cache Metrics
brief: Metrics collected from Varnish 3.0+
---
### Varnish Cache Metrics

Use the [varnish](https://collectd.org/wiki/index.php/Plugin:Varnish) collectd
plugin to collect metrics about Varnish. An example config file for collecting
data about Varnish using this plugin can be found in our
[collectd configs repo](https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/10-varnish.conf).
The authoritative location for information about the exact meaning of varnish metrics
is in the Varnish repository inside file [vsc_f_main.h](https://github.com/varnish/Varnish-Cache/blob/master/include/tbl/vsc_f_main.h).
The source code for collectd's varnish integration is in the collectd repository
inside file [varnish.c](https://github.com/signalfx/collectd/blob/master/src/varnish.c).

Use this plugin to monitor the following types of information from Varnish caches:

* hit rate
* connection states
* worker thread counts
* bytes in/out
* shared memory operations
* uptime
* session operations

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| Varnish   | 3.0.0 or later |
