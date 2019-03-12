# ![](./img/integration_azurekubernetesservice.png) Microsoft Azure Kubernetes Service

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)

### DESCRIPTION

Use SignalFx to monitor Azure Kubernetes Service via [Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

#### FEATURES

##### Built-in dashboards

- **Azure Managed Cluster**: Shows metrics of an Azure Managed Cluster.

  [<img src='./img/aks_cluster.png' width=200px>](./img/aks_cluster.png)

### INSTALLATION

To access this integration, [connect to Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

### USAGE

#### Interpreting Built-in dashboards

**Azure Managed Cluster**

- **Number of Nodes** - Number of nodes in the Azure Kubernetes Cluster.

  [<img src='./img/nodes.png' width=200px>](./img/nodes.png)

- **Number of Pods** - Number of pods in the Azure Kubernetes Cluster.

  [<img src='./img/pods.png' width=200px>](./img/pods.png)

- **Available CPU Cores** - Available CPU cores across the cluster.

  [<img src='./img/available_cpu_cores.png' width=200px>](./img/available_cpu_cores.png)

- **Available Memory** - Available memory in the cluster in Bytes.

  [<img src='./img/available_memory.png' width=200px>](./img/available_memory.png)

- **Pods By State** - Heatmap showing the number of pods in Ready state across the cluster. GREEN shows pods in Ready state.

  [<img src='./img/pods_by_state.png' width=200px>](./img/pods_by_state.png)

- **Pods by Phase** - Number of pods in different phases across the cluster.

  [<img src='./img/pods_by_phase.png' width=200px>](./img/pods_by_phase.png)

- **Number of Pods NOT in Ready state per namespace** - Number of pods per namespace that are not in Ready state.

  [<img src='./img/pods_not_ready_by_namespace.png' width=200px>](./img/pods_not_ready_by_namespace.png)

### METRICS

For more information about the metrics emitted by Azure Kubernetes Service, visit <a target="_blank" href="https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported#microsoftcontainerservicemanagedclusters">here</a>.
