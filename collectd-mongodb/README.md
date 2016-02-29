---
title: collectd MongoDB Plugin
brief: MongoDB plugin for collectd.
---

# MongoDB Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use the [mongodb](https://github.com/signalfx/collectd-mongodb) collectd
plugin to collect metrics from MongoDB nodes.

The plugin uses collectd to capture following statistical data:

* memory
* network input/output bytes count
* heap usage
* db connections
* operations count
* active client connections
* queued operations

The plugin also captures following DB-specific metrics:

* db size
* db counters

Original MongoDB Documentation http://docs.mongodb.org/manual/

### REQUIREMENTS AND DEPENDENCIES

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  4.9 or later  |
| MongoDB   |  2.4 or later  |

### INSTALLATION

1. Install the Python plugin for collectd.

 RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following commands to install the Python plugin for collectd, pip, and pymongo:

 ```
 yum install -y epel-release
 yum install -y python-pip
 yum install -y collectd-python
 pip install pymongo==2.8
 ```

 Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

1. Run the following commands to install pip and pymongo:

 ```
 apt-get install -y python-pip python-dev build-essential
 pip install pymongo==2.8
 ```
1. Download the [Python module for MongoDB](https://github.com/signalfx/collectd-mongodb)  

1. Download SignalFx's [sample configuration file](https://github.com/signalfx/Integrations/collectd-mongodb/10-mongodb.conf)

1. Modify the sample configuration file as described in [Configuration](#configuration)

1. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file:

 ```
 include '/path/to/10-mongodb.conf'
 ```

1. Restart collectd.

1. Metrics from MongoDB will begin streaming into SignalFx, and new built-in dashboards will be created for you. Check the status of your new integration on the Integrations page.

### CONFIGURATION

#### Required configuration

Change the Host/Port/User/Password/Database/Instance to settings that allow you to connect to the mongodb instance. **Note:** For additional *MongoDB Instances* it is required to specify and additional `<Module>` block.

The following configuration options are *required*. This means that you must supply values for them in configuration in order for the plugin to work.

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | /opt/setup/scripts |
| Host | Host IP | 127.0.0.1 |
| Port | Port number for IP connection | 27017 |
| User | Valid mongodb user | admin |
| Password | Associated Password for valid user | password |
| Database | Name(s) of database(s) that you would like metrics from | admin, db-prod, db-dev |
| Instance | Name of mongodb Instance | PROD |



```
TypesDB "/opt/setup/scripts/types.db"
LoadPlugin python
<Plugin "python">
  ModulePath "/opt/setup/scripts"
  Import "mongodb"
  <Module mongodb>
    Host "127.0.0.1"
    Port "27017"
    User "admin"
    Password "password"
    Database "admin" "db-prod" "db-dev"
    Instance ""
  </Module>
</Plugin>
```

### USAGE

This plugin is an example that emits values on its own, and does not connect to software. It emits a repeating sine wave in the metric gauge.sine. The metric should look like this:

![Example chart showing gauge.sine](http://fixme)

The following conditions may be cause for concern:

*You see a straight line instead of a curve.*

This may indicate a period of missing data points. In the example chart shown above, some data points are missing between 16:40 and 16:41, and SignalFx is interpolating a straight line through the gap.

### METRICS



For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This plugin is released under the Apache 2.0 license. See LICENSE for more details.
