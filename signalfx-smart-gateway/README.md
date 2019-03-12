# ![](https://github.com/signalfx/integrations/blob/master/signalfx-smart-gateway/img/integration_smartgateway.png) SignalFx Smart Gateway

Information associated with the SignalFx Smart Gateway can be found <a target="_blank" href="https://github.com/signalfx/integrations/tree/release/signalfx-smart-gateway">here</a>.

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)

### DESCRIPTION

The SignalFx Smart Gateway observes every transaction across distributed services, generates metrics for each unique span and trace path, and prioritizes interesting outlier traces to forward to SignalFx as part of our NoSample™ Tail-Based Distributed Tracing feature. The Smart Gateway can be deployed as a scalable, self-coordinating cluster for high-availability and volume applications.

### INSTALLATION

The SignalFx Smart Gateway is available as a single, statically-linked binary that can be downloaded <a target="_blank" href="/#/smart-gateway/download">here</a> from SignalFx. Alternatively, you can download the SignalFx Smart Gateway from the command line using `curl`:

```
$ curl -qs -H"X-SF-Token:YOUR_SIGNALFX_API_TOKEN" \
    https://app.YOUR_SIGNALFX_REALM.signalfx.com/v2/smart-gateway/download | gunzip > smart-gateway
```

The Smart Gateway is designed to run in your environment, close to your applications, and receive all metrics and trace spans from your applications before they are forwarded to SignalFx.

Once you have downloaded the Smart Gateway, follow the installation, configuration and deployment instructions from the <a target="_blank" href="https://docs.signalfx.com/en/latest/apm/apm-deployment/smart-gateway.html#install-and-configure-the-smart-gateway">Smart Gateway Deployment Guide</a>.

### USAGE

The SignalFx Smart Gateway is built on top of the SignalFx Gateway. Please refer to the <a target="_blank" href="https://docs.signalfx.com/en/latest/integrations/integrations-reference/integrations.signalfx.gateway.html">SignalFx Gateway documentation</a> after configuring the SignalFx Smart Gateway for information on additional configuration options.
