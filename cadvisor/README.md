[![Build Status](https://travis-ci.org/signalfx/cadvisor-integration.svg?branch=master)](https://travis-ci.org/signalfx/cadvisor-integration) [![Docker Repository on Quay.io](https://quay.io/repository/signalfx/cadvisor-integration/status "Docker Repository on Quay.io")](https://quay.io/repository/signalfx/cadvisor-integration)

# cadvisor-integration
## Overview
This tool designed to run inside of Kubernetes cluster. After installation it will auto discover cluster nodes and will query stats from them on time basis.
## Installation
You may clone and build tool by yourself but the easiest way is to use prebuild docker image. Here is an example yaml file:

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
## Full options list

| Option | Default val. | Comment | Env. Var. |
| ------ | ------------ | ------- | --------- |
| --ingestURL | "https://ingest.signalfx.com"  | SignalFx ingest URL. |
| --apiToken |   | API token. | $SFX_SCRAPPER_API_TOKEN |
| --clusterName | | Cluster name will appear as dimension.  | $SFX_SCRAPPER_CLUSTER_NAME |
| --sendRate | "1s"  | Rate at which data is queried from cAdvisor and send to SignalFx. Possible values: [10s 30s 1m 5m 1h 1s 5s] | $SFX_SCRAPPER_SEND_RATE |
| --cadvisorPort | 4194  | Port on which cAdvisor listens. | $SFX_SCRAPPER_CADVISOR_PORT |
| --nodeServiceDiscoveryRate | "5m" | Rate at which nodes and services will be rediscovered. Possible values: [20m 3m 5m 10m 15m] | $SFX_SCRAPPER_NODE_SERVICE_DISCOVERY_RATE |

## License

This tool is licensed under the Apache License, Version 2.0. See LICENSE for full license text.
