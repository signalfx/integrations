# Example Python Plugin

>This file contains information about our example Python plugin. It also contains instructions for producing similar README files for other plugins. 
>
> In this document, sections in block quotes (like this one) contain instructions for plugin authors. Follow the instructions to format your README file, then remove them before submitting your contribution. 

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

> In this section, give a general description of what your plugin is, what it does, and what the user can expect. 

This is the SignalFx Example Python plugin. Use it to send a sine wave to SignalFx. 

This plugin emits 3 metrics:
- one gauge in the form of a sine wave
- two counters for number of datapoints and events seen

The plugin also emits a notification every time it starts up.

### REQUIREMENTS AND DEPENDENCIES

>In this section, list:
>- collectd version requirements
>- Version and configuration requirements for the application being monitored
>- Other plugins that this plugin depends on (like the Python or Java plugins for collectd)
>- Any other dependencies that this plugin requires in order to run successfully

This plugin requires:

- collectd v5.5.0-sfx8
- Python plugin for collectd (included with SignalFx collectd)
- Python 2.6+

### INSTALLATION

>In this section, provide step-by-step instructions that a user can follow to install this plugin. Each step should allow the user to verify that it has been completed successfully. 
>
>This section should also contain instructions for any steps that the user must take to modify or reconfigure the software to be monitored. For instance, the plugin might collect data from an API endpoint that must be enabled by the user.

Follow these steps to install this plugin:

1. Download this repository to your local machine.
2. Download the sample configuration file from signalfx-integrations/helloworld/.
3. Modify the sample configuration file to contain values that make sense for your environment, as described in the header.
4. Add the following line to collectd.conf, replacing the path with the path to the sample configuration file you downloaded in step 2: 

  ``` 
  include '/path/to/10-configfile.conf' 
  ```
5. Restart collectd. 

### CONFIGURATION 

>Provide in this section instructions on how to configure the plugin, before and after installation. If this plugin has a configuration file with properties, list each property, define its purpose and give an example or list the default value.

#### Required configuration 

The following configuration options are *required* and have no defaults. This means that you must supply values for them in configuration in order for the plugin to work. 

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| required_option | An example of a required configuration property. | 12345 |

#### Optional configuration 

The following configuration options are *optional*. You may specify them in the configuration file in order to override default values provided by the plugin. 

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| ModulePath | Path on disk where collectd can find this module. | "/opt/example" |
| Frequency  | Cycles of the sine wave per minute. | 0.5 | 

### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Chart images demonstrating each important condition or failure mode

This plugin is an example that emits values on its own, and does not connect to software. It emits a repeating sine wave in the metric gauge.sine. The metric should look like this:

![Example chart showing gauge.sine](http://fixme)

The following conditions may be cause for concern:

*You see a straight line instead of a curve.*

This may indicate a period of missing data points. In the example chart shown above, some data points are missing between 16:40 and 16:41, and SignalFx is interpolating a straight line through the gap. 

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, see the `docs` directory in this repository. 

### LICENSE

> Include licensing information for the plugin in this section.

This plugin is released under the Apache 2.0 license. See LICENSE for more details. 


