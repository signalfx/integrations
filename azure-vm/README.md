# ![](./img/integrations_azurevm.png) Microsoft Azure Virtual Machines

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Azure Virtual Machines via [Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

#### FEATURES

##### Built-in dashboards

- **Azure Virtual Machine**: Shows metrics of a virtual machine.

  [<img src='./img/vm.png' width=200px>](./img/vm.png)

- **Azure Virtual Machine (Classic)**: Shows metrics of a classic virtual machine.

  [<img src='./img/vm.classic.png' width=200px>](./img/vm.classic.png)

- **Azure Virtual Machines**: Shows metrics of all virtual machines being monitored.

  [<img src='./img/vms.png' width=200px>](./img/vms.png)

### INSTALLATION

To access this integration, [connect to Microsoft Azure](https://github.com/signalfx/integrations/tree/master/azure)[](sfx_link:azure).

### USAGE

#### Interpreting Built-in dashboards

**Azure Compute Virtual Machine**

- **CPU Percent** - Percentage of CPU used by the virtual machine.

  [<img src='./img/vm.cpu.percent.png' width=200px>](./img/vm.cpu.percent.png)

- **CPU Percent Trend** - Trend of percentage of CPU used by the virtual machine.

  [<img src='./img/vm.cpu.percent.trend.png' width=200px>](./img/vm.cpu.percent.trend.png)

- **Disk I/O** - List of counts of disk operations.

  [<img src='./img/vm.disk.png' width=200px>](./img/vm.disk.png)

- **Disk I/O Trend** - Trend of disk I/O bytes per second by the virtual machine.

  [<img src='./img/vm.disk.io.trend.png' width=200px>](./img/vm.disk.io.trend.png)

- **Disk IOPs Trend** - Trend of the disk I/O operations performed by virtual machine.

  [<img src='./img/vm.disk.iops.trend.png' width=200px>](./img/vm.disk.iops.trend.png)

- **Network I/O** - Number of bytes received from/sent to the network by the virtual machine.

  [<img src='./img/vm.network.png' width=200px>](./img/vm.network.png)

- **Network I/O Bytes Trend** - Trend of the number of bytes received/sent by the virtual machine.

  [<img src='./img/vm.network.io.trend.png' width=200px>](./img/vm.network.io.trend.png)

The above charts are applicable to all Azure Virtual Machines. The following two charts, however, are only applicable to Burstable machines.

- **CPU Credits Remaining** - Number of CPU credits remaining for a burstable machine.

  [<img src='./img/vm.cpu.credits.remaining.png' width=200px>](./img/vm.cpu.credits.remaining.png)

- **CPU Credits Used** - Number of CPU credits used by a burstable machine.

  [<img src='./img/vm.cpu.credits.used.png' width=200px>](./img/vm.cpu.credits.used.png)

**Azure Compute Virtual Machines**

- **Azure Virtual Machines** - Total number of virtual machine being monitored.

  [<img src='./img/vms.count.png' width=200px>](./img/vms.count.png)

- **Top Virtual Machines by CPU percent** - List of virtual machines that use most CPU.

  [<img src='./img/vms.top.cpu.png' width=200px>](./img/vms.top.cpu.png)

- **Azure Virtual Machines by Region** - Count of Azure virtual machines by region.

  [<img src='./img/vms.by.region.png' width=200px>](./img/vms.by.region.png)

- **Network Bytes In** - Percentile trend of bytes received by virtual machines.

  [<img src='./img/vms.network.png' width=200px>](./img/vms.network.png)

- **Top Virtual Machines by Bytes In** - List of virtual machines with top bytes received.

  [<img src='./img/vms.top.network.png' width=200px>](./img/vms.top.network.png)

- **Network Bytes In vs. 24h Change percent** - Comparison of change in aggregate bytes received by all virtual machines.

  [<img src='./img/vms.network.in.change.png' width=200px>](./img/vms.network.in.change.png)

- **Network Bytes Out** - Percentile trend of bytes sent by virtual machines.

  [<img src='./img/vms.network.out.png' width=200px>](./img/vms.network.out.png)

- **Top Virtual Machines by Bytes Out** - List of virtual machines with top bytes sent.

  [<img src='./img/vms.top.network.out.png' width=200px>](./img/vms.top.network.out.png)

- **Network Bytes Out vs. 24h Change percent** - Comparison of change in aggregate bytes sent by all virtual machines.

  [<img src='./img/vms.network.out.change.png' width=200px>](./img/vms.network.out.change.png)

- **Disk I/O Bytes/Sec** - Aggregated disk I/O bytes per second from all virtual machines.

  [<img src='./img/vms.disk.io.bytes.png' width=200px>](./img/vms.disk.io.bytes.png)

- **Disk Ops/Sec** - Aggregated disk I/O operations per second from all virtual machines.

  [<img src='./img/vms.disk.ops.png' width=200px>](./img/vms.disk.ops.png)




### METRICS

For more information about the metrics emitted by Azure Virtual Machines, visit <a target="_blank" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-supported-metrics#microsoftcomputevirtualmachines">here</a>.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
