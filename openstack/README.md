# ![](./img/integration_openstack.png) OpenStack

#### FEATURES

##### Built-in dashboards


- **HYPERVISOR**: Provides a high-level overview of metrics for an OpenStack hypervisor.

  [<img src='./img/openstack-hypervisor-dashboard-top.png' width=200px>](./img/openstack-hypervisor-dashboard-top.png)

  [<img src='./img/openstack-hypervisor-dashboard-bottom.png' width=200px>](./img/openstack-hypervisor-dashboard-bottom.png)

- **TENANT**: Provides metrics from an OpenStack project/tenant.

  [<img src='./img/openstack-tenant-dashboard-top.png' width=200px>](./img/openstack-tenant-dashboard-top.png)

  [<img src='./img/openstack-tenant-dashboard-bottom.png' width=200px>](./img/openstack-tenant-dashboard-bottom.png)

- **NEUTRON**: Provides metrics from an OpenStack Neutron component.

  [<img src='./img/openstack-neutron-dashboard.png' width=200px>](./img/openstack-neutron-dashboard.png)

- **INSTANCE**: Provides metrics from an OpenStack compute instance.

  [<img src='./img/openstack-instance-dashboard-top.png' width=200px>](./img/openstack-instance-dashboard-top.png)

  [<img src='./img/openstack-instance-dashboard-bottom.png' width=200px>](./img/openstack-instance-dashboard-bottom.png)


### USAGE

#### Interpreting Built-in dashboards

- **HYPERVISOR**:

  - **Running VMs**: Shows the number of VMs running in the hypervisor.

    [<img src='./img/chart-openstack-hypervisor-vms.png' width=200px>](./img/chart-openstack-hypervisor-vms.png)

  - **Load Average**: Shows the average CPU load on the hypervisor.

    [<img src='./img/chart-openstack-hypervisor-load.png' width=200px>](./img/chart-openstack-hypervisor-load.png)

  - **Memory Usage**: Shows the memory usage free vs used in the hypervisor.

    [<img src='./img/chart-openstack-hypervisor-memory-usage.png' width=200px>](./img/chart-openstack-hypervisor-memory-usage.png)

  - **Disk Usage**: Shows the disk usage free vs used in the hypervisor.

    [<img src='./img/chart-openstack-hypervisor-disk-usage.png' width=200px>](./img/chart-openstack-hypervisor-disk-usage.png)

  - **CPUs and VCPUs**: Shows the number of CPUs available and VCPUs used in the hypervisor.

    [<img src='./img/chart-openstack-hypervisor-cpus-vcpus.png' width=200px>](./img/chart-openstack-hypervisor-cpus-vcpus.png)

  - **Physical CPUs**: Shows the number of pysical cores on the host running hypervisor.

    [<img src='./img/chart-openstack-hypervisor-physical-cpus.png' width=200px>](./img/chart-openstack-hypervisor-physical-cpus.png)

  - **Total Disk**: Shows the total disk available on the host running hypervisor.

    [<img src='./img/chart-openstack-hypervisor-total-disk.png' width=200px>](./img/chart-openstack-hypervisor-total-disk.png)

  - **Total Memory**: Shows the total RAM available on the host running hypervisor.

    [<img src='./img/chart-openstack-hypervisor-total-memory.png' width=200px>](./img/chart-openstack-hypervisor-total-memory.png)


