import pytest

from awsimport import Fetcher, Metric, ListExtractor, TableExtractor


def filter_metrics(metrics, only_metrics):
    return [m for m in metrics if m.name in only_metrics]


@pytest.yield_fixture("session")
def fetcher():
    with Fetcher() as f:
        yield f


def test_list_format(fetcher):
    assert fetcher.fetch(
        "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html",
        ListExtractor()) == [
               Metric("InboundQueryVolume",
                      "For inbound endpoints, the number of DNS queries forwarded from your network to your VPCs "
                      "through the endpoint specified by EndpointId."),
               Metric("OutboundQueryVolume",
                      "For outbound endpoints, the number of DNS queries forwarded from your VPCs to your network "
                      "through the endpoint specified by EndpointId.")
           ]


def test_table_format_2col(fetcher):
    metrics = fetcher.fetch(
        "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.html",
        TableExtractor())
    subset = filter_metrics(metrics, {"Requests", "4xxErrorRate"})
    assert subset == [
        Metric("Requests", "The number of requests for all HTTP methods and for both HTTP and HTTPS requests."),
        Metric("4xxErrorRate", "The percentage of all requests for which the HTTP status code is 4xx.")
    ]


def test_table_format_3col(fetcher):
    metrics = fetcher.fetch("https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.Redis.html",
                      TableExtractor())
    subset = filter_metrics(metrics, {"CurrConnections", "ListBasedCmds"})
    assert subset == [
        Metric("CurrConnections", "The number of client connections, excluding connections from read replicas."),
        Metric("ListBasedCmds", "The total number of commands that are list-based.")
    ]


def test_multiple_tables(fetcher):
    metrics = fetcher.fetch("https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html",
                      TableExtractor())
    subset = filter_metrics(metrics, {"CPUSurplusCreditBalance", "EBSWriteBytes", "StatusCheckFailed"})
    assert subset == [
        # Picked a few metrics from different tables.
        Metric("CPUSurplusCreditBalance",
               "The number of surplus credits that have been spent by an unlimited instance when its CPUCreditBalance "
               "value is zero."),
        Metric("StatusCheckFailed",
               "Reports whether the instance has passed both the instance status check and the system status check in "
               "the last minute."),
        Metric("EBSWriteBytes",
               "Bytes written to all EBS volumes attached to the instance in a specified period of time."),
    ]
