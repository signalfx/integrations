# ![](https://github.com/signalfx/integrations/blob/master/apache/img/integrations_apache.png) Apache

Metadata associated with the Apache collectd plugin can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/apache">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/collectd/blob/master/src/apache.c">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

The Smart Agent `collectd/apache` monitor monitors the Apache Webserver using the information provided in the module `mod_status`.

#### FEATURES

##### Built-in dashboards

- **Apache Web Servers**: Overview of data from all Apache webserver instances.

  [<img src='./img/dashboard_apache_webservers.png' width=200px>](./img/dashboard_apache_webservers.png)

- **Apache Web Server**: Focus on a single Apache webserver instance.

  [<img src='./img/dashboard_apache_webserver.png' width=200px>](./img/dashboard_apache_webserver.png)

### REQUIREMENTS AND DEPENDENCIES

This plugin collects metrics from the Apache `mod_status` module.

#### Version information

| Software     | Version        |
|--------------|----------------|
| Smart Agent  |  *  |


### CONFIGURATION

This integration is part of the <a
href="https://docs.signalfx.com/en/latest/integrations/agent/index.html"
target="_blank">SignalFx Smart Agent</a> -- see the docs for <a
href="https://docs.signalfx.com/en/latest/integrations/agent/monitors/collectd-apache.html"
target="_blank">the collectd/apache monitor</a> for details on how to configure
the Smart Agent to work with this integration.

### USAGE

Apache worker threads can be in one of the following states:

| State        | Remark                                  |
|--------------|-----------------------------------------|
| Open         | Open (unused) slot - no process         |
| Waiting      | Idle and waiting for request            |
| Sending      | Serving response                        |
| KeepAlive    | Kept alive for possible next request    |
| Idle\_cleanup | Idle and marked for cleanup             |
| Closing      | Closing connection                      |
| Logging      | Writing to log file                     |
| Reading      | Reading request                         |
| Finishing    | Finishing as part of graceful shutdown  |
| Starting     | Starting up to serve                    |

Sample of built-in dashboard in SignalFx:

![](././img/dashboard_apache.png)

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
