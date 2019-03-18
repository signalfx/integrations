# ![](https://github.com/signalfx/integrations/blob/master/pops/img/integrations_pops.png) SignalFx Point of Presence Service (POPS)

Information associated with the SignalFx POPS can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/pops">here</a>. The relevant code for the project can be found <a target="_blank" href="https://github.com/signalfx/pops">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

### DESCRIPTION

Use the SignalFx Point Of Presence Service (POPS) to aggregate metrics and send them to SignalFx with different access tokens. It is a multilingual datapoint demultiplexer that can accept time series data from the collectd or SignalFx protocols and emit those datapoints to SignalFx.

SignalFx POPS can help you get the right data to SignalFx many different scenarios. For details, see [Usage](#usage).

### REQUIREMENTS AND DEPENDENCIES

SignalFx POPS is deployed as a container and requires the docker engine to run.

We recommend placing POPS either on the same server as another existing metrics aggregator or on a central server that is already receiving datapoints.

#### Sizing details

The size of the machine that hosts pops depends on the amount of data that will be transmitted through it.

A key performance indicator is `total_datapoints_buffered`. When summed and viewed as an average, it reflects the number of datapoints waiting to be emitted by POPS. This buffer should be a steady value with steady data input. The input rate can be monitored in Datapoints Per Minute by taking the metric `total_datapoints_by_token` with `rate/sec` rollup, summing, and then multiplying by `60`.  If the buffer begins to grow while the rate of input stays the same, then the configurations should be adjusted to prevent the buffer from backing up.

- Increasing the number of draining threads will also increase cpu utilization, but should allow the pops instance to emit more datapoints.
- Increasing the number of channels will increase both cpu utilization and memory utilization, but will allow more work to be processed when there a large number of tokens passing through POPS.

Memory Utilization has the potential to be high when using POPS.

- Increasing the number of draining threads will increase cpu utilization but may help clear the buffer quicker and decrease memory utilization overall.

- The `MAX_RETRY` is an intentionally low number to prevent POPS from backing up and datapoints will be dropped if errors are consistently encountered.  It is recommended that the number of retries is kept to a very small number such as 1 or 2.

A host comparable to AWS's m3.large is known to handle up to approximately 400 thousand DPM (data points per minute) before the datapoint buffer starts to back up. For safety, we recommend large margins - running close to resource limits risks delayed data transmission, especially if the rate of data points is highly variable.

### INSTALLATION

#### Deploying Container

1. Identify a server on which to deploy SignalFx POPS.
1. Ensure that the docker engine is installed on the server
1. Run the SignalFx POPS container specifying the `VERSION_TAG` with a valid [image tag](https://quay.io/repository/signalfx/pops?tab=tags), the port to expose on the host and any [configuration](#configuration) options you wish to assign to the container.

        $ docker run -tdi \
          -e "SF_METRICS_AUTH_TOKEN=YOUR_SIGNALFX_API_TOKEN" \
          -p 0.0.0.0:8100:8100 \
          quay.io/signalfx/pops:<VERSION_TAG>

    It is recommended to use a specific version rather than `latest`.
1. Begin transmitting data to the host and port on which SignalFx POPS is running. The data will be transformed and forwarded.

#### Building Binary

If a binary must be executed outside of the pops container, it can be built by checking out this git repository.  The actual build occurs inside of a docker container that includes the go compiler.

1. Checkout this repository
1. `cd` into the repository directory.
1. Issue the following make command to build the pops binary for linux in a container.  It will output the binary `pops` to `output/linux/`.
1. Execute the binary passing in the [configurations](#configuration) as in-line variables.

        $ SF_METRICS_AUTH_TOKEN=YOUR_SIGNALFX_API_TOKEN ./output/linux/pops


### CONFIGURATION


#### Configuring the ingest endpoint

Before we can forward metrics to SignalFx, we need to make sure you are sending them to the correct SignalFx realm.
To determine what realm you are in (YOUR_SIGNALFX_REALM), check your profile page in the SignalFx web application (click the avatar in the upper right and click My Profile).
If you are not in the `us0` realm, you will need to set the `DATA_SINK_DP_ENDPOINT`, `DATA_SINK_EVENT_ENDPIONT`, and `SF_METRICS_STATSENDPOINT` configuration options to use the correct realm, as shown below.

#### Configuration options

The SignalFx Point Of Presence Service is configured by environment variables which are set on the container at run time. When POPS starts up it looks for the following environment variables to configure itself.

| Option | Description | Default Value | Example |
| ------ | ----------- | ------------- | ------- |
| `CHANNEL_SIZE` | The size of each channel in POPS. A channel is a buffer of request  datapoint payloads. | `1000000` | `CHANNEL_SIZE=1000000` |
| `DATA_SINK_DP_ENDPOINT` | The  datapoint endpoint POPS will forward  datapoints to. | `https://ingest.us0.signalfx.com/v2/datapoint` | `DATA_SINK_DP_ENDPOINT=https://ingest.YOUR_SIGNALFX_REALM.signalfx.com/v2/datapoint` |
| `DATA_SINK_EVENT_ENDPOINT` | The event endpoint POPS will forward events to. | `https://ingest.us0.signalfx.com/v2/event`  | `DATA_SINK_EVENT_ENDPOINT=https://ingest.YOUR_SIGNALFX_REALM.signalfx.com/v2/event` |
| `DATA_SINK_SHUTDOWN_TIMEOUT` | The shutdown time out used when shutting down worker threads of a POPS instance. If connections have already been drained, then graceful shutdown period should already have drained connections. Graceful shutdown is a period where POPS waits for connections to stop.  This feature is useful for when POPS is behind something like a load balancer which can stop sending traffic before terminating the POPS instance. | `3s` | `DATA_SINK_SHUTDOWN_TIMEOUT=3s` |
| `LOG_DIR` | The directory inside the container that POPS should log to. The pops log is named pops.log.json. If no directory is specified, POPS will log to stdout. |  | `LOG_DIR=/var/log/pops` |
| `MAX_DRAIN_SIZE` | POPS batches  datapoints together for a given token as much as possible. `MAX_DRAIN_SIZE` is the maximum number of  datapoints a single batch of metrics can be. | `5000` | `MAX_DRAIN_SIZE=5000` |
| `MAX_RETRY` | If an unknown error or an http status code for timeout is encountered, POPS will attempt to retry up to `MAX_RETRY` before dropping the batch of  datapoints. Depending on workloads this number should be very small to prevent POPS from backing up. | `1` | `MAX_RETRY=1` |
| `NUM_CHANNELS` | Channels are buffers for  datapoint request payloads. Each channel will then have `NUM_DRAINING_THREADS` workers reading and emitting datapoints from the channel. | `50` | `NUM_CHANNELS=50` |
| `NUM_DRAINING_THREADS` | Number of workers to attach to each channel. Each channel will have  `NUM_DRAINING_THREADS` workers that read and emit datapoints from the channel. | `2` | `NUM_DRAINING_THREADS=2` |
| `POPS_DEBUGPORT` | The port which the debug server should operate over | `6060` | `POPS_DEBUGPORT=6060` |
| `POPS_GRACEFUL_MIN_WAIT_TIME` | The minimum wait time to wait for POPS to gracefully shutdown. Graceful shutdown is a period where POPS waits for connections to stop. This feature is useful for when POPS is behind something like a load balancer which can stop sending traffic before terminating the POPS instance. | `5s` | `POPS_GRACEFUL_MIN_WAIT_TIME=5s` |
| `POPS_GRACEFUL_MAX_WAIT_TIME` | The maximum wait time to wait for pops to gracefully shutdown. Graceful shutdown is a period where POPS waits for connections to stop. This feature is useful for when POPS is behind something like a load balancer which can stop sending traffic before terminating the POPS instance. | `25s` | `POPS_GRACEFUL_MAX_WAIT_TIME=25s` |
| `POPS_GRACEFUL_CHECK_INTERVAL` | How often during graceful shutdown to check if the pops instance has completed graceful shutdown. | `0s` | `POPS_GRACEFUL_CHECK_INTERVAL=1s` |
| `POPS_GRACEFUL_SILENT_TIME` | How long pops will sit silent during a graceful shutdown period. Graceful shutdown is a period where POPS waits for connections to stop. This feature is useful for when POPS is behind something like a load balancer which can stop sending traffic before terminating the POPS instance.| `3s` |  `POPS_GRACEFUL_SILENT_TIME=3s` |
| `POPS_PORT` | The port for POPS to operate on inside of the container. | `8100` | `POPS_PORT=8100` |
| `SF_METRICS_AUTH_TOKEN` | The authentication token used for emitting internal metrics from POPS. |  | `SF_METRICS_AUTH_TOKEN=YOUR_SIGNALFX_API_TOKEN` |
| `SF_METRICS_REPORT_INTERVAL` | The interval for emitting internal metrics about POPS. | `5s` | `SF_METRICS_REPORT_INTERVAL=5s` |
| `SF_METRICS_STATSENDPOINT` | The ingest url for emitting internal metrics about POPS .| `https://ingest.us0.signalfx.com/v2/datapoint` | `SF_METRICS_STATSENDPOINT=https://ingest.YOUR_SIGNALFX_REALM.signalfx.com/v2/datapoint` |
| `SF_SOURCE_NAME` | A dimension appended to pops internal metrics. |  | `SF_SOURCE_NAME=pops_forwarder` |

#### Listeners

SignalFx POPS listens for datapoints and events in the collectd and SignalFx formats.

| protocol | endpoints |
| -------- | -------- |
| collectd | `/v1/collectd` |
| SignalFx | `/v2/datapoint` |
| SignalFx | `/v2/event` |

### USAGE

SignalFx POPS can help you get the right data to the right destination in many different scenarios.

#### Concentrate outgoing HTTP connections

SignalFx recommends instrumenting each host with the SignalFx collectd agent, which transmits data to SignalFx over HTTP using the `write_http` plugin. In some environments it is not desirable for every host to maintain its own out-of-network HTTP connection: for instance, when a firewall is in use. In this scenario, you can deploy the SignalFx POPS, configure each collectd instance to transmit to the POPS instance, then configure your network to authorize just the POPS instance to transmit outside the firewall to SignalFx.

Because the SignalFx POPS instance multiplexes incoming traffic from incoming instances of collectd, it sends larger, more efficient messages to SignalFx. For this reason, it is also a good fit when servers have high transmission latency to the region where SignalFx is located. Forwarding metrics through the SignalFx POPS instance reduces hosts' exposure to transmission latency.

#### Debug Server

There is a debug server that exposes some diagnostic information about the pops instance.  This server operates over port `6060` in the container and has the endpoint `/debug/explorer/`.  An alternate port for the debug server may be defined by setting the environment variable `POPS_DEBUGPORT`.

### METRICS

POPS emits metrics about itself using the `SF_METRICS_STATSENDPOINT` and `SF_METRICS_AUTH_TOKEN`.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
