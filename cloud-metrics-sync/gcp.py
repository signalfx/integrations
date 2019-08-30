import os
from typing import List, Mapping

from google.cloud import monitoring_v3
from google.cloud.monitoring_v3 import enums

from model import Metric, Fetcher

DOCS: Mapping[str, str] = {
    "google-appengine": "appengine.googleapis.com",
    "google-bigquery": "bigquery.googleapis.com",
    "google-cloud-bigtable": "bigtable.googleapis.com",
    "google-cloud-datastore": "datastore.googleapis.com",
    "google-cloud-functions": "cloudfunctions.googleapis.com",
    "google-cloud-pubsub": "pubsub.googleapis.com",
    "google-cloud-router": "router.googleapis.com",
    "google-cloud-spanner": "spanner.googleapis.com",
    "google-cloud-storage": "storage.googleapis.com",
    "google-compute-engine": "compute.googleapis.com",
    "google-container-engine": "container.googleapis.com",
}

KIND_MAPPING = {
    enums.MetricDescriptor.MetricKind.CUMULATIVE: "cumulative",
    enums.MetricDescriptor.MetricKind.DELTA: "counter",
    enums.MetricDescriptor.MetricKind.GAUGE: "gauge",
}


class GCPFetcher(Fetcher):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __init__(self, project_id=None, docs=DOCS):
        self._client = monitoring_v3.MetricServiceClient()
        self._docs = docs
        if not project_id:
            project_id = os.environ.get("GCP_PROJECT_ID")
            if not project_id:
                raise ValueError("GCP_PROJECT_ID must be set to a valid GCP project ID")
        self._project = self._client.project_path(project_id)

    def list(self) -> List[str]:
        return list(self._docs.keys())

    def get(self, integration: str) -> List[Metric]:
        namespace = self._docs[integration]
        for metric in self._client.list_metric_descriptors(
            self._project, filter_=f'metric.type = starts_with("{namespace}/")'
        ):
            kind = KIND_MAPPING.get(metric.metric_kind)
            if kind is None:
                continue

            name = metric.type.replace(f"{namespace}/", "")
            yield Metric(
                title=name,
                brief=metric.display_name,
                metric_type=kind,
                description=metric.description,
            )
