from gcp import GCPFetcher
from model import Metric
from tests.helpers import filter_metrics


def test_gcp():
    f = GCPFetcher()
    metrics = f.get("google-cloud-spanner")
    assert [
        Metric(
            "instance/cpu/utilization",
            "gauge",
            "CPU utilization",
            "Utilization of provisioned CPU, between 0 and 1.",
        )
    ] == filter_metrics(metrics, {"instance/cpu/utilization"})
