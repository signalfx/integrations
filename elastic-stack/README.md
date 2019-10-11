# ![](./img/integration_elastic_stack.png) Elastic Stack Links

- [Description](#description)
- [Installation](#installation)
- [License](#license)

### DESCRIPTION

Create links from SignalFx charts and alerts to any URL-addressable destination such as Kibana.

The links appear for metric properties for which they are targeted for (triggered for) in the configuration.

The links appear in the Action menus adjacent to metric property values displayed in dashboards and alerts.

The metric property values are used as query parameter and/or path variable values of the URL link.

### INSTALLATION

Installation is actually configuring linking from property values on SignalFx charts and alerts to any URL-addressable destination. 

Read about the possible configurations [here](https://docs.signalfx.com/en/latest/dashboards/dashboard-links.html) and priority linking [here](https://docs.signalfx.com/en/latest/managing/data-links.html#local-and-global-data-links).

To read about creating local data links, click [here](https://docs.signalfx.com/en/latest/managing/data-links.html#local-links).

You must be an account administrator to configure new global links.

To access Global Data Link configuration options page, click [here](https://app.signalfx.com/#/organization/CfhbPnRAcAM?selectedKeyValue=sf_section:globaldatalinks). 

Complete the instructions below.
1. Click **New Link** on that page to configure.  
2. Enter a Link Label.
3. Select a destination for the link.
4. Enter other choices appropriate for the destination.
5. Click **Save**.

[Click here to get started](/#/organization/YOUR_SIGNALFX_ORG_ID?selectedKeyValue=sf_section:globaldatalinks). 

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
