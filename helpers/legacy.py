# Legacy code for moving stuff to product-docs.  This code is generally poor
# quality and highly repetitive.  No new integrations should need to use any of
# this code.

import os
import re
import shutil
from pathlib import Path
from typing import Dict

from .constants import DIRS_TO_SKIP, MONITOR_DOC_BASE_URL, RTD_BASE_URL
from .paths import *
from .patterns import (
    doc_folder_link_pattern,
    doc_link_pattern,
    image_inline_pattern,
    image_pattern,
    integration_github_link_pattern,
    integrations_link_pattern,
    link_inline_pattern,
    link_md_pattern,
    sfx_link_inline_pattern,
    sfx_link_pattern,
    sfx_monitor_github_link_pattern,
)
from .toc import toc_non_sam, toc_sam
from .util import collect_metrics_yaml, extract, get_file_contents, get_output_filename, sanitize_link

RTD_URLS: Dict[str, str] = {}


def extract_section(src_path, toc_item):
    input_file = Path(os.path.join(src_path, toc_item.get("content")))
    contents = input_file.read_text(encoding="utf-8")

    extracted = ""
    extracted += extract(
        contents, toc_item.get("fingerprints").get("starter"), toc_item.get("fingerprints").get("stopper")
    )
    return extracted


def collect_metrics(monitor):
    metrics_yaml = os.path.join(INTEGRATIONS_PATH, monitor + "/metrics.yaml")
    return collect_metrics_yaml(metrics_yaml)


def tabulate_metrics(metrics):
    metric_table = ""
    metric_list = ""
    show_type_column = False
    for metric in metrics:
        if metric.get("metric_type"):
            show_type_column = True
            break
    for metric in metrics:
        metric_table += (
            "| ["
            + metric.get("metric_name")
            + "](#"
            + re.sub(r"[\.\s\_\/]", "-", metric.get("metric_name").lower())
            + ") | "
            + metric.get("brief")
        )
        if show_type_column:
            metric_table += " | " + metric.get("metric_type")
        metric_table += " |\n"
        metric_list += "## " + metric.get("metric_name") + "\n"
        if metric.get("metric_type"):
            metric_list += "`" + metric.get("metric_type") + "`\n\n"
        metric_list += metric.get("description") + "\n\n"

    tabulated = "\n| Metric Name | Description | Type |\n| --- | --- | --- |\n"
    if not show_type_column:
        tabulated = "\n| Metric Name | Description |\n| --- | --- |\n"
    tabulated += metric_table
    tabulated += "\n"
    tabulated += metric_list

    return tabulated


def copy_image(src_path, dest_path):
    try:
        shutil.copyfile(src_path, dest_path)
    except OSError:
        print("couldn't copy image: " + src_path + " to " + dest_path)


