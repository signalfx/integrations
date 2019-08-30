from typing import List

from model import Metric


def filter_metrics(metrics: List[Metric], only_metrics):
    return [m for m in metrics if m.title in only_metrics]
