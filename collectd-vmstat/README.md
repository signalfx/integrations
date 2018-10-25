# VMStat

Metadata associated with the VMStat plugin for collectd can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-vmstat">here</a>.  The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/vmstat-collectd">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION
A collectd python based plugin for collecting metrics from VMStat

#### Features
##### Built-in dashboards
At this time there are no built in dashboards.  You may find metrics reported by this plugin in the catalog.

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software | Version      |
|----------|--------------|
| collectd | 5.0 or later |
| Python   | 2.6 or later |
| vmstat  |   |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |

### INSTALLATION
1.  Ensure that vmstat is installed on the host.
2.  Download the <a target="_blank" href="https://github.com/signalfx/vmstat-collectd">vmstat-collectd</a> Python module
3.  Place the contents of the repo in /usr/share/collectd/vmstat-collectd
4.  Download SignalFx’s [sample configuration file](./10-vmstat.conf) for this plugin to `/etc/collectd/managed_config`.
5.  Modify the configuration file to provide values that make sense for your environment, as described in [Configuration](#configuration) below.
6.  Restart collectd.

### CONFIGURATION
Using the example configuration file <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-vmstat/10-vmstat.conf">10-vmstat.conf</a> as a guide, provide values for the configuration options listed below that make sense for your environment.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/usr/share/collectd/vmstat-collectd" |
| Import | Path to the name of the pythom module with out the .py extension | `vmstat_collectd` |
| Path | Path to the vmstat executable | "/usr/bin/vmstat" |
| Verbose | Turns on verbose log statements | false |
| Include | Explicit list of metrics to report.  If no metrics are specified to be included then all metrics will be reported. | `"r", "b", "swpd", "free", "buff", "cache", "inact", "active", "si", "so", "bi", "bo", "in", "cs", "us", "sy", "id", "wa", "st"`|

### Usage
All metrics reported by the VMStat collectd plugin will contain the following dimensions:
* `host` will contain the hostname (as known by collectd) of the machine reporting the metrics.
* `plugin` is always set to `vmstat`.
* `plugin_instance` will always be `vmstat`.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is licensed under the MIT license.  See [LICENSE](./LICENSE)
