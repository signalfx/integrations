# ![](./img/integrations_azureappservice.png) Microsoft Azure App Service

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Azure App Service via [Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

#### FEATURES

##### Built-in dashboards

- **Azure App Service**: An overview of all the Azure apps being monitored by SignalFx. Users can also specify an app's name to view metrics from a single app.

  [<img src='./img/app.service.png' width=200px>](./img/app.service.png)

### INSTALLATION

To access this integration, [connect to Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

### USAGE

#### Interpreting Built-in dashboards

**Azure App Service**

- **Connections per App** - A stacked chart of number of connections aggregated by app.

  [<img src='./img/connections.png' width=200px>](./img/connections.png)

- **Requests per App** - A stacked chart of number of requests aggregated by app.

  [<img src='./img/requests.png' width=200px>](./img/requests.png)

- **Bytes Received** - Total bytes received by all the apps being monitored.

  [<img src='./img/bytes.received.png' width=200px>](./img/bytes.received.png)

- **Bytes Sent** - Total bytes sent by all the apps being monitored.

  [<img src='./img/bytes.sent.png' width=200px>](./img/bytes.sent.png)

- **Http 2xx Responses** - Number of 2xx responses returned by apps aggregated by app.

  [<img src='./img/http.2xx.png' width=200px>](./img/http.2xx.png)

- **Http 4xx Responses** - Number of 4xx responses returned by apps aggregated by app.

  [<img src='./img/http.4xx.png' width=200px>](./img/http.2xx.png)

- **Http 5xx Responses** - Number of 5xx responses returned by apps aggregated by app.

  [<img src='./img/http.5xx.png' width=200px>](./img/http.5xx.png)

- **CPU Time (s)** - CPU time of the monitored apps.

  [<img src='./img/cpu.png' width=200px>](./img/cpu.png)

- **Average Response Time (s)** - Average response time for each of the apps.

  [<img src='./img/response.time.png' width=200px>](./img/response.time.png)

### METRICS

For more information about the metrics emitted by Azure App Service, visit <a target="_blank" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-supported-metrics#microsoftwebsites-excluding-functions">here</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
