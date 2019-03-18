# Validated Integrations

SignalFx indexes available and validated integrations <a target="_blank" href="http://signalfx.github.io">here</a>. On this page, users can browse available integrations and find the integration that monitors the software they care about. This also provides a single place to view all of the integrations that SignalFx has validated and for which SignalFx has provided built-in content in the SignalFx application. Each integration has a link to the code as well as a Project repository with information on:

- How to install, configure and use the integration
- The metrics that are emitted
- For the given application or component, what to monitor and how

In order to be added to the integration index, SignalFx validates each integration for stability, scale, and compatibility. If you would like to contribute here is the process:

1. Create and publish a integration for SignalFx.
 1. We have built an example <a target="_blank" href="https://github.com/signalfx/collectd-example/blob/master/example_plugin.py">collectd-based plugin</a> to help you get started.
 1. For other data collector types you'll just need to make sure that you can direct the output to SignalFx and use one of our <a target="_blank" href="https://developers.signalfx.com/">supported formats</a>
1. Ensure that your plugin meets the validation requirements - more on that below.
1. Clone <a target="_blank" href="https://github.com/signalfx/Integrations">this repository</a> locally.
1. Create a directory in this repository named after your plugin.
1. Add required documentation content to that directory.
1. Commit and submit a pull request to this repository. Pull request template will prompt for all required information. When you change or enhance your plugin, send updates through a pull request.

## What is required for a new integration

Here are SignalFx's requirements for a new plugin:

- **Validated integration code**
- **Documentation** that describes the integration and how it operates
  - Metadata file that points to integration code
  - Metrics docs
  - Sample Dashboard
  - Example configuration file
  - License file (Apache 2.0 recommended)
- **Support information**
  - Contact info for support

## Validation Requirements

You're the expert in the software that you wrote the integration for. The goal of this exercise is to convey your expertise in the software being monitored to non-expert users. You do this by providing documentation, usage information and examples. It’s also important to make sure that your integration performs well and collects the right data to get the job done.

### Code Requirements
Below are requirements for integration code:

1. Include a README file that matches the <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/Example/readme.md">prescribed format</a>. This file should contain all the information that a user would need to install, run and derive value from your integration.
1. Submit your performance test plan and results.
1. Make sure that your integration collects all the data that is necessary to monitor the software in question.
  - When deciding which metrics your integration should report, err on the side of a concise list that reports just the important metrics, rather than a longer one that reports everything available. A good model is to separate metrics into those that will be sent by default, and those that are available in "detailed" mode. Use other validated integrations as a guide on what to include.
1. Include dimensions by adding key-value pairs to metric names. Dimensions can include any context that a user needs to drill down or slice-and-dice metrics through their environment (ex. cluster name, node name, region). Dimensions can capture any important concepts of the software being monitored, such as *queue name* for a message queue or *index name* for a search utility. To read more about dimensions, see SignalFx's data model on <a target="_blank" href="http://developers.signalfx.com">developers.signalfx.com</a>.

### Documentation Requirements

Metadata about your integration is stored in the SignalFx integration index to help users find the integration they're looking for. This includes:

1. A structured document that includes a link to and description of your integration
1. Sample configuration for your integration
1. Documentation of the metrics emitted by your integration
1. Screenshots of example charts that show how data from your integration should be used

An example can be found here: <a target="_blank" href="https://github.com/signalfx/collectd-example">github.com/signalfx/collectd-example</a>

#### Structured document (YAML File)

We will programmatically read this document to generate a description on your integration for the catalog. Please provide the following fields:

| field name | description |
|------------|-------------|
| display\_name | name that will display in the integration tile|
| description | description of integration |
| project\_url | URL of 'metadata' directory (`https://github.com/signalfx/integrations/tree/master/[integration-foo]`)|
| code | URL of code repository |
| featured | flag to put integration in "Top Integrations" section |
| logo\_large | URL of 300x300 pixel logo image |
| logo\_small | URL of 150x150 pixel logo image |
| feature | the feature associated with the integration |


Example:

```
{ "display_name":"AppDynamics Metrics Integration",
  "description": "AppDynamics metrics integration",
  "project_url": "https://github.com/signalfx/integrations/tree/master/appdynamics",
  "code": "https://github.com/signalfx/appd-integration",
  "featured": false,
  "logo_large": "/images/repos/appdynamics/img/integrations_appdynamics%402x.png",
  "logo_small": "/images/repos/appdynamics/img/integrations_appdynamics.png",
  "feature": "<feature_name>"
},
```

#### Sample configuration

To help users get up and running quickly, provide a sample configuration for your integration that includes sensible default values and highlights required configuration.

An example of a sample configuration file can be found in in the <a target="_blank" href="https://github.com/signalfx/integrations/blob/master/Example/10-example.conf">Example directory</a>.

#### Metrics and dimensions documentation

To help users make sense of their new data, provide documentation of each metric and dimension that the integration emits, including name, type (counter, gauge, or cumulative counter) and description of what it measures.

An example metrics documentation file can be found in <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/Example/docs">Example "docs" directory</a>.

#### Sample dashboard

Include a dashboard for your users to import into their monitoring solution, so that they can get instant value out of running your integration. SignalFx provides extended trial accounts for plugin developers that you can use to develop your dashboard. <a target="_blank" href="mailto:community@signalfx.com">Contact us to learn more</a>.