def process_images(src_path, monitor, contents):
    (OUTPUT_IMAGE_PATH / monitor).mkdir(exist_ok=True)

    contents = image_inline_pattern.sub(repl="![](\\1)", string=contents)

    for p in re.finditer(image_pattern, contents):
        image_filename = p.group(1)
        is_integrations_github = re.match(
            r"https:\/\/github\.com\/signalfx\/integrations\/blob\/master\/(.*\/img\/([^\/]*))$", image_filename
        )
        if is_integrations_github:
            src_image_path = os.path.join(INTEGRATIONS_PATH, is_integrations_github.group(1))
            if not os.path.exists(src_image_path):
                continue
            image_filename = is_integrations_github.group(2)
            dest_image_path = os.path.join(OUTPUT_IMAGE_PATH, monitor + "/" + image_filename)
        else:
            src_image_path = os.path.join(src_path, image_filename)
            image_filename = image_filename.replace("./img/", "")
            dest_image_path = os.path.join(OUTPUT_IMAGE_PATH, monitor + "/" + image_filename)
        copy_image(src_image_path, dest_image_path)

    for p in re.finditer(image_pattern, contents):
        image_filename = p.group(1)
        is_integrations_github = re.match(
            r"https:\/\/github\.com\/signalfx\/integrations\/blob\/master\/(.*\/img\/([^\/]*))$", image_filename
        )
        if is_integrations_github:
            src_image_path = os.path.join(INTEGRATIONS_PATH, is_integrations_github.group(1))
            if not os.path.exists(src_image_path):
                continue
            image_filename = is_integrations_github.group(2)
            dest_image_path = os.path.join(OUTPUT_IMAGE_PATH, monitor + "/" + image_filename)
        else:
            src_image_path = os.path.join(src_path, image_filename)
            image_filename = image_filename.replace("./img/", "")
            dest_image_path = os.path.join(OUTPUT_IMAGE_PATH, monitor + "/" + image_filename)
        image_filename = image_filename.replace("./", "")
        contents = contents.replace(
            p.group(1), "../../_images/images-integrations/integrations-reference/" + monitor + "/" + image_filename
        )

    header = contents.split("\n")[0]
    contents_no_header = contents.replace(header + "\n", "")
    for p in re.finditer(image_pattern, contents_no_header):
        image_link = p.group(1)
        is_integrations_github = re.match(
            r"https:\/\/github\.com\/signalfx\/integrations\/blob\/master\/(.*\/img\/([^\/]*))$", image_link
        )
        if is_integrations_github:
            image_link = is_integrations_github.group(2)
        else:
            image_link = re.sub(pattern=r"_images\/(.*\/)", repl="_images/", string=image_link)

        contents_no_header = contents_no_header.replace(
            p.group(0), '<a href="' + image_link + '" target="_blank">' + p.group(0) + "</a>"
        )
    contents = header + "\n" + contents_no_header
    return contents


def remove_links(contents):
    contents = sfx_link_pattern.sub(repl="", string=contents)
    contents = sfx_link_inline_pattern.sub(repl="", string=contents)
    contents = doc_folder_link_pattern.sub(repl="", string=contents)
    return contents


def link_sub(m):
    link = sanitize_link(m.group("link"))
    is_monitor_github_link = re.search(sfx_monitor_github_link_pattern, link)
    if is_monitor_github_link:
        new_link = MONITOR_DOC_BASE_URL + is_monitor_github_link.group(1) + ".html"
    else:
        docUrl = find_doc_url(link)
        if docUrl:
            new_link = docUrl
        else:
            new_link = link

    prefix = ""
    if "check_is_image" in m.groupdict():
        prefix = m.group("check_is_image")

    if new_link.startswith("http") == True and new_link.startswith("https://docs.signalfx.com/en") != True:
        # should open in new tab
        return prefix + '<a target="_blank" href="' + new_link + '">' + m.group("text") + "</a>"
    else:
        return prefix + "[" + m.group("text") + "](" + new_link + ")"


def find_doc_url(link):
    match = re.match(integration_github_link_pattern, link)
    if match and match.group("monitor") in RTD_URLS.keys():
        return RTD_URLS[match.group("monitor")]
    return None


def process_links(contents):
    contents = remove_links(contents)
    contents = re.sub(link_md_pattern, link_sub, contents)
    contents = re.sub(link_inline_pattern, link_sub, contents)

    for p in re.finditer(integrations_link_pattern, contents):
        old = p.group(0)
        original_link = old.split("(")[1][:-1]
        folder = original_link.split("/")[-1]
        try:
            contents = contents.replace(original_link, RTD_URLS[folder])
        except:
            pass

    for p in re.finditer(doc_link_pattern, contents):
        contents = contents.replace(p.group(1), "#" + p.group(2))

    return contents


def prepare_rtd_url(folder, contents):
    output_filename = (
        re.sub(r"\!\[[^\[\]]*\]\(([^\(\)]*)\)", "", contents.splitlines()[0]).split("|")[-1].replace("#", "")
    )
    output_filename = output_filename.strip().lower()
    output_filename = output_filename.replace(" ", ".").replace("/", ".")
    if output_filename == "":
        output_filename = folder
    url = "%s%s.html" % (RTD_BASE_URL, output_filename)
    return url


