# Apache Webserver Plugin

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION
Follow these instructions to install the Apache plugin for collectd. This will send data about Apache to SignalFx, enabling built-in Apache monitoring dashboards.

### REQUIREMENTS AND DEPENDENCIES
Use the [Apache collectd plugin](https://collectd.org/wiki/index.php/Plugin:Apache) to collect metrics about Apache Webserver.  This plugin collects metrics from the module `mod_status`. 

Apache worker threads can be in one of the following states: 

| State        | Remark                                  |
|--------------|-----------------------------------------|
| Open         | Open (unused) slot - no process         |
| Waiting      | Idle and waiting for request            |
| Sending      | Serving response                        |
| KeepAlive    | Kept alive for possible next request    |
| Idle_cleanup | Idle and marked for cleanup             |
| Closing      | Closing connection                      |
| Logging      | Writing to log file                     |
| Reading      | Reading request                         |
| Finishing    | Finishing as part of graceful shutdown  |
| Starting     | Starting up to serve                    |

### Version information

| Software  | Version        |
|-----------|----------------|
| collectd  |  3.9 or later  |


### INSTALLATION

1. [Enable the `mod_status` module](http://httpd.apache.org/docs/2.4/mod/mod_status.html) in your Apache server.

1. Add the following configuration to your Apache server:

 ```
 ExtendedStatus on
 <Location /mod_status>
   SetHandler server-status
 </Location>
 ```

1. Restart apache.

1. Install the apache collectd plugin.

 #### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

 #### RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09 

 Run the following command to install this plugin:

 ```
 yum install collectd-apache
 ```

1. Download SignalFx's [sample configuration file](https://github.com/signalfx/signalfx-collectd-configs/blob/master/managed_config/10-apache.conf) for this plugin.

1. Modify the sample configuration file to provide values that make sense for your environment, as described in the header.

 #### Note: Make sure that the URL you provide for your mod_status module ends in "?auto". This returns the status page as text/plain, which this plugin requires.

1. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file you downloaded in step 2:

 ```
 include '/path/to/10-apache.conf'
 ```

1. Restart collectd.

1. Metrics from apache will begin streaming into SignalFx, and new built-in dashboards will be created for you. Check the status of your new integration on the Integrations page.

### CONFIGURATION 

>Provide in this section instructions on how to configure the plugin, before and after installation. If this plugin has a configuration file with properties, list each property, define its purpose and give an example or list the default value.

#### Required configuration 

The following configuration options are *required* and have no defaults. This means that you must supply values for them in configuration in order for the plugin to work. 

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| required_option | An example of a required configuration property. | 12345 |

#### Optional configuration 

The following configuration options are *optional*. You may specify them in the configuration file in order to override default values provided by the plugin. 

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/opt/example" |
| Frequency  | Cycles of the sine wave per minute. | 0.5 | 

### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Chart images demonstrating each important condition or failure mode

### METRICS

For full documentation of the metrics and dimensions emitted by this plugin, see the `docs` directory in this repository. 

### LICENSE

This plugin is released under the Apache 2.0 license. See LICENSE for more details. 
