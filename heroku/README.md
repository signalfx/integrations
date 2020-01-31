<!--- OVERVIEW --->
## <!-- -->


You can use this document to learn how to integrate your Heroku environment with SignalFx.

Based on the information you want to collect, there are two ways to integrate with SignalFx:
  * Option 1: Collect and send default Heroku metrics
  * Option 2: Collect and send properties from heroku-metadata, as well as configure other smart agent monitors


## Installation

Based on the information you want to collect, there are two ways to integrate with SignalFx. Review the appropriate option. 

  * **To collect and send default Heroku metrics**, see <a href="#option1">Option 1: Collect default metrics with the Heroku SignalFx Collector</a>.
  * **To collect and send properties from heroku-metadata**, as well as configure other smart agent monitors, see Option 2: Collect heroku-metadata with the SignalFx Smart Agent Heroku Buildpack.
  
***  

<a name="option1"></a>
### Option 1: Collect default metrics with the Heroku SignalFx Collector

You can use these instructions to collect and send default Heroku metrics to SignalFx. Specifically, you can collect:
 * Application metrics
 * Heroku Dyno metrics
 * Custom metric
Before you begin, consider the following statements:
 * In SignalFx, application metrics and Heroku Dyno metrics will be prefixed by `heroku.`.
 * Metrics are collected and sent via a Golang Heroku app.
 * At a high level, the collector runs as a HTTPS Log Drain app on Heroku.
    * To learn more, please see [HTTPS drains](https://devcenter.heroku.com/articles/log-drains#https-drains).

##### Install the Heroku SignalFx Collector

**Step 1: Deplpoy the Heroku SignalFx Collector**

1. Run the following command to clone the repo:

```
git clone git@github.com:signalfx/heroku-signalfx-collector.git
```

2. Run the following command to create a Heroku app:

```
cd heroku-signalfx-collector/
heroku create
```

3. Run the following command to add the Golang buildpack:

```
heroku buildpacks:add heroku/go
```

4. Configure the collector with the follwing environment variables:

| Envrionment Variable | Description   | Example | Required or optional |         
| -------------------- | ------------- | ------- | -------------------- |
| `SFX_TOKEN`          | Enter the SignalFx access token for the organization that will receive the data. | $`somevalidtoken` | Required |
| `SFX_INGEST_URL`     | Enter the Ingest URL to forward data to your SignalFx account. | `https://ingest.us0.signalfx.com` | Required if `SFX_REALM` is not set |
| `SFX_REALM`          | Enter the SignalFx realm for your SignalFx account. | `us0`, `us1`, `us2`, `eu0`, `ap0` | Required if `SFX_INGEST_URL` is not set |
| `SFX_METRICS_TO_EXCLUDE` | To have the collector ignore specific metrics, enter comma-seaprated metrics names. | `metric_name1,metric_name2,metric_name3` | Optional |
| `SFX_DIMENSION_PAIRS_TO_EXCLUDE` | To have the collector ignore specific dimension key-value pairs, enter comma-separated dimension key-value pairs. | `key1=val1,key2=val2` | Optional |
| `SFX_REPORTING_INTERVAL` | Configure a reporting interval for the collector in seconds. The default value is 10 seconds. | 20 | Optional |
| `SFX_INTERNAL_METRICS`  | Indicate if you want to report internal metrics. By default, this is set to `true`. | `false` | Optional

***

**Step 2: Configure the Heroku app to enable runtime metrics and dyno** metadata

1. Run the following command to Configure the Heroku app to send log run-time metrics:  

```
heroku labs:enable log-runtime-metrics
```

To learn more, please see [Log runtime metrics](https://devcenter.heroku.com/articles/log-runtime-metrics).

2. Run the following command to configure the Heroku app to send Dyno metadata:

```
heroku labs:enable runtime-dyno-metadata
```

This metadata is required by internal metrics to report accurate dimensions for fields like `app_name` and `dyno_id`. To learn more, please see [Dyno metadata](https://devcenter.heroku.com/articles/dyno-metadata).

3. Run the command below to configure the Heroku app to send data to the SignalFx collector app.

In the command below, note that:

 * `SFX_COLLECTOR_APP_NAME` is the name of the SignalFx collector app.
 * `APP_NAME` is the name of the Heroku app to monitor.
    * To set this name, use `heroku apps:info | grep '===' | cut  -d' '  -f2`
    * `app_name` is added as dimension to datapoints being by the collector.
    * This parameter is required.

```
heroku drains:add "https://<SFX_COLLECTOR_APP_NAME>.herokuapp.com?app_name=<APP_NAME>"
```

4. (Optional) When you configure the log drain, you can add query parameters, which will add custom dimensions to all datapoints sent by the SignalFx collector.

```
heroku drains:add "https://<SFX_COLLECTOR_APP_NAME>.herokuapp.com?app_name=<APP_NAME>&dim1=key1&dim2=key2"
```

In the above example, the log drain will add `dim1=key1` and `dim2=key2` to all datapoints emitted by the collector.  

***

**Step 3: Deploy the collector and send custom metrics**

1. Run the following command to deploy the SignalFx collector to Heroku:

```
git push heroku master
heroku ps:scale web=1
```

2. To send custom metrics, review the two examples below.

 * The following example displays the standard format used by Heroku to send default metrics:

```
\<(?P<pri>\d+)\>(?P<version>1) (?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{6})?\+\d{2}:\d{2}) (?P<hostname>[a-z0-9\-\_\.]+) (?P<appname>[a-z0-9\.-]+) (?P<procid>[a-z0-9\-\_\.]+) (?P<msgid>\-) (?P<message>.*)$
```

In the above example, note that:
 * The Heroku app looks for logs in this format.
 * All fields are generated by the Heroku platform, with the exception of `message`. `message` will contain application logs.
 * You can use this format to define custom metrics.

 * The following example displays the standard format with populated custom metrics:

```
gauge#quota_used=20 cumulative#response_bytes=100 sfxdimension#service=backend sfxdimension#client=sfx_app
```

In the above example, note that:
 * There are 2 datapoints:
    * `quota_used` (a `gauge` with value `20`)
    * `response_bytes` (a `cumulative counter` with value 100).
 * Both datapoints contain the `service=backend` and `client_sfx_app` dimensions.

When adding custom metrics, you can use the following keywords to construct custom metrics, which is used to identify key-value pairs as either metrics or dimensions:
 * gauge#
    * `gauge` type
 * counter#
    * `counter` type
 * cumulative#
    * `cumulative counter` type
 * sfxdimension#
    * `dimension`

***

**Step 4: Review internal metrics**

By default, these internal metrics are collected.

To turn off collection for these internal metrics, set `SFX_INTERNAL_METRICS` to `false`.

Review the following list of internal metrics:  

| Metric Name                       | Description                                                                                                                                               |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `sfx_heroku.total_drain_requests` | Number of drain requests received by the collector                                                                                                        |
| `sfx_heroku.tracked_metrics`      | Number of metrics collected per metric type. Metric types are determined by the dimension called `type` (i.e., `cumulative_counter`, `counter`, `gauge`). |

***

### Option 2: Collect heroku-metadata metrics with the SignalFx Smart Agent Heroku Buildpack

You can use this document to learn how to collect heroku-metadata, as well as configure other agent monitors.  

At a high level, you will add a Heroku buildpack to your project, to run the SignalFx Smart Agent on a Dyno.


**Step 1: Add the buildpack**

1. Access the Heroku project directory.

2. Run the following command to add the buildpack for the SignalFx agent. In `BUILDPACK_VERSION`, you must specify the version tag of the buildpack.

```
heroku buildpacks:add https://github.com/signalfx/heroku-signalfx-buildpack.git#<BUILDPACK_VERSION>
```

3. Run the following command to setup your SignalFx access token:

```
heroku config:set SFX_TOKEN=<YOUR_SFX_ACCESS_TOKEN>
```

4. To add the buildpack to an existing project, you must create an empty commit before you deploy the app:

```
git commit --allow-empty -m "empty commit"
```

5. Run the following command to deploy the app:

```
git push heroku master
```

***

**Step 2: Configure the buildpack and app**

1. Configure the buildpack with the following environment variables:

| Environment Variable   | Description   | Required or optional   |
| ---------------------- | ------------- | ---------------------- |
| `SFX_TOKEN`            | Enter your SignalFx access token. | Required |
| `SFX_AGENT_VERSION`    | Enter your SignalFx agent version, which must be at least 4.18.0. | Required |  
| `SFX_AGENT_LOG_FILE`   | Enter a location of the agent logs. | Optional, but if a location is not specified, then logs will go to `stdout`. |   


2. Run the following command to configure Heroku App to expose Dyno metadata:

```
heroku labs:enable runtime-dyno-metadata
```

The SignalFx agent requires this metadata to set global dimensions such as `app_name`, `app_id` and `dyno_id`. To learn more, please see [Heroku's documentation](https://devcenter.heroku.com/articles/dyno-metadata).

3. Override the default agent changes.

The default [SignalFx Agent config](https://github.com/signalfx/heroku-signalfx-buildpack/blob/master/setup/config.yaml) will be overridden if a config is provided in `signalfx/agent.yaml`
in the root of the Heroku project directory. In such cases, SignalFx recommends that the following defaults are retained:


```
signalFxAccessToken: {"#from": "env:SFX_TOKEN"}

globalDimensions:
  dyno_id: {"#from": "env:HEROKU_DYNO_ID"}
  app_id: {"#from": "env:HEROKU_APP_ID"}
  app_name: {"#from": "env:HEROKU_APP_NAME"}

collectd:
  configDir: tmp/collectd

monitors:
  - type: heroku-metadata
```

***
