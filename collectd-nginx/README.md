---
title: NGINX collectd Plugin
brief: NGINX plugin for collectd.
---
# ![](https://github.com/signalfx/integrations/blob/master/collectd-nginx/img/integrations_nginx.png) NGINX collectd Plugin

_This is a directory consolidate all the metadata associated with the NGINX collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/nginx.c)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This NGINX plugin. This will send data about NGINX to SignalFx, enabling built-in NGINX monitoring dashboards.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd |  4.2+  |

### INSTALLATION

1. Enable the `stub_status` module in your nginx server as described [below](#configuration).

1. Install the collectd plugin.

 ##### RHEL/CentOS 6.x & 7.x, and Amazon Linux 2014.09, 2015.03 & 2015.09

 Run the following command to install the collectd plugin:
 ```
 yum install collectd-nginx
 ```
 ##### Ubuntu 12.04, 14.04, 15.04 & Debian 7, 8:

 This plugin is included with [SignalFx's collectd package](https://github.com/signalfx/integrations/tree/master/collectd).

1. Download SignalFx’s [sample configuration file](https://github.com/signalfx/integrations/blob/master/collectd-nginx/10-nginx.conf)

1. Modify the sample configuration file to provide values that make sense for your environment, as described in the header.

1. Add the following line to /etc/collectd.conf, replacing the example path with the location of the configuration file you downloaded in step 2:
 ```
 include '/path/to/10-nginx.conf'
 ```
1. Restart collectd.

### CONFIGURATION

#### NGINX service configuration:

From [nginx docs](http://nginx.org/en/docs/http/ngx_http_stub_status_module.html):
>The `ngx_http_stub_status_module` module provides access to basic status information.

>This module is not built by default, it should be enabled with the `--with-http_stub_status_module` configuration parameter.

>Example Configuration:
```
location /basic_status {
   stub_status;
}
```
This configuration creates a simple web page with basic status data which may look like as follows:
```
Active connections: 291
server accepts handled requests
 16630948 16630948 31070465
Reading: 6 Writing: 179 Waiting: 106
```

#### [nginx collectd configuration file](https://github.com/signalfx/integrations/blob/master/collectd-nginx/10-nginx.conf)

- Change the URL parameter to the location you setup above.

### USAGE


### METRICS

The following status information is provided:

| Metric | definition |
| ---------------------|-------------|
|Active connections| The current number of active client connections including Waiting connections.|
|accepts|The total number of accepted client connections.|
|handled|The total number of handled connections. Generally, the parameter value is the same as accepts unless some resource limits have been reached (for example, the worker_connections limit).|
|requests|The total number of client requests.|
|Reading|The current number of connections where nginx is reading the request header.|
|Writing|The current number of connections where nginx is writing the response back to the client.|
|Waiting|The current number of idle client connections waiting for a request.|


Segmented metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/nginx.c).
