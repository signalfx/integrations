# There are also AWS docs in markdown format at https://github.com/awsdocs but more complex
# metric descriptions had formatting errors and sometimes linked out to the HTML docs themselves.

# https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html
import argparse
from dataclasses import asdict
from pathlib import Path

from ruamel import yaml
from tabulate import tabulate

from aws import AWSFetcher
from gcp import GCPFetcher
from azure import AzureFetcher

FETCHERS = {"aws": AWSFetcher, "gcp": GCPFetcher, "azure": AzureFetcher}


def sync(name, metrics):
    """Write markdown docs"""
    metrics_file = Path().resolve().parent / name / "metrics.yaml"
    cur = {}

    if metrics_file.exists():
        cur = yaml.round_trip_load(metrics_file.read_text())

    for m in metrics:
        entry = cur.setdefault(m.title, asdict(m))

        # If the fetched value exists override it, otherwise leave the current one alone.
        if m.description:
            entry["description"] = m.description
        if m.brief:
            entry["brief"] = m.brief
        if m.metric_type:
            entry["metric_type"] = m.metric_type

    with metrics_file.open("wt") as f:
        yaml.round_trip_dump(cur, f)


def show(name, metrics):
    """Show metrics in a table format"""
    print(
        tabulate(
            sorted(
                ((m.title, m.metric_type, m.brief, m.description) for m in metrics),
                key=lambda x: x[0],
            ),
            headers=("Metric", "Type", "Brief", "Description"),
        )
    )


def main(platform, only, cmd_show, cmd_sync, cmd_list):
    fetcher = FETCHERS.get(platform)
    if not fetcher:
        raise RuntimeError(f"unknown platform {platform}")

    with fetcher() as f:
        if cmd_list:
            print("\n".join(f.list()))
            return

        for integration in f.list():
            if only is not None and integration not in only:
                continue

            metrics = list(f.get(integration))

            if len(metrics) == 0:
                raise RuntimeError(f"Zero metrics were returned for {integration}")

            if cmd_show:
                show(integration, metrics)

            if cmd_sync:
                sync(integration, metrics)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Cloud metric documentation importer

sync: output contents to metrics.yaml
show: print contents in a table format
list: print configured integrations for this platform""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--platform", "-p", choices=("aws", "gcp", "azure"), required=True, help="cloud platform"
    )
    parser.add_argument("--only", "-o", action="append", help="run only the specified integrations")
    parser.add_argument("action", choices=("sync", "show", "list"), help="see program description")
    args = parser.parse_args()
    main(
        args.platform,
        args.only,
        args.action == "show",
        args.action == "sync",
        args.action == "list",
    )
