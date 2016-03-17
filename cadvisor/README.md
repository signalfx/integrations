---
title: cAdvisor Integration
brief: cAdvisor integration to send metrics to SignalFx
---

#![](https://github.com/signalfx/Integrations/blob/master/cadvisor/img/integrations_kubernetes.png) cAdvisor Integration   

_This is a directory consolidate all the metadata associated with the cAdvisor integration. The relevant code for the plugin can be found [here](https://github.com/signalfx/cadvisor-integration)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This tool is designed to run inside a Kubernetes cluster. After installation it will auto-discover cluster nodes and periodically query stats from them.

### REQUIREMENTS AND DEPENDENCIES

>In this section, list:
>- collectd version requirements
>- Version and configuration requirements for the application being monitored
>- Other plugins that this plugin depends on (like the Python or Java plugins for collectd)
>- Any other dependencies that this plugin requires in order to run successfully


### INSTALLATION

>In this section, provide step-by-step instructions that a user can follow to install this plugin. Each step should allow the user to verify that it has been completed successfully.
>
>This section should also contain instructions for any steps that the user must take to modify or reconfigure the software to be monitored. For instance, the plugin might collect data from an API endpoint that must be enabled by the user.

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

## CONFIGURATION

| Option | Default value | Comment | Env. Var. |
| ------ | ------------ | ------- | --------- |
| ingestURL | "https://ingest.signalfx.com"  | SignalFx ingest URL.|
| apiToken |   | API token. | $SFX_SCRAPPER_API_TOKEN |
| clusterName | | Cluster name that will appear as a dimension.  | $SFX_SCRAPPER_CLUSTER_NAME |
| sendRate | "1s"  | Rate at which data is queried from cAdvisor and sent to SignalFx. Possible values: [1s 5s 10s 30s 1m 5m 1h] | $SFX_SCRAPPER_SEND_RATE |
| cadvisorPort | 4194  | Port on which cAdvisor listens. | $SFX_SCRAPPER_CADVISOR_PORT |
| nodeServiceDiscoveryRate | "5m" | Rate at which nodes and services will be rediscovered. Possible values: [3m 5m 10m 15m 20m] | $SFX_SCRAPPER_NODE_SERVICE_DISCOVERY_RATE |

### USAGE

>This section contains information about how best to monitor the software in question, using the data from this plugin. In this section, the plugin author shares experience and expertise with the software to be monitored, for the benefit of users of the plugin. This section includes:
>
>- Important conditions to watch out for in the software
>- Common failure modes, and the values of metrics that will allow the user to spot them
>- Chart images demonstrating each important condition or failure mode

### METRICS

>This section refers to the metrics documentation found in the `/docs` subdirectory. See [`/docs/README.md`](././docs/readme.md) for formatting instructions.

### LICENSE

This tool is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/cadvisor-integration/blob/master/LICENSE) for more details.
