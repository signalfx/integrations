# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png) Load

_This directory consolidates all the metadata associated with the Load collectd plugin. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/blob/master/src/load.c)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Load):

> The Load plugin collects the system load. These numbers give a rough overview over the utilization of a machine, though their meaning is mostly overrated.
The system load is defined as the number of runnable tasks in the run-queue and is provided by many operating systems as a one, five or fifteen minute average.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

| Software          | Version        |
|-------------------|----------------|
| collectd |  1.0+ |

### INSTALLATION

Installation and initial configuration options are available as part of the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd).


### CONFIGURATION

The Load plugin does not have any configuration settings.

### USAGE

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

License for this plugin can be found [in the header of the plugin](https://github.com/signalfx/collectd/blob/master/src/load.c)
