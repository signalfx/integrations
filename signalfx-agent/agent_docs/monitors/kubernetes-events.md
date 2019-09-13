
<!--- Generated by to-integrations-repo script in Smart Agent repo, DO NOT MODIFY HERE --->
<!--- GENERATED BY gomplate from scripts/docs/monitor-page.md.tmpl --->

# kubernetes-events

Monitor Type: `kubernetes-events` ([Source](https://github.com/signalfx/signalfx-agent/tree/master/internal/monitors/kubernetes/events))

**Accepts Endpoints**: No

**Multiple Instances Allowed**: Yes

## Overview

This monitor sends Kubernetes events as SignalFx
events.  Upon startup, it will send all of the events that K8s has that are
still persisted and then send any new events that come in.  The various
agents perform leader election amongst themselves to decide which instance
will send events, unless the `alwaysClusterReporter` config option is set to
true.

To use this monitor, will need to configure which events to send. You can
see the types of events happening in your cluster with
`kubectl get events -o yaml --all-namespaces`.
From the output, you can select which events you would like to send by picking
out the Reason (Started, Created, Scheduled...) and
Kind (Pod, ReplicaSet, Deployment...) combinations. These are placed in the
whitelistedEvents configuration option as a list of events you want to send.

Example YAML Configuration

```
- type: kubernetes-events
  whitelistedEvents:
    - reason: Created
      involvedObjectKind: Pod
    - reason: SuccessfulCreate
      invovledObjectKind: ReplicaSet
```

Event names will match the `reason` name.


## Configuration

To activate this monitor in the Smart Agent, add the following to your
agent config:

```
monitors:  # All monitor config goes under this key
 - type: kubernetes-events
   ...  # Additional config
```

**For a list of monitor options that are common to all monitors, see [Common
Configuration](../monitor-config.html#common-configuration).**


| Config option | Required | Type | Description |
| --- | --- | --- | --- |
| `kubernetesAPI` | no | `object (see below)` | Configuration of the Kubernetes API client |
| `whitelistedEvents` | no | `list of objects (see below)` | A list of event types to send events for.  Only events matching these items will be sent. |
| `alwaysClusterReporter` | no | `bool` | Whether to always send events from this agent instance or to do leader election to only send from one agent instance. (**default:** `false`) |


The **nested** `kubernetesAPI` config object has the following fields:

| Config option | Required | Type | Description |
| --- | --- | --- | --- |
| `authType` | no | `string` | How to authenticate to the K8s API server.  This can be one of `none` (for no auth), `tls` (to use manually specified TLS client certs, not recommended), `serviceAccount` (to use the standard service account token provided to the agent pod), or `kubeConfig` to use credentials from `~/.kube/config`. (**default:** `serviceAccount`) |
| `skipVerify` | no | `bool` | Whether to skip verifying the TLS cert from the API server.  Almost never needed. (**default:** `false`) |
| `clientCertPath` | no | `string` | The path to the TLS client cert on the pod's filesystem, if using `tls` auth. |
| `clientKeyPath` | no | `string` | The path to the TLS client key on the pod's filesystem, if using `tls` auth. |
| `caCertPath` | no | `string` | Path to a CA certificate to use when verifying the API server's TLS cert.  Generally this is provided by K8s alongside the service account token, which will be picked up automatically, so this should rarely be necessary to specify. |


The **nested** `whitelistedEvents` config object has the following fields:

| Config option | Required | Type | Description |
| --- | --- | --- | --- |
| `reason` | no | `string` |  |
| `involvedObjectKind` | no | `string` |  |



