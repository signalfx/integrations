---
title: collectd MySQL plugin
brief: Use this plugin to collect metrics from MySQL. 
---

> Fill in the structured header above to allow products like SignalFx to programmatically display this document. 

# MySQL Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This file describes the MySQL plugin for collectd. Use it to monitor MySQL database performance. 

This plugin connects to a MySQL instance and reports on the values returned by a `SHOW STATUS` command. This includes the following:

  - Number of commands processed
  - Table and row operations (handlers)
  - State of the query cache 
  - Status of MySQL threads
  - Network traffic

### REQUIREMENTS AND DEPENDENCIES

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  3.6 or later  |
| MySQL     |  4.x or later  |

### INSTALLATION

Follow these steps to install and configure this plugin:

1. Install the plugin.

  **Ubuntu 12.04, 14.04, & 15.04 and Debian 7 & 8:**

  This plugin is included with SignalFx's collectd package.

  **RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09**:

  Run the following command to install this plugin:

  ```
  yum install collectd-mysql
  ```

1. Download SignalFx's [sample configuration file](./10-mysql.conf) for this plugin.
1. Modify the sample configuration file as described in [Configuration](#configuration), below.
1. Add the following line to `/etc/collectd.conf`, replacing the example path with the location of the configuration file:

  ```
  include '/path/to/10-mysql.conf'
  ```

1. Restart collectd.

Follow these steps to install this plugin:

1. Download this repository to your local machine.
2. Download the sample configuration file from signalfx-integrations/helloworld/.
3. Modify the sample configuration file to contain values that make sense for your environment, as described [below](#configuration).
4. Add the following line to collectd.conf, replacing the path with the path to the sample configuration file you downloaded in step 2: 

  ``` 
  include '/path/to/10-configfile.conf' 
  ```
5. Restart collectd. 

### CONFIGURATION 

Using the example configuration file [`10-mysql.conf`](././10-mysql.conf) as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the MySQL instance to be monitored.

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| Database (in block declaration) | The value of the dimension `plugin_instance` that will be recorded for this database. | hostA_database1 |
| Host  | The host on which MySQL is running. | "10.128.8.2" | 
| Socket | A socket that collectd can use to connect to the database. You may be able to find this value by looking at the command used to run MySQL on your server as follows: <code>ps auwxxx &#124; grep mysql<code> | "/var/run/mysqld/mysqld.sock" |
| User | A valid username that collectd can use to connect to MySQL. | "root"
| Password | Password for the username given in User. | "abcdABCD1." |
| Database (within block) | The name of the MySQL database to monitor. | "mysql_one" |

#### Note: Monitoring multiple instances
The sample configuration file is configured to illustrate how to configure this plugin to monitor multiple databases, on the same host or on different hosts. 

To monitor just one database, include just one Database block and delete the others. 

#### Note: Two different directives called "Database"
This plugin configuration file uses directives called “Database” in two different places: one in each block declaration, and one within each block. 

The value of “Database” in the block declaration indicates the value of the  `plugin_instance` dimension that will be recorded for this database. The value of “Database” within the block indicates the `db_name` of the MySQL database to monitor using this configuration. 

To illustrate the difference between these two uses of "Database", the example configuration given in [`10-mysql.conf`](././10-mysql.conf) directs collectd to collect metrics for three total MySQL databases: the databases named `mysql_one` and `mysql_two` on host 10.128.8.2, and the database named `mysql_one` on host 10.128.8.3. 

### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Chart images demonstrating each important condition or failure mode

This plugin is an example that emits values on its own, and does not connect to software. It emits a repeating sine wave in the metric gauge.sine. The metric should look like this:

![Example chart showing gauge.sine](http://fixme)

The following conditions may be cause for concern:

*You see a straight line instead of a curve.*

This may indicate a period of missing data points. In the example chart shown above, some data points are missing between 16:40 and 16:41, and SignalFx is interpolating a straight line through the gap. 

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

> Include licensing information for the plugin in this section.

This plugin is released under the [GNU General Public license v2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).
