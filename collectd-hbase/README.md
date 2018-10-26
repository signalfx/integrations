# ![](https://github.com/signalfx/integrations/blob/master/collectd-hbase/img/integrations_hbase.png) HBase collectd Plugin

Metadata associated with the HBase collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd-hbase">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/java.c">here</a>.

- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9+  |
| java collectd plugin | 4.9+ |

### INSTALLATION

1. Install the <a target="_blank" href="https://collectd.org/wiki/index.php/Plugin:GenericJMX">Java plugin</a>.

    * RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09. Run the following command to install the Java plugin for collectd:

            yum install collectd-java


    * Ubuntu 12.04, 14.04, 16.04 & Debian 7, 8:
      - This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/integrations/tree/master/collectd).

2. Download SignalFx's sample JMX configuration file and sample Cassandra configuration file from the following URLs:

    * <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf">JMX.conf</a>

    * <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-hbase/20-hbase.conf">hbase.conf</a>

3. Modify <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-hbase/20-hbase.conf">hbase.conf</a> to provide values that make sense for your environment, as described in the header.

    * Add the following lines to /etc/collectd.conf, replacing the example paths with the locations of the configuration files you downloaded in step 2:

            include '/path/to/10-jmx.conf'
            include '/path/to/20-hbase.conf'

4. Restart collectd.

Metrics from HBase will begin streaming into SignalFx.

### CONFIGURATION

#### System modifications:



You must include <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf">JMX.conf</a> this ensures that the Java collectd plugin will properly run prior to loading the Cassandra specific configuration.

| Value | Description |
|-------|-------------|
| ServiceURL | URL of your JMX application|
| Host | The name of your host (_Please leave the identifier `[hostHasService=hbase]` in the host name)_|


### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
