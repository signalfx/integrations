# OVERVIEW

## Description

**This integration primarily consists of the Smart Agent monitor `collectd/apache`.
Below is an overview of that monitor.**

### Smart Agent Monitor


Monitors Apache webservice instances using the information provided by
`mod_status`.

### Worker states
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

# SETUP

## INSTALLATION

This integration is part of the [SignalFx Smart Agent](https://github.com/signalfx/integrations/tree/master/signalfx-agent)[](sfx_link:signalfx-agent)
as the `collectd/apache` monitor. You should first deploy the Smart Agent to the
same host as the service you want to monitor, and then continue with the
configuration instructions below.


<!--- SETUP --->
## Apache Setup
To configure the Apache webserver itself to expose status metrics:

1. Enable the <a target="_blank" href="http://httpd.apache.org/docs/2.4/mod/mod_status.html">mod_status</a> module in your Apache server.
2. Add the following configuration to your Apache server:

   ```
    ExtendedStatus on
    <Location /mod_status>
    SetHandler server-status
    </Location>
   ```
3. Restart Apache.

_Note_: Make sure that the URL you provide for your `mod_status` module
ends in `?auto`. This returns the status page as `text/plain`, which this
plugin requires.

<!--- SETUP --->
## Config Examples

```
monitors:
 - type: collectd/apache
   host: localhost
   port: 80
```

If `mod_status` is exposed on an endpoint other than `/mod_status`, you can
use the `url` config option to specify the path:

```
monitors:
 - type: collectd/apache
   host: localhost
   port: 80
   url: "http://{{ '{{' }}.Host}}:{{ '{{' }}.Port}}/server-status?auto"
```

For a full list of options, see [Configuration](#configuration).


## Configuration

To activate this monitor in the Smart Agent, add the following to your
agent config:

```
monitors:  # All monitor config goes under this key
 - type: collectd/apache
   ...  # Additional config
```

**For a list of monitor options that are common to all monitors, see [Common
Configuration](https://github.com/signalfx/signalfx-agent/tree/master/docs/monitors/../monitor-config.md#common-configuration).**


| Config option | Required | Type | Description |
| --- | --- | --- | --- |
| `host` | **yes** | `string` | The hostname of the Apache server |
| `port` | **yes** | `integer` | The port number of the Apache server |
| `name` | no | `string` | This will be sent as the `plugin_instance` dimension and can be any name you like. |
| `url` | no | `string` | The URL, either a final URL or a Go template that will be populated with the host and port values. (**default:** `http://{{ '{{' }}.Host}}:{{ '{{' }}.Port}}/mod_status?auto`) |
| `username` | no | `string` |  |
| `password` | no | `string` |  |


# Metrics

Metrics that are categorized as
[container/host](https://docs.signalfx.com/en/latest/admin-guide/usage.html#about-custom-bundled-and-high-resolution-metrics)
(*default*) are ***in bold and italics*** in the list below.

These are the metrics available for this integration.

{% import "macros.jinja" as macros %}
{{ macros.metric_list(metrics) }}

## Dimensions

The following dimensions may occur on metrics emitted by the monitors. Some
dimensions may be specific to certain metrics.

| Name | Description |
| ---  | ---         |
| `plugin_instance` | Set to whatever you set in the `name` config option. |

# FEATURES

## Built-in dashboards

Sample of built-in dashboard in SignalFx:

  ![](././img/dashboard_apache.png)

- **Apache Web Servers**: Overview of data from all Apache webserver instances.

  [<img src='./img/dashboard_apache_webservers.png' width=200px>](./img/dashboard_apache_webservers.png)

- **Apache Web Server**: Focus on a single Apache webserver instance.

  [<img src='./img/dashboard_apache_webserver.png' width=200px>](./img/dashboard_apache_webserver.png)
