# ![](https://github.com/signalfx/integrations/blob/master/appdynamics/img/integrations_appdynamics.png) AppDynamics   

Metadata associated with the AppDynamics Integration can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/appdynamics">here</a>. The relevant code for the integration can be found <a target="_blank" href="https://github.com/signalfx/appd-integration">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

This is the SignalFx AppDynamics integration, which brings metrics captured through AppDynamics into SignalFx.

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| Java  |  7.0 or later  |
| Maven | (match with Java version) |

### INSTALLATION

The <a target="_blank" href="https://github.com/signalfx/appd-integration/tree/master/appd-report-standalone">appd-report-standalone</a> module is a standalone process that parses configurations and reports
AppDynamics metrics at specified intervals.

Install this module as follows:

```
maven install
cd appd-report-standalone
maven exec:java
```

### CONFIGURATION

Provide configuration to this process by setting environment variables as follows.

#### Required Environment Variables

| Variable name | Definition |
|---------------|------------|
| APPD_USERNAME | AppDynamics username |
| APPD_PASSWORD | AppDynamics password |
| APPD_HOST | AppDynamics hostname |
| SIGNALFX\_TOKEN | YOUR_SIGNALFX_API_TOKEN |
| SIGNALFX\_APPD\_METRICS | Name of the metrics configuration file (default: metrics.json) |
| APPD\_INTERVAL | Frequency in minutes with which metrics will be sent to SignalFx (default: 1 minute) |

### USAGE

<a target="_blank" href="https://github.com/signalfx/appd-integration/blob/master/appd-report-standalone/metrics.json">Metrics.json</a> contains configurations for the list of apps, metrics inside each app, and dimensions mapping for each app.

AppDynamics metric paths are described as a pipe-delimited string (|), as follows: `Performance|AppServer1|Resources|CPU`

Each metric is reported to SignalFx with the last element of this path as the metric name,
and each previous element is mapped to a dimension according to the dimensionsPathMap.

Elements can be ignored by specifying the target dimension as - (dash) in the dimensionsPathMap.

Wild cards `*` can be used to specify that all matching AppDynamics metrics are
to be collected. Mapping to dimensions through the dimensionsPathMap will still happen on
the actual value of that metric path element.

Example with ignoring element:

```
MetricPath = Performance|AppServer1|Resources|CPU
DimensionsPathMap = category|host|-

would be mapped to
{
    metric_name : "CPU"
    dimensions {
        category: "Performance",
        host: "AppServer1"
    }
}
```

Example with wildcard:

```
MetricPath = Performance|*|Resources|CPU
DimensionsPathMap = category|host|-

If the entity at the second level matches both 'Server1' and 'Server2'. We would get 2 metric
time series as
{
    metric_name : "CPU"
    dimensions {
        category: "Performance",
        host: "Server1"
    }
},
{
    metric_name : "CPU"
    dimensions {
        category: "Performance",
        host: "Server2"
    }
}
```

Optional extra dimensions can also be specified for each metric path.

### Process Status Metrics

appd-report-standalone also reports metrics pertaining to the syncing process to SignalFx.

That includes:
- mtsReported
- mtsEmpty
- dataPointsReported
- appdRequestFailure

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
