import re
from abc import abstractmethod
from dataclasses import dataclass
from typing import List, Mapping, Iterable

import requests
from bs4 import BeautifulSoup

from model import Metric, Fetcher

RE_WHITESPACE = re.compile(r"\s+")
RE_REMOVE_PARENS = re.compile(r"^\(.*\)")


def _clean_whitespace(s):
    """Replaces consecutive whitespace with a single space anywhere inside the string."""
    return RE_WHITESPACE.sub(" ", s).strip()


def _remove_parens(s):
    """Removes all text inside parenthesis at the beginning of the string"""
    return RE_REMOVE_PARENS.sub("", s).strip()


def _replace_brackets(s):
    """Replace brackets with parenthesis because it breaks the UI"""
    # It probably thinks the brackets are markdown or something.
    return s.replace("[", "(").replace("]", ")").strip()


def get_description(desc):
    clean, *rest = _replace_brackets(_remove_parens(_clean_whitespace(desc.text))).split(".")

    if clean.endswith("."):
        return clean
    else:
        return clean + "."


class Extractor:
    @abstractmethod
    def extract(self, text: str) -> List[Metric]:
        pass


class TableExtractor(Extractor):
    """Pulls metrics from a <table> that has at least the columns "Metric" and "Description" (but maybe more which
    will be ignored. """

    # Sometimes Metric header has trailing whitespace.
    METRIC_HEADER = re.compile(r"Metric\s*")

    def extract(self, text: str) -> List[Metric]:
        html = BeautifulSoup(text, "html.parser")
        # Find all the table headers with a value of Metric.
        for metric_header in html.find_all("th", text=self.METRIC_HEADER):
            # Go up the tree to the table element.
            table = metric_header.parent.parent
            # Iterate through all the table rows, skipping the first one
            # which is the table header.
            for row in table.find_all("tr")[1:]:
                metric, raw_desc, *_, = row.find_all("td")
                desc = get_description(raw_desc)

                # Sometimes there will be more than one metric in the table with the same description.
                for metric in metric.text.split(","):
                    yield Metric(
                        title=metric.strip(), metric_type=None, brief=None, description=desc
                    )


class ListExtractor(Extractor):
    """Pulls metrics that are in an HTML description list (<dl>)"""

    def extract(self, text: str) -> List[Metric]:
        html = BeautifulSoup(text, "html.parser")
        # Assume all dt and dd elements are metric names and descriptions respectively.
        for metric, raw_desc in zip(html.find_all("dt"), html.find_all("dd")):
            desc = get_description(raw_desc)
            yield Metric(title=metric.text.strip(), metric_type=None, brief=None, description=desc)


@dataclass
class DocSet:
    """Specifies a set of URLs to fetch and an extractor that can extract metrics from them"""

    extractor: Extractor
    urls: Iterable[str]


LIST = ListExtractor()
TABLE = TableExtractor()

DOCS: Mapping[str, List[DocSet]] = {
    # AWS
    "aws-alb": [
        DocSet(
            TABLE,
            {
                "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html"
            },
        )
    ],
    "aws-api-gateway": [
        DocSet(
            TABLE,
            {
                "https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html"
            },
        )
    ],
    "aws-autoscaling": [
        DocSet(
            TABLE,
            {"https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html"},
        )
    ],
    "aws-cloudfront": [
        DocSet(
            TABLE,
            {
                "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.html"
            },
        )
    ],
    "aws-dynamodb": [
        DocSet(
            TABLE,
            {
                "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html"
            },
        )
    ],
    "aws-ebs": [
        DocSet(
            TABLE, {"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html"}
        )
    ],
    "aws-ec2": [
        DocSet(
            TABLE,
            {
                "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html"
            },
        )
    ],
    "aws-ecs": [
        DocSet(
            TABLE,
            {"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html"},
        )
    ],
    "aws-elasticache": [
        DocSet(
            TABLE,
            # Make this a list so that the order is deterministic. There are some duplicate events across
            # ElasticCache Redis and memcache so we just pick one.
            [
                "https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.Redis.html",
                "https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.HostLevel.html",
                "https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/CacheMetrics.Memcached.html",
                "https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/CacheMetrics.HostLevel.html",
            ],
        )
    ],
    "aws-elb": [
        DocSet(
            TABLE,
            {
                "https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-cloudwatch-metrics.html"
            },
        )
    ],
    "aws-kinesis": [
        DocSet(
            TABLE,
            {"https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html"},
        )
    ],
    "aws-lambda": [
        DocSet(
            TABLE,
            {"https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-metrics.html"},
        )
    ],
    "aws-opsworks": [
        DocSet(
            TABLE,
            {"https://docs.aws.amazon.com/opsworks/latest/userguide/monitoring-cloudwatch.html"},
        )
    ],
    "aws-rds": [
        DocSet(
            TABLE,
            {"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html"},
        )
    ],
    "aws-redshift": [
        DocSet(TABLE, {"https://docs.aws.amazon.com/redshift/latest/mgmt/metrics-listing.html"})
    ],
    "aws-route53": [
        DocSet(
            LIST,
            {
                "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-cloudwatch.html",
                "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html",
            },
        )
    ],
    "aws-sns": [
        DocSet(
            TABLE,
            {"https://docs.aws.amazon.com/sns/latest/dg/sns-monitoring-using-cloudwatch.html"},
        )
    ],
    "aws-sqs": [
        DocSet(
            TABLE,
            {
                "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html"
            },
        )
    ],
}


class AWSFetcher(Fetcher):
    def __init__(self, docs=DOCS):
        self._sess = requests.Session()
        self._docs = docs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def list(self):
        return self._docs.keys()

    def get(self, id: str) -> List[Metric]:
        docsets = self._docs[id]
        metrics = []
        metrics_seen = set()

        for docset in docsets:
            for url in docset.urls:
                text = self._sess.get(url).content
                new_metrics = list(docset.extractor.extract(text))
                new_metric_set = {m.title for m in new_metrics}

                if len(metrics_seen & new_metric_set) != 0:
                    print(f"WARNING: Duplicate metrics {new_metric_set & metrics_seen}")

                metrics_seen.update(new_metric_set)
                metrics += new_metrics

        return metrics

    def close(self):
        self._sess.close()
