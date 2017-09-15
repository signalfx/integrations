# ![](https://github.com/signalfx/integrations/blob/master/collectd-memcached/img/integrations_memcached.png) Memcached

This is a directory that consolidates all the metadata associated with the Memcached plugin for collectd. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/memcached.c).

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use the Memcached plugin for collectd to monitor the following types of information from a Memcached node:

* request information (including hits, misses & evictions)
* current connections
* net input/output bytes
* number of items cached

Documentation for Memcached can be found here: [https://github.com/memcached/memcached/wiki](https://github.com/memcached/memcached/wiki)

#### FEATURES

##### Built-in dashboards

- **Memcached (a)**: Overview of data from all Memcached hosts.

  [<img src='./img/dashboard_memcached_a.png' width=200px>](./img/dashboard_memcached_a.png)

- **Memcached**: Focus on a single Memcached host.

  [<img src='./img/dashboard_memcached.png' width=200px>](./img/dashboard_memcached.png)

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.2 or later  |
| memcached |  1.1 or later  |

### INSTALLATION

1. Download SignalFx's [sample memcached configuration file](https://github.com/signalfx/integrations/blob/master/collectd-memcached/10-memcached.conf) to `/etc/collectd/managed_config`.

2. Modify the sample configuration file to provide values that make sense for your environment, as described in [Configuration](#configuration), below.

3. Restart collectd.

### CONFIGURATION

Using the example configuration file [10-memcached.conf](https://github.com/signalfx/integrations/tree/master/collectd-memcached/10-memcached.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the Memcached instance to be monitored.

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| Host | Hostname at which collectd can connect to Memcached. | 127.0.0.1 |
| Port | Port at which collectd can connect to Memcached. | 11211 |

### USAGE

Sample of pre-built dashboard in SignalFx:

![](././img/dashboard_memcached.png)

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
