# ![](https://github.com/signalfx/integrations/blob/master/signalfx-smart-gateway/img/integration_smartgateway.png) SignalFx Smart Gateway

Information associated with the SignalFx Smart Gateway can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/signalfx-smart-gateway">here</a>.

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)

### DESCRIPTION

The SignalFx Smart Gateway observes every transaction across distributed services, generates metrics for each unique span and trace path, and prioritizes interesting outlier traces to forward to SignalFx as part of our NoSample™ Tail-Based Distributed Tracing feature. The Smart Gateway can be deployed as a scalable, self-coordinating cluster for high-availability and volume applications.

### INSTALLATION

The SignalFx Smart Gateway is available as a single, statically-linked binary. The latest version can be downloaded <a target="_blank" href="/#/smart-gateway/download/v2.1.0">here</a> from SignalFx. Alternatively, you can download a specific version of the SignalFx Smart Gateway from the command line using `curl`:

```
curl -qs -H"X-SF-Token:YOUR_SIGNALFX_API_TOKEN" https://app.YOUR_SIGNALFX_REALM.signalfx.com/v2/smart-gateway/download/v2.1.0 | gunzip > smart-gateway
```

Make sure to mark the `smart-gateway` binary as executable:

```
chmod +x smart-gateway
```

The Smart Gateway is designed to run in your environment, close to your applications, and receive all metrics and trace spans from your applications before they are forwarded to SignalFx.

Once you have downloaded the Smart Gateway, follow the installation, configuration and deployment instructions from the <a target="_blank" href="https://docs.signalfx.com/en/latest/apm/apm-deployment/smart-gateway.html#install-and-configure-the-smart-gateway">Smart Gateway Deployment Guide</a>.

#### Verifying the Smart Gateway Download

To verify the integrity of your Smart Gateway binary, use `sha256sum` to compute the checksum of the file, and compare to the checksum listed below for your respective version

```
sha256sum smart-gateway
```

It is also possible to download the checksum using `curl`, to automate the verification:

```
curl -qs -H"X-SF-Token:YOUR_SIGNALFX_API_TOKEN" https://app.YOUR_SIGNALFX_REALM.signalfx.com/v2/smart-gateway/checksum/v2.1.0 > smart-gateway.sha256
sha256sum -c smart-gateway.sha256
```

The downloaded checksum assumes that the Smart Gateway binary is in the current directory, in a file named `smart-gateway`

#### Changelog

##### Latest Version: v2.1.0 (October 28, 2019)

<a target="_blank" href="/#/smart-gateway/download/v2.1.0">Download Smart Gateway v2.1.0</a><br/>
_SHA256: `8308b031b07892131a0bdb0f1bba0b9666c8625398f1645d4b7fb0518cf18494`_

* Scale and performance fixes that allow the Smart Gateway cluster to scale to billions of spans per minute
* <a target="_blank" href="https://docs.signalfx.com/en/latest/apm/apm-deployment/advanced-gateway-features.html#extended-span-identity-metrics-with-custom-dimensionalization">Custom dimensionalization</a>.
* Tracing metrics emitted are now based on the previous 10 seconds instead of total history
* Spans coming through Istio proxies are tagged appropriately
* Tag initiating spans with the Smart Gateway which selected it

##### v2.0.4 (September 13, 2019)

<a target="_blank" href="/#/smart-gateway/download/v2.0.4">Download Smart Gateway v2.0.4</a><br/>
_SHA256: `7429a8f42e2eb7ebfe340656ad7cab9822b52b44a41471fba619bdc77a73909d`_

* Critical bug fix to 2.0.3 around metrics reporting

##### v2.0.3 (September 10, 2019)

<a target="_blank" href="/#/smart-gateway/download/v2.0.3">Download Smart Gateway v2.0.3</a><br/>
_SHA256: `9f334adf76e11df5bb12e41c5aded1ed443efd0960dda37266935fef65ed86fe`_

* DO NOT USE THIS VERSION, use v2.0.4 instead
* Provides code to do seamless rolling upgrade to imminant performance release

##### v2.0.2 (September 3, 2019)

<a target="_blank" href="/#/smart-gateway/download/v2.0.2">Download Smart Gateway v2.0.2</a><br/>
_SHA256: `e3b7bb4e85a12bbda2a8d7793aa9f7cf710e69c90def9b48bf9a491d22b81f75`_

* Fix a critical bug in the Smart Gateway

##### v2.0.1 (August 16, 2019)

<a target="_blank" href="/#/smart-gateway/download/v2.0.1">Download Smart Gateway v2.0.1</a><br/>
_SHA256: `cbbc447f5ce714fd06218a65b187e36441f69bad20122b81b66622993f0ee396`_

**Note: this is a major update with breaking changes; existing Smart Gateway clusters cannot be upgraded via a rolling update. To upgrade a Smart Gateway cluster from 1.x to 2.x, you must fully shutdown your existing cluster, and follow the <a href="https://docs.signalfx.com/en/latest/apm/apm-deployment/smart-gateway-clusters.html#bootstrapping">bootstrap</a> procedure to start new 2.x instances.**

