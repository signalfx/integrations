| **OpenTelemetry Semantics**                                                              | **Legacy Semantics**                                      |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `container.filesystem.usage` (metric)                                                    | `container_fs_usage_bytes` (metric)                       |
| `container.image.name` (dimension)                                                       | `container_image` (dimension)                             |
| `container.memory.available` (metric)                                                    | `container_memory_available_bytes` (metric)               |
| `container.memory.major_page_faults` (metric)                                            | `container_memory_major_page_faults` (metric)             |
| `container.memory.page_faults` (metric)                                                  | `container_memory_page_faults` (metric)                   |
| `container.memory.rss` (metric)                                                          | `container_memory_rss_bytes` (metric)                     |
| `container.memory.working_set` (metric)                                                  | `container_memory_working_set_bytes` (metric)             |
| `container.name` (dimension)                                                             | `container_name` (dimension)                              |
| `k8s.container.cpu_limit` (metric)                                                       | `kubernetes.container_cpu_limit` (metric)                 |
| `k8s.container.cpu_request` (metric)                                                     | `kubernetes.container_cpu_request` (metric)               |
| `k8s.container.ephemeral-storage_limit` (metric)                                         | `kubernetes.container_ephemeral_storage_limit` (metric)   |
| `k8s.container.ephemeral-storage_request` (metric)                                       | `kubernetes.container_ephemeral_storage_request` (metric) |
| `k8s.container.memory.limit` (metric)                                                    | `kubernetes.container_memory_limit` (metric)              |
| `k8s.container.memory.request` (metric)                                                  | `kubernetes.container_memory_request` (metric)            |
| `k8s.container.name` (dimension)                                                         | `container_spec_name` (dimension)                         |
| `k8s.container.ready` (metric)                                                           | `kubernetes.container_ready` (metric)                     |
| `k8s.container.restarts` (metric)                                                        | `kubernetes.container_restart_count` (metric)             |
| `k8s.cronjob.active_jobs` (metric)                                                       | `kubernetes.cronjob.active` (metric)                      |
| `k8s.daemonset.current_scheduled_nodes` (metric)                                         | `kubernetes.daemonset.current_scheduled` (metric)         |
| `k8s.daemonset.desired_scheduled_nodes` (metric)                                         | `kubernetes.daemonset.desired_scheduled` (metric)         |
| `k8s.daemonset.misscheduled_nodes` (metric)                                              | `kubernetes.daemonset.misscheduled` (metric)              |
| `k8s.daemonset.ready_nodes` (metric)                                                     | `kubernetes.daemonset.ready` (metric)                     |
| `k8s.deployment.available` (metric)                                                      | `kubernetes.deployment.available` (metric)                |
| `k8s.deployment.desired` (metric)                                                        | `kubernetes.deployment.desired` (metric)                  |
| `k8s.hpa.current_replicas` (metric)                                                      | `kubernetes.hpa.status.current_replicas` (metric)         |
| `k8s.hpa.desired_replicas` (metric)                                                      | `kubernetes.hpa.status.desired_replicas` (metric)         |
| `k8s.hpa.max_replicas` (metric)                                                          | `kubernetes.hpa.spec.max_replicas` (metric)               |
| `k8s.hpa.min_replicas` (metric)                                                          | `kubernetes.hpa.spec.min_replicas` (metric)               |
| `k8s.job.active_pods` (metric)                                                           | `kubernetes.job.active` (metric)                          |
| `k8s.job.desired_successful_pods` (metric)                                               | `kubernetes.job.completions` (metric)                     |
| `k8s.job.failed_pods` (metric)                                                           | `kubernetes.job.failed` (metric)                          |
| `k8s.job.max_parallel_pods` (metric)                                                     | `kubernetes.job.parallelism` (metric)                     |
| `k8s.job.successful_pods` (metric)                                                       | `kubernetes.job.succeeded` (metric)                       |
| `k8s.namespace.name` (dimension)                                                         | `kubernetes_namespace` (dimension)                        |
| `k8s.namespace.phase` (metric)                                                           | `kubernetes.namespace_phase` (metric)                     |
| `k8s.node.condition_memory_pressure` (metric)                                            | `kubernetes.node_memory_pressure` (metric)                |
| `k8s.node.condition_network_unavailable` (metric)                                        | `kubernetes.node_network_unavailable` (metric)            |
| `k8s.node.condition_out_of_disk` (metric)                                                | `kubernetes.node_out_of_disk` (metric)                    |
| `k8s.node.condition_p_i_d_pressure` (metric)                                             | `kubernetes.node_p_i_d_pressure` (metric)                 |
| `k8s.node.condition_ready` (metric)                                                      | `kubernetes.node_ready` (metric)                          |
| `k8s.node.uid` (dimension)                                                               | `kubernetes_node_uid` (dimension)                         |
| `k8s.pod.name` (dimension)                                                               | `kubernetes_pod_name` (dimension)                         |
| `k8s.pod.network.errors` (metric) with dimension name `direction` equal to `receive`     | `pod_network_receive_errors_total` (metric)               |
| `k8s.pod.network.errors` (metric) with dimension name `direction` equal to `transmit`    | `pod_network_transmit_errors_total` (metric)              |
| `k8s.pod.network.io` (metric) with dimension name `direction` equal to `receive`         | `pod_network_receive_bytes_total` (metric)                |
| `k8s.pod.network.io` (metric) with dimension name `direction` equal to `transmit`        | `pod_network_transmit_bytes_total` (metric)               |
| `k8s.pod.phase` (metric)                                                                 | `kubernetes.pod_phase` (metric)                           |
| `k8s.pod.uid` (dimension)                                                                | `kubernetes_pod_uid` (dimension)                          |
| `k8s.replicaset.available` (metric)                                                      | `kubernetes.replicaset.available` (metric)                |
| `k8s.replicaset.desired` (metric)                                                        | `kubernetes.replicaset.desired` (metric)                  |
| `k8s.replication_controller.available` (metric)                                          | `kubernetes.replication_controller.available` (metric)    |
| `k8s.replication_controller.desired` (metric)                                            | `kubernetes.replication_controller.desired` (metric)      |
| `k8s.resource_quota.hard_limit` (metric)                                                 | `kubernetes.resource_quota_hard` (metric)                 |
| `k8s.resource_quota.used` (metric)                                                       | `kubernetes.resource_quota_used` (metric)                 |
| `k8s.resourcequota.name` (dimension)                                                     | `quota_name` (dimension)                                  |
| `k8s.statefulset.current_pods` (metric)                                                  | `kubernetes.statefulset.current` (metric)                 |
| `k8s.statefulset.desired_pods` (metric)                                                  | `kubernetes.statefulset.desired` (metric)                 |
| `k8s.statefulset.ready_pods` (metric)                                                    | `kubernetes.statefulset.ready` (metric)                   |
| `k8s.statefulset.updated_pods` (metric)                                                  | `kubernetes.statefulset.updated` (metric)                 |
| `k8s.volume.available` (metric)                                                          | `kubernetes.volume_available_bytes` (metric)              |
| `k8s.volume.capacity` (metric)                                                           | `kubernetes.volume_capacity_bytes` (metric)               |
| `k8s.volume.inodes.free` (metric)                                                        | `kubernetes.volume_inodes_free` (metric)                  |
| `k8s.volume.inodes.used` (metric)                                                        | `kubernetes.volume_inodes_used` (metric)                  |
| `k8s.volume.inodes` (metric)                                                             | `kubernetes.volume_inodes` (metric)                       |
| `k8s.workload.kind` (dimension)                                                          | `kubernetes_workload` (dimension)                         |
| `k8s.workload.name` (dimension)                                                          | `kubernetes_workload_name` (dimension)                    |
| `system.cpu.load_average.15m` (metric)                                                   | `load.longterm` (metric)                                  |
| `system.cpu.load_average.1m` (metric)                                                    | `load.shortterm` (metric)                                 |
| `system.cpu.load_average.5m` (metric)                                                    | `load.midterm` (metric)                                   |
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
