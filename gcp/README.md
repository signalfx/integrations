# ![](./img/integration_gcp.png) Google Cloud Platform

- [Description](#description)
- [Configuration](#configuration)
- [Usage](#usage)
- [Metrics](#metrics)
- [License](#license)

### DESCRIPTION

Use SignalFx to monitor Google Cloud Platform (GCP) services via StackDriver
Monitoring. This integration enables data collection from all GCP web services
that report to StackDriver.

#### FEATURES

Connecting to GCP allows you to take advantage of SignalFx’s extensive GCP support.

- SignalFx can sync metadata about your GCP hosts to enrich metrics reported by
    StackDriver or the [SignalFx collectd
    agent](https://github.com/signalfx/integrations/tree/master/collectd)[](sfx_link:sfxcollectd).
- SignalFx provides built-in dashboards for many GCP services that report to
    StackDriver, such as [Google Compute Engine](https://github.com/signalfx/integrations/tree/master/google-compute-engine)[](sfx_link:google-compute-engine)
    and [Google Cloud Datastore](https://github.com/signalfx/integrations/tree/master/google-cloud-datastore)[](sfx_link:google-cloud-datastore).



### CONFIGURATION

Connect to GCP on the Integrations page in SignalFx.

To connect SignalFx to GCP, you’ll create a new IAM member and role in GCP for
SignalFx to use, provide information from SignalFx to a GCP label, then specify
services to monitor in SignalFx. You must be an administrator of
your SignalFx account to connect SignalFx to GCP.

You must be an administrator of your SignalFx account to connect SignalFx to
GCP. [Click here for detailed
instructions](http://docs.signalfx.com/en/latest/getting-started/send-data.html#gcp).

### USAGE

#### Data available from GCP

##### Importing GCP metrics and dimensions

### METRICS

For more information about the metrics emitted by GCP StackDriver, see the documentation for individual services.

### LICENSE

This integration is released under the Apache 2.0 license. See [LICENSE](./LICENSE) for more details.
