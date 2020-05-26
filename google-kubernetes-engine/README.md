# Google Kubernetes Engine

To monitor Google Kubernetes Engine, integrate SignalFx with [Google Cloud
Platform](https://github.com/signalfx/integrations/tree/master/gcp)[](sfx_link:gcp).

## Properties

Each metric synced from StackDriver is given a special `gcp_id` dimension that
uniquely identifies that resource (node, pod, or container) and on which
certain metadata properties will be set, which will cause those properties to
be propagated to all MTSs with that `gcp_id` dimension.

### k8s_node

The `gcp_id` dimension is in the format `<project_id>_<cluster_name>_<node_name>`.

The following properties are synced to `gcp_id`:

 - All labels on the node are synced to properties of the form: `gcp_<label_name>: <label_value>`
 - `gcp_node_uid`: The UID of that node

### k8s_pod

The `gcp_id` dimension is in the format `<project_id>_<cluster_name>_<namespace_name>_<pod_name>`.

The following properties are synced to `gcp_id`:

 - All pod labels are synced to properties of the form: `gcp_<label_name>: <label_value>`
 - `gcp_pod_uid`: The UID of the pod
 - `gcp_node_name`: The name of the node on which the pod is running

### k8s_container

The `gcp_id` dimension is in the format `<project_id>_<cluster_name>_<namespace_name>_<pod_name>_<container_name>`.

The following properties are synced to `gcp_id`:

 - `gcp_container_image`: The name of the image used by this container, as it appears in the pod spec
 - `gcp_node_name`: The name of the node on which the container is running

### Required Permissions

To sync properties for GKE you need the following IAM permissions on the
service account associated with the GCP integration with SignalFx:

 - `container.clusters.get`
 - `container.clusters.list`
 - `container.pods.get`
 - `container.pods.getStatus`
 - `container.pods.list`
 - `container.nodes.get`
 - `container.nodes.getStatus`
 - `container.nodes.list`

## METRICS

Note that older versions of GKE clusters may still emit metrics under the
Container Engine service in StackDriver.  This is determined by the cluster
config option "Kubernetes Engine Monitoring" option in the Cloud Console.  If
it is set to _Legacy Monitoring and Logging_ metrics will appear under the
Container Engine service and not under the Kubernetes service.

For more information about the metrics emitted by Google Kubernetes Engine,
visit [the service's metric page](https://cloud.google.com/monitoring/api/metrics_kubernetes).
