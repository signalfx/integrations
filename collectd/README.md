# ![](https://github.com/signalfx/integrations/blob/master/collectd/img/integration_signalfx.png) SignalFx collectd agent

Metadata associated with the SignalFx collectd agent can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/collectd">here</a>. The code repository for this project can be found <a target="_blank" href="https://github.com/signalfx/collectd/">here</a>.

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

### DESCRIPTION

**We have a new agent called the SignalFx Smart Agent that wraps collectd and
provides auto-discovery of services, among other features.  See [the
integration tile for the new agent](?selectedKeyValue=plugin:signalfx-agent)
for more information.  We strongly recommend using this new agent instead of
collectd, which is described below for legacy purposes.**

<a target="_blank" href="http://collectd.org">collectd</a> is an open source daemon that collects statistics from a system and publishes them to a destination of your choice. You can use collectd to monitor infrastructure metrics, and install collectd plugins that monitor a wide range of software. It’s fast, performs well at scale, and enjoys great community support. We released the <a target="_blank" href="https://github.com/signalfx/collectd">SignalFx collectd agent</a> to make a great agent even better.

The <a target="_blank" href="https://github.com/signalfx/collectd">SignalFx collectd agent</a> introduces the following changes from community collectd:

* **Increased Character limit:** We’ve increased the number of characters that can be used in dimension key-value pairs to 1024, up from 64. In practice, this allows you to send as many dimensions as you want.
* **Buffer Flushing:** To ensure that metrics always arrive in a timely manner, we’ve added a timer to ensure that data is transmitted either when the data buffer is full or when a time limit is reached, whichever happens first. This capability is particularly useful if you are only collecting small quantities of time-sensitive metrics.
* **HTTP Error Logging:** We’re providing greater visibility into how collectd itself is functioning, by logging HTTP codes from unsuccessful data transmissions by the `write_http` plugin, and by logging the name of every plugin that is loaded at startup.

All changes have been submitted back to the <a target="_blank" href="http://collectd.org">collectd project</a> for the benefit of the community at large.

#### FEATURES

Sending data using collectd allows you to take advantage of SignalFx’s extensive collectd support.

- The <a target="_blank" href="https://docs.signalfx.com/en/latest/built-in-content/infra-nav.html">SignalFx Infrastructure page</a> visualizes hosts that are monitored using the SignalFx collectd agent.

  [<img src='./img/collectdhostspage.png' width=200px>](./img/collectdhostspage.png)

  [<img src='./img/hostspagesinglehost.png' width=200px>](./img/hostspagesinglehost.png)

- SignalFx provides <a target="_blank" href="http://docs.signalfx.com/en/latest/built-in-content/recommended-detectors.html">recommended detectors</a> for hosts instrumented with the SignalFx collectd agent. These built-in templates allow you to instantly create intelligent detectors based on SignalFx’s powerful analytics.

- SignalFx provides validated plugins for collectd that help you monitor specific software in your environment. Integrations include built-in dashboards, recommended detectors, and metrics documentation. Browse plugins that have been validated by SignalFx on the Integrations page, or <a target="_blank" href="http://signalfx.github.io">here on Github</a>.
- The <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/signalfx-metadata">SignalFx plugin for collectd</a> is a plugin that enriches your data by sending metadata about your hosts to SignalFx. This plugin is included by default in SignalFx’s collectd packages.

### REQUIREMENTS AND DEPENDENCIES

The SignalFx collectd agent is supported on the following operating systems:

| Operating System  | Version        |
|-----------|----------------|
| Amazon Linux | 2014.09, 2015.03, 2015.09, & 2016.03 |
| Debian  | 7, 8, & 9 |
| Mac OS X | 10.8+ |
| RHEL/Centos | 6.x & 7.x |
| Ubuntu  | 12.04, 14.04 & 16.04 |

You must have administrator (sudo) privileges to install this agent.

### INSTALLATION


#### Configuring the ingest endpoint
Before we can send metrics to SignalFx, we need to make sure you are sending them to
the correct SignalFx realm. To determine what realm you are in (YOUR_SIGNALFX_REALM), check your
profile page in the SignalFx web application (click the avatar in the upper right and click My Profile).
If you are not in the `us0` realm, you will need to configure ingest url, as shown below.

#### Install on a host

Run the following command to install the SignalFx collectd agent (<a target="_blank" href="https://github.com/signalfx/signalfx-collectd-installer/blob/master/README.md">click here to read about available configuration options</a>):
```
sudo curl -sSL https://dl.signalfx.com/collectd-install | bash -s YOUR_SIGNALFX_API_TOKEN -U https://ingest.YOUR_SIGNALFX_REALM.signalfx.com
```
#### Install in a privileged container

SignalFx supports two Docker images of the SignalFx collectd agent for containerized environments:

