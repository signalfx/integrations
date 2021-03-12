| **OpenTelemetry Semantics**                                                              | **Legacy Semantics**                                      |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `container.filesystem.usage` (metric)                                                    | `container_fs_usage_bytes` (metric)                       |
| `container.id` (dimension)                                                               | `container_id` (dimension)                                |
| `container.image.name` (dimension)                                                       | `container_image` (dimension)                             |
| `container.memory.available` (metric)                                                    | `container_memory_available_bytes` (metric)               |
| `container.memory.major_page_faults` (metric)                                            | `container_memory_major_page_faults` (metric)             |
| `container.memory.page_faults` (metric)                                                  | `container_memory_page_faults` (metric)                   |
| `container.memory.rss` (metric)                                                          | `container_memory_rss_bytes` (metric)                     |
| `container.memory.working_set` (metric)                                                  | `container_memory_working_set_bytes` (metric)             |
| `container.name` (dimension)                                                             | `container_name` (dimension)                              |
| `container.status.reason` (property)                                                     | `container_status_reason` (property)                      |
| `container.status` (property)                                                            | `container_status` (property)                             |
| `host.name` (dimension)                                                                  | `host` (dimension)                                        |
| `k8s.cluster.name` (dimension)                                                           | `kubernetes_cluster` (dimension)                          |
| `k8s.container.cpu_limit` (metric)                                                       | `kubernetes.container_cpu_limit` (metric)                 |
| `k8s.container.cpu_request` (metric)                                                     | `kubernetes.container_cpu_request` (metric)               |
| `k8s.container.ephemeral-storage_limit` (metric)                                         | `kubernetes.container_ephemeral_storage_limit` (metric)   |
| `k8s.container.ephemeral-storage_request` (metric)                                       | `kubernetes.container_ephemeral_storage_request` (metric) |
| `k8s.container.memory.limit` (metric)                                                    | `kubernetes.container_memory_limit` (metric)              |
| `k8s.container.memory_request` (metric)                                                  | `kubernetes.container_memory_request` (metric)            |
| `k8s.container.name` (dimension)                                                         | `container_spec_name` (dimension)                         |
| `k8s.container.ready` (metric)                                                           | `kubernetes.container_ready` (metric)                     |
| `k8s.container.restarts` (metric)                                                        | `kubernetes.container_restart_count` (metric)             |
| `k8s.cronjob.active_jobs` (metric)                                                       | `kubernetes.cronjob.active` (metric)                      |
| `k8s.cronjob.name` (property)                                                            | `cronJob` (property)                                      |
| `k8s.cronjob.uid` (property)                                                             | `cronJob_uid` (property)                                  |
| `k8s.daemonset.current_scheduled_nodes` (metric)                                         | `kubernetes.daemon_set.current_scheduled` (metric)        |
| `k8s.daemonset.desired_scheduled_nodes` (metric)                                         | `kubernetes.daemon_set.desired_scheduled` (metric)        |
| `k8s.daemonset.misscheduled_nodes` (metric)                                              | `kubernetes.daemon_set.misscheduled` (metric)             |
| `k8s.daemonset.name` (property)                                                          | `daemonSet` (property)                                    |
| `k8s.daemonset.ready_nodes` (metric)                                                     | `kubernetes.daemon_set.ready` (metric)                    |
| `k8s.daemonset.uid` (property)                                                           | `daemonSet_uid` (property)                                |
| `k8s.deployment.available` (metric)                                                      | `kubernetes.deployment.available` (metric)                |
| `k8s.deployment.desired` (metric)                                                        | `kubernetes.deployment.desired` (metric)                  |
| `k8s.deployment.name` (property)                                                         | `deployment` (property)                                   |
| `k8s.deployment.uid` (property)                                                          | `deployment_uid` (property)                               |
| `k8s.hpa.current_replicas` (metric)                                                      | `kubernetes.hpa.status.current_replicas` (metric)         |
| `k8s.hpa.desired_replicas` (metric)                                                      | `kubernetes.hpa.status.desired_replicas` (metric)         |
| `k8s.hpa.max_replicas` (metric)                                                          | `kubernetes.hpa.spec.max_replicas` (metric)               |
| `k8s.hpa.min_replicas` (metric)                                                          | `kubernetes.hpa.spec.min_replicas` (metric)               |
| `k8s.job.active_pods` (metric)                                                           | `kubernetes.job.active` (metric)                          |
| `k8s.job.desired_successful_pods` (metric)                                               | `kubernetes.job.completions` (metric)                     |
| `k8s.job.failed_pods` (metric)                                                           | `kubernetes.job.failed` (metric)                          |
| `k8s.job.max_parallel_pods` (metric)                                                     | `kubernetes.job.parallelism` (metric)                     |
| `k8s.job.name` (property)                                                                | `job` (property)                                          |
| `k8s.job.successful_pods` (metric)                                                       | `kubernetes.job.succeeded` (metric)                       |
| `k8s.job.uid` (property)                                                                 | `job_uid` (property)                                      |
| `k8s.namespace.name` (dimension)                                                         | `kubernetes_namespace` (dimension)                        |
| `k8s.namespace.phase` (metric)                                                           | `kubernetes.namespace_phase` (metric)                     |
| `k8s.node.condition_memory_pressure` (metric)                                            | `kubernetes.node_memory_pressure` (metric)                |
| `k8s.node.condition_network_unavailable` (metric)                                        | `kubernetes.node_network_unavailable` (metric)            |
| `k8s.node.condition_out_of_disk` (metric)                                                | `kubernetes.node_out_of_disk` (metric)                    |
| `k8s.node.condition_p_i_d_pressure` (metric)                                             | `kubernetes.node_p_i_d_pressure` (metric)                 |
| `k8s.node.condition_ready` (metric)                                                      | `kubernetes.node_ready` (metric)                          |
| `k8s.node.name` (dimension)                                                              | `kubernetes_node` (dimension)                             |
| `k8s.node.uid` (dimension)                                                               | `kubernetes_node_uid` (dimension)                         |
| `k8s.pod.name` (dimension)                                                               | `kubernetes_pod_name` (dimension)                         |
| `k8s.pod.network.errors` (metric) with dimension name `direction` equal to `receive`     | `pod_network_receive_errors_total` (metric)               |
| `k8s.pod.network.errors` (metric) with dimension name `direction` equal to `transmit`    | `pod_network_transmit_errors_total` (metric)              |
| `k8s.pod.network.io` (metric) with dimension name `direction` equal to `receive`         | `pod_network_receive_bytes_total` (metric)                |
| `k8s.pod.network.io` (metric) with dimension name `direction` equal to `transmit`        | `pod_network_transmit_bytes_total` (metric)               |
| `k8s.pod.phase` (metric)                                                                 | `kubernetes.pod_phase` (metric)                           |
| `k8s.pod.uid` (dimension)                                                                | `kubernetes_pod_uid` (dimension)                          |
| `k8s.replicaset.available` (metric)                                                      | `kubernetes.replica_set.available` (metric)               |
| `k8s.replicaset.desired` (metric)                                                        | `kubernetes.replicaset.desired` (metric)                  |
| `k8s.replicaset.name` (property)                                                         | `replicaSet` (property)                                   |
| `k8s.replicaset.uid` (property)                                                          | `replicaSet_uid` (property)                               |
| `k8s.replication_controller.available` (metric)                                          | `kubernetes.replication_controller.available` (metric)    |
| `k8s.replication_controller.desired` (metric)                                            | `kubernetes.replication_controller.desired` (metric)      |
| `k8s.resource_quota.hard_limit` (metric)                                                 | `kubernetes.resource_quota_hard` (metric)                 |
| `k8s.resource_quota.used` (metric)                                                       | `kubernetes.resource_quota_used` (metric)                 |
| `k8s.resourcequota.name` (dimension)                                                     | `quota_name` (dimension)                                  |
| `k8s.statefulset.current_pods` (metric)                                                  | `kubernetes.stateful_set.current` (metric)                |
| `k8s.statefulset.desired_pods` (metric)                                                  | `kubernetes.stateful_set.desired` (metric)                |
| `k8s.statefulset.name` (property)                                                        | `statefulSet` (property)                                  |
| `k8s.statefulset.ready_pods` (metric)                                                    | `kubernetes.stateful_set.ready` (metric)                  |
| `k8s.statefulset.uid` (property)                                                         | `statefulSet_uid` (property)                              |
| `k8s.statefulset.updated_pods` (metric)                                                  | `kubernetes.stateful_set.updated` (metric)                |
| `k8s.volume.available` (metric)                                                          | `kubernetes.volume_available_bytes` (metric)              |
| `k8s.volume.capacity` (metric)                                                           | `kubernetes.volume_capacity_bytes` (metric)               |
| `k8s.volume.inodes.free` (metric)                                                        | `kubernetes.volume_inodes_free` (metric)                  |
| `k8s.volume.inodes.used` (metric)                                                        | `kubernetes.volume_inodes_used` (metric)                  |
| `k8s.volume.inodes` (metric)                                                             | `kubernetes.volume_inodes` (metric)                       |
| `k8s.workload.kind` (property)                                                           | `kubernetes_workload` (property)                          |
| `k8s.workload.name` (property)                                                           | `kubernetes_workload_name` (property)                     |
| `system.cpu.load_average.15m` (metric)                                                   | `load.longterm` (metric)                                  |
| `system.cpu.load_average.1m` (metric)                                                    | `load.shortterm` (metric)                                 |
| `system.cpu.load_average.5m` (metric)                                                    | `load.midterm` (metric)                                   |
| `system.disk.io` (metric) with dimension name `direction` equal to `read`                | `disk_octets.read` (metric)                               |
| `system.disk.io` (metric) with dimension name `direction` equal to `write`               | `disk_octets.write` (metric)                              |
| `system.disk.merged` (metric) with dimension name `direction` equal to `read`            | `disk_merged.read` (metric)                               |
| `system.disk.merged` (metric) with dimension name `direction` equal to `write`           | `disk_merged.write` (metric)                              |
| `system.disk.operations` (metric) with dimension name `direction` equal to `read`        | `disk_ops.read` (metric)                                  |
| `system.disk.operations` (metric) with dimension name `direction` equal to `write`       | `disk_ops.write` (metric)                                 |
| `system.disk.time` (metric) with dimension name `direction` equal to `read`              | `disk_time.read` (metric)                                 |
| `system.disk.time` (metric) with dimension name `direction` equal to `write`             | `disk_time.write` (metric)                                |
| `system.filesystem.inodes.usage` (metric) with dimension name `state` equal to `free`    | `df_inodes.free` (metric)                                 |
| `system.filesystem.inodes.usage` (metric) with dimension name `state` equal to `used`    | `df_inodes.used` (metric)                                 |
| `system.filesystem.usage` (metric) with dimension name `state` equal to `free`           | `df_complex.free` (metric)                                |
| `system.filesystem.usage` (metric) with dimension name `state` equal to `reserved`       | `df_complex.reserved` (metric)                            |
| `system.filesystem.usage` (metric) with dimension name `state` equal to `used`           | `df_complex.used` (metric)                                |
| `system.memory.usage` (metric) with dimension name `state` equal to `buffered`           | `memory.buffered` (metric)                                |
| `system.memory.usage` (metric) with dimension name `state` equal to `cached`             | `memory.cached` (metric)                                  |
| `system.memory.usage` (metric) with dimension name `state` equal to `free`               | `memory.free` (metric)                                    |
| `system.memory.usage` (metric) with dimension name `state` equal to `inactive`           | `memory.inactive` (metric)                                |
| `system.memory.usage` (metric) with dimension name `state` equal to `slab_reclaimable`   | `memory.slab_recl` (metric)                               |
| `system.memory.usage` (metric) with dimension name `state` equal to `slab_unreclaimable` | `memory.slab_unrecl` (metric)                             |
| `system.memory.usage` (metric) with dimension name `state` equal to `used`               | `memory.used` (metric)                                    |
| `system.network.dropped` (metric) with dimension name `direction` equal to `receive`     | `if_dropped.rx` (metric)                                  |
| `system.network.dropped` (metric) with dimension name `direction` equal to `transmit`    | `if_dropped.tx` (metric)                                  |
| `system.network.errors` (metric) with dimension name `direction` equal to `receive`      | `if_errors.rx` (metric)                                   |
| `system.network.errors` (metric) with dimension name `direction` equal to `transmit`     | `if_errors.tx` (metric)                                   |
| `system.network.io` (metric) with dimension name `direction` equal to `receive`          | `if_octets.rx` (metric)                                   |
| `system.network.io` (metric) with dimension name `direction` equal to `transmit`         | `if_octets.tx` (metric)                                   |
| `system.network.packets` (metric) with dimension name `direction` equal to `receive`     | `if_packets.rx` (metric)                                  |
| `system.network.packets` (metric) with dimension name `direction` equal to `transmit`    | `if_packets.tx` (metric)                                  |
| `system.paging.faults` (metric) with dimension name `type` equal to `major`              | `vmpage_faults.majflt` (metric)                           |
| `system.paging.faults` (metric) with dimension name `type` equal to `minor`              | `vmpage_faults.minflt` (metric)                           |