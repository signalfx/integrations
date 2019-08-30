import azure

from azure import AzureFetcher
from model import Metric
from .helpers import filter_metrics


def test_parse():
    res = AzureFetcher._parse(azure.URL)
    print(res)
    assert "Microsoft.Web/sites (functions)" in res
    assert filter_metrics(res["Microsoft.Network/frontdoors"], {"ResponseSize"}) == [
        Metric(
            "ResponseSize",
            None,
            "Response Size",
            "The number of bytes sent as responses from HTTP/S proxy to clients",
        )
    ]