This update significantly increases the performance and accuracy of the Smart Gateway via improvements to Trace and Span sharding, histogram improvements, and an optional trace distribution layer.

_Please refer to the <a target="_blank" href="https://docs.signalfx.com/en/latest/apm/apm-deployment/smart-gateway.html#instance-sizing">sizing guidelines</a> for updated size recommendations._

* Update base SignalFx Gateway version to v1.2.9
* Improved accuracy of tail-based sampling baselines and tracing metrics by utilizing t-digest histograms.
* Metrics about the Smart Gateway are prefixed with `gateway.*`
* The runtime flag `-version` will print the Smart Gateway version to the console.
* The Smart Gateway can be configured as a two-tier deployment with an intelligent distribution tier to route traces and spans to their appropriate Smart Gateway.

##### v1.1.1 (June 4, 2019)

<a target="_blank" href="/#/smart-gateway/download/v1.1.1">Download Smart Gateway v1.1.1</a><br>
_SHA256: `c85c33dc988f7fe996718b74e616854e5585c36ce5f9af644fb05c77d6c01103`_

* Fix for attaching cluster variable to retained traces

##### v1.1.0 (May 29, 2019)

<a target="_blank" href="/#/smart-gateway/download/v1.1.0">Download Smart Gateway v1.1.0</a><br>
_SHA256: `82774e826ef5fc511bd29a85e3aa79bf60db5719d05fc32eb7b05ae5e1b0dcdc`_

* Update base SignalFx Gateway version to v1.0.31
* Report Gateway and NoSample Module version properties as version number, instead of commit hash
* Fix accuracy of `traces.count` and `spans.count` metrics

##### v1.0.5 (April 29, 2019)

<a target="_blank" href="/#/smart-gateway/download/v1.0.5">Download Smart Gateway v1.0.5</a><br>
_SHA256: `56e8a00ca268ef8534a715aadbf6853d54c1b2a4fbf4d58d69bc7cb866d7a94f`_

* Update base SignalFx Gateway version to v1.0.29
* Ensure http client drains and closes responses
* Improve joining existing Smart Gateway clusters

##### v1.0.4 (April 23, 2019)

<a target="_blank" href="/#/smart-gateway/download/v1.0.4">Download Smart Gateway v1.0.4</a><br>
_SHA256: `faa2dc350a1c223c652069c09038f647ea584fab4d2b7953fd4322519779fe64`_

* Update base SignalFx Gateway version to v1.0.28
* Proactively clean up expired file descriptors

##### v1.0.3 (April 11, 2019)

<a target="_blank" href="/#/smart-gateway/download/v1.0.3">Download Smart Gateway v1.0.3</a><br>
_SHA256: `0f59091d2f802f1866f59e27d1d1c05bf670159d21e26a897791d4af6419ac65`_

* Add `ForceTraceInitiatingSpan` config to force an initiating span if none is present on the trace

##### v1.0.2 (March 26, 2019)

<a target="_blank" href="/#/smart-gateway/download/v1.0.2">Download Smart Gateway v1.0.2</a><br>
_SHA256: `71ac690d578d09057d6893e04fc52d70b86a4f4e4e88f883c0f91e03acb352a4`_

* Update base SignalFx Gateway version to v1.0.27
* Expose and pass through etcd configurations
    * EtcdElectionTimeout
    * EtcdSnapCount
    * EtcdMaxSnapFiles
    * EtcdMaxWalFiles
* Enable client-only mode for clustered Smart Gateways
* Add `ObfuscateSpanTags` and `RemoveSpanTags` config

##### v1.0.1 (March 6, 2019)

<a target="_blank" href="/#/smart-gateway/download/v1.0.1">Download Smart Gateway v1.0.1</a><br>
_SHA256: ``53819394425c1a0db60fdc3fc9ba8bab2d85d1c027e1218ee2b938357b50e818``_

* Update base SignalFx Gateway version to v1.0.18
* Utilize new on-disk format to reduce memory usage
* Enforce consistent cluster name within etcd cluster
* Add `AuthTokenEnvVar` config
* Add `SpanNameReplacementBreakAfterMatch` config

##### v1.0.0 (February 4, 2019)

<a target="_blank" href="/#/smart-gateway/download/v1.0.0">Download Smart Gateway v1.0.0</a><br>
_SHA256: `2fadd3abeb99e1b781a7805ea524bcc9773a5efc122260abdd684f6799afdda9`_

* Update base SignalFx Gateway version to v1.0.9
* Update Smart Gateway to use Golang 1.11.5
* Add `SpanNameReplacementRules` config

### USAGE

The SignalFx Smart Gateway is built on top of the SignalFx Gateway. Please refer to the <a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.signalfx.gateway.html">SignalFx Gateway documentation</a> after configuring the SignalFx Smart Gateway for information on additional configuration options.
