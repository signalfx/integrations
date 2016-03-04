---
title: collectd interface Plugin
brief: Interface metrics for collectd.
---

# Interface collectd Plugin  ![](https://github.com/signalfx/Integrations/blob/master/collectd/img/integrations_collectd.png)

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

From [collectd wiki](https://collectd.org/wiki/index.php/Plugin:Interface):

The Interface plugin collects information about the traffic (octets per second), packets per second and errors of interfaces (of course number of errors during one second). If you're not interested in all interfaces but want to exclude some, or only collect information of some selected interfaces, you can select the “interesting” interfaces using the plugin's configuration.

### REQUIREMENTS AND DEPENDENCIES

This plugin requires:

- collectd 1.0+

### INSTALLATION

This plugin is included with [SignalFx's collectd package](https://support.signalfx.com/hc/en-us/articles/208080123).

### CONFIGURATION

#### Optional configuration

The following configuration options are *optional*. You may specify them in the configuration file in order to override default values provided by the plugin.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| Interface | Include specific Interface(s) | "lo" "sit0" |
| IgnoreSelected  | Ignore the designation of specific Disks | true |

### USAGE

The primary use of this plugin is to track the I/O of system interfaces. This is not only valuable data to understand the workloads on specific systems but can be combined with other systema dn application metrics to identify issues related to network and data I/O traffic.

### METRICS

For documentation of the metrics and dimensions emitted by this plugin, [click here](././docs).

### LICENSE

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; only version 2 of the License is applicable.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
