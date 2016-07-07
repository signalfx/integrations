---
title: SignalFx Metric Proxy
brief: Aggregate and translate metrics before forwarding to SignalFx.
---

# ![](https://github.com/signalfx/integrations/blob/master/metricproxy/img/integrations_metricproxy.png) SignalFx Metric Proxy

_This is a directory that consolidates metadata associated with the SignalFx Metric Proxy. The relevant code for the project can be found [here](https://github.com/signalfx/metricproxy)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

### DESCRIPTION

Use the SignalFx Metric Proxy to aggregate metrics and send them to SignalFx. It is a multilingual datapoint demultiplexer that can accept time series data from the carbon (Graphite), collectd or SignalFx protocols and emit those datapoints to a series of servers using the carbon, collectd or SignalFx protocols. 

### REQUIREMENTS AND DEPENDENCIES

All dependencies for this Go project are included in `/Godeps` in the project repository. 

We recommend placing the proxy either on the same server as another existing metrics aggregator or on a central server that is already receiving datapoints, such as Graphite's carbon database.

The size of the machine that hosts the proxy depends on the amount of data that will be transmitted through it. The key performance indicator for the host is CPU idle (higher is better). A host comparable to AWS's c3.2xlarge is known to handle up to approximately 7 million DPM (data points per minute) while reporting 70% CPU idle. For safety, we recommend large margins here - running close to resource limits risks delayed data transmission, especially if the rate of data points is variable. 

### INSTALLATION

1. Identify a server on which to deploy the SignalFx Metric Proxy will run.
1. Edit the file `sfdbconfig.conf` to configure the proxy. Example configurations are given [below](#configuration).
1. Use the [install script](https://github.com/signalfx/metricproxy/blob/master/install.sh) to install or upgrade the proxy, as follows. 

 ```
  curl -s https://raw.githubusercontent.com/signalfx/metricproxy/master/install.sh | sudo sh
  # Config at    /etc/sfdbconfig.conf
  # Binary at    /opt/sfproxy/bin/metricproxy
  # Logs at      /var/log/sfproxy
  # PID file at  /var/run/metricproxy.pid
 ```
1. Start the proxy as follows:

  ```
    /etc/init.d/metricproxy start
  ```
  
1. Begin transmitting data to the host and port on which the proxy is running. The data will be transformed and forwarded as specified in the [configuration](#configuration). 

#### Note: Deploying using Docker

 The proxy is packaged as a Docker image that is built and deployed
 to [quay.io](https://quay.io/repository/signalfx/metricproxy). This image does not include configuration. To use this image, ensure that you have a sfdbconfig.json file cross-mounted to
 `/var/config/sfproxy/sfdbconfig.json` for the container to use.

### CONFIGURATION

#### Config file format

See the [example configuration](exampleSfdbproxy.conf) file for an example of how
configuration looks.  Configuration is a JSON file with two important fields:
`ListenFrom` and `ForwardTo`.

`ListenFrom` defines the data format that the proxy will receive, and on what port. It also defines the transformation that the data will undergo, if any. `ForwardTo` defines the data format that the proxy will transmit, and to where. 

##### ListenFrom

ListenFrom is where you define what services the proxy will pretend to be and
what ports to listen for those services on.

##### signalfx

You can pretend to be a signalfx endpoint with the signalfx type.  For this,
you will need to specify which port to bind to.  An example config:

```
        {
            "ListenAddr": "0.0.0.0:18080",
            "Type": "signalfx"
        },
```

##### carbon (for read)

You can pretend to be carbon (the graphite database) with this type.  For
this, you will need to specify the port to bind to.  An example config:

```
        {
            "ListenAddr": "0.0.0.0:12003",
            "Type": "carbon"
        }
```

##### common properties

All listeners support a "Dimensions" property which is expected to be a
map(string => string) and adds the dimensions to all points sent.  For example:

        {
            "ListenAddr": "0.0.0.0:18080",
            "Dimensions": { "env": "prod" },
            "Type": "signalfx"
        }

#### ForwardTo

ForwardTo is where you define where the proxy should send datapoints.  Each datapoint
that comes from a ListenFrom definition will be send to each of these.

##### csv

You can write datapoints to a CSV file for debugging with this config.  You
will need to specify the filename.

```
        {
            "Filename": "/tmp/filewrite.csv",
            "Name": "filelocal",
            "type": "csv"
        }
```

##### carbon (for write)

You can write datapoints to a carbon server.  If the point came from a carbon
listener, it will write the same way the proxy saw it.  Host/Port define where
the carbon server is.

```
        {
            "Name": "ourcarbon",
            "Host": "example.com",
            "Port": 2003,
            "type": "carbon"
        },
```

##### signalfx-json

You can write datapoints to SignalFx with this endpoint.  You will need to
configure your auth token inside DefaultAuthToken.

```
        {
            "type": "signalfx-json",
            "DefaultAuthToken": "___AUTH_TOKEN___",
            "Name": "testproxy",
        },
```

### Example configs

#### Basic

This config will listen for graphite metrics on port 2003 and forward them
to signalfx with the token ABCD.  It will also report local stats
to signalfx at 1s intervals

```
{
  "StatsDelay": "1s",
  "LogDir": "/var/log/sfproxy",
  "ListenFrom": [
    {
      "Type": "carbon",
      "ListenAddr" : "0.0.0.0:2003",
      "Timeout" : "2m"
    },
  ],

  "ForwardTo": [
    {
      "type": "signalfx-json",
      "DefaultAuthToken": "ABCD",
      "Name": "signalfxforwarder"
    }
  ]
}
```

#### Graphite Options

This config will listen using CollectD's HTTP protocol and forward
all those metrics to a single graphite listener.  It will collect
stats at 1s intervals.  It also signals to graphite that when it creates
a graphite name for a metric, it should put the 'source' (which is usually
proxy) and 'forwarder' (in this case 'graphite-west') first in the graphite
dot delimited name.

```
{
  "StatsDelay": "1s",
  "ListenFrom": [
    {
      "Type": "collectd",
      "ListenAddr" : "0.0.0.0:8081",
    },
  ],

  "ForwardTo": [
    {
      "type": "carbon",
      "DefaultAuthToken": "ABCD",
      "Host": "graphite.database.dc1.com",
      "DimensionsOrder": ["source", "forwarder"],
      "Name": "graphite-west"
    }
  ]
}
```

#### Graphite Dimensions

This config will pull dimensions out of graphite metrics if they fit the commakeys
format.  That format is "\_METRIC_NAME\_\[KEY:VALUE,KEY:VALUE]".  For example,
"user.hit_rate\[host:server1,type:production]".  It also has the extra option
of adding a metric type to the datapoints.  For example, if one of the
dimensions is "metrictype" in this config and the dimension's value is "count",
then the value is sent upstream as a datapoint.Count.

It also sets the timeout on idle connections to 1 minute, from the default of 30
seconds.

```
{
  "StatsDelay": "1s",
  "ListenFrom": [
    {
      "Type": "carbon",
      "ListenAddr" : "0.0.0.0:2003",
      "Timeout": "1m",
      "MetricDeconstructor": "commakeys",
      "MetricDeconstructorOptions": "mtypedim:metrictype"
    },
  ],

  "ForwardTo": [
    {
      "type": "signalfx-json",
      "DefaultAuthToken": "ABCD",
      "Name": "signalfxforwarder",
    }
  ]
}
```

#### Graphite Dimensions using Regular Expressions

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

```
  "FallbackDeconstructor": nil,
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
```

In the above example, if you sent in the metric foo.bar.baz it would match the
first rule and the metric name would become foo.baz with a dimensions of
"middle":"bar", and then an additional metric with "key":"value" added and the
type would be the default of gauge.

If you sent in the metric "counter.page_views" the resulting metric name would
continue to be "counter.page_views" (because you named it sf_metric) but have
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

#### Graphite Dimensions using Delimiters

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

```
metricName = thread_count
metricType = Gauge
dimensions = {service=cassandra, instance=cassandra23, tier=production}
```

```
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
      "type": "signalfx-json",
      "DefaultAuthToken": "ABCD",
      "Name": "signalfxforwarder"
    }
  ]
}
```

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
additional metric terms that are `*` (match anything).

If this config were used to process a metric named
`cassandra.bbac.23.foo.primary.prod.nodefactory.node.counter.count`, it would
output the following:

```
metricName = tiered.counter.count
metricType = counter
dimensions = {customer=Acme, component=cassandra, identifier=bbac,
              instance=23, type=primary, tier=prod, item=nodefactory.node,
              business_unit=Coyote}
```

```
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
            "MetricType": "count",
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
      "type": "signalfx-json",
      "DefaultAuthToken": "ABCD",
      "Name": "signalfxforwarder"
    }
  ]
}
```

The following is a full list of overridable options and their defaults:

```
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
```

### SignalFx perf options

This config listens for carbon data on port 2003 and forwards it to SignalFx
using an internal datapoint buffer size of 1,000,000 and sending with 50 threads
simultaneously with each thread sending no more than 5,000 points in a single
call.  It also turns on debug logging, which will spew a large number of log
messages.  Only use debug logging temporarily.

```
{
  "StatsDelay": "1s",
  "LogLevel": "debug",
  "ListenFrom": [
    {
      "Type": "carbon",
      "ListenAddr" : "0.0.0.0:2003"
    },
  ],

  "ForwardTo": [
    {
      "type": "signalfx-json",
      "DefaultAuthToken": "ABCD",
      "Name": "signalfxforwarder",
      "BufferSize": 1000000,
      "DrainingThreads": 50,
      "MaxDrainSize": 5000
    }
  ]
}
```

### CollectD listener dimensions

The CollectD listener supports setting dimensions on all received metrics with
the Dimensions attribute which expects a map of string => string.

```
{
  "StatsDelay": "1s",
  "ListenFrom": [
    {
      "Type": "collectd",
      "ListenAddr" : "0.0.0.0:8081",
      "Dimensions" : {"hello": "world"}
    },
  ],

  "ForwardTo": [
    {
      "type": "carbon",
      "DefaultAuthToken": "ABCD",
      "Host": "graphite.database.dc1.com",
      "DimensionsOrder": ["source", "forwarder"],
      "Name": "graphite-west"
    }
  ]
}
```

### SignalFx to SignalFx

This config listens using the signalfx protocol, buffers, then forwards
points to signalfx.

```
{
  "StatsDelay": "1s",
  "ListenFrom": [
    {
      "Type": "signalfx",
      "ListenAddr" : "0.0.0.0:8080",
    },
  ],

  "ForwardTo": [
    {
      "type": "signalfx-json",
      "DefaultAuthToken": "ABCD",
      "Name": "signalfxforwarder",
    }
  ]
}
```

### Status Page and profiling

This config only loads a status page.  You can see status information at
`http://localhost:6009/status`, a health check page (useful for load balances) at
`http://localhost:6009/health`, and pprof information at
`http://localhost:6009/debug/pprof/`.  You can learn more about pprof for golang
on [the pprof help page](http://golang.org/pkg/net/http/pprof/).

```
{
  "LocalDebugServer": "0.0.0.0:6009"
}
```

### Debugging connections via headers

Setup a debug config

```
{
  "DebugFlag": "secretdebug",
  "ForwardTo": [
    {
      "type": "signalfx-json",
      "DefaultAuthToken": "ABCD",
      "Name": "signalfxforwarder",
    }
}
```

Then, send a request with the debug header set to secretdebug.

```
curl -H "X-Debug-Id:secretdebug" -H "Content-Type: application/json" -XPOST \
   -d '{"gauge": [{"metric":"bob", "dimensions": {"org":"dev"}, "value": 3}]}' localhost:8080/v2/datapoint
```

The config will tell the HTTP request to debug each datapoint sent with X-Debug-Id
set to secretdebug and log statements will show when each item is through the
proxy pipeline.

### Debugging connections via debug dimensions

Setup a local debug server, then you can configure which dimensions are
logged out.

```
{
  "LocalDebugServer": "0.0.0.0:6060",
  "ForwardTo": [
    {
      "type": "signalfx-json",
      "DefaultAuthToken": "ABCD",
      "Name": "signalfxforwarder",
    }
}
```

Then set which dimensions to debug via a POST.

```
curl -XPOST -d '{"org":"dev"}' localhost:6060/debug/dims
```

Then, any datapoints with the "org" dimension of "dev" will be logged.

### USAGE

There are several scenarios in which the SignalFx metric proxy can help you get the right data to the right destination. 

#### Sending data to multiple destinations

You can use the proxy to duplicate a data stream to multiple destinations. Add each destination to the `ForwardTo` block as in the following example.

```
"ForwardTo": [
  {
    "type": "signalfx-json",
    "DefaultAuthToken": "ABCD",
    "Name": "signalfxforwarder",
  },
  {
    "Filename": "/tmp/filewrite.csv",
    "Name": "filelocal",
    "type": "csv"
  }
] 
```

#### Transforming carbon dot-delimited metric names into metrics with dimensions

SignalFx's chart builder supports treating components of metric names as dimensions for the purpose of chart building. However it may be more efficient to define dimensions once before transmission, rather than many times afterward in charts. Use the proxy's MetricDeconstructor features to transform carbon (Graphite)'s long dot-delimited metric names into metrics with dimensions before transmission to SignalFx. 

Note that you can apply MetricDeconstructor in individual `ForwardTo` destinations. 

#### Concentrate outgoing HTTP connections

SignalFx recommends instrumenting each host with the SignalFx collectd agent, which transmits data to SignalFx over HTTP using the `write_http` plugin. In some environments it is not desirable for every host to maintain its own out-of-network HTTP connection: for instance, when a firewall is in use. In this scenario, you can deploy the metric proxy, configure each collectd instance to transmit to the metric proxy instead of directly to SignalFx, then authorize just the metric proxy to transmit outside the firewall. 

#### Buffer outgoing traffic

To guard against dropped data from network disruption, the metric proxy can be used as data buffer external to the SignalFx collectd agent. If collectd is unable to transmit data, it will buffer data points in memory which may impact the host being monitored. If collectd always transmits to the metric proxy within network, the metric proxy host assumes the risk of buffering points to memory when external transmissions are disrupted. This ensures that the inability to transmit data alone will not impact performance of services monitored. 

#### Simplify configuration of collectd

Because the metric proxy can apply dimensions to all outgoing data points, you can use it to annotate metrics from many instances of collectd at once, with information of which individual collectd hosts may not be aware. This can make it easier to add new context to your metrics. 

### LICENSE

This product is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/metricproxy/blob/master/LICENSE) for more details.
