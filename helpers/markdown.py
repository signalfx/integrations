import re
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, Template

from helpers.helpers import sanitize_link
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


def render_template(template, integration_dir):
    env = Environment(loader=FileSystemLoader(Path(__file__).parent.parent))

    context = {}
    for yaml_file in sorted(integration_dir.glob("*.yaml")):
        context[yaml_file.stem] = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))

    return env.from_string(template).render(**context)


# Remove this and associated code when all integrations are migrated.
def uses_legacy_build(integration_dir):
    meta_path = integration_dir / "meta.yaml"
    if not meta_path.exists():
        return True
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))

    return meta.get("useLegacyBuild", False)


def process_markdown_for_app(markdown, integration_dir):
    if not uses_legacy_build(integration_dir):
        markdown = render_template(markdown, integration_dir)

    return process_links(markdown)
