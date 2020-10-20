This directory contains values.yaml files that can be used with helm to install the [OpenTelemetry Collector helm chart](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/master/charts/opentelemetry-collector).

It configures the OpenTelemetry collector in forwarding mode where it sends traces and metrics sent to it to SignalFx.

1. Download [values.yaml](values.yaml) and [env.yaml](env.yaml).
1. Edit `env.yaml` to contain your access token, realm, etc.
1. Install helm chart, e.g.:

```sh
$ helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
$ helm install my-opentelemetry-collector open-telemetry/opentelemetry-collector -f values.yaml -f env.yaml
```

Note: env.yaml must come after values.yaml

A Kubernetes service is created (the name depends on the helm install name, using the above instructions it's named `my-opentelemetry-collector`). Using this service you can send metrics and traces to the collector. The table below details which port accepts which protocol.

| Protocol | Port |
|---|---|
| OTLP | 55680 |
| Jaegar-Thrift | 14268 |
| Jaeger-gRPC | 14250 |
| Zipkin | 9411 |
| SignalFx Metrics Protobuf | 9943 |
| SAPM | 7276 |
