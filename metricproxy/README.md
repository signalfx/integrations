# ![](https://github.com/signalfx/integrations/blob/master/metricproxy/img/integrations_metricproxy.png) SignalFx metric proxy

_This is a directory that consolidates metadata associated with the SignalFx metric proxy. The relevant code for the project can be found [here](https://github.com/signalfx/metricproxy)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

### DESCRIPTION

Use the SignalFx metric proxy to aggregate metrics and send them to SignalFx. It is a multilingual datapoint demultiplexer that can accept time series data from the carbon (Graphite), collectd or SignalFx protocols and emit those datapoints to a series of servers using the carbon, collectd or SignalFx protocols. 

### REQUIREMENTS AND DEPENDENCIES

The SignalFx metric proxy must be deployed on a system that is capable of running Go. All dependencies for this Go project are included in `/Godeps` in the project repository. 

We recommend placing the proxy either on the same server as another existing metrics aggregator or on a central server that is already receiving datapoints, such as Graphite's carbon database.

#### Sizing details 

The size of the machine that hosts the proxy depends on the amount of data that will be transmitted through it. The key performance indicator for the host is CPU idle (higher is better). A host comparable to AWS's c3.2xlarge is known to handle up to approximately 7 million DPM (data points per minute) while reporting 70% CPU idle. For safety, we recommend large margins - running close to resource limits risks delayed data transmission, especially if the rate of data points is highly variable. 

### INSTALLATION

1. Identify a server on which to deploy the SignalFx metric proxy.
1. Edit the file `sfdbconfig.conf` to configure the proxy. Configuration options are defined [below](#configuration), and example configurations are available in the [main project documentation](https://github.com/signalfx/metricproxy/README.md).
1. Use the [install script](https://github.com/signalfx/metricproxy/blob/master/install.sh) to install or upgrade the proxy, as follows. 

 ```
  curl -s https://raw.githubusercontent.com/signalfx/metricproxy/master/install.sh | sudo sh
  # Config at    /etc/sfdbconfig.conf
  # Binary at    /opt/sfproxy/bin/metricproxy
  # Logs at      /var/log/sfproxy
  # PID file at  /var/run/metricproxy.pid
 ```
1. Start the proxy as follows:

  ```
    /etc/init.d/metricproxy start
  ```
  
1. Begin transmitting data to the host and port on which the proxy is running. The data will be transformed and forwarded as specified in the [configuration](#configuration). 

#### Note: Deploying using Docker

 The SignalFx metric proxy is also packaged as a Docker image that has been built and deployed
 to [quay.io](https://quay.io/repository/signalfx/metricproxy). This image does not include configuration. To use this image, ensure that you have a `sfdbconfig.json` file cross-mounted to
 `/var/config/sfproxy/sfdbconfig.json` for the container to use.

### CONFIGURATION

#### Config file format

See the [example configuration](exampleSfdbproxy.conf) file for an example of how
configuration looks.  Configuration is a JSON file with two important fields:
`ListenFrom` and `ForwardTo`.

##### ListenFrom

`ListenFrom` defines the data format that the proxy will receive, and on what port. It also defines the transformation that the data will undergo, if any. 

| Configuration property | Definition | Example values |
|---------------|-------------|-----------|
| `ListenAddr` | Defines the port on which to listen for incoming data. | "0.0.0.0:18080" |
| `Type` | Defines the listener that will handle the incoming data. Possible listeners are `signalfx`, `carbon`, and `collectd`. | "carbon" |
| `Dimensions` | A map of dimension-value pairs that adds the specified dimension to every data point sent by the listener. | { "env": "prod" } |

**Graphite options**

For incoming carbon (Graphite) data only, the proxy supports transforming long dot-delimited metric names into metrics and dimensions for transmission to SignalFx. For details on how to use these options, see https://github.com/signalfx/metricproxy/blob/master/README.md#graphite-options.
For carbon listeners we support either TCP or UDP with the default being TCP.  For more information see https://github.com/signalfx/metricproxy/blob/master/README.md#carbon-for-read.

##### ForwardTo

`ForwardTo` defines the data format that the proxy will transmit, and to where. 

| Configuration property | Definition | Example values |
|--------|----------|--------|
| `Name` | A name for this forwarder. | "ourcarbon" |
| `type` | The type of data that the proxy will emit. Possible values are `csv` for writing to a CSV file, `carbon` for sending to a Graphite server, and `signalfx-json` for sending to SignalFx. | "carbon" |

Additional configuration properties differ depending on the type of data being written. 

**"type": "signalfx-json"**

| Configuration property | Definition | Example values |
|--------|----------|--------|
| `DefaultAuthToken` | A SignalFx API token that the proxy will use to transmit data to SignalFx. | "ABCD" |

**"type": "carbon"** 

| Configuration property | Definition | Example values |
|--------|----------|--------|
| `Host` | Hostname of a carbon server. | "example.com" |
| `Port` | Port at which carbon is running on `Host`. | 2003 |

**"type": "csv"** 

| Configuration property | Definition | Example values |
|--------|----------|--------|
| `Filename` | Location on disk of a CSV file to write metric data to. | "/tmp/filewrite.csv" |

### USAGE

SignalFx metric proxy can help you get the right data to the right destination in many different scenarios. 

#### Sending data to multiple destinations

You can use the proxy to duplicate a data stream to multiple destinations. Add each destination to the `ForwardTo` block as in the following example.

```
"ForwardTo": [
  {
    "type": "signalfx-json",
    "DefaultAuthToken": "ABCD",
    "Name": "signalfxforwarder",
  },
  {
    "Filename": "/tmp/filewrite.csv",
    "Name": "filelocal",
    "type": "csv"
  }
] 
```

#### Transforming carbon dot-delimited metric names into metrics with dimensions

SignalFx's chart builder supports treating components of metric names as dimensions for the purpose of chart building. However, it can be more efficient to define dimensions once, before transmission, rather than many times afterward when building charts. Use the SignalFx metric proxy's `MetricDeconstructor` for the carbon listener to transform Graphite's long dot-delimited metric names into metrics with dimensions before transmission to SignalFx. 

Note that you can apply different MetricDeconstructor rules in each `ForwardTo` destination. 

#### Concentrate outgoing HTTP connections

SignalFx recommends instrumenting each host with the SignalFx collectd agent, which transmits data to SignalFx over HTTP using the `write_http` plugin. In some environments it is not desirable for every host to maintain its own out-of-network HTTP connection: for instance, when a firewall is in use. In this scenario, you can deploy the SignalFx metric proxy, configure each collectd instance to transmit to the proxy, then configure your network to authorize just the proxy to transmit outside the firewall to SignalFx. 

Because the SignalFx metric proxy multiplexes incoming traffic from incoming instances of collectd, it sends larger, more efficient messages to SignalFx. For this reason, it is also a good fit when servers have high transmission latency to the region where SignalFx is located. Forwarding metrics through the proxy reduces hosts' exposure to transmission latency. The proxy can be configured to buffer in-memory if needed. 

#### Simplify configuration of collectd

The SignalFx metric proxy provides one single point of configuration management. Configuring the proxy with your SignalFx API token allows you to manage the token once, on the proxy, rather than on each individual agent. 

In addition, because the SignalFx metric proxy can apply dimensions to all outgoing data points, you can use it to annotate metrics from many instances of collectd at once, with information of which individual collectd hosts may not be aware. This can make it easier to add new context to your metrics. 

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
