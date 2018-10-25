# ![](./img/integrations_azure.png) Microsoft Azure

- [Description](#description)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Microsoft Azure services via Azure Monitor.

#### FEATURES

Connecting to Microsoft Azure allows you to take advantage of SignalFx’s extensive Azure support.

- SignalFx can sync metadata about your Azure Virtual Machines (only applicable to the VM's created/managed by Azure Resource Manager) to enrich metrics reported by Azure Monitor or the [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd).
- SignalFx provides built-in dashboards for many Azure services that report to Monitor, such as [Azure Virtual Machines](https://github.com/signalfx/integrations/tree/master/azure-vm)[](sfx_link:azure-vm) and [Azure Logic App](https://github.com/signalfx/integrations/tree/master/azure-logic-app)[](sfx_link:azure-logic-app).

### CONFIGURATION

To connect SignalFx to Microsoft Azure, you’ll create a new Application in Azure for SignalFx to use. You must be an administrator of your SignalFx account to connect SignalFx to Microsoft Azure.

### USAGE

See <a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/azure-info.html">our detailed Azure integration guide</a> for more information.

### METRICS

For more information about the metrics emitted by Microsoft Azure Monitor, see the documentation for individual services.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
