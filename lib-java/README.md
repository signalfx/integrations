---
title: Java client library
brief: Libraries for instrumenting Java applications and reporting metrics to SignalFx
---


# Java client library for SignalFx


- [Description](#description)
- [Requirements and Dependencies](#requirements-and-dependencies)
- [Installation](#installation)
- [CodaHale Metrics 3.0.x](#codahale3)
- [Yammer Metrics](#yammer)
- [Example Project](#example-project)
- [Sending Metrics Without CodaHale](#nocoda)
- [License](#license)


### <a name="description"></a>DESCRIPTION

This repository contains libraries for instrumenting Java applications and
reporting metrics to SignalFx, using Codahale Metrics.

You can also use the module `signalfx-java` to send metrics directly to SignalFx
using protocol buffers, without using Codahale or Yammer metrics.


### <a name="requirements-and-dependencies"></a>REQUIREMENTS AND DEPENDENCIES

#### Codahale, Yammer and Dropwizard Metrics version

We recommend sending metrics with Java using Codahale Metrics version 3.0+. You
can also use Yammer Metrics 2.0.x (an earlier version of Codahale Metrics). More
information on the Codahale Metrics library can be found on the
[Codahale Metrics website](https://dropwizard.github.io/metrics/).

#### Supported languages

Java 6+ with `signalfx-metrics`.


#### API access token

To use this library, you need a SignalFx API access
token. [Click here for more information on retrieving your API token](https://developers.signalfx.com/docs/authentication-overview). 


### <a name="installation"></a>INSTALLATION

#### Using this library in your project with Maven

If you're using Maven, add the following to your project's `pom.xml` file.

To work with Codahale 3.0.x:

```xml
<dependency>
  <groupId>com.signalfx.public</groupId>
  <artifactId>signalfx-codahale</artifactId>
  <version>0.0.23</version>
</dependency>
```

To work with Yammer Metrics 2.0.x:

```xml
<dependency>
<groupId>com.signalfx.public</groupId>
  <artifactId>signalfx-yammer</artifactId>
  <version>0.0.23</version>
</dependency>
```

#### Using this library in your project with SBT

If you're using SBT, add the following to your project's `build.sbt` file.

To work with Codahale 3.0.x:

```
libraryDependencies += "com.signalfx.public" % "signalfx-codahale" % "0.0.23"
```

To work with Yammer Metrics 2.0.x:

```
libraryDependencies += "com.signalfx.public" % "signalfx-yammer" % "0.0.23"
```

#### From source

You can also install this library from source by cloning the repo and using
`mvn install` as follows. However, we strongly recommend using the automated
mechanisms described above.

```
$ git clone https://github.com/signalfx/signalfx-java.git
Cloning into 'signalfx-java'...
remote: Counting objects: 930, done.
remote: Compressing objects: 100% (67/67), done.
remote: Total 930 (delta 20), reused 0 (delta 0)
Receiving objects: 100% (930/930), 146.79 KiB | 0 bytes/s, done.
Resolving deltas: 100% (289/289), done.
Checking connectivity... done.
$ cd signalfx-java
$ mvn install
[INFO] Scanning for projects...
...
...
...
[INFO] SignalFx parent .................................. SUCCESS [  2.483 s]
[INFO] SignalFx Protocol Buffer definitions ............. SUCCESS [  5.503 s]
[INFO] SignalFx Protobuf Utilities ...................... SUCCESS [  2.269 s]
[INFO] SignalFx java libraries .......................... SUCCESS [  3.728 s]
[INFO] Codahale to SignalFx ............................. SUCCESS [  2.910 s]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 17.120 s
[INFO] ------------------------------------------------------------------------
```


### <a name="codahale3"></a>CODAHALE METRICS 3.0.x

#### 1. Set up the Codahale reporter

```java
final MetricRegistry metricRegistry = new MetricRegistry();
final SignalFxReporter signalfxReporter = new SignalFxReporter.Builder(
    metricRegistry,
    "SIGNALFX_AUTH_TOKEN"
).build();
signalfxReporter.start(1, TimeUnit.SECONDS);
final MetricMetadata metricMetadata = signalfxReporter.getMetricMetadata();
```

#### 2. Send a metric

```java
// This will send the current time in ms to SignalFx as a gauge
metricRegistry.register("gauge", new Gauge<Long>() {
    public Long getValue() {
        return System.currentTimeMillis();
    }
});
```

#### 3. Add existing dimensions and metadata to metrics

You can add SignalFx specific metadata to Codahale metrics by first gathering
available metadata using `getMetricMetadata()`, then attaching the
MetricMetadata to the metric.

When you use MetricMetadata, call the .register() method you get from the call
forMetric() rather than registering your metric directly with the
metricRegistry.  This will construct a unique Codahale string for your metric.

```java
/*
 * This will send the size of a queue as a gauge, and attach dimension
 * 'queue_name' to the gauge.
 */
final Queue customerQueue = new ArrayBlockingQueue(100);
metricMetadata.forMetric(new Gauge<Long>() {
    @Override
    public Long getValue() {
        return customerQueue.size();
    }
}).withDimension("queue_name", "customer_backlog")
  .register(metricRegistry);
```

#### 4. (optional) Add dimensions without knowing if they already exist

We recommend creating your Codahale object as a field of your class, as a
counter or gauge, then using that field to increment values. If you don't want
to maintain this for reasons of code cleanliness, you can create it on the fly
with our builders.

For example, if you wanted a timer that included a dimension indicating which
store it is from, you could use code like this.

```java
Timer t = metricMetadata
    .forBuilder(MetricBuilder.TIMERS)
    .withMetricName("request_time")
    .withDimension("storename", "electronics")
    .createOrGet(metricRegistery);

Timer.Context c = t.time();
try {
    System.out.println("Doing store things");
} finally {
    c.close();
}

/*
 * Java 7 alternative:
 *
 * try (Timer.Context ignored = t.time()) {
 *     System.out.println("Doing store things");
 * }
 */
```

#### After setting up Codahale

After setting up a SignalFxReporter, you can use Codahale metrics as you
normally would, reported at the frequency configured by the `SignalFxReporter`.

#### Default Dimensions
Sometimes there is a desire to set one or more dimension key/value pairs
on every datapoint that is reported by this library. In order to do this
call `addDimension(String key, String value)` or
`addDimensions(Map<String,String> dimensions)` on the `SignalFxReport.Builder`
object. Note that if IncrementalCounter is used to create a distributed
counter you will want to make sure that none of the dimensions passed
to addDimension/addDimensions are unique to the reporting source
(e.g. hostname, AWSUniqueId) as this will make make the counter
non-distributed. For such dimensions use `addUniqueDimensions/addUniqueDimension`
on the `SignalFxReport.Builder` object.

#### AWS Integration
To enable AWS integration in SignalFx (i.e aws tag/property syncing) to a metric
you can use `com.signalfx.metrics.aws.AWSInstanceInfo`. And either add it as
a dimension in `MetricMetadata` or add it as a default dimension.

```java
String instanceInfo = AWSInstanceInfo.get()
Timer t = metricMetadata
    .forBuilder(MetricBuilder.TIMERS)
    .withMetricName("request_time")
    .withDimension(AWSInstanceInfo.DIMENSION_NAME, instanceInfo)
    .createOrGet(metricRegistery);

/**
 * As default dimension
 */
final SignalFxReporter signalfxReporter = new SignalFxReporter.Builder(
    metricRegistry,
    "SIGNALFX_AUTH_TOKEN"
).addUniqueDimension(AWSInstanceInfo.DIMENSION_NAME, instanceInfo).build();
```

### <a name="yammer"></a>YAMMER METRICS

You can also use this library with Yammer metrics 2.0.x as shown in the
following examples.

#### 1. Set up Yammer metrics

```java
final MetricRegistry metricRegistry = new MetricRegistry();
final SignalFxReporter signalfxReporter = new SignalFxReporter.Builder(
    metricRegistery,
    "SIGNALFX_AUTH_TOKEN"
).build();
signalfxReporter.start(1, TimeUnit.SECONDS);
final MetricMetadata metricMetadata = signalfxReporter.getMetricMetadata();
```

#### 2. Send a metric with Yammer metrics

```java
// This will send the current time in ms to SignalFx as a gauge
MetricName gaugeName = new MetricName("group", "type", "gauge");
Metric gauge = metricRegistry.newGauge(gaugeName, new Gauge<Long>() {
    @Override
    public Long value() {
        return System.currentTimeMillis();
    }
});
```

#### 3. Add Dimensions and SignalFx metadata to Yammer metrics

Use the MetricMetadata of the reporter as shown.

```java
final Queue customerQueue = new ArrayBlockingQueue(100);

MetricName gaugeName = new MetricName("group", "type", "gauge");
Metric gauge = metricRegistry.newGauge(gaugeName, new Gauge<Integer>() {
    @Override
    public Integer value() {
        return customerQueue.size();
    }
});

metricMetadata.forMetric(gauge)
    .withDimension("queue_name", "customer_backlog");
```

#### 4. Adding Dimensions without knowing if they already exist

This is not supported in Yammer Metrics 2.0.x.

#### Changing the default source

The default source name for metrics is discovered by [SourceNameHelper]
(signalfx-java/src/main/java/com/signalfx/metrics/SourceNameHelper.java).
If you want to override the default behavior, you can pass a third parameter to
your Builder and that String is then used as the source.

For example:

```
final SignalFxReporter signalfxReporter = new SignalFxReporter.Builder(
    metricRegistry,
    "SIGNALFX_AUTH_TOKEN",
    "MYHOST1"
).build();
```

#### Default Dimensions
Sometimes there is a desire to set one or more dimension key/value pairs
on every datapoint that is reported by this library. In order to do this
call `addDimension(String key, String value)` or
`addDimensions(Map<String,String> dimensions) on the `SignalFxReport.Builder`
object.

#### AWS Integration
To enable AWS integration in SignalFx (i.e aws tag/property syncing) to a metric
you can use `com.signalfx.metrics.aws.AWSInstanceInfo`. And either add it as
a dimension in `MetricMetadata` or add it as a default dimension.

```java
String instanceInfo = AWSInstanceInfo.get()
Timer t = metricMetadata
    .forBuilder(MetricBuilder.TIMERS)
    .withMetricName("request_time")
    .withDimension(AWSInstanceInfo.DIMENSION_NAME, instanceInfo)
    .createOrGet(metricRegistery);

/**
 * As default dimension
 */
final SignalFxReporter signalfxReporter = new SignalFxReporter.Builder(
    metricRegistry,
    "SIGNALFX_AUTH_TOKEN"
).addDimension(AWSInstanceInfo.DIMENSION_NAME, instanceInfo).build();
```

### <a name="example-project"></a>EXAMPLE PROJECT

You can find a full-stack example project called "signalfx-yammer-example" in
the repo.

Run it as follows:

1. Download the code and create an "auth" file in the "signalfx-yammer-example"
   directory. The auth file should contain the following:

    ```
    auth=<signalfx API Token>
    host=https://ingest.signalfx.com
    ```

2. Run the following commands in your terminal to install and run the example
   project, replacing `path/to/signalfx-yammer-example` with the location of the
   example project code in your environment. You must have Maven installed.

    ```
    cd path/to/signalfx-yammer-example
    mvn install
    mvn exec:java -Dexec.mainClass="com.signalfx.yammer.example.App"
    ```

New metrics from the example project should appear in SignalFx.

### <a name="nocoda"></a>SENDING METRICS WITHOUT CODAHALE

We recommend sending metrics using Codahale as shown above. You can also
interact with our Java library directly if you do not want to use Codahale. To
do this, you will need to build the metric manually using protocol buffers as
shown in the following example.

```java
DataPointReceiverEndpoint dataPointEndpoint = new DataPointEndpoint();
AggregateMetricSender mf = new AggregateMetricSender("test.SendMetrics",
    new HttpDataPointProtobufReceiverFactory(dataPointEndpoint).setVersion(2),
    new StaticAuthToken(auth_token),
    Collections.<OnSendErrorHandler> singleton(new OnSendErrorHandler() {
        @Override
        public void handleError(MetricError metricError) {
            System.out.println("Unable to POST metrics: " + metricError.getMessage());
        }
    }));

try (AggregateMetricSender.Session i = mf.createSession()) {
    i.setDatapoint(
        SignalFxProtocolBuffers.DataPoint.newBuilder()
            .setMetric("curtime")
            .setValue(
                SignalFxProtocolBuffers.Datum.newBuilder()
                    .setIntValue(System.currentTimeMillis()))
            .addDimensions(
                SignalFxProtocolBuffers.Dimension.newBuilder()
                    .setKey("source")
                    .setValue("java"))
            .build());
}
```

### <a name="license"></a>LICENSE

This library is released under the Apache 2.0 license. See [LICENSE](https://github.com/signalfx/signalfx-java/blob/master/LICENSE)for more details.
