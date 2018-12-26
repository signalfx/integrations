# ![](https://github.com/signalfx/integrations/blob/master/signalfx-smart-gateway/img/integration_smartgateway.png) SignalFx Smart Gateway

Information associated with the SignalFx Smart Gateway can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/signalfx-smart-gateway">here</a>.

- [Description](#description)
- [Sizing Details](#sizing-details)
- [Installation](#installation)
    - [Single Smart Gateway](#single-smart-gateway)
    - [Clustered Smart Gateway](#clustered-smart-gateway)
- [Usage](#usage)

### DESCRIPTION

The SignalFx Smart Gateway observes every transaction across distributed services, generates metrics for each unique span and trace path, and prioritizes interesting outlier traces to forward to SignalFx as part of our NoSample™ Tail-Based Distributed Tracing feature. The Smart Gateway can be deployed as a scalable, self-coordinating cluster for high-availability and volume applications.

#### Sizing Details

Please refer to the the sizing details located <a target="_blank" href="https://docs.signalfx.com/en/latest/apm/apm-deployment/smart-gateway.html#instance-sizing">here</a>.

### INSTALLATION

You will want to download the Smart Gateway binary at <a target="_blank" href="/#/smart-gateway/download">here</a>.

To deploy the SignalFx Smart Gateway, start by reviewing the <a target="_blank" href="https://docs.signalfx.com/en/latest/apm/apm-deployment/smart-gateway.html#instance-sizing">sizing information</a> to determine the recommended hardware for running the Smart Gateway.

#### Single Smart Gateway

Installation and configuration information for a single Smart Gateway instance can be found <a target="_blank" href="https://docs.signalfx.com/en/latest/apm/apm-deployment/smart-gateway.html#install-and-configure-the-smart-gateway">here</a>.

#### Clustered Smart Gateway

If you have determined it is necessary, install and configure a Smart Gateway cluster referring to the cluster installation and configuration  <a target="_blank" href="https://docs.signalfx.com/en/latest/apm/apm-deployment/smart-gateway.html#install-and-configure-a-clustered-smart-gateway">documentation</a>.

After the SignalFx Smart Gateway is deployed either in standalone or cluster mode, you can point your applications at it for reporting their trace spans.

### USAGE

The SignalFx Smart Gateway is built on top of the SignalFx Gateway.  Please refer to the SignalFx Gateway <a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.signalfx.gateway.html">documentation</a> after configuring the SignalFx Smart Gateway for information on additional configuration options.
