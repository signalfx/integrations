# ![](https://github.com/signalfx/integrations/blob/master/heka-filter-signalfx/img/integrations_heka.png) Heka Filter for SignalFx

Metadata associated with the Heka filter integration can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/heka-filter-signalfx">here</a>. The relevant code for the integration can be found <a target="_blank" href="https://github.com/Clever/heka-clever-plugins/blob/master/lua/filters/signalfxbatch.lua">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

This integration provides support for pushing Heka metrics into SignalFx. <a target="_blank" href="http://hekad.readthedocs.org/en/v0.10.0/">Heka</a> is an open source stream processing software system developed by Mozilla. This filter for was built by Clever, a SignalFx customer. The integration extracts data from Fields in messages. Generates JSON suitable for send to datapoint SignalFx API. Batches multiple messages into one string, which can be passed to an `HttpOutput` using a `PayloadEncoder`. Currently, only supports writing data points, NOT events.

Heka is a “Swiss Army Knife” type tool for data processing, useful for a wide variety of different tasks, such as:

* Loading and parsing log files from a file system.
* Accepting statsd type metrics data for aggregation and forwarding to upstream time series data stores such as graphite or InfluxDB.
* Launching external processes to gather operational data from the local system.
* Performing real time analysis, graphing, and anomaly detection on any data flowing through the Heka pipeline.
* Shipping data from one location to another via the use of an external transport (such as AMQP) or directly (via TCP).
* Delivering processed data to one or more persistent data stores.

### REQUIREMENTS AND DEPENDENCIES

This filter requires:

| Software          | Version        |
|-------------------|----------------|
| Heka | 0.10+ |

### INSTALLATION

Heka installation instructions are available in the <a target="_blank" href="http://hekad.readthedocs.org/en/v0.10.0/installing.html">Heka documentation</a>

### CONFIGURATION

#### Configuring your ingest endpoint

Before we can send metrics to SignalFx, we need to make sure you are sending them to
the correct SignalFx realm. To determine what realm you are in (YOUR_SIGNALFX_REALM), check your
profile page in the SignalFx web application (click the avatar in the upper right and click My Profile).
If you are not in the `us0` realm, you will need to configure the Heka address to point to
the correct ingest URL. See the example configuration below.


Full Heka configuration setting are available in the <a target="_blank" href="http://hekad.readthedocs.org/en/v0.10.0/config/index.html">Heka docs</a>

Configuration for the SignalFx filter:

| Setting            | type  |   default   | description          |
|--------------------|-------|-------------|----------------------|
|metric\_name | string | (required) no default set | String to use as the `metric` name in SignalFx. Supports interpolation of field values from the processed message, using `%{fieldname}`. Any `fieldname` values of "Type", "Payload", "Hostname", "Pid", "Logger", "Severity", or "EnvVersion" will be extracted from the the base message schema, any other values will be assumed to refer to a dynamic message field. Only the first value of the first instance of a dynamic message field can be used for series name interpolation. If the dynamic field doesn't exist, the uninterpolated value will be left in the series name. Note that it is not possible to interpolate either the "Timestamp" or the "Uuid" message fields into the series name, those values will be interpreted as referring to dynamic message fields.|
| value_field | string | (optional) defaults to `"value"` | The `fieldname` to use as the value for the metric in signalfx. If the `value` field is not present this encoder will set one as the value for counters: `1`. A value of `0` will be used for `gauges`. |
| msg\_type | string | (optional) defaults to `"signalfxbatch"` | `Type` of the message outputted from this filter. |
| max\_count | int  | (optional) defaults to `"20"` | Max number of messages before a batch is flushed from the filter.|
| dimensions | string | (optional) defaults to `""` | A space delimited list of field names. Each of these will be written as "dimensions" on the SignalFx data point, which you can filter by in SignalFx.*|

`dimentions` example: a value of "Hostname Severity" would write the field:

```
"dimensions": {
    "Hostname": "my-hostname.example.com",
    "Severity": 0
}
```

#### Example Heka Configuration

```
.. code-block:: ini
    [SignalfxBatchFilter]
    message_matcher = "Fields[title] == 'your-metric' && Fields[metric_value] != NIL"
    type = "SandboxFilter"
    script_type = "lua"
    filename = "lua/filters/signalfxbatch.lua"
       [SignalfxBatchFilter.config]
       metric_name = "test-metric.%{title}.%{Hostname}"
       value_field = "metric_value"
       dimensions = "Hostname Severity"
       max_count = 5
    [SignalfxHttpOutput]
    message_matcher = "Fields[payload_name] == 'signalfxbatch'"
    type = "HttpOutput"
    encoder = "PayloadEncoder"
    address = "https://ingest.YOUR_SIGNALFX_REALM.signalfx.com/v2/datapoint"
      [signalfx.headers]
      content-type = ["application/json"]
      X-SF-Token = "YOUR_SIGNALFX_API_TOKEN"
```

### METRICS

Documentation of the metrics and dimensions emitted by this integration, are available in the <a target="_blank" href="https://hekad.readthedocs.org/en/v0.10.0/config/outputs/index.html#common-output-parameters">Heka docs</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
