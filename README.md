## Validated Plugins

SignalFx indexes available and validated collectd plugins [here](http://signalfx-integrations.github.io). On this page, users of collectd can browse available plugins and find the plugin that monitors the software they care about. This also provides a single place to view all of the collectd plugins that SignalFx has validated and for which SignalFx has provided built-in content in the SignalFx application. Each plugin has a link to the code as well as a Project repository with complete information on:

- How to install, configure and use the plugin
- The metrics that are emitted
- For the given application or component, what to monitor and how

In order to be added to the plugin index, SignalFx validates each collectd plugin for stability, scale, and compatibility. If you would like to contribute here is the process:

1. Create and publish a plugin for collectd. To get started, [see our example plugin code](https://github.com/signalfx/collectd-example/blob/master/example_plugin.py).
1. Ensure that your plugin meets the validation requirements - more on that below.
1. Clone [this](https://github.com/signalfx/Integrations) repository locally.
1. Create a directory in this repository named after your plugin.
1. Add required documentation content to that directory. 
1. Commit and submit a pull request to this repository. Pull request template will prompt for all required information
  - When you change or enhance your plugin, send updates through a pull request.

## What is required for a new plugin

Here are SignalFx's requirements for a new plugin:

- **Validated plugin code**
- **Documentation** that describes the plugin and how it operates
  - Metadata file that points to plugin code
  - Metrics docs
  - Sample Dashboard
  - Example configuration file
  - License file
- **Test plans and expected outcomes**
- **Docker container definition**
- **Support information**
  - Contact info for support
  
## Validation Requirements

You're the expert in the software that you wrote the plugin for. The goal of this exercise is to convey your expertise in the software being monitored to non-expert users. You do this by providing documentation, usage information and examples. It’s also important to make sure that your plugin performs well and collects the right data to get the job done. 

### Code Requirements
Below are requirements for plugin code:

1. Include a README file that matches the [prescribed format](https://github.com/signalfx/Integrations/blob/master/Example/README.md). This file should contain all the information that a user would need to install, run and derive value from your plugin.
1. Submit your performance test plan and results.
1. Make sure that your plugin collects all the data that is necessary to monitor the software in question. 
  - When deciding which metrics your plugin should report, err on the side of a concise list that reports just the important metrics, rather than a longer one that reports everything available. A good model is to separate metrics into those that will be sent by default, and those that are available in "detailed" mode. Use other validated plugins as a guide on what to include.
1. Include dimensions by adding key-value pairs to collectd metric names. Dimensions can include any context that a user needs to drill down or slice-and-dice metrics through their environment (ex. cluster name, node name, region). Dimensions can capture any important concepts of the software being monitored, such as _queue name_ for a message queue or _index name_ for a search utility. To read more about dimensions, see SignalFx's data model on [developers.signalfx.io](http://developers.signalfx.io).

### Documentation Requirements

Metadata about your plugin is stored in the SignalFx plugin index to help users find the plugin they're looking for. This includes:

1. A structured document that includes a link to and description of your plugin
1. Sample configuration for your plugin
1. Documentation of the metrics emitted by your plugin
1. Screenshots of example charts that show how data from your plugin should be used

An example can be found here: [github.com/signalfx/collectd-example](https://github.com/signalfx/collectd-example)

#### Structured document (YAML File)

We will programmatically read this document to generate a description on your plugin's page at http://link/. Please provide the following fields:

| field name | description |
|------------|-------------|
| fixme | |

- Plugin name
- Plugin URL (like a link to a Github repo)
- A brief description of what this plugin is for, in two to three hundred words.

#### Sample configuration

To help users get up and running quickly, provide a sample configuration for your plugin that includes sensible default values and highlights required configuration.

An example of a sample configuration file can be found in http://sampleplugin/example.yaml.

#### Metrics and dimensions documentation

To help users make sense of their new data, provide documentation of each metric and dimension that the plugin emits, including name, type (counter, gauge, cumulative counter) and description of what it measures.

An example metrics documentation file can be found in http://sampleplugin/metrics.md.

#### Sample dashboard

Include a dashboard for your users to import into their monitoring solution, so that they can get instant value out of running your plugin. SignalFx provides free accounts for plugin developers that you can use to develop your dashboard. [Contact us to learn more](mailto:support@signalfx.com).

### Testing Requirements

In order to validate your plugin we need to know how to test it. Depending on the service or application that you are gathering metrics for, your test plan should reflect common use as well as assumed constraints. Please articulate the tests used for unit tests as well as any scale testing you've performed.

### Docker Container Properties

To help us recreate your test environment, provide us with a complete Docker image definition. Here are some words about what that entails. 
