# ![](./img/integrations_kong.png) Kong

Metadata associated with the Kong plugin for collectd can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd-kong">here</a>.

The relevant code for the integration can be found <a target="_blank" href="https://github.com/signalfx/collectd-kong">here</a> and for its Kong plugin dependency <a target="_blank" href="https://github.com/signalfx/kong-plugin-signalfx">here</a>.

- [Description](#description)
- [Features](#features)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

The SignalFx Kong collectd plugin provides users with the ability to gather and report their service traffic
metrics with collectd, in tandem with <a target="_blank" href="https://github.com/signalfx/kong-plugin-signalfx">kong-plugin-signalfx</a>.

This plugin emits metrics for configurable request/response lifecycle groups including:

* Counters for response counts
* Counters for cumulative response and request sizes
* Counters for cumulative request, upstream, and Kong latencies

These request/response lifecycle groups can be optionally partitioned by tunable levels of granularity by:

* API or Service Name/ID
* Route ID
* Request HTTP Method
* Response HTTP Status Code

In addition to these groups, system-wide connection stats can be provided, including:

* A counter for total fielded requests
* Gauges for active connections and their various states
* A gauge for database connectivity

#### FEATURES

##### Built-in dashboards

- **Kong Servers Overview**: High-level Kong performance for all reporting servers

  [<img src='./img/kong_servers_overview.png' width=200px>](./img/kong_servers_overview.png)

- **Kong Server Overview**: High-level Kong performance for an individual server

  [<img src='./img/kong_server_overview.png' width=200px>](./img/kong_server_overview.png)

- **API Objects**: API object activity metrics

  [<img src='./img/api_objects.png' width=200px>](./img/api_objects.png)

- **Service Objects**: Service object activity metrics

  [<img src='./img/service_objects.png' width=200px>](./img/service_objects.png)

- **Route Objects**: Route object activity metrics

  [<img src='./img/route_objects.png' width=200px>](./img/route_objects.png)

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd | 4.9+ |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |
| Python | 2.6+ |
| Kong | 0.11.2+ |
| Configured <a target="_blank" href="https://github.com/signalfx/kong-plugin-signalfx">kong-plugin-signalfx</a> | 0.0.1+ |

### INSTALLATION

Both the SignalFx Smart Agent and collectd agent report metrics made available by the <a target="_blank" href="https://github.com/signalfx/kong-plugin-signalfx">kong-plugin-signalfx</a> metric endpoint. Please download and install this Lua module on all Kong servers using its <a target="_blank" href="https://github.com/signalfx/kong-plugin-signalfx/blob/master/README.md">instructions</a>.

* If you are using the SignalFx Smart Agent, collectd-kong is already included.  Please see <a target="_blank" href="https://github.com/signalfx/signalfx-agent/blob/master/docs/monitors/collectd-kong.md">the monitor documentation</a> for configuration instructions.

* If you are using the SignalFx collectd agent follow the steps below.

1. Download and install the <a target="_blank" href="https://github.com/signalfx/collectd-kong/">collectd-kong</a> Python module.

2. Download SignalFx’s <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-kong/10-kong.conf">sample configuration file</a> to `/etc/collectd/managed_config`.

3. Modify the configuration file as described in [Configuration](#configuration) below.

4. Restart collectd.

### CONFIGURATION

Using the example configuration file <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/collectd-kong/10-kong.conf">10-kong.conf</a> as a guide, provide values for the configuration options listed below that make sense for your environment.

| Configuration option | Definition | Example value |
| ---------------------|------------|---------------|
| URL | The URL for the `/signalfx` kong-plugin-signalfx metric endpoint | `"https://my_kong_server:8443/signalfx"` |
| AuthHeader | The name and value of a header to be passed with GETs to the URL | `"Authorization" "Basic YWRtaW46cGFzc3dvcmQ="` |
| VerifyCerts | Whether to verify the ssl certificates for HTTPS requests to the URL | `true` |
| CABundle | Path to a CA\_BUNDLE file or directory with certificates of trusted CAs when `VerifyCerts` is true | `"/path/ca_bundle/`" |
| ClientCert | Client side certificate to use for HTTPS requests to the URL | `"/path/client.cert"` |
| ClientCertKey | Separate client side certificate key if not included with cert file | `"/path/client.key"` |
| Metric | The short name and report boolean for (un)desired metrics to emit.  See [Metrics](#metrics). | `"request_latency" false` |
| ExtraDimension | The name and value of any custom dimension to be sent with each datapoint | `"my_dimension" "my_dimension_value"` |
| ReportAPIIDs | The UUID assigned to each API object upon creation | `false` |
| ReportAPINames | The optional, user-created name assigned to API objects (recommended) | `true` |
| ReportServiceIDs | The UUID assigned to each Service object upon creation | `false` |
| ReportServiceNames | The optional, user-created name assigned to Service objects  (recommended) | `true` |
| ReportRouteIDs | The UUID assigned to each Route object upon creation (recommended) | `true` |
| ReportHTTPMethods | The HTTP method of each request made to the Kong proxy | `true` |
| ReportStatusCodeGroups | The HTTP status code group (e.g. 4xx) for each proxy server fielded request (recommended) | `true` |
| ReportStatusCodes | The HTTP status code for each fielded request | `false` |
| APIIDs | The pattern(s) of API IDs to add as dimensions for applicable datapoints | `"my-api-id"` |
| APIIDsBlacklist | The pattern(s) of API IDs to not report as dimensions for applicable datapoints | `"my-unwanted-id" "my-other-unwanted-id"` |
| APINames | The pattern(s) of API Names to add as dimensions for applicable datapoints | `"MyAPI"` |
| APINamesBlacklist | The pattern(s) of API Names to not report as dimensions for applicable datapoints | `"MyUnwantedAPI" "MyOtherUnwantedAPI"` |
| ServiceIDs | The pattern(s) of Service IDs to add as dimensions for applicable datapoints | `"my-service-id"` |
| ServiceIDsBlacklist | The pattern(s) of Service IDs to not report as dimensions for applicable datapoints | `"my-unwanted-id" "my-other-unwanted-id"` |
| ServiceNames | The pattern(s) of Service Names to add as dimensions for applicable datapoints | `"MyService"` |
| ServiceNamesBlacklist | The pattern(s) of Service Names to not report as dimensions for applicable datapoints | `"MyUnwantedService" "MyOtherUnwantedService"` |
| RouteIDs | The pattern(s) of Route IDs to add as dimensions for applicable datapoints | `"my-route-id"` |
| RouteIDsBlacklist | The pattern(s) of Route IDs to not report as dimensions for applicable datapoints | `"my-unwanted-id" "my-other-unwanted-id"` |
| HTTPMethods | The pattern(s) of HTTP methods to add as dimensions for applicable datapoints | `"GET" "POST" "DELETE"` |
| HTTPMethodsBlacklist | The pattern(s) of HTTP methods to not report as dimensions for applicable datapoints | `"HEAD" "OPTIONS"` |
| StatusCodes | The pattern(s) of status codes to add as dimensions for applicable datapoints | `"2*"`
| StatusCodesBlacklist | The pattern(s) of status codes to not report as dimensions for applicable datapoints | `"1*" "3*"` |
| Interval | How often, in seconds, Kong metrics are obtained. | `10` |
| Verbose | Whether to emit lower level metric collection and processing statements to the LogFile plugin | `true` |

### USAGE

Sample of built-in dashboard in SignalFx:

![](././img/catalog_view.png)

### METRICS

For documentation of the metrics emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/collectd-kong/blob/master/LICENSE) for more details.
