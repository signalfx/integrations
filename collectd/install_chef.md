# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_chef.png)INSTALL WITH CHEF

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

## System Requirements

This cookbook has been tested on the following operating systems:

- CentOS 6, 7;  
- Amazon Linux 1503, 1509;  
- Ubuntu 1504, 1404, 1204;  
- Debian GNU/Linux 7, 8;

### Cookbook dependencies

This cookbook requires the following cookbooks:

- apt (2.8.2)
- yum-epel (0.6.3)
- build-essential (2.2.4)
- yum (3.8.1)
- python (1.4.6)

## Usage

- Use the default recipe to install collectd, configure plugins, and configure collectd to send metrics to SignalFx.
- Use the individual collectd plugin recipes to install individual collectd plugins.


1. Install on your local machine

 ```
 knife cookbook site install chef_install_configure_collectd
 ```

 This command installs the chef_install_configure_collectd cookbook with all dependencies.

1. Supply your SignalFx API token.

 In order to send data to SignalFx, you must provide a value for your SignalFx API token in `attributes/default.rb` as follows, replacing `YOUR_SIGNALFX_API_TOKEN` with the API token for your SignalFx organization:

 ```
 default['write_http']['API_TOKEN'] = 'YOUR_SIGNALFX_API_TOKEN'
 ```

1. (Optional) Supply configuration for collectd and plugins.

 This cookbook includes default configuration for collectd in `attributes/default.rb`, and for plugins in individually-named files in the attributes directory. Before using this cookbook to install collectd plugins, supply configuration values for each plugin you will install in that plugin's attributes file.

 See [Attributes](#attributes) below for a detailed list of all available attributes.

1. Upload to Chef server

 ```
 knife cookbook upload chef_install_configure_collectd --include-dependencies
 ```

 This command uploads the `chef_install_configure_collectd` cookbook and all its dependencies to your Chef server.

1. Apply to Chef clients

 **Using bootstrap**

 After supplying attributes, use `knife bootstrap` to apply the recipes to Chef clients. For example, the following command applies the `chef_install_configure_collectd` recipe and installs the Apache collectd plugin:

 ```
 knife bootstrap $ip --ssh-user $username --node-name $nodename --run-list 'recipe[chef_install_configure_collectd], recipe[chef_install_configure_collectd::config-apache]'
 ```

### Attributes

#### Collectd Attributes

- `attributes/SignalFx_repo.rb` - Contains the names and locations of SignalFx collectd packages.
- `attributes/default.rb` - Basic attributes for SignalFx configuration.

  - `default['write_http']['AWS_integration']` : 'true' if you want to sync AWS metadata to SignalFx, otherwise 'false' (default: 'true')
  - `default['write_http']['Ingest_host']` : URL of the SignalFx ingest service.
  - `default['write_http']['API_TOKEN']` : Your SignalFx API token.
  - `default['collectd_version']` : The version of SignalFx collectd to install. (default: 'latest')


- To add a dimension to every datapoint sent to SignalFx, add an entry to `default.rb` as follows:

 ```ruby
  default["write_http"]["Ingest_host_parameters"]["YOUR_KEY1"] = "YOUR_VALUE1"
  default["write_http"]["Ingest_host_parameters"]["YOUR_KEY2"] = "YOUR_VALUE2"
 ```

### Plugin-specific Attributes

##### Apache
* attributes/apache_plugin.rb
   - default['apache']['instanceName'] : Name of your Apache instance
   - default['apache']['url'] : URL at which to access the output of Apache's mod_status module. (default: `http://localhost/mod_status?auto`)

##### Cassandra
* attributes/cassandra_plugin.rb
   - default['cassandra']['serviceurl'] : Your Cassandra service URL (default: `service:jmx:rmi:///jndi/rmi://localhost:7199/jmxrmi`)

##### Docker
* attributes/docker_plugin.rb
   - default['docker']['dbfile_folder'] : The location on disk to store this plugin's DB files. (default: `/opt/setup/scripts`)
   - default['docker']['python_folder'] : The location on disk to store this plugin's Python files. (default: `/opt/setup/scripts`)
   - default['docker']['base_url'] : URL at which to connect to the Docker instance to be monitored. (default : `unix://var/run/docker.sock`)

##### Elasticsearch
* attributes/elasticsearch_plugin.rb
   - default['elasticsearch']['clustername'] : Name of your ElasticSearch cluster. (default: `elasticsearch`)
   - default['elasticsearch']['indexes'] : Which indexes to monitor. (default: `_all`)
   - default['elasticsearch']['python_folder'] : The location on disk of the collectd Python plugin. (default: `/usr/share/collectd/python`)

##### Kafka
* attributes/kafka_plugin.rb
   - default['kafka']['serviceurl'] : Your Kafka service URL (default: `service:jmx:rmi:///jndi/rmi://localhost:7099/jmxrmi`)

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
   - default['redis_master']['python_folder'] : The location on disk of the collectd Python plugin. (default: `/usr/share/collectd/python`)

* attributes/redis_slave_plugin.rb
   - default['redis_slave']['hostname'] : Hostname or IP address of your Redis slave instance.
   - default['redis_slave']['port'] : Port on which your Redis slave runs.
   - default['redis_slave']['python_folder'] : The location on disk of the collectd Python plugin. (default: `/usr/share/collectd/python`)

##### Zookeeper
* attributes/zookeeper_plugin.rb
   - default['zookeeper']['hostname'] = Hostname or IP address of your Zookeeper instance.
   - default['zookeeper']['port'] : Port on which your Zookeeper instance runs.
   - default['zookeeper']['python_folder'] : The location on disk of the collectd Python plugin. (default: `/usr/share/collectd/python`)
