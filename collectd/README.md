---
title: SignalFx collectd
brief: SignalFx validated version of collectd.
---

# SignalFx collectd Agent

_This is a directory consolidate all the metadata associated with the SignalFx collectd Agent. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation - shell script](#install-with-shell-script)
- [Installation - Puppet](#install-with-puppet)
- [Installation - CHEF](#install-with-chef)
- [License](#license)

## DESCRIPTION

SignalFx has always recommended the open-source data collection agent [collectd](http://collectd.org) to our customers, as it’s fast, performs well at scale, and enjoys great community support. We released a new [SignalFx collectd](https://github.com/signalfx/collectd) package to make a great agent even better.

**[SignalFx collectd agent](https://github.com/signalfx/collectd)** introduces the following changes:

* **Increased Character limit:** We’ve increased the number of characters that can be used in dimension key-value pairs to 1024, up from 64. In practice, this allows you to send as many dimensions as you want.
* **Buffer Flushing** To ensure that metrics always arrive in a timely manner, we’ve added a timer to SignalFx collectd so that it transmits data to SignalFx either when the data buffer is full or when a time limit is reached, whichever happens first. This capability is particularly useful if you are only collecting small quantities of time-sensitive metrics.
* **HTTP Error Logging** We’re providing greater visibility into how collectd itself is functioning, by logging HTTP codes from unsuccessful data transmissions by the write_http plugin, and by logging the name of every collectd plugin that is loaded at startup. In addition, we’re also updating the SignalFx metadata plugin for collectd to report the DPM transmitted by each collectd plugin installed on a host, to help you manage and keep track of your usage. Find this in the Catalog under the metric gauge.sf.host-dpm.

You can view the full [changelog](https://github.com/signalfx/collectd/blob/collectd-5.5.0-sfx/ChangeLog). All changes have also been submitted back to the [collectd project](http://collectd.org) so that everyone can benefit.

## REQUIREMENTS AND DEPENDENCIES

SignalFx has built an installation script for the following versions of Linux:

| Software  | Version        |
|-----------|----------------|
| Debian  | 7 & 8 |
| Ubuntu  | 12.04, 14.04 & 15.04 |
| RHEL/Centos | 6.x & 7.x |
| Amazon Linux | 2014.09 & 2015.03 |

To get started, you'll need your org's API token. To find it:

Open your SignalFx profile page at https://app.signalfx.com/#/myprofile.

Locate the words "API Token" on the page.

Click the link next to "API Token" that says "show". Your API token appears.

## INSTALL WITH SHELL SCRIPT

SignalFx provides a shell script that you can use to install our latest build of collectd, install and configure important plugins, and configure collectd to send metrics to SignalFx.

If you have already installed collectd, this script will install the SignalFx metadata plugin and configure collectd to send metrics to SignalFx.

Follow these instructions to use the script.

1. **Download and run the script**

 **note:** You must have administrator (sudo) privileges to run this script.

 Run the following command in your command-line, replacing API_TOKEN with your org's API token.
 ```
 sudo curl -sSL https://dl.signalfx.com/collectd-install | bash -s API_TOKEN
 ```
 This command will download and run the script. On startup, the script will ask you to confirm that you want to proceed.

1. **Provide your hostname**

 During the configuration of collectd, the script will ask you to provide collectd with your system's hostname.

 * Type 'dns' and press enter to automatically collect this system's hostname from DNS.
 * Type 'input' and press enter to provide the hostname yourself. When prompted, type in your desired hostname and press enter.

When the script successfully completes, it starts up collectd, which begins reporting metrics to SignalFx. If you encounter any errors see Troubleshooting below, or send us an email at support@signalfx.com.

## ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_puppet.png)INSTALL WITH PUPPET

### Overview

There are three Puppet modules for SignalFx:

| Module name | Description |
|------------|--------------|
|[puppet_install_collectd](https://github.com/signalfx/puppet_install_collectd) [puppet module](https://forge.puppetlabs.com/signalfx/install_collectd) | Install and stay up-to-date with SignalFx's latest build of collectd. |
|[configure_collectd_plugins](https://github.com/signalfx/puppet_configure_collectd_plugins) [puppet module](https://forge.puppetlabs.com/signalfx/configure_collectd_plugins) | Enable and configure a set of collectd plugins that work well with SignalFx.|
|[send_collectd_metrics](https://github.com/signalfx/puppet_send_collectd_metrics) [puppet module](https://forge.puppetlabs.com/signalfx/send_collectd_metrics) | Configure collectd to send metrics to SignalFx.|

### Setup - `puppet_install_collectd`

Install the latest release of install_collectd module from SignalFx using:

```shell
puppet module install signalfx/install_collectd
```

#### What install_collectd affects

The install_collectd module only installs SignalFx's latest build of collectd on your system. SignalFx provides additional modules to configure collectd plugins and send metrics to SignalFx. See [Module Description](#module-description).

### Usage

Install_collectd module accepts various parameters:

**1. ensure**
Default value of ensure is present. There are three supported cases:  
  1.1. If your system does not have any existing collectd, the default value, 'present' allows the module to install the latest collectd packages from SignalFx repositories.  
  1.2. If you want to install only a specific version of collectd, you can set 'version' as this parameter's value. For example, set ensure as '5.5.0-sfx3~trusty' to get the exact specified version.  
  1.3. If your system already has collectd, you have to change this value to 'latest' to get the newest version. (Remember to change this value back to present once you have updated all your nodes, else, puppet will be automatically updating your collectd version as new packages are released by SignalFx)  

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

### Limitations

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

### Configure - `configure_collectd_plugins`

Install the latest release of configure_collectd_plugins module from SignalFx using:
  ```shell
  puppet module install signalfx/configure_collectd_plugins
  ```

#### What configure_collectd_plugins affects

The configure_collectd_plugins module configures an existing instance of collectd to collect useful and interesting system metrics. You must have collectd installed in order to use this module.

SignalFx provides additional modules to install collectd and send metrics to SignalFx. See [Module Description](#module-description).

### Usage

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

##### Apache

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

##### Cassandra

```shell
  class { 'configure_collectd_plugins::plugins::cassandra':
    hostname => $::hostname
  }
```

|  Parameter | Description|
|----------|------------|
|  hostname | The name of the host running Cassandra. |

##### Docker

```shell
  include 'configure_collectd_plugins::plugins::docker'
```

##### Elasticsearch

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

##### Kafka version 0.8.2.1 and up

```shell
  class { 'configure_collectd_plugins::plugins::kafka_82':
    hostname => $::hostname
  }
```

|Parameter | Description|
|----------|------------|
|  hostname | The name of the host running Kafka. |

##### Memcached

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

##### MySQL

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

##### Nginx

```shell
  class { 'configure_collectd_plugins::plugins::nginx':
    url => 'http://localhost:80/nginx_status'
  }
```

|Parameter | Description|
|----------|------------|
|  url | The URL at which collectd can read the output of nginx's stub status module. |

##### PostgreSQL

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

##### Redis Master

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

##### Redis Slave

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

##### Varnish

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

##### Zookeeper

```shell
  include 'configure_collectd_plugins::plugins::zookeeper'
```

### Send Metrics - `send_collectd_metrics`

Install the latest release of send_collectd_metrics module from SignalFx using:

```shell
puppet module install signalfx/send_collectd_metrics
```

#### What send_collectd_metrics affects

The send_collectd_metrics module configures collectd's write_http plugin to send metrics to SignalFx. You must have collectd installed in order to use this module.

SignalFx provides additional modules to install collectd and configure data collection plugins. See [Overview](#overview).

#### Usage

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

## ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_chef.png)INSTALL WITH CHEF

Use this cookbook to install and configure collectd to send data to SignalFx. It can perform the following tasks:

- Install [SignalFx's build of collectd](https://github.com/signalfx/collectd), an open-source monitoring daemon.
- Install and configure [SignalFx's metadata plugin for collectd](https://github.com/signalfx/integrations/tree/master/collectd-signalfx)
- Configure collectd's [write_http plugin](https://github.com/signalfx/integrations/tree/master/collectd-write_http) to send data to SignalFx
- Install and configure collectd plugins for data collection from the following software:
  - [Apache webserver](https://github.com/signalfx/integrations/tree/master/collectd-apache)
  - [Docker](https://github.com/signalfx/integrations/tree/master/collectd-docker)
  - [Cassandra](https://github.com/signalfx/integrations/tree/master/collectd-cassandra)
  - [ElasticSearch](https://github.com/signalfx/integrations/tree/master/collectd-elasticsearch)
  - [Kafka](https://github.com/signalfx/integrations/tree/master/collectd-kafka)
  - [Memcached](https://github.com/signalfx/integrations/tree/master/collectd-memcached)
  - [MySQL](https://github.com/signalfx/integrations/tree/master/collectd-mysql)
  - [Nginx](https://github.com/signalfx/integrations/tree/master/collectd-nginx)
  - [Varnish](https://github.com/signalfx/integrations/tree/master/collectd-varnish)
  - [Zookeeper](https://github.com/signalfx/integrations/tree/master/collectd-zookeeper)
  - [Postgres](https://github.com/signalfx/integrations/tree/master/collectd-postgresql)
  - [Redis](https://github.com/signalfx/integrations/tree/master/collectd-redis)
  - [MongoDB](https://github.com/signalfx/integrations/tree/master/collectd-mongodb)

### System Requirements

This cookbook has been tested on the following operating systems:

* CentOS 6, 7;  
* Amazon Linux 1503, 1509;  
* Ubuntu 1504, 1404, 1204;  
* Debian GNU/Linux 7, 8;

### Cookbook dependencies

This cookbook requires the following cookbooks:

- apt (2.8.2)
- yum-epel (0.6.3)
- build-essential (2.2.4)
- yum (3.8.1)
- python (1.4.6)

### Usage

* Use the default recipe to install collectd, configure plugins, and configure collectd to send metrics to SignalFx.
* Use the individual collectd plugin recipes to install individual collectd plugins.

1. Install on your local machine

```
knife cookbook site install chef_install_configure_collectd
```

This command installs the chef_install_configure_collectd cookbook with all dependencies.

2. Supply your SignalFx API token.

In order to send data to SignalFx, you must provide a value for your SignalFx API token in `attributes/default.rb` as follows, replacing `YOUR_SIGNALFX_API_TOKEN` with the API token for your SignalFx organization:

```
default['write_http']['API_TOKEN'] = 'YOUR_SIGNALFX_API_TOKEN'
```

3. (Optional) Supply configuration for collectd and plugins.

This cookbook includes default configuration for collectd in `attributes/default.rb`, and for plugins in individually-named files in the attributes directory. Before using this cookbook to install collectd plugins, supply configuration values for each plugin you will install in that plugin's attributes file.

See [Attributes](#attributes) below for a detailed list of all available attributes.

4. Upload to Chef server

```
knife cookbook upload chef_install_configure_collectd --include-dependencies
```

This command uploads the `chef_install_configure_collectd` cookbook and all its dependencies to your Chef server.

5. Apply to Chef clients

### Using bootstrap

After supplying attributes, use `knife bootstrap` to apply the recipes to Chef clients. For example, the following command applies the `chef_install_configure_collectd` recipe and installs the Apache collectd plugin:

```
knife bootstrap $ip --ssh-user $username --node-name $nodename --run-list 'recipe[chef_install_configure_collectd], recipe[chef_install_configure_collectd::config-apache]'
```

### Attributes

#### Collectd Attributes

* attributes/SignalFx_repo.rb - Contains the names and locations of SignalFx collectd packages.
* attributes/default.rb - Basic attributes for SignalFx configuration.
   - default['write_http']['AWS_integration'] : 'true' if you want to sync AWS metadata to SignalFx, otherwise 'false' (default: 'true')
   - default['write_http']['Ingest_host'] : URL of the SignalFx ingest service.
   - default['write_http']['API_TOKEN'] : Your SignalFx API token.
   - default['collectd_version'] : The version of SignalFx collectd to install. (default: 'latest')

* To add a dimension to every datapoint sent to SignalFx, add an entry to default.rb as follows:

```ruby
   default["write_http"]["Ingest_host_parameters"]["YOUR_KEY1"] = "YOUR_VALUE1"
   default["write_http"]["Ingest_host_parameters"]["YOUR_KEY2"] = "YOUR_VALUE2"
```

### Plugin-specific Attributes

##### Apache
* attributes/apache_plugin.rb
   - default['apache']['instanceName'] : Name of your Apache instance
   - default['apache']['url'] : URL at which to access the output of Apache's mod_status module. (default: 'http://localhost/mod_status?auto')

##### Cassandra
* attributes/cassandra_plugin.rb
   - default['cassandra']['serviceurl'] : Your Cassandra service URL (default: 'service:jmx:rmi:///jndi/rmi://localhost:7199/jmxrmi')

##### Docker
* attributes/docker_plugin.rb
   - default['docker']['dbfile_folder'] : The location on disk to store this plugin's DB files. (default: '/opt/setup/scripts')
   - default['docker']['python_folder'] : The location on disk to store this plugin's Python files. (default: '/opt/setup/scripts')
   - default['docker']['base_url'] : URL at which to connect to the Docker instance to be monitored. (default : 'unix://var/run/docker.sock')

##### Elasticsearch
* attributes/elasticsearch_plugin.rb
   - default['elasticsearch']['clustername'] : Name of your ElasticSearch cluster. (default: `'elasticsearch')`
   - default['elasticsearch']['indexes'] : Which indexes to monitor. (default: `'_all'`)
   - default['elasticsearch']['python_folder'] : The location on disk of the collectd Python plugin. (default: `'/usr/share/collectd/python'`)

##### Kafka
* attributes/kafka_plugin.rb
   - default['kafka']['serviceurl'] : Your Kafka service URL (default: 'service:jmx:rmi:///jndi/rmi://localhost:7099/jmxrmi')

##### Memcached
* attributes/memcached_plugin.rb
   - default['memcached']['hostname'] : Memcached hostname
   - default['memcached']['port'] : Memcached port

##### MySQL
* attributes/mysql_plugin.rb
   - default['mysql']['database']... : 'database' is the database name that will be reported to SignalFx.
   - default['mysql']['database']['Host'] : IP address of MySQL database
   - default['mysql']['database']['Socket'] : Socket of MySQL database
   - default['mysql']['database']['User'] : Database username
   - default['mysql']['database']['Password'] : Database password
   - default['mysql']['database']['Database'] : Database name

##### Nginx
* attributes/nginx_plugin.rb
   - default['nginx']['url'] : URL at which to access Nginx status. (default: 'http://localhost:80/nginx_status')

##### PostgreSQL
* attributes/postgresql_plugin.rb
   - default['postgresql']['hostname'] : Hostname or IP address of your PostgreSQL database.
   - default['postgresql']['user'] : Database username
   - default['postgresql']['password'] : Database password

##### Redis
* attributes/redis_master_plugin.rb
   - default['redis_master']['hostname'] : Hostname or IP address of your Redis master instance.
   - default['redis_master']['port'] : Port on which your Redis master runs.
   - default['redis_master']['python_folder'] : The location on disk of the collectd Python plugin. (default: '/usr/share/collectd/python')

* attributes/redis_slave_plugin.rb
   - default['redis_slave']['hostname'] : Hostname or IP address of your Redis slave instance.
   - default['redis_slave']['port'] : Port on which your Redis slave runs.
   - default['redis_slave']['python_folder'] : The location on disk of the collectd Python plugin. (default: '/usr/share/collectd/python')

##### Zookeeper
* attributes/zookeeper_plugin.rb
   - default['zookeeper']['hostname'] = Hostname or IP address of your Zookeeper instance.
   - default['zookeeper']['port'] : Port on which your Zookeeper instance runs.
   - default['zookeeper']['python_folder'] : The location on disk of the collectd Python plugin. (default: '/usr/share/collectd/python')

## LICENSE

SignalFx version of collectd is released under the Apache 2.0 license. See LICENSE for more details.
