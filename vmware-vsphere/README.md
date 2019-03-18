# ![](./img/integrations_vsphere.png) vSphere

Metadata associated with SignalFx's vSphere integration can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/vmware-vsphere">here</a>. The relevant code for the plugin can be found <a target="_blank" href="https://github.com/signalfx/signalfx-vsphere/tree/master">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx vSphere integration. It collects metrics from vCenter and reports metrics to SignalFx

#### FEATURES

##### Built-in dashboards

- **vCenter**: Overview of vCenter architecture from all Objects in the vCenter inventory.

  [<img src='./img/dashboard_vsphere_vcenter_top.png' width=200px>](./img/dashboard_vsphere_vcenter_top.png)
  
  [<img src='./img/dashboard_vsphere_vcenter_bottom.png' width=200px>](./img/dashboard_vsphere_vcenter_bottom.png)
  
- **ESX-Host**: Provides metrics for a single ESX-Host.

  [<img src='./img/dashboard_vsphere_esx_host_top.png' width=200px>](./img/dashboard_vsphere_esx_host_top.png)
  
  [<img src='./img/dashboard_vsphere_esx_host_middle.png' width=200px>](./img/dashboard_vsphere_esx_host_middle.png)

  [<img src='./img/dashboard_vsphere_esx_host_bottom.png' width=200px>](./img/dashboard_vsphere_esx_host_bottom.png)

- **ESX-Hosts**: Provides metrics for all the ESX-Hosts in vCenter.

  [<img src='./img/dashboard_vsphere_esx_hosts_top.png' width=200px>](./img/dashboard_vsphere_esx_hosts_top.png)
  
  [<img src='./img/dashboard_vsphere_esx_hosts_bottom.png' width=200px>](./img/dashboard_vsphere_esx_hosts_bottom.png)

- **VM**: Provides metrics for a single Virtual Machine.

  [<img src='./img/dashboard_vsphere_vm_top.png' width=200px>](./img/dashboard_vsphere_vm_top.png)
  
  [<img src='./img/dashboard_vsphere_vm_bottom.png' width=200px>](./img/dashboard_vsphere_vm_bottom.png)

- **VMs**: Provides metrics for all the Virtual Machines in vCenter.

  [<img src='./img/dashboard_vsphere_vms.png' width=200px>](./img/dashboard_vsphere_vms.png)

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software  | Version        |
|-----------|----------------|
| vCenter | 5.5 or later |


### INSTALLATION

1. Download the latest SignalFx-vSphere monitoring application <a target="_blank" href="https://github.com/signalfx/signalfx-vsphere/releases"> ovf template</a> zip file.

2. Unzip the ovf template zip file.

3. Deploy the ovf template to the vCenter using a connected/configured vSphere client.

4. Login to the virtual machine . User : ```signalfx``` Password : ```signalfx```