def prepare():
    for folder in os.listdir(INTEGRATIONS_PATH):
        full_path = os.path.join(INTEGRATIONS_PATH, folder)
        isdir = os.path.isdir(full_path)
        folder = folder.lower()

        if isdir and folder not in DIRS_TO_SKIP:
            # Prepare mapping
            readme_path = os.path.join(full_path, "README.md")
            if os.path.isfile(readme_path):
                readme_contents = get_file_contents(readme_path)
                RTD_URLS[folder] = prepare_rtd_url(folder, readme_contents)


def render_header(monitor, sections):
    src_path = os.path.join(INTEGRATIONS_PATH, monitor)
    first_line = get_file_contents(os.path.join(src_path, "README.md")).split("\n")[0]

    output_filename = re.sub(r"!\[[^\[\]]*\]\([^\(\)]*\)", "", first_line).split("|")[-1].replace("#", "")
    output_filename = output_filename.strip().lower()
    output_filename = output_filename.replace(" ", ".").replace("/", ".")

    if not output_filename.strip():
        first_line = first_line + " " + monitor.capitalize()

    header = first_line + "\n\n"
    for section in sections:
        header += "- [" + section.capitalize() + "](#" + section.replace(" ", "-") + ")\n"
    header += "\n"

    return header


def do_smart_agent_monitor(src_path: Path):
    monitor = src_path.name

    contents = ""
    sections = []
    for toc_item in toc_sam:
        section = extract_section(src_path, toc_item)
        if section.strip() == "":
            continue
        sections.append(toc_item["name"])
        contents += "## " + toc_item["name"].upper() + "\n"
        if toc_item["name"] == "metrics":
            contents += tabulate_metrics(collect_metrics(monitor))
        contents += section

    contents = render_header(monitor, sections) + contents
    contents = process_images(src_path, monitor, contents)
    contents = process_links(contents)

    output_filename = get_output_filename(monitor, contents.split("\n", 1)[0])
    output_path = os.path.join(OUTPUT_DOC_PATH, output_filename)

    try:
        os.remove(output_path)
    except:
        pass

    fout = open(output_path, "ab")
    fout.write(contents.encode("utf-8"))
    fout.close()


def do_non_smart_agent_monitor_with_readme(src_path: Path):
    monitor = src_path.name

    contents = ""
    sections = []
    for toc_item in toc_non_sam:
        section = extract_section(src_path, toc_item)
        if section.strip() == "":
            continue
        sections.append(toc_item["name"])
        contents += "## " + toc_item["name"].upper() + "\n"
        if toc_item["name"] == "metrics":
            contents += tabulate_metrics(collect_metrics(monitor))
        contents += section

    contents = render_header(monitor, sections) + contents
    contents = process_images(src_path, monitor, contents)
    contents = process_links(contents)

    output_filename = get_output_filename(monitor, contents.split("\n", 1)[0])
    output_path = os.path.join(OUTPUT_DOC_PATH, output_filename)

    try:
        os.remove(output_path)
    except OSError:
        pass

    fout = open(output_path, "ab")
    fout.write(contents.encode("utf-8"))
    fout.close()


def do_non_smart_agent_monitor_without_readme(src_path: Path):
    monitor = src_path.name

    contents = get_file_contents(os.path.join(src_path, "README.md"))
    contents = process_images(src_path, monitor, contents)
    contents = process_links(contents)
    contents = re.split(r"#+.*LICENSE", contents, 1)[0]

    output_filename = get_output_filename(monitor, contents.split("\n", 1)[0])
    output_path = os.path.join(OUTPUT_DOC_PATH, output_filename)

    try:
        os.remove(output_path)
    except OSError:
        pass

    fout = open(output_path, "ab")
    fout.write(contents.encode("utf-8"))
    fout.close()


def process_integration(integration_dir: Path):
    if integration_dir.name in DIRS_TO_SKIP:
        return

    if not (integration_dir / "README.md").exists():
        return

    if (integration_dir / "SMART_AGENT_MONITOR.md").exists():
        do_smart_agent_monitor(integration_dir)
    elif (integration_dir / "docs").exists():
        do_non_smart_agent_monitor_with_readme(integration_dir)
    else:
        do_non_smart_agent_monitor_without_readme(integration_dir)


def process_legacy_product_docs():
    prepare()
