import re
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, Template

from helpers.patterns import check_sfx_link, image_inline_pattern


def link_sub(m):
    prefix = m.group("check_is_image")

    # Don't process images
    if prefix == "!":
        return m.group(0)

    # Don't process sfx_links
    if m.group("check_is_sfx_link"):
        return m.group(0)

    # Don't process image links
    if re.search(image_inline_pattern, m.group(0)):
        return m.group(0)

    return prefix + '<a target="_blank" href="' + m.group("link") + '">' + m.group("text") + "</a>"


def process_links(content):
    # Convert all links to open in new tab except sfx_links
    return re.sub(check_sfx_link, link_sub, content)


def render_template(template, integration_dir, extra_context=None):
    env = Environment(loader=FileSystemLoader(Path(__file__).parent.parent), lstrip_blocks=True)

    context = {}

    if extra_context:
        context.update(extra_context)

    for yaml_file in sorted(integration_dir.glob("*.yaml")):
        context[yaml_file.stem] = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))

    return env.from_string(template).render(**context)


def process_markdown_for_app(markdown, integration_dir, is_legacy):
    if not is_legacy:
        markdown = render_template(markdown, integration_dir, {"target": "tile"})

    return process_links(markdown)