- **TENANT**:

  - **Used Instances**: Shows the number of used instances in the tenant/project.

    [<img src='./img/chart-openstack-tenant-used-instances.png' width=200px>](./img/chart-openstack-tenant-used-instances.png)

  - **Memory Utilization**: Shows the percentage of utilized memory in the tenant/project.

    [<img src='./img/chart-openstack-tenant-memory-util.png' width=200px>](./img/chart-openstack-tenant-memory-util.png)

  - **Disk Utilization**: Shows the percentage of utilized disk space in the tenant/project.

    [<img src='./img/chart-openstack-tenant-disk-util.png' width=200px>](./img/chart-openstack-tenant-disk-util.png)

  - **Instances Available vs Used**: Shows the number of available and used instances in the tenant/project.

    [<img src='./img/chart-openstack-tenant-instances.png' width=200px>](./img/chart-openstack-tenant-instances.png)

  - **Memory Usage**: Shows the overall memory available and used in the tenant/project.

    [<img src='./img/chart-openstack-tenant-memory-usage.png' width=200px>](./img/chart-openstack-tenant-memory-usage.png)

  - **Disk Usage**: Shows the overall disk space available and used in the tenant/project.

    [<img src='./img/chart-openstack-tenant-disk-usage.png' width=200px>](./img/chart-openstack-tenant-disk-usage.png)

  - **Volumes Available vs Used**: Shows the maximum number of block storage volumes available and used in the tenant/project.

    [<img src='./img/chart-openstack-tenant-volumes.png' width=200px>](./img/chart-openstack-tenant-volumes.png)

  - **VCPUs Available vs Used**: Shows the maximum number of virtual CPUs available and used in the tenant/project.

    [<img src='./img/chart-openstack-tenant-vcpus.png' width=200px>](./img/chart-openstack-tenant-vcpus.png)

  - **Top Instances by CPU %**: Shows the top five instances by CPU usage percentage in the tenant/project.

    [<img src='./img/chart-openstack-tenant-top-cpu.png' width=200px>](./img/chart-openstack-tenant-top-cpu.png)

  - **Top Instances by Memoery Used**: Shows the top five instances by memory usage in the tenant/project.

    [<img src='./img/chart-openstack-tenant-top-memory.png' width=200px>](./img/chart-openstack-tenant-top-memory.png)

  - **Top Instances by VCPUs**: Shows the top five instances by virtual CPUs used in the tenant/project.

    [<img src='./img/chart-openstack-tenant-top-vcpus.png' width=200px>](./img/chart-openstack-tenant-top-vcpus.png)


- **NEUTRON**:

  - **Networks**: Shows the total number of networks created in all projects.

    [<img src='./img/chart-openstack-neutron-networks.png' width=200px>](./img/chart-openstack-neutron-networks.png)

  - **Routers**: Shows the total number of routers created in all projects.

    [<img src='./img/chart-openstack-neutron-routers.png' width=200px>](./img/chart-openstack-neutron-routers.png)

  - **Subnets**: Shows the total number of subnets created in all projects.

    [<img src='./img/chart-openstack-neutron-subnets.png' width=200px>](./img/chart-openstack-neutron-subnets.png)

  - **Flaoting IPs Available vs Used**: Shows the maximum number of floating IPs available and used in all projects.

    [<img src='./img/chart-openstack-neutron-floating-ips.png' width=200px>](./img/chart-openstack-neutron-floating-ips.png)

  - **Security Groups Available vs Used**: Shows the maximum number of security groups available and used in all projects.

    [<img src='./img/chart-openstack-neutron-security-groups.png' width=200px>](./img/chart-openstack-neutron-security-groups.png)


- **INSTANCE**:

  - **VCPUs**: Shows the number of virtual CPUs allocated to the instance.

    [<img src='./img/chart-openstack-instance-vcpus.png' width=200px>](./img/chart-openstack-instance-vcpus.png)

  - **CPU Used %**: Shows the current percentage of CPU usage of an instance.

    [<img src='./img/chart-openstack-instance-cpu-used.png' width=200px>](./img/chart-openstack-instance-cpu-used.png)

  - **CPU %**: Shows the percentage of instance CPU usage over the time.

    [<img src='./img/chart-openstack-instance-cpu.png' width=200px>](./img/chart-openstack-instance-cpu.png)

  - **Memory**: Shows the memory usage of the instance.

    [<img src='./img/chart-openstack-instance-memory.png' width=200px>](./img/chart-openstack-instance-memory.png)

  - **Total Bytes Sent/Received**: Shows the number of bytes sent and received over the network.

    [<img src='./img/chart-openstack-instance-bytes-sent-received.png' width=200px>](./img/chart-openstack-instance-bytes-sent-received.png)

  - **Received vs Transmitted Packers/sec**: Shows the number of network packets sent and received per second.

    [<img src='./img/chart-openstack-instance-packets-sent-received.png' width=200px>](./img/chart-openstack-instance-packets-sent-received.png)

  - **Virtual Disk Read and Write Requests**: Shows the number of virtual disk read and write requests.

    [<img src='./img/chart-openstack-instance-vda-read-write-requests.png' width=200px>](./img/chart-openstack-instance-vda-read-write-requests.png)

  - **Size of VDS Reads and Writes**: Shows the size of virtual disk reads and writes.

    [<img src='./img/chart-openstack-instance-vda-read-write-size.png' width=200px>](./img/chart-openstack-instance-vda-read-write-size.png)


A few other details:

* `plugin` is always set to `openstack`
* `plugin_instance` will contain the project id and name of the project given in the configuration


### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