5. Modify the sample configuration file located at ```/etc/vsphere/config.yaml``` as described in [Configuration](#configuration), below.

6. Perform basic checks for network connectivity of VM by ```$ service vsphere-monitor check```

7. If the version of the vCenter is less than 6.5, please check the article <a target="_blank" href="https://kb.vmware.com/s/article/2107096">https://kb.vmware.com/s/article/2107096</a> to increase the volume of metrics sent by vCenter.

8. Restart the service by  ```$ service vsphere-monitor restart```

### CONFIGURATION

#### Configuring the ingest endpoint

Before we can send metrics to SignalFx, we need to make sure you are sending them to the correct SignalFx realm.
To determine what realm you are in (YOUR_SIGNALFX_REALM), check your profile page in the SignalFx web application (click the avatar in the upper right and click My Profile).
If you are not in the `us0` realm, you will need to configure the `IngestEndpoint` configuration option shown below to include your realm in the URL.

#### Authentication

To use this library, you will need a valid SiganlFx organization access token (YOUR_SIGNALFX_API_TOKEN).
For more information on authentication, see the API's [Authentication documentation](https://developers.signalfx.com/basics/authentication.html).

#### Configuration Options

Using the example configuration file <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/vmware-vsphere/config.yaml">config.yaml</a> as a guide, provide values for the configuration options listed below that make sense for your environment and allow you to connect to the VCenter to be monitored.

| configuration option | definition | example value |
| ---------------------|------------|---------------|
| host | Hostname or IP address of the vCenter Server. | 192.168.1.60 |
| username | Username required to login to vCenter Server. | administrator@vsphere.local |
| password | Password required to login to vCenter Server. | Abcd123$ |
| Name | Name of the vCenter Server. | VCenter-Signalfx |
| IngestToken | SignalFx Organization Access Token required to send metrics to SignalFx | YOUR_SIGNALFX_API_TOKEN |
| MORSyncInterval | Time interval at which the vCenter inventory should be synced. | 300 |
| MORSyncTimeout | The time that the application should wait for the vCenter inventory to synchronize the first time. Larger inventories will require a longer timeout. This timeout should be increased according to the inventory size when the application fails with MORSyncTimeout error message.| 600 |
| MetricSyncInterval | Time interval at which the available metrics should be synced. | 300 |
| MetricSyncTimeout | The time that the application should wait for metrics to synchronize the first time. This should be increased when the volume of metrics is high.  This timeout should be increased when the application fails with MetricSyncTimeout error message. | 600 |
| IngestEndpoint | The url of ingest endpoint to send to metrics. | https://ingest.YOUR_SIGNALFX_REALM.signalfx.com |
| IngestTimeout | The timeout interval for sending metrics to signalfx ingest endpoint. | 20 |
| IncludeMetrics | Metrics required for different inventory objects can be included individually. Currently metrics can be added for datacenter, cluster, host and vm. | mem.usage.average |
| ExcludeMetrics | Metrics emitted from different inventory objects can be excluded individually. | mem.usage.average |
| Dimensions | Additional dimensions to be added to each datapoint. | dimension_key: "dimension_value" |

#### Configuration Examples

```apache
config:
  - host: 192.168.1.60
    username: administrator@vsphere.local
    password: Abcd123$
    Name: VCenter4
    IngestToken: YOUR_SIGNALFX_API_TOKEN
    IngestEndpoint: 'https://ingest.YOUR_SIGNALFX_REALM.signalfx.com'
    IngestTimeout: 20
    MORSyncInterval: 300
    MORSyncTimeout: 600
    MetricSyncInterval: 300
    MetricSyncTimeout: 600
    IncludeMetrics:
      host:
        - mem.swapused.average
      cluster:
        - mem.usage.average
    Dimensions:
      dimension_key: "dimension_value"
      dimension_key1: "dimension_value1"

```

The application can be configured to collect metrics from multiple VCenters in the following manner.

```apache
config:
  - host: 192.168.1.60
    username: administrator@vsphere.local
    password: Abcd123$
    Name: VCenter4
    IngestToken: YOUR_SIGNALFX_API_TOKEN
    IngestEndpoint: 'https://ingest.YOUR_SIGNALFX_REALM.signalfx.com'
    IngestTimeout: 10
    MORSyncInterval: 300
    MORSyncTimeout: 1200
    MetricSyncInterval: 300
    MetricSyncTimeout: 900
    IncludeMetrics:
      host:
        - mem.swapused.average
      cluster:
        - mem.usage.average
    Dimensions:
      dimension_key: "dimension_value"
      dimension_key1: "dimension_value1"

  - host: 192.168.1.20
    username: administrator@vsphere.local
    password: Abcd123$
    Name: 192.168.1.20
    IngestToken: YOUR_SIGNALFX_API_TOKEN
    IngestEndpoint: 'https://ingest.YOUR_SIGNALFX_REALM.signalfx.com'
    MORSyncInterval: 20
    MetricSyncInterval: 60
    ExcludeMetrics:
      host:
        - disk.usage.average
```


### USAGE

#### Interpreting Built-in dashboards

- **vCenter**:

  - **Number of Datacenters**: Total number of Datacenters in the vCenter.

    [<img src='./img/chart_vsphere_vcenter_number_datacenters.png' width=200px>](./img/chart_vsphere_vcenter_number_datacenters.png)

  - **Number of Clusters**: Total number of Clusters in the vCenter.

    [<img src='./img/chart_vsphere_vcenter_number_clusters.png' width=200px>](./img/chart_vsphere_vcenter_number_clusters.png)

  - **Number of Hosts**: Total number of Hosts in the vCenter.

    [<img src='./img/chart_vsphere_vcenter_number_hosts.png' width=200px>](./img/chart_vsphere_vcenter_number_hosts.png)

  - **Number of VMs**: Total number of Virtual Machines in the vCenter.

    [<img src='./img/chart_vsphere_vcenter_number_vms.png' width=200px>](./img/chart_vsphere_vcenter_number_vms.png)

  - **Top Hosts by CPU Usage**: List of top hosts having highest CPU Usage 

    [<img src='./img/chart_vsphere_vcenter_host_cpu.png' width=200px>](./img/chart_vsphere_vcenter_host_cpu.png)

  - **Top Hosts by Memory Usage**: List of top hosts having highest Memory Usage 

    [<img src='./img/chart_vsphere_vcenter_host_memory.png' width=200px>](./img/chart_vsphere_vcenter_host_memory.png)


- **ESX-Host**:
  
  - **Up time**: Total uptime of ESX-Host in days.

    [<img src='./img/chart_vsphere_esx_host_uptime.png' width=200px>](./img/chart_vsphere_esx_host_uptime.png)

  - **CPU Usage**: CPU Usage percentage of ESX-Host.

    [<img src='./img/chart_vsphere_esx_host_cpu_usage.png' width=200px>](./img/chart_vsphere_esx_host_cpu_usage.png)

  - **Memory Usage**: Memory Usage percentage of ESX-Host.

    [<img src='./img/chart_vsphere_esx_host_memory_usage.png' width=200px>](./img/chart_vsphere_esx_host_memory_usage.png)

  - **Disk Usage**: Disk Usage percentage of ESX-Host.

    [<img src='./img/chart_vsphere_esx_host_disk_usage.png' width=200px>](./img/chart_vsphere_esx_host_disk_usage.png)

  - **Network IO**: Network IO operations of ESX-Host in bits/sec.

    [<img src='./img/chart_vsphere_esx_host_network_io.png' width=200px>](./img/chart_vsphere_esx_host_network_io.png)

  - **Number of VMs**: Total number of Virtual Machines in the ESX-Host.

    [<img src='./img/chart_vsphere_esx_host_number_vms.png' width=200px>](./img/chart_vsphere_esx_host_number_vms.png)


- **ESX-Hosts**:
  
  - **Top Hosts by VM count**: List of top Hosts having highest VM count.

    [<img src='./img/chart_vsphere_esx_hosts_vm_count_top.png' width=200px>](./img/chart_vsphere_esx_hosts_vm_count_top.png)

  - **CPU Usage**: Percentile distribution of CPU Usage of different Hosts in the vCenter.

    [<img src='./img/chart_vsphere_esx_hosts_cpu_percentile.png' width=200px>](./img/chart_vsphere_esx_hosts_cpu_percentile.png)

  - **Memory Usage**: Percentile distribution of Memory Usage of different Hosts in the vCenter.

    [<img src='./img/chart_vsphere_esx_hosts_memory_percentile.png' width=200px>](./img/chart_vsphere_esx_hosts_memory_percentile.png)

  - **Disk Usage**: Percentile distribution of Disk Usage of different Hosts in the vCenter

    [<img src='./img/chart_vsphere_esx_hosts_disk_percentile.png' width=200px>](./img/chart_vsphere_esx_hosts_disk_percentile.png)

  - **Network IO**: Percentile distribution of Network Usage of different Hosts in the vCenter.

    [<img src='./img/chart_vsphere_esx_hosts_network_percentile.png' width=200px>](./img/chart_vsphere_esx_hosts_network_percentile.png)

  - **Number of VMs**: Stack chart of VM count of different Hosts present in the vCenter.

    [<img src='./img/chart_vsphere_esx_hosts_vm_count_stack.png' width=200px>](./img/chart_vsphere_esx_hosts_vm_count_stack.png)

  
- **VM**:
  
  - **Up time**: Total uptime of VM in days.

    [<img src='./img/chart_vsphere_vm_uptime.png' width=200px>](./img/chart_vsphere_vm_uptime.png)

  - **CPU Usage**: CPU Usage percentage of VM.

    [<img src='./img/chart_vsphere_vm_cpu_usage.png' width=200px>](./img/chart_vsphere_vm_cpu_usage.png)

  - **Memory Usage**: Memory Usage percentage of VM.

    [<img src='./img/chart_vsphere_vm_memory_usage.png' width=200px>](./img/chart_vsphere_vm_memory_usage.png)

  - **Disk Usage**: Disk Usage percentage of VM.

    [<img src='./img/chart_vsphere_vm_disk_usage.png' width=200px>](./img/chart_vsphere_vm_disk_usage.png)

  - **Network IO**: Network IO operations of VM in bits/sec.

    [<img src='./img/chart_vsphere_vm_network_io.png' width=200px>](./img/chart_vsphere_vm_network_io.png)

  - **Datastore Latency**: Datastore latency of VM in seconds.

    [<img src='./img/chart_vsphere_vm_datastore_latency.png' width=200px>](./img/chart_vsphere_vm_datastore_latency.png)
  
- **VMs**:
  
  - **CPU Usage**: Percentile distribution of CPU Usage of different VMs in the vCenter.

    [<img src='./img/chart_vsphere_vms_cpu_percentile.png' width=200px>](./img/chart_vsphere_vms_cpu_percentile.png)

  - **Memory Usage**: Percentile distribution of Memory Usage of different VMs in the vCenter.

    [<img src='./img/chart_vsphere_vms_memory_percentile.png' width=200px>](./img/chart_vsphere_vms_memory_percentile.png)

  - **Disk Usage**: Percentile distribution of Disk Usage of different VMs in the vCenter

    [<img src='./img/chart_vsphere_vms_disk_percentile.png' width=200px>](./img/chart_vsphere_vms_disk_percentile.png)

  - **Network IO**: Percentile distribution of Network Usage of different VMs in the vCenter.

    [<img src='./img/chart_vsphere_vms_network_percentile.png' width=200px>](./img/chart_vsphere_vms_disk_percentile.png)

  - **Up time**: List of top VMs having highest uptime in the vCenter.

    [<img src='./img/chart_vsphere_vms_uptime_top.png' width=200px>](./img/chart_vsphere_vms_uptime_top.png)

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](./docs).

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
