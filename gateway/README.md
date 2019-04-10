# ![](https://github.com/signalfx/integrations/blob/master/gateway/img/integration_sfxgateway.png) SignalFx Gateway

Information associated with the SignalFx Gateway can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/gateway">here</a>. The relevant code for the project can be found <a target="_blank" href="https://github.com/signalfx/gateway">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
    - [Migrating From Metricproxy](#migrating-from-metricproxy)
    - [Sizing Details](#sizing-details)
- [Installation](#installation)
    - [Docker Container Deployment](#docker-container-deployment)
- [Configuration](#configuration)
    - [Forwarders](#forwardto)
        - [SignalFx](#signalfx-forwarder)
        - [CSV](#csv-forwarder)
        - [Carbon](#carbon-forwarder)
    - [Listeners](#listenfrom)
        - [SignalFx](#signalfx-listener)
            - [Add Tags to Spans](#add-tags-to-spans)
            - [Identify and Replace variables in Span Names](#identify-and-replace-variables-in-span-names)
            - [Using AdditionalSpanTags and SpanNameReplacementRules Together](#using-additionalspantags-and-spannamereplacementrules-together)
            - [Obfuscating Span Tag Metadata](#obfuscating-span-tag-metadata)
            - [Removing Span Tag Metadata](#removing-span-tag-metadata)
            - [Span Processing Order of Operations](#span-processing-order-of-operations)
        - [collectd](#collectd-listener)
        - [Prometheus](#prometheus-listener)
        - [Wavefront](#wavefront-listener)
        - [Carbon](#carbon-listener)
            - [Graphite Options](#graphite-options)
            - [Graphite Dimensions](#graphite-dimensions)
            - [Graphite Dimensions using Regular Expressions](#graphite-dimensions-using-regular-expressions)
            - [Graphite Dimensions using Delimiters](#graphite-dimensions-using-delimiters)
- [Usage](#usage)
    - [Running the daemon](#running-the-daemon)
    - [Stopping the daemon](#stopping-the-daemon)
    - [Health checks](#health-checks)
    - [Graceful Shutdown](#graceful-shutdown)
    - [Sending SignalFx data to SignalFx](#sending-signalfx-data-to-signalfx)
    - [Sending data to multiple destinations](#sending-data-to-multiple-destinations)
    - [Sending To Alternate Ingest Targets](#sending-to-alternate-ingest-targets)
    - [HTTP Proxy Support](#http-proxy-support)
    - [SignalFx Performance Options](#signalfx-performance-options)
    - [Transforming carbon dot-delimited metric names into metrics with dimensions](#transforming-carbon-dot-delimited-metric-names-into-metrics-with-dimensions)
    - [Concentrate outgoing HTTP connections](#concentrate-outgoing-http-connections)
    - [Simplify configuration of collectd](#simplify-configuration-of-collectd)
    - [Teeing a subset of metrics on a forwarder](#teeing-a-subset-of-metrics-on-a-forwarder)
- [Debugging](#debugging)
    - [Status page and profiling](#status-page-and-profiling)
    - [Debugging via logfile](#debugging-via-logfile)
    - [Debugging connections via headers](#debugging-connections-via-headers)
    - [Debugging connections via debug dimensions](#debugging-connections-via-debug-dimensions)
- [License](#license)

### DESCRIPTION

Use the SignalFx Gateway to aggregate metrics and send them to SignalFx. It is a multilingual datapoint demultiplexer that can accept time series data from the carbon (Graphite), collectd or SignalFx protocols and emit those datapoints to a series of servers using the carbon, collectd or SignalFx protocols.

The SignalFx Gateway can help you get the right data to the right destination in many different scenarios. For details, see [Usage](#usage).

### REQUIREMENTS AND DEPENDENCIES

The SignalFx Gateway must be deployed on a system that is capable of running Go. All dependencies for this Go project are included in `/Godeps` in the project repository.

We recommend placing the gateway either on the same server as another existing metrics aggregator or on a central server that is already receiving datapoints, such as Graphite's Carbon Database.

Additional Steps are required to install the gateway on Ubuntu machines
because the golang package in Ubuntu is not up to date. The following steps
to [update](https://github.com/golang/go/wiki/Ubuntu) the golang package on
Ubuntu must be executed before running the install script.

    sudo add-apt-repository ppa:gophers/archive
    sudo apt-get update
    sudo apt-get install golang-1.11.1

If `/usr/bin/go` does NOT exist then create a symbolic link

    sudo ln /usr/lib/go-1.11.1/bin/go /usr/bin/go

Or if `/usr/bin/go` does exist, then overwrite the older binary

    sudo cp /usr/lib/go-1.11.1/bin/go /usr/bin/go

#### Migrating From Metricproxy

Additional steps are required if you are upgrading from a version from the deprecated
metricproxy repo.  You'll want rename the following:

    /etc/sfdbconfig.conf -> /etc/gateway.conf
    /var/log/sfproxy -> /var/log/gateway

Some files generated by the metricproxy have also changed:

    /var/log/sfprpoxy/metricproxy.log -> /var/log/gateway/gateway.log
    /var/run/metricproxy.pid -> /var/run/gateway.pid

If you were running the metricproxy using our docker container, please note that
the paths and filenames have also changed.  You must update any infrastructure 
that interacts with the files:

    /var/log/sfproxy -> /var/log/gateway
    /var/config/sfproxy -> /var/config/gateway
    /var/config/sfproxy/sfdbproxy.conf ->  /var/config/gateway/gateway.conf

No changes to the contents of the gateway.conf are required.

#### SIZING DETAILS

The size of the machine that hosts the gateway depends on the amount of data that will be transmitted through it. The key performance indicator for the host is CPU idle (higher is better). A host comparable to AWS's c3.2xlarge is known to handle up to approximately 7 million DPM (data points per minute) while reporting 70% CPU idle. For safety, we recommend large margins - running close to resource limits risks delayed data transmission, especially if the rate of data points is highly variable.

### INSTALLATION

1. Identify a server on which to deploy the SignalFx Gateway.
2. Edit the file `gateway.conf` to configure the gateway. Configuration options are defined [below](#configuration), and example configurations are available in the <a target="_blank" href="https://github.com/signalfx/gateway">main project documentation</a>.
3. Use the <a target="_blank" href="https://raw.githubusercontent.com/signalfx/gateway/master/install.sh">install script</a> to install or upgrade the gateway, as follows.

        curl -s https://raw.githubusercontent.com/signalfx/gateway/master/install.sh | sudo sh
        # Config at    /etc/gateway.conf
        # Binary at    /opt/gateway/bin/gateway
        # Logs at      /var/log/gateway
        # PID file at  /var/run/gateway.pid

4. Start the gateway as follows:

        /etc/init.d/gateway start

5. Configure your endpoints:

By default, the SignalFx Gateway sends metrics to the `us0` realm.
If you are not in this realm, you will need to explicitly set the endpoint urls to use your realm.
To determine if you are in a different realm (YOUR_SIGNALFX_REALM) and need to explicitly set the endpoints, check your profile page in the SignalFx web application.
See the configuration section on [sending to alternate ingest targets](#sending-to-alternate-ingest-targets) below.

6. Begin transmitting data to the host and port on which the gateway is running. The data will be transformed and forwarded as specified in the [configuration](#configuration).

#### Docker Container Deployment

 The SignalFx Gateway is also packaged as a Docker image that has been built and deployed to <a target="_blank" href="https://quay.io/repository/signalfx/gateway">quay.io</a>. This image does not include configuration. To use this image, ensure that you have a `gateway.conf` file cross-mounted to `/var/config/gateway/gateway.conf` for the container to use. As an example, if you have the configuration file setup on the host at the location `/tmp/gateway/gateway.conf` then the docker command would be `docker run -ti -v /tmp/gateway:/var/config/gateway quay.io/signalfx/gateway`

### CONFIGURATION

See the <a target="_blank" href="https://github.com/signalfx/gateway/blob/master/exampleGateway.conf">example configuration</a> file for an example of how configuration looks.  Configuration is a JSON file with two important fields: `ListenFrom` and `ForwardTo`.

#### ForwardTo

`ForwardTo` defines the data format that the gateway will transmit, and to where.

| Configuration property | Definition | Example values |
|--------|----------|--------|
| `Name` | A name for this forwarder. | "ourcarbon" |
| `type` | The type of data that the gateway will emit. Possible values are `csv` for writing to a CSV file, `carbon` for sending to a Graphite server, and `signalfx` for sending to SignalFx. | "carbon" |
| `BufferSize` | A performance configuration that specifies how many datapoints/events should be buffered in forwarders.  This is very useful when the gateway is configured with a `StatsDelay`. | `1000000` |
| `MaxDrainSize` | A performance configuration that specifies the maximum amount of datapoints/events to emit in a single outbound request. This is very useful when the gateway is configured with a `StatsDelay`. | `5000` |
| `DrainingThreads` | A performance configuration that specifies how many go routines should drain a buffer. This is very useful when the gateway is configured with a `StatsDelay`. | `50` |

Additional configuration properties differ depending on the type of data being written.


##### SignalFx forwarder

You can write datapoints to SignalFx by configuring a forwarder with the type `signalfx`.

| Configuration property | Definition | Example values |
|--------|----------|--------|
| `DefaultAuthToken` | A SignalFx API token that the gateway will use to transmit data to SignalFx. | "YOUR_SIGNALFX_API_TOKEN" |
| `DisableCompression` | Optionally disables gzip compression when forwarding to SignalFx | `true` |
| `AuthTokenEnvVar` | An environment variable to check for a SignalFx API token | "AUTH_TOKEN_VAR" |

You will need to configure your auth token inside DefaultAuthToken.

    {
        "Type": "signalfx",
        "Name": "testgateway",
        "DefaultAuthToken": "___AUTH_TOKEN___"
    }

Or you can use AuthTokenEnvVar to point to an environment variable that contains your auth token

    {
        "Type": "signalfx",
        "Name": "testgateway",
        "AuthTokenEnvVar": "AUTH_TOKEN_VAR"
    }

where `AUTH_TOKEN_VAR` is set in your environment

    export AUTH_TOKEN_VAR="___AUTH_TOKEN___"

If `AuthTokenEnvVar` is set and available in the environment, it will be preferred to `DefaultAuthToken`. If `DefaultAuthToken` is not set, and the value of `AuthTokenEnvVar` is not available in the environment, the gateway will also check the environment for `SIGNALFX_ACCESS_TOKEN` for a value to use as your auth token

By default gzip compression talking to SignalFx is turned on, if for some
reason you want to turn it off you can disable it in the SignalFx forward config
like this:

    {
        "Type": "signalfx",
        "Name": "testgateway",
        "DefaultAuthToken": "___AUTH_TOKEN___",
        "DisableCompression": true
    }

##### CSV forwarder

You can write datapoints to a CSV file for debugging by configuring a forwarder with the type `csv`.

 | Configuration property | Definition | Example values |
 |--------|----------|--------|
 | `Filename` | Location on disk of a CSV file to write metric data to. | "/var/config/gateway/filewrite.csv" |
 
 You will need to specify the filename.

    {
        "Type": "csv",
        "Filename": "/var/config/gateway/filewrite.csv",
        "Name": "filelocal"
    }

##### Carbon forwarder

You can write datapoints to a carbon server.  If the point came from a carbon
listener, it will write the same way the gateway saw it.

| Configuration property | Definition | Example values |
|--------|----------|--------|
| `Host` | Hostname of a carbon server. | "example.com" |
| `Port` | Port at which carbon is running on `Host`. | 2003 |

    {
        "Type": "carbon",
        "Name": "ourcarbon",
        "Host": "example.com",
        "Port": 2003
    }

#### ListenFrom

`ListenFrom` defines the data format that the gateway will receive, and on what port. It also defines the transformation that the data will undergo, if any.

| Configuration property | Definition | Example values |
|---------------|-------------|-----------|
| `Type` | Defines the listener that will handle the incoming data. Possible listeners are `signalfx`, `carbon`, and `collectd`. | "carbon" |
| `ListenAddr` | Defines the port on which to listen for incoming data. | "0.0.0.0:18080" |
| `Dimensions` | A map of dimension-value pairs that adds the specified dimension to every data point sent by the listener. | { "env": "prod" } |

##### SignalFx listener

You can expose a SignalFx endpoint with the `signalfx` type. A SignalFx
endpoint can listen on all the SignalFx protocols in both `Protocol Buffers`
and `JSON` for events and datapoints (e.g. `/v2/datapoint`, `/v2/event`). It can
also listen on the collectd protocol (`/v1/collectd`).

Additionally, this listener will expose a `/v1/trace` endpoint to ingest trace
spans. Both Jaeger's Thrift wire format and Zipkin's JSON formats (v1 and v2)
are supported.

For this, you will need to specify which port to bind to.  An example config:

    {
        "Type": "signalfx",
        "ListenAddr": "0.0.0.0:18080"
    }

##### Add Tags to Spans

The SignalFx listener has the ability to add tags to every span that passes through it. 
`AdditionalSpanTags` defines a set of tag name/value pairs that will be included on every span.

Warning: The tags defined by `AdditionalSpanTags` will overwrite any existing values that the incoming spans have set for the configured tag names

    {
        "Type": "signalfx",
        "ListenAddr": "0.0.0.0:18080",
        "AdditionalSpanTags": {
            "foo": "bar",
            "key": "value"
        }
    }

##### Identify and Replace variables in Span Names

The SignalFx listener has the ability to identify and replace variables in span names and turn them into tags. It uses regex-based replacement rules. See the [syntax here](https://golang.org/pkg/regexp/syntax/).
For example, with the configuration below, the Gateway would replace span name `/api/v1/document/321083210/update` with `/api/v1/document/{documentId}/update` and add the tag `"documentId":"321083210"` to the span. 

Every rule will be applied in the order they are defined to every span that goes through the listener. The config parameter `SpanNameReplacementBreakAfterMatch` controls whether to stop processing span name replacement rules after the first matching rule for a span. The default value for this parameter is `true`.
Use caution when leveraging this feature: every expression, and the complexity of those expressions, will impact the throughput of the Gateway. Make sure to monitor your Gateway's resource utilization and size your instance accordingly to support your needs.

    {
        "Type": "signalfx",
        "ListenAddr": "0.0.0.0:18080",
        "SpanNameReplacementRules": ["^\/api\/v1\/document\/(?P<documentId>.*)\/update$"],
        "SpanNameReplacementBreakAfterMatch": false
    }

##### Using AdditionalSpanTags and SpanNameReplacementRules Together

If a tag name is configured under both `AdditionalSpanTags` and `SpanNameReplacementRules`, the replacement rule will take precedence, and the additional span tag will only be used if the replacement rule is not matched, effectively creating a default value.
For example, with the configuration below, `documentId` will be replaced with the proper value if it matches the given regex, or set to "None" for all other spans

    {
        "Type": "signalfx",
        "ListenAddr": "0.0.0.0:18080",
        "SpanNameReplacementRules": ["^\/api\/v1\/document\/(?P<documentId>.*)\/update$"],
        "SpanNameReplacementBreakAfterMatch": false,
        "AdditionalSpanTags": {
            "documentId": "None"
        }
    } 

##### Obfuscating Span Tag Metadata

`ObfuscateSpanTags` can be used to replace the value of certain tags in the received trace spans. This can be used if you expect certain tags to contain sensitive information that you want redacted in your trace spans.  The tags to obfuscate can be specified by service name and operation name; both support using `*` for wildcard matching, and have a default value of `*` if left empty. All matching tags will have their value replaced with the string `<obfuscated>`.
For example, with the configuration below, the Gateway will replace the value of the `password` tag with `<obfuscated>` for any span that has a service that starts with `auth` and has an operation name `login`. It will also replace the value of the `zipcode`, `number`, and `CVV` tags with `<obfuscated>` in any span that contains `credit-card` in the operation name, from ANY service.

Use caution when leveraging this feature: every expression will impact the throughput of the Gateway. Make sure to monitor your Gateway's resource utilization and size your instance accordingly to support your needs.

```json
{
    "Type": "signalfx",
    "ListenAddr": "0.0.0.0:18080",
    "RemoveSpanTags": [
        {
            "Service": "auth*",
            "Operation": "login",
            "Tags": ["password"]
        },
        {
            "Operation": "*credit-card*",
            "Tags": ["zipcode", "number", "CVV"]
        }
    ]
}
```

##### Removing Span Tag Metadata

`RemoveSpanTags` can be used to remove certain tags from the received trace spans. This can be used if you expect certain tags to contain sensitive information that you want to remove from your trace spans. Like `ObfuscateSpanTags`, the tags to remove can be specified by service name and operation name; both support using `*` for wildcard matching, and have a default value of `*` if left empty.
For example, with the configuration below, the Gateway will remove the `password` tag in any span that has a service that starts with `auth`.

Use caution when leveraging this feature: every expression will impact the throughput of the Gateway. Make sure to monitor your Gateway's resource utilization and size your instance accordingly to support your needs.

```json
{
    "Type": "signalfx",
    "ListenAddr": "0.0.0.0:18080",
    "ObfuscateSpanTags": [
        {
            "Service": "auth*",
            "Tags": ["password"]
        }
    ]
}
```

##### Span Processing Order of Operations

When evaluating a span, the Gateway will add [`AdditionalSpanTags`](#add-tags-to-spans), then apply [`SpanNameReplacementRules`](#identify-and-replace-variables-in-span-names), then [`ObfuscateSpanTags`](#obfuscating-span-tag-metadata), and finally [`RemoveSpanTags`](#removing-span-tag-metadata). This allows the result of `SpanNameReplacementRules` to be configured as an `Operation` for `ObfuscateSpanTags` or `RemoveSpanTags`. This also ensures that any tags that are matched by `ObfuscateSpanTags` or `RemoveSpanTags` cannot be added by a later step of the processing chain.

##### collectd listener

You can receive data sent by CollectD by setting up a `collectd` endpoint.
For this, you will need to specify which port to bind to.  An example config:

    {
        "Type": "collectd",
        "ListenAddr": "0.0.0.0:18000"
    }

When configuring CollectD, the target URL path will be `/post-collectd`.

##### Prometheus listener

You can use the gateway as prometheus remote storage. To do this, you will
need to specify the port to bind to.  An example config:

    {
        "Type": "prometheus",
        "ListenAddr": "0.0.0.0:12003",
        "ListenPath": "/write"
    }

...and then add the following to your prometheus.yml:

    remote_write:
      - url: "http://hostname:12003/write"

If you want something different than the default endpoint of "/write" you can
specify it with "ListenPath". An alternative example config:

    {
        "Type": "prometheus",
        "ListenAddr": "0.0.0.0:12003",
        "ListenPath": "/receive"
    }

...and then add the following to your prometheus.yml:

    remote_write:
      - url: "http://hostname:12003/receive"

##### Wavefront listener

You can send wavefront metrics to SignalFx through our gateway in the same
fashion as you would have sent them to the wavefront proxy. You will need
to specify the port to bind to.  An example config:

    {
        "Type": "wavefront",
        "ListenAddr": "0.0.0.0:12878",
        "ExtractCollectdDimensions": "false"
    }

You can optionally choose to decode dimensions like we do from collectd style
metrics (although it's applied to all metrics coming in) by changing
`ExtractCollectdDimensions` to true. Default is true. If you were encoding
dimensions using the `[foo=bar]` syntax inside instance and host fields, this
will continue to give you the dimensions you expect.

    {
        "Type": "wavefront",
        "ListenAddr": "0.0.0.0:12878",
        "ExtractCollectdDimensions": "true"
    }

##### Carbon listener

You can pretend to be carbon (the graphite database) with this type.  For
this, you will need to specify the port to bind to.  An example config:

    {
        "Type": "carbon",
        "ListenAddr": "0.0.0.0:12003"
    }

You can optionally choose to listen to carbon over UDP as well (as opposed
to the default of TCP).

    {
        "Type": "carbon",
        "ListenAddr": "0.0.0.0:12003",
        "Protocol": "udp"
    }
    
For incoming carbon (Graphite) data only, the gateway supports transforming long dot-delimited metric names into metrics and dimensions for transmission to SignalFx.


###### Graphite Options

This config will listen using CollectD's HTTP protocol and forward
all those metrics to a single graphite listener.  It will collect
stats at 1s intervals.  It also signals to graphite that when it creates
a graphite name for a metric, it should put the 'source' (which is usually
the gateway) and 'forwarder' (in this case 'graphite-west') first in the
graphite dot delimited name.

    {
      "StatsDelay": "1s",
      "ListenFrom": [
        {
          "Type": "collectd",
          "ListenAddr" : "0.0.0.0:8081"
        }
      ],
    
      "ForwardTo": [
        {
          "Type": "carbon",
          "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
          "Host": "graphite.database.dc1.com",
          "DimensionsOrder": ["source", "forwarder"],
          "Name": "graphite-west"
        }
      ]
    }

###### Graphite Dimensions

This config will pull dimensions out of graphite metrics if they fit the commakeys
format.  That format is "\_METRIC_NAME\_\[KEY:VALUE,KEY:VALUE]".  For example,
"user.hit_rate\[host:server1,type:production]".  It also has the extra option
of adding a metric type to the datapoints.  For example, if one of the
dimensions is "metrictype" in this config and the dimension's value is "count",
then the value is sent upstream as a datapoint.Count.

It also sets the timeout on idle connections to 1 minute, from the default of 30
seconds.

    {
      "StatsDelay": "1s",
      "ListenFrom": [
        {
          "Type": "carbon",
          "ListenAddr" : "0.0.0.0:2003",
          "ConnectionTimeout": "1m",
          "MetricDeconstructor": "commakeys",
          "MetricDeconstructorOptions": "mtypedim:metrictype"
        }
      ],
    
      "ForwardTo": [
        {
          "Type": "signalfx",
          "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
          "Name": "signalfxforwarder"
        }
      ]
    }

###### Graphite Dimensions using Regular Expressions

You can use MetricRules to extract dimensions and metric names from the dot-
separated names of graphite metrics using regular expressions.

A metric will be matched to the first rule that matches the regular expression.
If no groups are specified the entire metric will be used as the metric name
and no dimensions will be parsed out. All groups should be named. If the named
group starts with sf_metric it will be appended together to form the metric
name, otherwise it will become a dimension with the name of the group name,
and the value of what it matches.

For each rule, you can define the following:

1. Regex - REQUIRED - regular expression with optionally named matching groups
1. AdditionalDimensions - used to add static dimensions to every metric that
   matches this rule
1. MetricType - to set the specific type of metric this is; default is gauge
1. MetricName - if present this will be the first part of the metricName.  If
   no named groups starting with sf_metric are specified, this will be the
   entire metric name.

e.g.

    {
      "Type": "carbon",
      "ListenAddr": "0.0.0.0:2003",
      "MetricDeconstructor": "regex",
      "MetricDeconstructorOptionsJSON": {
        "FallbackDeconstructor": "nil",
        "MetricRules": [
          {
            "Regex": "(?P<sf_metric_0>foo.*)\\.(?P<middle>.*)(?P<sf_metric_1>\\.baz)",
            "AdditionalDimensions": {
              "key": "value"
            }
          },
          {
            "Regex": "(?P<sf_metric>counter.*)",
            "MetricType": "cumulative_counter"
          },
          {
            "Regex": "madeup.*",
            "MetricName": "synthetic.metric"
          },
          {
            "Regex": "common.*"
          }
        ]
      }
    }

In the above example, if you sent in the metric foo.bar.baz it would match the
first rule and the metric name would become foo.baz with a dimensions of
"middle":"bar", and then an additional metric with "key":"value" added and the
type would be the default of gauge.

If you sent in the metric "counter.page_views" the resulting metric name would
continue to be "counter.page_views" (because you named it sf_metric)_but have
the type of cumulative counter.  No dimensions are being extracted or added in
this example.

If you sent in the metric "madeup.page_faults" the resulting metric name would
be "synthetic.metric" with type gauge.

If you sent in the metric "common.page_load_max", the resulting metric name
would continue to be "common.page_load_max" (because no groups were specified)
of type gauge.

If you sent in the metric "albatros.cpu.idle", this would fall through and go
to the FallbackDeconstructor and in this case since we're using the nil
deconstructor, be rejected and won't be passed on to SignalFx.

###### Graphite Dimensions using Delimiters

You can use MetricRules to extract dimensions from the dot-separated names of
graphite metrics.

A metric will be matched to only one matching rule. When multiple rules are
provided, they are evaluated for a match to a metric in the following order:

1. The rule must contain the same number of terms as the name of the metric to
  be matched.
1. If there is more than one rule with the same number of terms as the metric
  name, then matches will be evaluated in the order in which they are defined in
  the config.
1. If there are no rules that match the metric name, the FallbackDeconstructor
  is applied. By default this is "identity": all metrics are emitted as gauges
  with unmodified names.

The simplest rule contains only a DimensionsMap with the same number of terms
and separated by the same delimiter as the incoming metrics. In the following
example, the configuration contains two rules: one that matches all metrics
with four terms, and one that matches all metrics with six terms.

If the following example config were used to process a graphite metric called
`cassandra.cassandra23.production.thread_count`, it would output the following:

    metricName = thread_count
    metricType = Gauge
    dimensions = {service=cassandra, instance=cassandra23, tier=production}

Config

    {
      "ListenFrom": [
        {
          "Type": "carbon",
          "ListenAddr": "0.0.0.0:2003",
          "MetricDeconstructor": "delimiter",
          "MetricDeconstructorOptionsJSON": {
            "MetricRules": [
              {
                "DimensionsMap": "service.instance.tier.%"
              },
              {
                "DimensionsMap": "service.instance.tier.module.submodule.%"
              }
            ]
          }
        }
      ],
      "ForwardTo": [
        {
          "Type": "signalfx",
          "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
          "Name": "signalfxforwarder"
        }
      ]
    }


You can define more complex rules for determining the name, type and dimensions
of metrics to be emitted. In this next more complex example, we first define
Dimensions that will be added to every datapoint ('customer: Acme'). We then
explicitly define the metrics that will be sent in as counters rather than
gauges (anything that ends with 'counter.count' or starts with 'counter').

Define a MetricPath separately from the DimensionsMap to match only certain
metrics.

In the example below, the MetricPath `kafka|cassandra.*.*.*.!database`
matches metrics under the following conditions:

1. If the first term of the metric name separated by '.' matches either
  'kafka' or 'cassandra'
1. And the metric contains exactly 10 terms
1. And the fifth term des not match the string 'database'

The MetricPath is followed by a DimensionsMap:
`component.identifier.instance.-.type.tier.item.item.%.%`

1. The first three terms in the metric will be mapped to dimensions as
  indicated in the DimensionsMap: 'component', 'identifier', and 'instance',
  respectively.
1. The fourth term in the metric will be ignored, since it's specified in the
  DimensionsMap as the default ignore character '-'.
1. The fifth and sixth terms will be mapped to dimensions 'type' and 'tier',
  respectively.
1. The seventh and eighth terms will be concatenated together delimited by
  the default separator character '.', because they are both mapped to the
  dimension called 'item'.
1. The ninth and tenth terms are '%', the default metric character, which
  indicates that they should be used for the metric name.

This config also contains MetricName, the value of which will be prefixed onto
the name of every metric emitted.

Finally, note that the MetricPath contains five terms, but the DimensionsMap
contains ten. This means that the MetricPath implicitly contains five
additional metric terms that are '*' (match anything).

If this config were used to process a metric named
`cassandra.bbac.23.foo.primary.prod.nodefactory.node.counter.count`, it would
output the following:

    metricName = tiered.counter.count
    metricType = counter
    dimensions = {customer=Acme, component=cassandra, identifier=bbac,
                  instance=23, type=primary, tier=prod, item=nodefactory.node,
                  business_unit=Coyote}

Config

    {
      "ListenFrom": [
        {
          "Type": "carbon",
          "ListenAddr": "0.0.0.0:2003",
          "MetricDeconstructor": "delimiter",
          "MetricDeconstructorOptionsJSON": {
            "Dimensions": {
              "customer": "Acme"
            },
            "TypeRules": [
              {
                "MetricType": "counter",
                "EndsWith": "counter.count"
              },
              {
                "MetricType": "cumulative_counter",
                "StartsWith": "counter"
              }
            ],
            "FallbackDeconstructor": "nil",
            "MetricRules": [
              {
                "MetricPath": "kafka|cassandra.*.*.*.!database",
                "DimensionsMap": "component.identifier.instance.-.type.tier.item.item.%.%",
                "Dimensions": {
                  "business_unit": "Coyote"
                },
                "MetricName": "tiered"
              }
            ]
          }
        }
      ],
      "ForwardTo": [
        {
          "Type": "signalfx",
          "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
          "Name": "signalfxforwarder"
        }
      ]
    }

The following is a full list of overrideable options and their defaults:

    // For the top level
    {
      "Delimiter":".",
      "Globbing":"*",
      "OrDelimiter":"|",
      "NotDelimiter":"!",
      "IgnoreDimension":"-",
      "MetricIdentifer":"%",
      "DefaultMetricType":"Gauge",
      "FallbackDeconstructor":"identity",
      "FallbackDeconstructorConfig":"",
      "TypeRules":[],
      "MetricRules":[],
      "Dimensions":{}
    }
    // A MetricRule
    {
      "MetricType":"Gauge", // overrides the DefaultMetricType or TypeRules
      "MetricPath":"",
      "DimensionsMap":"",
      "MetricName":"",
      "Dimensions":{}
    }
    // A TypeRule. If StartsWith and EndsWith are both specified, they must both match.
    {
      "MetricType":"Gauge",
      "StartsWith":"",
      "EndsWith":""
    }

#### Other Configuration Options


| Configuration property | Definition | Example values |
|--------|----------|--------|
| `StatsDelay` | If and how often we should self report metrics about the gateway out all forwarders | "1s" |
| `ServerName` | All self-reported metrics emitted from the gatway have a `host` dimension. If this is not set it will be the name of current host system | "gateway-staging-1" |
| `AdditionalDimensions` | Any additional dimensions you might want to add to all self reported metrics | `{"cluster":"staging-west-1"}` |


### USAGE

SignalFx Gateway can help you get the right data to the right destination in many different scenarios.

#### Running the daemon

    /etc/init.d/gateway start

#### Stopping the daemon

    /etc/init.d/gateway stop

#### Health checks

Health checks are available on the listening port of any collectd or
SignalFx listener. E.g.  If you had a SignalFx listener at `8080`, the
healthcheck would be located at `http://localhost:8080/healthz`.
Healthchecks are useful when putting the gateway behind a loadbalancer.

#### Graceful Shutdown
The SignalFx Gateway will begin shutting down gracefully 
when it receives a `SIGTERM`.

During graceful shutdown all health checks will prevent
load balancers from initiating new connections.  Every `GracefulCheckInterval`
the number of in flight datapoints and events are checked until there are 0 
for the duration specified by `SilentGracefulTime`, or graceful shutdown has exceeded
the `MaxGracefulWaitTime`.  When the graceful shutdown has completed or timed out, 
all listeners and forwarders will be closed and the process will exit. 

If the SignalFx Gateway is in front of a load balancer the recommended `MaxGracefulWaitTime` 
is `30s`.  This gives the load balancer time to hit the health check and divert traffic.

The `MaxGracefulWaitTime` will always be hit if there is no load balancer in front of the gateway.
If no load balancer is in use, the recommended `MaxGracefulWaitTime` is `1s`

Example:

    {
      "MaxGracefulWaitTime": "1s",
      "GracefulCheckInterval": "1s",
      "SilentGracefulTime": "2s",
      "StatsDelay": "1s",
      "LogDir": "/tmp",
      "ListenFrom": [
        {
          "Type": "carbon",
          "ListenAddr": "0.0.0.0:2003"
        },
        {
          "Type": "signalfx",
          "ListenAddr": "0.0.0.0:8080"
        }
      ],
      "ForwardTo": [
        {
          "Type": "signalfx",
          "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
          "Name": "signalfxforwarder"
        }
      ]
    }
 
#### Sending SignalFx data to SignalFx

This config listens using the SignalFx protocol, buffers, then forwards
points to SignalFx.

    {
      "StatsDelay": "1s",
      "ListenFrom": [
        {
          "Type": "signalfx",
          "ListenAddr" : "0.0.0.0:8080"
        }
      ],
    
      "ForwardTo": [
        {
          "Type": "signalfx",
          "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
          "Name": "signalfxforwarder"
        }
      ]
    }

#### Sending data to multiple destinations

You can use the gateway to duplicate a data stream to multiple destinations. Add each destination to the `ForwardTo` block as in the following example.

    "ForwardTo": [
      {
        "Type": "signalfx",
        "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
        "Name": "signalfxforwarder"
      },
      {
        "Filename": "/tmp/filewrite.csv",
        "Name": "filelocal",
        "Type": "csv"
      }
    ]

#### Sending To Alternate Ingest Targets

You can configure the forwarder to send to alternate ingest endpoints such as another Gateway or an alternate SignalFx Deployment.
The SignalFx Gateway sends to the `us0` realm by default. If you are not in this realm, you will need to explicitly set the
endpoint urls above as shown below. To determine if you are in a different realm (YOUR_SIGNALFX_REALM) and need to
explicitly set the endpoints, check your profile page in the SignalFx web application. 

| Key | Description | Default |
| --- | ----------- | ------- |
| `URL` | Datapoint ingest url. | `https://ingest.us0.signalfx.com/v2/datapoint` |
| `EventURL` | Event ingest url. | `https://ingest.us0.signalfx.com/v2/event` |
| `TraceURL` | Trace ingest url. | `https://ingest.us0.signalfx.com/v1/trace` |


    "ForwardTo": [
      {
        "Type": "signalfx",
        "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
        "Name": "signalfxforwarder"
        "URL": "https://ingest.YOUR_SIGNALFX_REALM.signalfx.com/v2/datapoint",
        "EventURL": "https://ingest.YOUR_SIGNALFX_REALM.signalfx.com/v2/event",
        "TraceURL": "https://ingest.YOUR_SIGNALFX_REALM.signalfx.com/v1/trace"
      },
      {
        "Filename": "/tmp/filewrite.csv",
        "Name": "filelocal",
        "Type": "csv"
      }
    ]

#### HTTP Proxy Support

The SignalFx Gateway supports the use of http proxies configured 
via environment variable.  Setting the environment variable `HTTP_PROXY` to an
http proxy will make the SignalFx Gateway proxy all connections through the specified host and port.
This can be put into the start script, or as part of the environment sent into the container
if using a container solution like maestro.

Example:

    HTTP_PROXY="http://proxyhost:proxyport"

### SignalFx Performance Options

This config below listens for carbon data on port 2003 and forwards it to SignalFx
using an internal datapoint buffer size of 1,000,000 and sending with 50 threads
simultaneously with each thread sending no more than 5,000 points in a single
call.

StatsDelay being set to 10s means every 10s we'll emit metrics out all
forwarders about the running Gateway.  If you don't want these metrics, omit
this config value. These metrics are emitted with both host and
cluster dimensions. The host dimension will be set to the value of the
ServerName set in the config file or to the hostname of the machine by default.
The cluster dimension will be set to what you set in the config file, or to
the default value of "gateway".

Also note that we're setting LateThreshold and FutureThreshold to 10s.  This means
we'll count datapoints, events and spans that exceed those thresholds (if set) and
log them up to one per second. When you've turned on as described immediately above
you'll see metrics named late.count and future.count emitted counting each type of
data that was late or in the future respectively.

    {
      "StatsDelay": "10s",
      "ServerName": "gateway-us-east1",
      "LateThreshold": "10s",
      "FutureThreshold": "10s",
      "ListenFrom": [
        {
          "Type": "carbon",
          "ListenAddr" : "0.0.0.0:2003"
        }
      ],
    
      "ForwardTo": [
        {
          "Type": "signalfx",
          "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
          "Name": "signalfxforwarder",
          "BufferSize": 1000000,
          "DrainingThreads": 50,
          "MaxDrainSize": 5000
        }
      ]
    }

An alternative to using the above `StatsDelay` is to have the gateway provide a
signalfx datapoint endpoint that contains the same information but can be
scraped by our Smart Agent.  If you set the config
`InternalMetricsListenerAddress` to a host port combination and configure
the smart gateway to scrape that for internal metrics at `/internal-metrics`
it would accomplish the same thing.

#### Transforming carbon dot-delimited metric names into metrics with dimensions

SignalFx's chart builder supports treating components of metric names as dimensions for the purpose of chart building. However, it can be more efficient to define dimensions once, before transmission, rather than many times afterward when building charts. Use the SignalFx Gateway's `MetricDeconstructor` for the carbon listener to transform Graphite's long dot-delimited metric names into metrics with dimensions before transmission to SignalFx. <a target="_blank" href="https://github.com/signalfx/gateway#graphite-dimensions">Click here to read more on Github about MetricDeconstructor options</a>.

Note that you can apply different MetricDeconstructor rules in each `ForwardTo` destination.

#### Concentrate outgoing HTTP connections

SignalFx recommends instrumenting each host with the SignalFx collectd agent, which transmits data to SignalFx over HTTP using the `write_http` plugin. In some environments it is not desirable for every host to maintain its own out-of-network HTTP connection: for instance, when a firewall is in use. In this scenario, you can deploy the SignalFx Gateway, configure each collectd instance to transmit to the gateway, then configure your network to authorize just the gateway to transmit outside the firewall to SignalFx.

Because the SignalFx Gateway multiplexes incoming traffic from incoming instances of collectd, it sends larger, more efficient messages to SignalFx. For this reason, it is also a good fit when servers have high transmission latency to the region where SignalFx is located. Forwarding metrics through the gateway reduces hosts' exposure to transmission latency. The gateway can be configured to buffer in-memory if needed.

#### Simplify configuration of collectd

The SignalFx Gateway provides one single point of configuration management. Configuring the gateway with your SignalFx API token (YOUR_SIGNALFX_API_TOKEN) allows you to manage the token once, on the gateway, rather than on each individual agent.

In addition, because the SignalFx Gateway can apply dimensions to all outgoing data points, you can use it to annotate metrics from many instances of collectd at once, with information of which individual collectd hosts may not be aware. This can make it easier to add new context to your metrics.

#### Teeing a subset of metrics on a forwarder

The config listens on signalfx and graphite, and forwards everything to
graphite, and a smaller subset (excludes anything starting with cpu) to SignalFx.
Below any metric starting with cpu will be denied, except for cpu.idle.
If only allow was specificed, those that matched would be allowed and those
that failed would be denied.  If only deny was provided those that matched
would be denied and those that were not would be allowed.


    {
      "StatsDelay": "1s",
      "LogDir": "/tmp",
      "ListenFrom": [
        {
          "Type": "carbon",
          "ListenAddr": "0.0.0.0:2003"
        },
        {
          "Type": "signalfx",
          "ListenAddr": "0.0.0.0:8080"
        }
      ],
      "ForwardTo": [
        {
          "Type": "carbon",
          "Name": "ourcarbon",
          "Host": "example.com",
          "Port": 2003
        },
        {
          "Type": "signalfx",
          "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
          "Name": "signalfxforwarder",
          "Filters": {
            "Deny": [
              "^cpu"
            ],
            "Allow": [
              "^cpu.idle$"
            ]
          }
        }
      ]
    }

### Debugging

#### Status page and profiling

The SignalFx Gateway utilizes pprof to provide diagnostic information about the gateway.

To enable pprof configure `LocalDebugServer` in the `gateway.conf` file 
with an address and port to serve information on.

    {
      "LocalDebugServer": "0.0.0.0:6009"
    }

* View configuration information at `http://<address>:<port>/debug/vars`.
* Explore objects in memory at `http://<address>:<port>/debug/explorer/`.
* View pprof info at `http://<address>:<port>/debug/pprof/`.

You can learn more about pprof on [the pprof help page](http://golang.org/pkg/net/http/pprof/).

#### Debugging via logfile

    cd /var/log/gateway
    tail -F *

#### Debugging connections via headers

1. Setup a debug config

        {
          "DebugFlag": "secretdebug",
          "ForwardTo": [
            {
              "Type": "signalfx",
              "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
              "Name": "signalfxforwarder"
            }
        }
    
2. Then, send a request with the debug header set to `secretdebug`

        curl -H "X-Debug-Id:secretdebug" -H "Content-Type: application/json" -XPOST -d '{"gauge": [{"metric":"bob", "dimensions": {"org":"dev"}, "value": 3}]}' localhost:8080/v2/datapoint
        
    The config will tell the HTTP request to debug each datapoint sent with X-Debug-Id
    set to secretdebug and log statements will show when each item is through the gateway pipeline.

#### Debugging connections via debug dimensions

1. Setup a local debug server and specify which dimensions are
logged out.

        {
          "LocalDebugServer": "0.0.0.0:6060",
          "ForwardTo": [
            {
              "Type": "signalfx",
              "DefaultAuthToken": "YOUR_SIGNALFX_API_TOKEN",
              "Name": "signalfxforwarder"
            }
        }

2. Then set which dimensions to debug via a POST.

        curl -XPOST -d '{"org":"dev"}' localhost:6060/debug/dims
    
        # Any datapoints with the "org" dimension of "dev" will be logged.


### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
