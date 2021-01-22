This directory contains values.yaml files that can be used with Helm to install the [OpenTelemetry Collector helm chart](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/master/charts/opentelemetry-collector).

The chart configures the OpenTelemetry collector in forwarding mode where it sends traces and metrics sent to it to SignalFx.

1. Download [values.yaml](values.yaml) and [env.yaml](env.yaml).
1. Edit `env.yaml` to contain your access token, realm, etc.
1. Install Helm chart, for example:

```sh
$ helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
$ helm install my-opentelemetry-collector open-telemetry/opentelemetry-collector -f values.yaml -f env.yaml
```

**Note:** env.yaml must come after values.yaml

Installing the Helm chart creates a Kubernetes service. The name of the service depends on Helm install name. For example, using the instructions above, the service is named my-opentelemetry-collector.

You can use this service to send metrics and traces to the collector. The following table describes which ports accept which protocols.

| Protocol | Port |
|---|---|
| OTLP | 55680 |
| Jaegar-Thrift | 14268 |
| Jaeger-gRPC | 14250 |
| Zipkin | 9411 |
| SignalFx Metrics Protobuf | 9943 |
| SAPM | 7276 |
