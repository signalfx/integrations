import pytest
import requests

from aws import Metric, ListExtractor, TableExtractor
from tests.helpers import filter_metrics


@pytest.yield_fixture("session")
def sess():
    with requests.Session() as s:
        yield s


def test_list_format(sess):
    assert list(
        ListExtractor().extract(
            sess.get(
                "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html"
            ).content
        )
    ) == [
        Metric(
            "InboundQueryVolume",
            None,
            None,
            "For inbound endpoints, the number of DNS queries forwarded from your network to your VPCs through the endpoint specified by EndpointId.",
        ),
        Metric(
            "OutboundQueryVolume",
            None,
            None,
            "For outbound endpoints, the number of DNS queries forwarded from your VPCs to your network through the endpoint specified by EndpointId.",
        ),
    ]


def test_table_format_2col(sess):
    metrics = TableExtractor().extract(
        sess.get(
            "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.html"
        ).content
    )
    subset = filter_metrics(metrics, {"Requests", "4xxErrorRate"})
    assert subset == [
        Metric(
            "Requests",
            None,
            None,
            "The number of requests for all HTTP methods and for both HTTP and HTTPS requests.",
        ),
        Metric(
            "4xxErrorRate",
            None,
            None,
            "The percentage of all requests for which the HTTP status code is 4xx.",
        ),
    ]


def test_table_format_3col(sess):
    metrics = TableExtractor().extract(
        sess.get(
            "https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.Redis.html"
        ).content
    )
    subset = filter_metrics(metrics, {"CurrConnections", "ListBasedCmds"})
    assert subset == [
        Metric(
            "CurrConnections",
            None,
            None,
            "The number of client connections, excluding connections from read replicas.",
        ),
        Metric("ListBasedCmds", None, None, "The total number of commands that are list-based."),
    ]


def test_multiple_tables(sess):
    metrics = TableExtractor().extract(
        sess.get(
            "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html"
        ).content
    )
    subset = filter_metrics(
        metrics, {"CPUSurplusCreditBalance", "EBSWriteBytes", "StatusCheckFailed"}
    )
    assert subset == [
        # Picked a few metrics from different tables.
        Metric(
            "CPUSurplusCreditBalance",
            None,
            None,
            "The number of surplus credits that have been spent by an unlimited instance when its CPUCreditBalance "
            "value is zero.",
        ),
        Metric(
            "StatusCheckFailed",
            None,
            None,
            "Reports whether the instance has passed both the instance status check and the system status check in "
            "the last minute.",
        ),
        Metric(
            "EBSWriteBytes",
            None,
            None,
            "Bytes written to all EBS volumes attached to the instance in a specified period of time.",
        ),
    ]
