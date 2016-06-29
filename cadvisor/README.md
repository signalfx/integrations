---
title: cAdvisor Integration
brief: cAdvisor integration to send metrics to SignalFx
---

#![](https://github.com/signalfx/Integrations/blob/master/cadvisor/img/integrations_kubernetes.png) cAdvisor Integration   

_This is a directory consolidate all the metadata associated with the cAdvisor integration. The relevant code for the plugin can be found [here](https://github.com/signalfx/cadvisor-integration)_

- [Description](#description)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

This tool is designed to run inside a Kubernetes cluster. After installation it will auto-discover cluster nodes and periodically query stats from them.

### INSTALLATION

You can clone and build the tool yourself, but the easiest way to install is to use a prebuilt docker image. Here is an example yaml file:

```
	apiVersion: v1
	kind: Pod
	metadata:
	  name: "test-scrapper"
	  labels:
	    app: "test-scrapper"
	spec:
	  containers:
	  - name: scrapper
	    image: "quay.io/signalfx/prometheustosfx:latest"
	    env:
	    - name: SFX_SCRAPPER_API_TOKEN
	      value: <API TOKEN>
	    - name: SFX_SCRAPPER_CLUSTER_NAME
	      value: <CLUSTER NAME>
	    - name: SFX_SCRAPPER_SEND_RATE
	      value: 5s
```

### CONFIGURATION

| Option | Default value | Comment | Env. Var. |
| ------ | ------------ | ------- | --------- |
| ingestURL | "https://ingest.signalfx.com"  | SignalFx ingest URL.|
| apiToken |   | API token. | $SFX_SCRAPPER_API_TOKEN |
| clusterName | | Cluster name that will appear as a dimension.  | $SFX_SCRAPPER_CLUSTER_NAME |
| sendRate | "1s"  | Rate at which data is queried from cAdvisor and sent to SignalFx. Possible values: [1s 5s 10s 30s 1m 5m 1h] | $SFX_SCRAPPER_SEND_RATE |
| cadvisorPort | 4194  | Port on which cAdvisor listens. | $SFX_SCRAPPER_CADVISOR_PORT |
| nodeServiceDiscoveryRate | "5m" | Rate at which nodes and services will be rediscovered. Possible values: [3m 5m 10m 15m 20m] | $SFX_SCRAPPER_NODE_SERVICE_DISCOVERY_RATE |

### LICENSE

This tool is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/cadvisor-integration/blob/master/LICENSE) for more details.
