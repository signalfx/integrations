# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integration_signalfx.png) SignalFx collectd agent

_This is a directory that consolidates all the metadata associated with the SignalFx collectd agent. The code repository for this project can be found [here](https://github.com/signalfx/collectd/)._

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

[collectd](http://collectd.org) is an open source daemon that collects statistics from a system and publishes them to a destination of your choice. You can use collectd to monitor infrastructure metrics, and install collectd plugins that monitor a wide range of software. It’s fast, performs well at scale, and enjoys great community support. We released the [SignalFx collectd agent](https://github.com/signalfx/collectd) to make a great agent even better.

The [SignalFx collectd agent](https://github.com/signalfx/collectd) introduces the following changes from community collectd:

* **Increased Character limit:** We’ve increased the number of characters that can be used in dimension key-value pairs to 1024, up from 64. In practice, this allows you to send as many dimensions as you want.
* **Buffer Flushing:** To ensure that metrics always arrive in a timely manner, we’ve added a timer to ensure that data is transmitted either when the data buffer is full or when a time limit is reached, whichever happens first. This capability is particularly useful if you are only collecting small quantities of time-sensitive metrics.
* **HTTP Error Logging:** We’re providing greater visibility into how collectd itself is functioning, by logging HTTP codes from unsuccessful data transmissions by the `write_http` plugin, and by logging the name of every plugin that is loaded at startup.

All changes have been submitted back to the [collectd project](http://collectd.org) for the benefit of the community at large.

#### FEATURES

Sending data using collectd allows you to take advantage of SignalFx’s extensive collectd support.

- The [SignalFx Hosts page](http://docs.signalfx.com/en/latest/built-in-content/host-nav.html) visualizes hosts that are monitored using the SignalFx collectd agent.

  [<img src='./img/collectdhostspage.png' width=200px>](./img/collectdhostspage.png)

  [<img src='./img/hostspagesinglehost.png' width=200px>](./img/hostspagesinglehost.png)

- SignalFx provides [recommended detectors](http://docs.signalfx.com/en/latest/built-in-content/recommended-detectors.html) for hosts instrumented with the SignalFx collectd agent. These built-in templates allow you to instantly create intelligent detectors based on SignalFx’s powerful analytics.

- SignalFx provides validated plugins for collectd that help you monitor specific software in your environment. Integrations include built-in dashboards, recommended detectors, and metrics documentation. Browse plugins that have been validated by SignalFx on the Integrations page, or [here on Github](http://signalfx.github.io).
- The [SignalFx plugin for collectd](https://github.com/signalfx/integrations/tree/master/collectd-signalfx) is a plugin that enriches your data by sending metadata about your hosts to SignalFx. This plugin is included by default in SignalFx’s collectd packages.

### REQUIREMENTS AND DEPENDENCIES

The SignalFx collectd agent is supported on the following operating systems:

| Operating System  | Version        |
|-----------|----------------|
| Amazon Linux | 2014.09, 2015.03, 2015.09, & 2016.03 |
| Debian  | 7 & 8 |
| Mac OS X | 10.8+ |
| RHEL/Centos | 6.x & 7.x |
| Ubuntu  | 12.04, 14.04, 15.04 & 16.04 |

You must have administrator (sudo) privileges to install this agent. 

### INSTALLATION

#### Install on a host

Run the following command to install the SignalFx collectd agent ([click here to read about available configuration options](https://github.com/signalfx/signalfx-collectd-installer/blob/master/README.md)):

          sudo curl -sSL https://dl.signalfx.com/collectd-install | bash -s YOUR_SIGNALFX_API_TOKEN

#### Install in a privileged container

SignalFx supports two Docker images of the SignalFx collectd agent for containerized environments:

- Alpine: [quay.io/signalfuse/collectd-alpine](quay.io/signalfuse/collectd-alpine)
- Ubuntu: [quay.io/signalfuse/collectd](quay.io/signalfuse/collectd)

Run the following command to start the container, replacing `IMAGE_URL` with the URL of the desired image:

          docker run --privileged \
            --net="host" \
            -e "SF_API_TOKEN=YOUR_SIGNALFX_API_TOKEN" \
            -v /etc/hostname:/mnt/hostname:ro \
            -v /proc:/mnt/proc:ro \
            -v /var/run/docker.sock:/var/run/docker.sock \
            -v /etc:/mnt/etc:ro \
            IMAGE_URL

To read more about the SignalFx collectd agent Docker image, [click here for complete documentation on Github](https://github.com/signalfx/docker-collectd).

#### Additional installation options

- **[Chef cookbook: chef\_install\_configure\_collectd](https://supermarket.chef.io/cookbooks/chef_install_configure_collectd)**

  SignalFx supports a Chef cookbook that installs the SignalFx collectd agent and important plugins on a host. [Click here to access it on Chef Supermarket](https://supermarket.chef.io/cookbooks/chef_install_configure_collectd).

- **[Puppet module: signalfx/collectd](https://forge.puppet.com/signalfx/collectd)**

  SignalFx provides Puppet modules to install the SignalFx collectd agent and important plugins on a host. [Click here to access it on Puppet Forge](https://forge.puppet.com/signalfx/collectd).

- **Manual step-by-step installation**

  To manually complete the steps that SignalFx's install script performs automatically, [check out the source here on Github](https://github.com/signalfx/signalfx-collectd-installer/blob/master/install.sh).

### CONFIGURATION

The SignalFx collectd agent is accompanied by a default configuration file, `collectd.conf`, that does not need to be modified in order to function. [Click here to read an example configuration file for the SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd/collectd.conf).

### USAGE

To use the data transmitted by the SignalFx collectd agent, check out the Hosts page in SignalFx. On this page you'll find a visualization of all transmitting hosts, built-in dashboards to show the health of your infrastructure, and recommended detectors to send intelligent alerts.

![](./img/hostspagesinglehost.png)

Installing the SignalFx collectd agent allows you to install many of the integrations that SignalFx supports. Browse available plugins for collectd on the Integrations page.

#### Adding dimensions to all datapoints

You can add a dimension to every datapoint that collectd sends to SignalFx by adding HTTP query parameters to the SignalFx ingest URL, part of the configuration for the `write_http` plugin. This allows you to add information about the host or environment to every metric. For instance, you could identify all metrics coming from production boxes with a dimension like `environment=prod`.

The SignalFx URL to which collectd will transmit data is specified in `10-write_http-plugin.conf` and by default has a value like https://ingest.signalfx.com/v1/collectd. 

Append dimensions to the  URL as `sfxdim_[DIMENSION NAME]=[DIMENSION VALUE]`. Multiple dimensions may be specified. 

For example, the following URL sends data points to SignalFx with the added dimensions `serverType=API` and `tier=middleware`.

```
    URL "https://ingest.signalfx.com/v1/collectd?sfxdim_serverType=API&sfxdim_tier=middleware"
```

#### Transmitting outside a network

If instances of collectd are unable to transmit outside the network, the [SignalFx metric proxy](https://github.com/signalfx/integrations/tree/master/metricproxy)[](sfx_link:metricproxy) can be used to receive connections from many instances of collectd, and forward transmissions to SignalFx using a single outgoing HTTP connection. This is suitable for environments in which transmissions exiting a network are highly restricted.

[Click here for more information about the SignalFx metric proxy](https://github.com/signalfx/integrations/tree/master/metricproxy)[](sfx_link:metricproxy).

#### Transmitting through an existing HTTP proxy

The SignalFx collectd agent can be configured to use an HTTP proxy if needed. The changes would need to be made on files that are sourced by the init scripts. Modify or create the indicated file, with the following contents:

On CentOS/RHEL: `/etc/sysconfig/collectd`

On Debian/Ubuntu: `/etc/default/collectd`

Sample contents of the file:
```
export http_proxy="http://HTTP_PROXY:PROXY_PORT"
export https_proxy="https://HTTPS_PROXY:PROXY_PORT"
```

Replace `HTTP_PROXY` and `HTTPS_PROXY` with the hostname of the HTTP proxy to be used, and `PROXY_PORT` with the port at which to access it.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
