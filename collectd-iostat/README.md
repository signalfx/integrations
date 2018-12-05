# IOStat

Metadata associated with the IOStat plugin for collectd can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-iostat">here</a>.  The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/iostat-collectd-python">here</a>.

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
| sysstat  | 10.0.3 or later |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |

### INSTALLATION
1.  Ensure that sysstat is installed on the host.
2.  Download the <a target="_blank" href="https://github.com/signalfx/iostat-collectd-python">iostat-collectd-python</a> Python module.
3.  Place the contents of the repo in /usr/share/collectd/iostat-collectd-python
4.  Download SignalFx’s [sample configuration file](./10-iostat.conf) for this plugin to `/etc/collectd/managed_config`.
5.  Modify the configuration file to provide values that make sense for your environment, as described in [Configuration](#configuration) below.
6.  Restart collectd.

### CONFIGURATION
Using the example configuration file <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-iostat/10-iostat.conf">10-iostat.conf</a> as a guide, provide values for the configuration options listed below that make sense for your environment.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/usr/share/collectd/iostat-collectd-python" |
| Import | Path to the name of the pythom module with out the .py extension | `collectd_iostat_python` |
| Path | Path to the iostat executable | "/usr/bin/iostat" |
| Verbose | Turns on verbose log statements | false |
| Include | Explicit list of metrics to report.  If no metrics are specified to be included then all metrics will be reported. | `"tps", "Blk_read/s", "kB_read/s", "MB_read/s", "Blk_wrtn/s", "kB_wrtn/s", "MB_wrtn/s", "Blk_read", "kB_read", "MB_read", "Blk_wrtn", "kB_wrtn", "MB_wrtn", "rrqm/s", "wrqm/s", "r/s", "w/s", "rsec/s", "rkB/s", "rMB/s", "wsec/s", "wkB/s", "wMB/s", "avgrq-sz", "avgqu-sz", "await", "r_await", "w_await", "svctm", "%util"` |

### Usage
All metrics reported by the IOStat collectd plugin will contain the following dimensions:
* `host` will contain the hostname (as known by collectd) of the machine reporting the metrics.
* `plugin` is always set to `iostat`.
* `plugin_instance` will contain the name of the disk the metrics relevant to.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is licensed under the MIT license.  See [LICENSE](./LICENSE)
