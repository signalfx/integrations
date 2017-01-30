# ![](https://github.com/signalfx/integrations/blob/master/collectd-docker/img/integrations_docker.png) Docker

_This directory consolidates all the metadata associated with the Docker plugin for collectd. The relevant code for the plugin can be found [here](https://github.com/signalfx/docker-collectd-plugin)_

- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

This is the SignalFx Docker plugin. Follow these instructions to install the Docker plugin for collectd.

The [`docker-collectd`](https://github.com/signalfx/docker-collectd-plugin) plugin collects metrics about the Docker containers running on the system using Docker's stats API. It reports metrics about the CPU utilization of each container, their memory consumption, and their network and disk activity.

#### FEATURES

##### Built-in dashboards

- **Docker Hosts**: Overview of all data from Docker hosts.

  [<img src='./img/dashboard_docker_hosts.png' width=200px>](./img/dashboard_docker_hosts.png)

- **Docker Host**: Focus on a single Docker host.

  [<img src='./img/dashboard_docker_host.png' width=200px>](./img/dashboard_docker_host.png)

- **Docker Container**: Focus further on a single running Docker container.

  [<img src='./img/dashboard_docker_container.png' width=200px>](./img/dashboard_docker_container.png)

### REQUIREMENTS AND DEPENDENCIES

#### Version information

| Software | Version      |
|----------|--------------|
| collectd | 5.0 or later |
| Python   | 2.6 or later |
| Docker   | 1.5 or later |
| Python plugin for collectd | (included with [SignalFx collectd agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd)) |


### INSTALLATION

1. Download the [docker-collectd-plugin](https://github.com/signalfx/docker-collectd-plugin) Python module.

1. Run the following command to install the module’s dependencies using `pip`, replacing the example path with the download location of the `docker-collectd-plugin` module:

  ```
  sudo pip install -r /path/to/docker-collectd-plugin/requirements.txt
  ```

 **On Amazon Linux**: Run the following commands instead:
  ```
  yum install python26-pip
  sudo pip-2.6 install -r /path/to/docker-collectd-plugin/requirements.txt
  ```

1. Download SignalFx’s [sample configuration file](https://github.com/signalfx/integrations/blob/master/collectd-docker/10-docker.conf) for this plugin to `/etc/collectd/managed_config`.

1. Modify the configuration file to provide values that make sense for your environment, as described in [Configuration](#configuration) below.

1. Restart collectd.

### CONFIGURATION

Using the example configuration file [10-docker.conf](https://github.com/signalfx/integrations/tree/master/collectd-docker/10-docker.conf) as a guide, provide values for the configuration options listed below that make sense for your environment.

| configuration option | definition | default value |
| ---------------------|------------|---------------|
| TypesDB | Path on disk where collectd can find the Types.db file included in this module. | "/usr/share/collectd/docker-collectd-plugin/dockerplugin.db" |
| ModulePath | Path on disk where collectd can find this module. | "/usr/share/collectd/docker-collectd-plugin" |
| BaseURL | URL of your Docker daemon's remote API | "unix://var/run/docker.sock" |
| Timeout  | Time in seconds that collectd will wait for a response from Docker   | 3 |
| Verbose | Turns on verbose log statements | false |

### USAGE

All metrics reported by the Docker collectd plugin will contain the following dimensions:

* `host` will contain the hostname (as known by collectd) of the machine reporting the metrics
* `plugin` is always set to `docker`
* `plugin_instance` will contain the name of the container the metrics are from. The container name is used because that's usually a more stable value than the container ID, which changes on every restart.

Sample of built-in dashboard in SignalFx:

![](././img/dashboard_docker.png)

### METRICS

For full documentation of the metrics and dimensions emitted by this plugin, see the `docs` directory in this repository.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
