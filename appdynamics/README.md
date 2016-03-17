---
title: AppDynamics Integration
brief: For sending AppDynamics metrics to SignalFx.
---

# ![](https://github.com/signalfx/integrations/blob/master/appdynamics/img/integrations_appdynamics.png) AppDynamics Integration   

_This is a directory to consolidate all the metadata associated with the AppDynamics Integration. The relevant code for the integration can be found [here](https://github.com/signalfx/appd-integration)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx AppDynamics integration, which brings metrics captured through AppDynamics into SignalFx.

### REQUIREMENTS AND DEPENDENCIES

| Software  | Version        |
|-----------|----------------|
| Java  |  7.0 or later  |


### INSTALLATION

The [`appd-report-standalone` module](https://github.com/signalfx/appd-integration/tree/master/appd-report-standalone) is a standalone process that parses configurations and reports
AppDynamics metrics at specified intervals.

To install this module:
```
maven install
cd appd-report-standalone
maven exec:java
```
### CONFIGURATION

#### Required Environment Variables

```
APPD_USERNAME=<AppDynamics Username>
APPD_PASSWORD=<AppDynamics Password>
APPD_HOST=<https://AppDynamics Host>
SIGNALFX_TOKEN=<SignalFx token>
```

#### Optional Environment Variables

```
SIGNALFX_APPD_METRICS=<metric configurations filename (default to metrics.json)>
APPD_INTERVAL=<time in minutes of metric lookup interval (default to 1 minute)>
```

### USAGE

### METRICS

[Metrics.json](https://github.com/signalfx/appd-integration/blob/master/appd-report-standalone/metrics.json) contains configurations for the list of apps, metrics inside each app, and dimensions mapping for each app.

AppDynamics metric paths are described as a pipe-delimited string (|),
for example Performance|AppServer1|Resources|CPU.

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

Following is a working example of [metrics.json](https://github.com/signalfx/appd-integration/blob/master/appd-report-standalone/metrics.json) configurations:

```
[
  {
    "name": "<Your App Name>",
    "metrics": [
      {
        "metric_path": "Application Infrastructure Performance|Tier2|Individual Nodes|*|Hardware Resources|*|*",
        "dimensions_path_map": "metric_type|tier|-|node|resource_type|component_type",
        "dimensions": {
          "key1": "value1",
          "key2": "value2"
        }
      },
      {
        "metric_path": "Application Infrastructure Performance|Tier2|Individual Nodes|*|Hardware Resources|*|*|*",
        "dimensions_path_map": "metric_type|tier|-|node|resource_type|component_type|component_instance"
      },
      {
        "metric_path": "Application Infrastructure Performance|Tier2|Individual Nodes|*|Agent|*|*",
        "dimensions_path_map": "metric_type|tier|-|node|-|category",
        "dimensions": {
          "key3": "value3"
        }
      }
    ]
  }
]
```

A default [metrics.json](https://github.com/signalfx/appd-integration/blob/master/appd-report-standalone/metrics.json) is provided, with Application Infrastructure Performance metrics configured.


### Process Status Metrics

appd-report-standalone also reports metrics pertaining to the syncing process to SignalFx.

That includes:
- mtsReported
- mtsEmpty
- dataPointsReported
- appdRequestFailure


### LICENSE

This plugin is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/appd-integration/blob/master/LICENSE) for more details.
