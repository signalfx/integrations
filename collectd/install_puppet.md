# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_puppet.png)INSTALL WITH PUPPET

## Overview

There are three Puppet modules for SignalFx:

| Module name | Description |
|------------|--------------|
|[puppet_install_collectd](https://github.com/signalfx/puppet_install_collectd) [puppet module](https://forge.puppetlabs.com/signalfx/install_collectd) | Install and stay up-to-date with SignalFx's latest build of collectd. |
|[configure_collectd_plugins](https://github.com/signalfx/puppet_configure_collectd_plugins) [puppet module](https://forge.puppetlabs.com/signalfx/configure_collectd_plugins) | Enable and configure a set of collectd plugins that work well with SignalFx.|
|[send_collectd_metrics](https://github.com/signalfx/puppet_send_collectd_metrics) [puppet module](https://forge.puppetlabs.com/signalfx/send_collectd_metrics) | Configure collectd to send metrics to SignalFx.|

## Setup - `puppet_install_collectd`

Install the latest release of install_collectd module from SignalFx using:

```shell
puppet module install signalfx/install_collectd
```

### What install_collectd affects

The install_collectd module only installs SignalFx's latest build of collectd on your system. SignalFx provides additional modules to configure collectd plugins and send metrics to SignalFx. See [Module Description](#module-description).

## Usage

Install_collectd module accepts various parameters:

**1. ensure**

 Default value of ensure is present. There are three supported cases:  
 1. If your system does not have any existing collectd, the default value, 'present' allows the module to install the latest collectd packages from SignalFx repositories.  
 1. If you want to install only a specific version of collectd, you can set 'version' as this parameter's value. For example, set ensure as '5.5.0-sfx3~trusty' to get the exact specified version.  
 1. If your system already has collectd, you have to change this value to 'latest' to get the newest version. (Remember to change this value back to present once you have updated all your nodes, else, puppet will be automatically updating your collectd version as new packages are released by SignalFx)  

**2. ppa**  

 This optional variable applies to Ubuntu systems. It allows the module to use your local repository(cloned from SignalFx) for collectd packages. Default value is appropriate up-to-date ppa hosted by SignalFx.

 ```shell
 class { 'install_collectd':
  ensure       => "present",
  ppa          => 'ppa:signalfx/collectd-release',
  debian_ppa   => "deb https://dl.signalfx.com/debs/collectd/jessie/release /",
  purge        => undef,
  recurse      => undef,
  purge_config => false
 }
 ```

**3. debian_ppa**

 This optional variable applies to Debian GNU/Linux 7 and 8. It allows the module to use your local repository(cloned from SignalFx) for collectd packages. Default value is appropriate up-to-date ppa hosted by SignalFx.

**4. others**

 Set purge, recurse and purge_config to true to delete your existing collectd folders in case 1.3 and install just the latest version of collectd. The default values for purge, recurse and purge_config are undef, undef and false respectively.

## Limitations

Currently, the supported operating systems are
  1. Ubuntu 12.04
  1. Ubuntu 14.04
  1. Ubuntu 15.04
  1. CentOS 6
  1. CentOS 7
  1. Amazon Linux 2014.09
  1. Amazon Linux 2015.03
  1. Amazon Linux 2015.09
  1. Debian GNU/Linux 7 (wheezy)
  1. Debian GNU/Linux 8 (jessie)

## Configure - `configure_collectd_plugins`

Install the latest release of configure_collectd_plugins module from SignalFx using:

  ```shell
  puppet module install signalfx/configure_collectd_plugins
  ```

### What configure_collectd_plugins affects

The configure_collectd_plugins module configures an existing instance of collectd to collect useful and interesting system metrics. You must have collectd installed in order to use this module.

SignalFx provides additional modules to install collectd and send metrics to SignalFx. See [Module Description](#module-description).

## Usage

The configure_collectd_plugins module accepts parameters that enable or disable each of the plugins that it configures. The default value for all parameters is 'present'. To disable data collection by a plugin, change the value of its named parameter to 'absent'.

```shell
  class { 'configure_collectd_plugins':
      log_file => present,
      aggregation => present,
      chain => present,
      cpu => present,
      cpufreq => present,
      df => present,
      load => present,
      memory => present,
      uptime => present,
      disk => present,
      interface => present,
      protocols => present,
      vmem => present
  }
```

You can also use this module to install collectd plugins to monitor third-party software. To install a plugin, add its configuration snippet to your manifest file, and replace default configuration values with values that make sense for your environment as necessary.

### Apache

  ```shell
  class { 'configure_collectd_plugins::plugins::apache':
    instanceName  => 'myapacheinstance',
    url           => 'http://localhost/mod_status?auto'
  }
  ```

|Parameter | Description|
|----------|------------|
|  instanceName | Appears as the dimension `plugin_instance` in SignalFx. |
|  url | The URL at which the plugin can read the output of Apache's mod_status module. |

### Cassandra

```shell
  class { 'configure_collectd_plugins::plugins::cassandra':
    hostname => $::hostname
  }
```

|  Parameter | Description|
|----------|------------|
|  hostname | The name of the host running Cassandra. |

### Docker

```shell
  include 'configure_collectd_plugins::plugins::docker'
```

### Elasticsearch

```shell
  class { 'configure_collectd_plugins::plugins::elasticsearch':
    clustername         => 'elasticsearch',
    indexes             => '_all'
  }
```

|Parameter | Description|
|----------|------------|
|  clustername | Appears as the dimension `plugin_instance` in SignalFx. |
|  indexes | Indexes to monitor using this plugin. All indexes are monitored by default.

### Kafka version 0.8.2.1 and up

```shell
  class { 'configure_collectd_plugins::plugins::kafka_82':
    hostname => $::hostname
  }
```

|Parameter | Description|
|----------|------------|
|  hostname | The name of the host running Kafka. |

### Memcached

```shell
  class { 'configure_collectd_plugins::plugins::memcached':
    hostname => '127.0.0.1',
    port     => '11211'
  }
```

|Parameter | Description|
|----------|------------|
|  hostname | Name of the host on which memcached is running.|
|  port | Port on which memcached is running. |

### MySQL

```shell
  class { 'configure_collectd_plugins::plugins::mysql':
    hostname,
    user,
    password,
    database
  }
```

|Parameter | Description|
|----------|------------|
|  hostname | Name of the host on which MySQL is running.|
|  user | Username that collectd can use to connect to MySQL.|
|  password | Password that collectd can use to connect to MySQL.|
|  database | Name of the MySQL database to monitor. |

### Nginx

```shell
  class { 'configure_collectd_plugins::plugins::nginx':
    url => 'http://localhost:80/nginx_status'
  }
```

|Parameter | Description|
|----------|------------|
|  url | The URL at which collectd can read the output of nginx's stub status module. |

### PostgreSQL

```shell
  class { 'configure_collectd_plugins::plugins::postgresql':
    hostname,
    user,
    password
  }
```

|  Parameter | Description|
|----------|------------|
|  hostname | Name of the host on which PostgreSQL is running.|
|  user | Username that collectd can use to connect to PostgreSQL.|
|  password | Password that collectd can use to connect to PostgreSQL.|

### Redis Master

```shell
  class { 'configure_collectd_plugins::plugins::redis_master':
    hostname,
    port
  }
```

Use this configuration for Redis masters.

|  Parameter | Description|
|----------|------------|
|  hostname | Name of the host on which Redis is running.|
|  port | Port on which Redis is running. |

### Redis Slave

```shell
  class { 'configure_collectd_plugins::plugins::redis_slave':
    hostname,
    port
  }
```

Use this configuration for Redis slaves.

|  Parameter | Description|
|----------|------------|
|  hostname | Name of the host on which Redis is running.|
|  port | Port on which Redis is running. |

### Varnish

```shell
  class { 'configure_collectd_plugins::plugins::varnish':
    hostname,
    port
  }
```

|  Parameter | Description|
|----------|------------|
|  hostname | Name of the host on which Varnish is running.|
|  port | Port on which Varnish is running. |

### Zookeeper

```shell
  include 'configure_collectd_plugins::plugins::zookeeper'
```

## Send Metrics - `send_collectd_metrics`

Install the latest release of send_collectd_metrics module from SignalFx using:

```shell
puppet module install signalfx/send_collectd_metrics
```

### What send_collectd_metrics affects

The send_collectd_metrics module configures collectd's write_http plugin to send metrics to SignalFx. You must have collectd installed in order to use this module.

SignalFx provides additional modules to install collectd and configure data collection plugins. See [Overview](#overview).

## Usage

The send_collectd_metrics module accepts parameters to configure the write_http plugin as follows:

```shell
class {'send_collectd_metrics':
    api_token             => "<YOUR-API-TOKEN>",
    dimension_list        => {"key" => "value"},
    aws_integration       => true,
    signalfx_url          => "https://ingest.signalfx.com/v1/collectd",
    write_http_timeout    => 3000,
    write_http_buffersize => 4096,
    ensure_plugin_version => present,
    ppa                   => "ppa:signalfx/collectd-plugin-release",
    debian_ppa            => "deb https://dl.signalfx.com/debs/signalfx-collectd-plugin/jessie/release /",
}
```

|Parameter name | Description |
|---------------|--------------|
|api_token | Provide your SignalFx API token in this parameter to send data to SignalFx. |
|dimension_list | Use the dimension_list hash map to set custom dimensions on all of the metrics that collectd sends to SignalFx. For example, you can use a custom dimension to indicate that one of your servers is running Kafka by including it in the hash map as follows: `dimension_list => {"serverType" => "kafka"}`|
|aws_integration | This parameter controls AWS metadata syncing to SignalFx. Default is true. To disable AWS metadata syncing, set this parameter to false.|
|signalfx_url | If you use a proxy to send metrics to SignalFx, replace this parameter with the URL of your proxy.|
|write_http_timeout | sets Timeout option of write_http plugin of collectd. Default value is 3000.|
|write_http_buffersize | sets BufferSize option of write_http plugin of collectd. Default value is 4096.|
|ensure_plugin_version | This parameter controls the version of signalfx plugin installation. You can specify "latest" if you want to update your plugin. You can also specify "\<version-number\>" to get the exact version from your local PPA. Default value is present.|
|ppa | Change this value if you want to install the signalfx plugin from your local PPA. Applies only to Ubuntu systems. Default value is appropriate up-to-date ppa hosted by SignalFx.|
|debian_ppa | Change this value if you want to install the signalfx plugin from your local PPA. Applies only to Debian GNU/Linux 7 and 8 systems. Default value is appropriate up-to-date ppa hosted by SignalFx.|
