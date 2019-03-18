# ![](https://github.com/signalfx/integrations/blob/master/logstash-ciscoxr/img/integrations_ciscoiosxr.png) Cisco IOS XR integration

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

### DESCRIPTION

This integration for Cisco IOS XR telemetry metrics was build by the Cisco IOS XR team as part of the <a target="_blank" href="https://github.com/cisco/bigmuddy-network-telemetry-stacks">bigmuddy-network-telemetry-stacks</a>. The integration utilizes <a target="_blank" href="https://www.elastic.co/products/logstash">logstash</a> for initial metric collection and then adds a plugin to export the metrics directly to SignalFx in the appropriate format.

### REQUIREMENTS AND DEPENDENCIES

This integration requires:

| Software          | Version        |
|-------------------|----------------|
| IOS XR | 5.1+ |
| logstash | 2.2.0+ |

### INSTALLATION

Installation directions are provided by <a target="_blank" href="https://github.com/cisco/bigmuddy-network-telemetry-stacks">Cisco</a>:

>You will need a working <a target="_blank" href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">git</a> and <a target="_blank" href="https://docs.docker.com/installation/">docker</a> setup; look for "Docker tips" below if you need help with this. If host is behind an HTTP proxy, refer to the pertinent section below.

>Clone the repository, pick the stack you would like to run, and follow the steps below. I use `stack_elk` as an example, but the same applies for `stack_prometheus`, `stack_signalfx` or `stack_kafka`:

```
git clone https://github.com/cisco/bigmuddy-network-telemetry-stacks.git
#
# Change to the directory for the stack of your choice e.g.:
#
cd stack_elk
sudo COLLECTOR=a.b.c.d ./stack_build
```

>where `a.b.c.d` is the local IP address you wish to use. `stack_build` is executed to set up the default configurations, build the docker images etc, and is only required once.

>Start the fleet of containers using:

```
sudo ./stack_run
```

>At this point your stack should be running and telemetry streams can be pointed at it.

>If you are using default configurations port `2105` by `stack_signalfx`. TCP supports compressed JSON.

>Stopping the stack involves running `stack_stop`.

```
sudo ./stack_stop
```

>The stack can be started and stopped over and over (no intervening `stack_build` required). Configuration and data is preserved across stop/run cycles in the <a target="_blank" href="https://docs.docker.com/userguide/dockervolumes/">host mounted volumes</a>. A host mounted volume is a  per-stack-component directory which is mapped into the container.

>If the stack is (re)built, configuration files which are copied from the repository are regenerated and any changes to those files in the host mounted volume will be overwritten. Any other data is preserved unless the host mounted volumes are deleted explicitly. If you wish to purge all data and configuration to start from scratch, simply delete the host mounted volumes, and rerun `stack_build`.


### CONFIGURATION

Configuration directions are provided by <a target="_blank" href="https://github.com/cisco/bigmuddy-network-telemetry-stacks">Cisco</a>:

>In order to use `stack_signalfx`, registration is required at https://signalfx.com/. Once registered, an organisation API Token can be retrieved from the profile page. This token should be setup in the `stack_signalfx/src/environment` as shown here (note the token is not made up in the example):

```
export SIGNALFXTOKEN="YOUR_SIGNALFX_API_TOKEN"
```

>Streams should be pointed at the `logstash` setup as for the other stacks. Go to `https://app.signalfx.com/` to visualise the data. The Usage Metric dashboard should show some number of datapoints received per second. Below is an example of dashboard setup to show IP SLA and interface counter data.

### USAGE

![](https://github.com/signalfx/integrations/blob/master/logstash-ciscoxr/img/signalfxjitter.png)

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
