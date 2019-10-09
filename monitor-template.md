#test in github

INFO TAB

<monitor logo>
# <Monitor name>

Metadata associated with the <name> collectd plugin can be found here. The relevant code for the plugin can be found here.

[Description](#description)
[Features](#features)
[Use](#use)
[Metrics](#metrics)
[Dimensions](#dimensions)


## Description
Monitors <what> using the information provided by <what> which collects metrics from <what> instances by hitting these endpoints: 
* <link to item>
* <link to item>

## Features

For more information on the source data, see <https://example.com>

Monitor Source Code <link>

Accepts Endpoints: <yes/no>

Multiple Instances Allowed: <yes/no>


## Use

What the monitor is used for -- which metrics and for what -- discussion


## Metrics
Besides the common default metrics that are described [here](https://docs.signalfx.com/en/latest/integrations/agent/monitor-config.html), the following table shows additional optional metrics available for this monitor. Metrics that are marked as Default are standard metrics that are monitored by default. You may need to add a flag to these metrics. Check the config file for flag requirements. 

Name	Type	Default	Description
cpu.utilization	gauge	✔	Percentage of total CPU used within the last metric interval cycle.

### Optional metrics

To collect optional metrics, you must configure your monitor to listen for those metrics and then send those metrics to the agent.

To specify optional metrics, add a metricsToInclude filter to the agent configuration file, as shown in the code snippet below. The snippet lists all available optional metrics. Copy and paste the snippet into your monitor configuration file, then delete any optional metrics that you do not want.

Note that some of the optional metrics require you to set a flag in addition to adding them to the metricsToInclude list. Check the monitor configuration file to see if a flag is required for gathering optional metrics.

```
sh
metricsToInclude:
  - metricNames:
    - name
    - name
    monitorType: <name>
```

## Dimensions
The following dimensions may occur on metrics emitted by this monitor. Some dimensions may be specific to certain metrics; other dimensions can be configured. You can add extra dimensions to most metrics. The Common configuration options page [here](https://docs.signalfx.com/en/latest/integrations/agent/monitor-config.html) also describes how to configure for these extra dimensions. 

Name	Description
plugin_instance	Set to whatever you set in the name config option.


INSTALLATION TAB

[Requirements and Dependencies](#requirements-and-Dependencies)
[Installation](#installation)
[Configuration](#Configuration)
[Confirmation](#Confirmation)
[Troubleshooting](#Troubleshooting)

## Requirements and Dependencies
in table format

## Installation

## Configuration 
Config here

### YAML config
Sample YAML config with custom query:

```sh
monitors:
- type: collectd/couchbase
  host: 127.0.0.1
  port: 8091
  collectTarget: "NODE"
  clusterName: "my-cluster"
  username: "user"
  password: "password" 
```

### More Configuration options

In addition to the common configuration options shown [here](https://docs.signalfx.com/en/latest/integrations/agent/monitor-config.html), these configuration options can be set:

Config option	Required	Type	Description
item 						

## Confirmation
To confirm your installation is functioning properly...

## Troubleshooting

This is troubleshooting the installation.


USAGE TAB

[Dashboards](#Dashboards)
[How to](#how-to)
[Sample code for the how to](#sample-code-for-the-how-to])

## Dashboards
Dashboards in which the metrics from this monitor display.


## How To

Examples of how to use the monitor metrics for something useful.


## Sample code for the how to

This is where you can put the sample coding that matches the "how to" section above.












