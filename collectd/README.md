---
title: SignalFx collectd
brief: SignalFx validated version of collectd.
---

# SignalFx collectd Agent

_This is a directory consolidate all the metadata associated with the SignalFx collectd Agent. The relevant code for the plugin can be found [here](https://github.com/signalfx/collectd/)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation - shell script](#install-with-shell-script)
- [Additional Install Options](#additional-install-options)
 - [Installation - manual install](././install_manual.md)
 - [Installation - Puppet](././install_puppet.md)
 - [Installation - CHEF](././install_chef.md)
- [License](#license)
- [HTTP Proxy](#http-proxy)

## DESCRIPTION

SignalFx has always recommended the open-source data collection agent [collectd](http://collectd.org) to our customers, as it’s fast, performs well at scale, and enjoys great community support. We released a new [SignalFx collectd](https://github.com/signalfx/collectd) package to make a great agent even better.

**[SignalFx collectd agent](https://github.com/signalfx/collectd)** introduces the following changes:

* **Increased Character limit:** We’ve increased the number of characters that can be used in dimension key-value pairs to 1024, up from 64. In practice, this allows you to send as many dimensions as you want.
* **Buffer Flushing** To ensure that metrics always arrive in a timely manner, we’ve added a timer to SignalFx collectd so that it transmits data to SignalFx either when the data buffer is full or when a time limit is reached, whichever happens first. This capability is particularly useful if you are only collecting small quantities of time-sensitive metrics.
* **HTTP Error Logging** We’re providing greater visibility into how collectd itself is functioning, by logging HTTP codes from unsuccessful data transmissions by the write_http plugin, and by logging the name of every collectd plugin that is loaded at startup. In addition, we’re also updating the SignalFx metadata plugin for collectd to report the DPM transmitted by each collectd plugin installed on a host, to help you manage and keep track of your usage. Find this in the Catalog under the metric gauge.sf.host-dpm.

You can view the full [changelog](https://github.com/signalfx/collectd/blob/collectd-5.5.0-sfx/ChangeLog). All changes have also been submitted back to the [collectd project](http://collectd.org) so that everyone can benefit.

## REQUIREMENTS AND DEPENDENCIES

SignalFx has built an installation script for the following versions of Linux:

| Software  | Version        |
|-----------|----------------|
| Debian  | 7 & 8 |
| Ubuntu  | 12.04, 14.04 & 15.04 |
| RHEL/Centos | 6.x & 7.x |
| Amazon Linux | 2014.09 & 2015.03 |

To get started, you'll need your org's API token. To find it:

Open your SignalFx profile page at https://app.signalfx.com/#/myprofile.

Locate the words "API Token" on the page.

Click the link next to "API Token" that says "show". Your API token appears.

## INSTALL WITH SHELL SCRIPT

SignalFx provides a shell script that you can use to install our latest build of collectd, install and configure important plugins, and configure collectd to send metrics to SignalFx.

If you have already installed collectd, this script will install the SignalFx metadata plugin and configure collectd to send metrics to SignalFx.

Follow these instructions to use the script.

1. **Download and run the script**

 **note:** You must have administrator (sudo) privileges to run this script.

 Run the following command in your command-line, replacing API_TOKEN with your org's API token.
 ```
 sudo curl -sSL https://dl.signalfx.com/collectd-install | bash -s API_TOKEN
 ```
 This command will download and run the script. On startup, the script will ask you to confirm that you want to proceed.

1. **Provide your hostname**

 During the configuration of collectd, the script will ask you to provide collectd with your system's hostname.

 * Type 'dns' and press enter to automatically collect this system's hostname from DNS.
 * Type 'input' and press enter to provide the hostname yourself. When prompted, type in your desired hostname and press enter.

When the script successfully completes, it starts up collectd, which begins reporting metrics to SignalFx. If you encounter any errors see Troubleshooting below, or send us an email at support@signalfx.com.

## Additional Install Options

- [![Manual Install](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_collectd.png)](././install_manual.md)
- [![CHEF Install](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_chef.png)](././install_chef.md)
- [![Puppet Install](https://github.com/signalfx/integrations/blob/master/collectd/img/integrations_puppet.png)](././install_puppet.md)

## LICENSE

SignalFx version of collectd is released under the Apache 2.0 license. See LICENSE for more details.

## HTTP Proxy

Collectd can talk through an http proxy if needed. The changes would need to be made on files that are sourced by the init scripts.

On CentOS:
* Modify/Create either of the following files: '/etc/sysconfig/collectd' or '/etc/default/collectd'

On RHEL:
* Modify/Create the following file: '/etc/sysconfig/collectd'

On Debian/Ubuntu:
* Modify/Create the following file: '/etc/default/collectd'

Sample contents of the file:
```
export http_proxy="http://HTTP_PROXY:PROXY_PORT"
export https_proxy="https://HTTPS_PROXY:PROXY_PORT"
```

