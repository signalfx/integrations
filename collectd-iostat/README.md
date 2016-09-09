# IOStat

_This directory consolidates all the metadata associated with the IOStat plugin for collectd.  The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd-iostat-python)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION
A collectd python based plugin for collecting metrics from IOStat

#### Features
##### Built-in dashboards
At this time there are no built in dashboards.  You may find metrics reported by this plugin in the catalog

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software | Version      |
|----------|--------------|
| collectd | 5.0 or later |
| Python   | 2.6 or later |
| systat  | 10.0.3 or later |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |

### INSTALLATION
1.  Ensure that systat is installed on the host
2.  Download the [collectd-iostat-python](https://github.com/signalfx/collectd-iostat-python) Python module.
3.  Download SignalFx’s [sample configuration file](./10-iostat.conf) for this plugin to `/etc/collectd/managed_config`.
4.  Modify the configuration file to provide values that make sense for your environment, as described in [Configuration](#configuration) below.
5.  Restart collectd.

### CONFIGURATION
Using the example configuration file [10-iostat.conf](https://github.com/signalfx/integrations/tree/master/collectd-iostat/10-iostat.conf) as a guide, provide values for the configuration options listed below that make sense for your environment.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| TypesDB | Path on disk where collectd can find the Types.db file included in this module. | "/usr/share/collectd/collectd-iostat-python/iostat_types.db" |
| ModulePath | Path on disk where collectd can find this module. | "/usr/share/collectd/collectd-iostat-python" |
| Import | Path to the name of the pythom module with out the .py extension | `collectd_iostat_python` |
| Path | Path to the iostat executable | "/usr/bin/iostat" |
| Interval  | The interval for collectd to invoke the read callback of the IOStat plugin.  If unset, the default value is 60 seconds | 2 |
| Verbose | Turns on verbose log statements | false |
| NiceNames | Turns on nice descriptive names for each IOStat metric, rather than using the IOStat column headers.  Please note that if NiceNames are used, then the MB and kB values are converted to bytes.  i.e. `kB_read` is converted to `bytes` | True |
| Include | Explicit list of metrics to report.  If no metrics are specified to be included then all metrics will be reported. | `"avg_request_queue", "avg_request_size", "avg_service_time", "avg_wait_time", "avg_wait_time.read", "avg_wait_time.write", "bytes.read", "bytes.write", "bytes_per_second.read", "bytes_per_second.write", "percent.util", "requests_merged_per_second.read", "requests_merged_per_second.write", "requests_per_second.read", "requests_per_second.write", "transfers_per_second" "tps", "Blk_read/s", "kB_read/s", "MB_read/s", "Blk_wrtn/s", "kB_wrtn/s", "MB_wrtn/s", "Blk_read", "kB_read", "MB_read", "Blk_wrtn", "kB_wrtn", "MB_wrtn", "rrqm/s", "wrqm/s", "r/s", "w/s", "rsec/s", "rkB/s", "rMB/s", "wsec/s", "wkB/s", "wMB/s", "avgrq-sz", "avgqu-sz", "await", "r_await", "w_await", "svctm", "%util"`|

### Usage
All metrics reported by the IOStat collectd plugin will contain the following dimensions:
* `host` will contain the hostname (as known by collectd) of the machine reporting the metrics.
* `plugin` is always set to `iostat`.
* `plugin_instance` will contain the name of the disk the metrics relevant to.

### METRICS
For full documentation of the metrics and dimensions emitted by this plugin, see the `docs` directory in this repository.

### LICENSE

This integration is licensed under the MIT license.  See [LICENSE](./LICENSE)
