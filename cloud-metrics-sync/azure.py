from collections import defaultdict
from typing import List

import mistletoe
import requests
from mistletoe.block_token import Heading, Table

from model import Fetcher, Metric

URL = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/azure-monitor/platform/metrics-supported.md"

DOCS = {
    "azure-app-service": "Microsoft.Web/sites (excluding functions)",
    "azure-batch": "Microsoft.Batch/batchAccounts",
    "azure-event-hubs": "Microsoft.EventHub/namespaces",
    "azure-functions": "Microsoft.Web/sites (functions)",
    "azure-kubernetes-service": "Microsoft.ContainerService/managedClusters",
    "azure-logic-app": "Microsoft.Logic/workflows",
    "azure-redis": "Microsoft.Cache/redis",
    "azure-sql-databases": "Microsoft.Sql/servers/databases",
    "azure-sql-elasticpools": "Microsoft.Sql/servers/elasticPools",
    "azure-storage": "Microsoft.Storage/storageAccounts",
    "azure-vm": "Microsoft.Compute/virtualMachines",
    "azure-vmscaleset": "Microsoft.Compute/virtualMachineScaleSets",
}

RENDER = mistletoe.BaseRenderer()


def _get_text(c):
    return RENDER.render_inner(c)


class AzureFetcher(Fetcher):
    def __init__(self, docs=DOCS, url=URL):
        self._docs = docs
        self._url = url
        self._parsed = self._parse(url)

    @classmethod
    def _parse_table(cls, table):
        for row in table.children:
            if len(row.children) != 6:
                continue
            metric, display_name, _, _, description, _ = row.children
            yield Metric(_get_text(metric), None, _get_text(display_name), _get_text(description))

    @classmethod
    def _parse(cls, url):
        doc = mistletoe.Document(requests.get(url).text)
        metrics = {}
        for i, c in enumerate(doc.children):
            if isinstance(c, Heading):
                namespace = c.children[0].content

                assert (
                    i < len(doc.children) - 1
                ), f"Expected there to be a following section for {namespace} but there wasn't"

                # For metrics we expect a table to follow a heading.
                table = doc.children[i + 1]
                if isinstance(table, Table):
                    # Probably a metric table.
                    metrics[namespace] = list(cls._parse_table(table))

        return metrics

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def list(self) -> List[str]:
        return list(self._docs.keys())

    def get(self, id) -> List[Metric]:
        return self._parsed[self._docs[id]]
