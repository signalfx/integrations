# ![](./img/integrations_azurestorage.png) Microsoft Azure Storage

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Azure Storage via [Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

#### FEATURES

##### Built-in dashboards

- **Azure Storage Account**: Shows metrics of a storage account.

  [<img src='./img/account.png' width=200px>](./img/account.png)

- **Azure Storage Accounts**: Shows metrics of all storage accounts being monitored.

  [<img src='./img/accounts.png' width=200px>](./img/accounts.png)

### INSTALLATION

To access this integration, [connect to Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

### USAGE

#### Interpreting Built-in dashboards

**Azure Storage Account**

- **Ingress Traffic** - Amount of incoming data in bytes aggregated by API call.

  [<img src='./img/account.ingress.png' width=200px>](./img/account.ingress.png)

- **Egress Traffic** - Amount of outgoing data in bytes aggregated by API call.

  [<img src='./img/account.egress.png' width=200px>](./img/account.egress.png)

- **Latency of Successful Requests** - Average latency in milliseconds to process a successful request for each API call.

  [<img src='./img/account.latency.sucessful.png' width=200px>](./img/account.latency.sucessful.png)

- **End to End Latency of Successful Requests** - Average end-to-end latency in milliseconds of successful requests made for each API call.

  [<img src='./img/account.e2e.latency.successful.png' width=200px>](./img/account.e2e.latency.successful.png)

- **Availability by API Call** - Shows the availability for each of the API calls being made.

  [<img src='./img/account.availability.png' width=200px>](./img/account.availability.png)

- **Transactions** - Number of API calls aggregated by API call.

  [<img src='./img/account.transactions.png' width=200px>](./img/account.transactions.png)

- **Used Capacity** - Capacity used by the account in bytes.

  [<img src='./img/account.usedcapacity.png' width=200px>](./img/account.usedcapacity.png)

**Azure Storage Accounts**

- **Top Accounts by Used Capacity** - List of storage accounts by top used capacity.

  [<img src='./img/accounts.top.usedcapacity.png' width=200px>](./img/accounts.top.usedcapacity.png)

- **Lowest Available Storage Server** - Lists the storage accounts with lowest availability aggregated across all API calls.

  [<img src='./img/accounts.lowest.available.png' width=200px>](./img/accounts.lowest.available.png)

- **Top Accounts by Transactions** - List of storage accounts by top transactions.

  [<img src='./img/accounts.transactions.png' width=200px>](./img/accounts.transactions.png)

- **Latency of Successful Requests** - Distribution of latencies in milliseconds to process a successful request call.

  [<img src='./img/accounts.latency.successful.png' width=200px>](./img/accounts.latency.successful.png)

- **End to End Latency of Successful Requests** - Distribution of end-to-end latencies in milliseconds of successful requests.

  [<img src='./img/accounts.e2e.latency.successful.png' width=200px>](./img/accounts.e2e.latency.successful.png)

- **Total Network Ingress** - Amount of incoming data in bytes into all accounts combined.

  [<img src='./img/accounts.ingress.png' width=200px>](./img/accounts.ingress.png)

- **Total Network Egress** - Amount of outgoing data in bytes from all accounts combined.

  [<img src='./img/accounts.egress.png' width=200px>](./img/accounts.egress.png)




### METRICS

For more information about the metrics emitted by Azure Storage, visit <a target="_blank" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-supported-metrics#microsoftstoragestorageaccounts">here</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
