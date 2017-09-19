# ![](https://github.com/signalfx/integrations/blob/master/collectd-hbase/img/integrations_hbase.png) HBase collectd Plugin

This directory consolidates all the metadata associated with the HBase collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/java.c).

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

1. Install the [Java plugin](https://collectd.org/wiki/index.php/Plugin:GenericJMX).

    * RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09. Run the following command to install the Java plugin for collectd:

            yum install collectd-java


    * Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:
      - This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/integrations/tree/master/collectd).

2. Download SignalFx's sample JMX configuration file and sample Cassandra configuration file from the following URLs:

    * [JMX.conf](https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf)

    * [hbase.conf](https://github.com/signalfx/integrations/blob/master/collectd-hbase/20-hbase.conf)

3. Modify [hbase.conf](https://github.com/signalfx/integrations/blob/master/collectd-hbase/20-hbase.conf) to provide values that make sense for your environment, as described in the header.

    * Add the following lines to /etc/collectd.conf, replacing the example paths with the locations of the configuration files you downloaded in step 2:

            include '/path/to/10-jmx.conf'
            include '/path/to/20-hbase.conf'

4. Restart collectd.

Metrics from HBase will begin streaming into SignalFx.

### CONFIGURATION

#### System modifications:



You must include [JMX.conf](https://github.com/signalfx/integrations/blob/master/collectd-java/10-jmx.conf) this ensures that the Java collectd plugin will properly run prior to loading the Cassandra specific configuration.

| Value | Description |
|-------|-------------|
| ServiceURL | URL of your JMX application|
| Host | The name of your host (Please leave the identifier `[hostHasService=hbase]`) in the host name|

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
