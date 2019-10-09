import pathlib
import re

import yaml


def extract(content, starter, stopper):
    lines = content.splitlines(True)
    started = False
    if starter == None:
        started = True

    extracted = ""
    for line in lines:
        if started == False and line.strip().startswith(starter):
            started = True
            continue
        elif len(line.split()) > 0 and started and stopper and line.strip().startswith(stopper):
            break

        if started:
            extracted += line
    return extracted


def get_file_contents(file_path):
    return pathlib.Path(file_path).read_text(encoding="utf-8")


def get_output_filename(monitor, header):
    output_filename = re.sub(r"\!\[[^\[\]]*\]\(([^\(\)]*)\)", "", header).split("|")[-1].replace("#", "")
    output_filename = output_filename.strip().lower()
    output_filename = output_filename.replace(" ", ".").replace("/", ".")
    if output_filename == "":
        output_filename = monitor
    output_filename = "integrations." + output_filename + ".md"
    return output_filename


def collect_metrics_yaml(file_path):
    contents = get_file_contents(file_path)
    parsed = yaml.safe_load(contents)
    metrics = []
    for key in parsed:
        metric = parsed.get(key)
        metric_name = key
        brief = ""
        description = ""
        if metric.get("brief"):
            brief = metric.get("brief")
        if metric.get("description"):
            description = metric.get("description")
        metric_type = ""
        if metric.get("metric_type"):
            metric_type = metric.get("metric_type")
        metrics.append(
            {"metric_name": metric_name, "brief": brief, "description": description, "metric_type": metric_type}
        )
    return metrics

def sanitize_link(link):
    link = link.replace("/./", "/")
    link = re.sub(r"\/[^\/]*\/\.\.\/", "/", link)
    return link
