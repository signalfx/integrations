# ![](./img/integrations_azureeventhubs.png) Microsoft Azure Event Hubs

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Azure Event Hubs via [Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

#### FEATURES

- **Azure Event Hub**: Shows metrics of an Event hub.

  [<img src='./img/hub.png' width=200px>](./img/hub.png)

- **Azure Event Hubs**: Shows metrics of all Event hubs being monitored.

  [<img src='./img/hubs.png' width=200px>](./img/hubs.png)

### INSTALLATION

To access this integration, [connect to Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

### USAGE

#### Interpreting Built-in dashboards

**Azure Event Hub**

- **Incoming vs Successful Requests** - Charts shows a comparison of the total number of incoming requests and the ones that failed.

  [<img src='./img/hub.incoming.vs.success.reqs.png' width=200px>](./img/hub.incoming.vs.success.reqs.png)

- **Network I/O** - Number of incoming and outgoing bytes to/from the event hub.

  [<img src='./img/hub.network.png' width=200px>](./img/hub.network.png)

- **Messages I/O** - Number of incoming and outgoing messages to/from the event hub.

  [<img src='./img/hub.messages.png' width=200px>](./img/hub.messages.png)

- **Throttled Requests** - Trend of the number requests throttled.

  [<img src='./img/hub.throttled.reqs.png' width=200px>](./img/hub.throttled.reqs.png)

- **Quota Exceeded Errors** - Trend of the number errors due to exceeding quota.

  [<img src='./img/hub.quota.errors.png' width=200px>](./img/hub.quota.errors.png)

- **Server Errors** - Trend of the number server errors.

  [<img src='./img/hub.server.errors.png' width=200px>](./img/hub.server.errors.png)

- **User Errors** - Trend of the number user errors.

  [<img src='./img/hub.user.errors.png' width=200px>](./img/hub.user.errors.png)

- **Connections Opened** - Number of connections opened.

  [<img src='./img/hub.connections.png' width=200px>](./img/hub.connections.png)

**Azure Event Hubs**

- **Incoming Requests** - Shows the trend of incoming requests for all event hubs monitored.

  [<img src='./img/hubs.incoming.reqs.png' width=200px>](./img/hubs.incoming.reqs.png)

- **Successful Requests** - Shows the trend of successful requests for all event hubs monitored.

  [<img src='./img/hubs.successful.reqs.png' width=200px>](./img/hubs.successful.reqs.png)

- **Top Event Hubs by Server Errors** - List of event hubs with most number of server errors.

  [<img src='./img/hubs.top.server.errors.png' width=200px>](./img/hubs.top.server.errors.png)

- **Top Event Hubs by Quota Exceeded Errors** - List of event hubs with most number of quota exceeded errors.

  [<img src='./img/hubs.top.quota.errors.png' width=200px>](./img/hubs.top.quota.errors.png)

- **Top Event Hubs by Users Errors** - List of event hubs with most number of user errors.

  [<img src='./img/hubs.top.user.errors.png' width=200px>](./img/hubs.top.user.errors.png)

- **Total Network I/O** - Number of incoming and outgoing bytes to/from all event hubs.

  [<img src='./img/hubs.network.png' width=200px>](./img/hubs.network.png)

- **Total Messages I/O** - Number of incoming and outgoing messages to/from all event hubs.

  [<img src='./img/hubs.messages.png' width=200px>](./img/hubs.messages.png)

- **Connections Opened** - Number of connections opened stacked by event hub.

  [<img src='./img/hubs.connections.png' width=200px>](./img/hubs.connections.png)

- **Throttled Requests** - Number of requests throttled opened stacked by event hub.

  [<img src='./img/hubs.throttled.reqs.png' width=200px>](./img/hubs.throttled.reqs.png)



### METRICS

For more information about the metrics emitted by Azure Event Hubs, visit <a target="_blank" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-supported-metrics#microsofteventhubnamespaces">here</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
