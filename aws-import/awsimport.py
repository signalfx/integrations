# There are also AWS docs in markdown format at https://github.com/awsdocs but more complex
# metric descriptions had formatting errors and sometimes linked out to the HTML docs themselves.

# https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html
import argparse
import re
from abc import abstractmethod
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Set, List, Mapping

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

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


@dataclass
class Metric:
    name: str
    brief: str


class Extractor:
    @abstractmethod
    def extract(self, html) -> List[Metric]:
        pass


def get_description(desc):
    clean, *rest = _replace_brackets(_remove_parens(_clean_whitespace(desc.text))).split(".")

    if clean.endswith("."):
        return clean
    else:
        return clean + "."


class TableExtractor(Extractor):
    """Pulls metrics from a <table> that has at least the columns "Metric" and "Description" (but maybe more which
    will be ignored. """
    # Sometimes Metric header has trailing whitespace.
    METRIC_HEADER = re.compile(r"Metric\s*")

    def extract(self, html) -> List[Metric]:
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
                    yield Metric(metric.strip(), desc)


class ListExtractor(Extractor):
    """Pulls metrics that are in an HTML description list (<dl>)"""

    def extract(self, html) -> List[Metric]:
        # Assume all dt and dd elements are metric names and descriptions respectively.
        for metric, raw_desc in zip(html.find_all("dt"), html.find_all("dd")):
            desc = get_description(raw_desc)
            yield Metric(metric.text.strip(), desc)


LIST = ListExtractor()
TABLE = TableExtractor()


@dataclass
class DocSet:
    """Specifies a set of URLs to fetch and an extractor that can extract metrics from them"""
    extractor: Extractor
    urls: Set[str]


DOCS: Mapping[str, List[DocSet]] = {
    "alb": [
        DocSet(TABLE, {
            "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html"}),
    ],
    "api-gateway": [
        DocSet(TABLE, {
            "https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html",
        })
    ],
    "autoscaling": [
        DocSet(TABLE, {
            "https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html",
        })
    ],
    "cloudfront": [
        DocSet(TABLE,
               {"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.html"})
    ],
    "dynamodb": [
        DocSet(TABLE, {
            "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html",
        })
    ],
    "ebs": [
        DocSet(TABLE, {
            "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html"
        })
    ],
    "ec2": [
        DocSet(TABLE,
               {"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html"})
    ],
    "ecs": [
        DocSet(TABLE, {"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html"})
    ],
    "elasticache": [
        DocSet(TABLE,
               # Make this a list so that the order is deterministic. There are some duplicate events across
               # ElasticCache Redis and memcache so we just pick one.
               ["https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.Redis.html",
                "https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.HostLevel.html",
                "https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/CacheMetrics.Memcached.html",
                "https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/CacheMetrics.HostLevel.html"
                ]),
    ],
    "elb": [
        DocSet(TABLE, {"https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-cloudwatch-metrics.html"})
    ],
    "kinesis": [
        DocSet(TABLE, {"https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html"})
    ],
    "lambda": [
        DocSet(TABLE, {"https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-metrics.html"})
    ],
    "opsworks": [
        DocSet(TABLE, {"https://docs.aws.amazon.com/opsworks/latest/userguide/monitoring-cloudwatch.html"})
    ],
    "rds": [
        DocSet(TABLE, {"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html"})
    ],
    "redshift": [
        DocSet(TABLE, {"https://docs.aws.amazon.com/redshift/latest/mgmt/metrics-listing.html"})
    ],
    "route53": [
        DocSet(LIST, {"https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-cloudwatch.html",
                      "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html"}),
    ],
    "sns": [
        DocSet(TABLE, {"https://docs.aws.amazon.com/sns/latest/dg/sns-monitoring-using-cloudwatch.html"})
    ],
    "sqs": [
        DocSet(TABLE, {
            "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html"})
    ],
}


class Fetcher:
    def __init__(self):
        self._sess = requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def fetch(self, url: str, extractor: Extractor) -> List[Metric]:
        data = self._sess.get(url).content
        tree = BeautifulSoup(data, "html.parser")
        return list(extractor.extract(tree))

    def close(self):
        self._sess.close()


def sync(name, metrics):
    """Write markdown docs"""
    for metric in metrics:
        mdFile = f"{metric.name}.md"
        docs = Path().resolve().parent / f"aws-{name}" / "docs"
        docs.mkdir(exist_ok=True)

        (docs / mdFile).write_text(dedent(f"""
            ---
            title: {metric.name}
            brief: {metric.brief}
            metric_type:
            ---
            ### {metric.name}

            {metric.brief}
            """).strip() + "\n")


def show(name, metrics):
    """Show metrics in a table format"""
    print(tabulate(sorted(((m.name, m.brief) for m in metrics), key=lambda x: x[0]),
                   headers=("Metric", "Description"), tablefmt="github"))


def main(only=None, cmd_show=False, cmd_sync=False):
    with Fetcher() as f:
        for integration, docsets in DOCS.items():
            if only is not None and integration not in only:
                continue

            metrics = []
            metrics_seen = set()

            for docset in docsets:
                for url in docset.urls:
                    new_metrics = f.fetch(url, docset.extractor)
                    new_metric_set = {m.name for m in new_metrics}

                    if len(metrics_seen & new_metric_set) != 0:
                        print(f"WARNING: Duplicate metrics {new_metric_set & metrics_seen}")

                    metrics_seen.update(new_metric_set)
                    metrics += new_metrics

            if cmd_show:
                show(integration, metrics)

            if cmd_sync:
                sync(integration, metrics)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""AWS metric documentation importer

sync: output contents to meta.yaml files
show: print contents in a table format""", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("action", choices=("sync", "show"), help="see program description")
    parser.add_argument("--only", nargs="+", help="run only the specified integrations")
    args = parser.parse_args()
    main(args.only, args.action == "show", args.action == "sync")