- Alpine: <a target="_blank" href="http://www.quay.io/signalfuse/collectd-alpine">quay.io/signalfuse/collectd-alpine</a>
- Ubuntu: <a target="_blank" href="http://www.quay.io/signalfuse/collectd">quay.io/signalfuse/collectd</a>

Run the following command to start the container, replacing `IMAGE_URL` with the URL of the desired image:
```
docker run --privileged \
--net="host" \
-e "SF_API_TOKEN=YOUR_SIGNALFX_API_TOKEN" \
-e "SF_INGEST_HOST=https://ingest.YOUR_SIGNALFX_REALM.signalfx.com" \
-v /:/hostfs:ro \
-v /var/run/docker.sock:/var/run/docker.sock \
IMAGE_URL
```
To read more about the SignalFx collectd agent Docker image, <a target="_blank" href="https://github.com/signalfx/docker-collectd">click here for complete documentation on Github</a>.

#### Additional installation options

- **Chef cookbook: chef\_install\_configure\_collectd**

  SignalFx supports a Chef cookbook that installs the SignalFx collectd agent and important plugins on a host. <a target="_blank" href="https://supermarket.chef.io/cookbooks/chef_install_configure_collectd">Click here to access it on Chef Supermarket</a>.

- **Puppet module: signalfx/collectd**

  SignalFx provides Puppet modules to install the SignalFx collectd agent and important plugins on a host. <a target="_blank" href="https://forge.puppet.com/signalfx/collectd">Click here to access it on Puppet Forge</a>.

- **Manual step-by-step installation**

  To manually complete the steps that SignalFx's install script performs automatically, <a target="_blank" href="https://github.com/signalfx/signalfx-collectd-installer/blob/master/install.sh">check out the source here on Github</a>.

### CONFIGURATION

The SignalFx collectd agent is accompanied by a default configuration file, `collectd.conf`, that does not need to be modified in order to function. <a target="_blank" href="https://github.com/signalfx/integrations/tree/master/collectd/collectd.conf">Click here to read an example configuration file for the SignalFx collectd agent</a>.

### USAGE

To use the data transmitted by the SignalFx collectd agent, check out the Hosts page in SignalFx. On this page you'll find a visualization of all transmitting hosts, built-in dashboards to show the health of your infrastructure, and recommended detectors to send intelligent alerts.

![](./img/hostspagesinglehost.png)

Installing the SignalFx collectd agent allows you to install many of the integrations that SignalFx supports. Browse available plugins for collectd on the Integrations page.

#### Adding dimensions to all datapoints

You can add a dimension to every datapoint that collectd sends to SignalFx by adding HTTP query parameters to the SignalFx ingest URL, part of the configuration for the `write_http` plugin. This allows you to add information about the host or environment to every metric. For instance, you could identify all metrics coming from production boxes with a dimension like `environment=prod`.

The SignalFx URL to which collectd will transmit data is specified in `10-write_http-plugin.conf` and by default has a value like https://ingest.YOUR_SIGNALFX_REALM.signalfx.com/v1/collectd.

Append dimensions to the  URL as `sfxdim_[DIMENSION NAME]=[DIMENSION VALUE]`. Multiple dimensions may be specified.

For example, the following URL sends data points to SignalFx with the added dimensions `serverType=API` and `tier=middleware`.

```
    URL "https://ingest.YOUR_SIGNALFX_REALM.signalfx.com/v1/collectd?sfxdim_serverType=API&sfxdim_tier=middleware"
```

#### Transmitting outside a network

If instances of collectd are unable to transmit outside the network, the <a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.signalfx.metric.proxy.html">SignalFx metric proxy</a> can be used to receive connections from many instances of collectd, and forward transmissions to SignalFx using a single outgoing HTTP connection. This is suitable for environments in which transmissions exiting a network are highly restricted.

<a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.signalfx.metric.proxy.html">Click here for more information about the SignalFx metric proxy</a>.

#### Transmitting through an existing HTTP proxy

The SignalFx collectd agent can be configured to use an HTTP proxy if needed. The changes would need to be made on files that are sourced by the init scripts. Modify or create the indicated file, with the following contents:

On CentOS/RHEL: `/etc/sysconfig/collectd`

Sample contents of the file:
```
HTTP_PROXY="http://YOUR_HTTP_PROXY:PROXY_PORT"
HTTPS_PROXY="https://YOUR_HTTPS_PROXY:PROXY_PORT"
```

On Debian/Ubuntu: `/etc/default/collectd`

Sample contents of the file:
```
export http_proxy="http://YOUR_HTTP_PROXY:PROXY_PORT"
export https_proxy="https://YOUR_HTTPS_PROXY:PROXY_PORT"
```

Replace `YOUR_HTTP_PROXY` and `YOUR_HTTPS_PROXY` with the hostname of the HTTP proxy to be used, and `PROXY_PORT` with the port at which to access it.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
