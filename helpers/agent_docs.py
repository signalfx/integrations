# Helpers for moving Smart Agent docs to the product-docs agent reference
# section.

import os
import re
from distutils import dir_util
from pathlib import Path

from helpers.legacy import process_links

from .paths import *

# Most of the files from the agent docs are copied directly over to product docs.
# However, there are a few files that need to be renamed or moved to a different
# location before being synced to product docs. This keeps a map between, the
# files names relative to the path in "OUTPUT_AGENT_DOC_PATH" variable
# and the target location
AGENT_DOCS_WITH_DIFFERENT_TARGETS = {
    "observer-config.md": "observers/_observer-config.md",
    "monitor-config.md": "monitors/_monitor-config.md",
}


def move_smart_agent_docs():
    """
    Process and copy Agent docs from
    https://github.com/signalfx/integrations/tree/master/signalfx-agent/agent-docs
    to the product-docs repo. The source of these docs are originally:
    https://github.com/signalfx/signalfx-agent/tree/master/docs
    """
    move_agent_docs()
    grouped_files = group_files()
    all_files = grouped_files["."] + grouped_files["monitors"] + grouped_files["observers"]
    agent_doc_filenames = get_simple_file_names(grouped_files["."])

    for doc in all_files:
        doc_filename = str(doc)
        print("Fixing relative path in %s" % doc_filename)

        content = doc.read_text(encoding="utf-8")

        """
        Since monitor and observer config doc files are placed in different locations
        in product-docs compared to the agent repo, relative links might be broken. This
        method should fix all such links that need to be updated
        """
        if doc in grouped_files["."]:
            content = fix_relative_links_in_root(content)
        elif doc in grouped_files["monitors"]:
            content = fix_relative_links_in_monitor(content, doc_filename, agent_doc_filenames)
        elif doc in grouped_files["observers"]:
            content = fix_relative_links_in_observer(content, doc_filename, agent_doc_filenames)
        content = process_links(content)

        doc.write_text(content, encoding="utf-8")


def move_agent_docs():
    print("Copying %s to %s" % (INTEGRATIONS_AGENT_DOC_PATH, OUTPUT_AGENT_DOC_PATH))
    assert INTEGRATIONS_AGENT_DOC_PATH.exists()
    assert OUTPUT_AGENT_DOC_PATH.exists()

    dir_util.copy_tree(str(INTEGRATIONS_AGENT_DOC_PATH), str(OUTPUT_AGENT_DOC_PATH))

    for curr_path, target_path in AGENT_DOCS_WITH_DIFFERENT_TARGETS.items():
        (OUTPUT_AGENT_DOC_PATH / curr_path).rename(OUTPUT_AGENT_DOC_PATH / target_path)


RELATIVE_LINK_PATTERN = re.compile(r"(\[.*?\])\((\.\.?/.+?)\)")


def fix_relative_links_in_monitor(content, filename, agent_docs):
    monitor_docs_link_pattern = re.compile(r"(\[.*\]\(\.)\/monitors(\/.*\))")
    if "monitors/_monitor-config.md" in filename:
        # Handle relative links to root level docs
        for agent_doc in agent_docs:
            content = content.replace("](./%s" % agent_doc, "](../%s" % agent_doc)

        content = re.sub(monitor_docs_link_pattern, r"\1\2", content)
        content = content.replace("](./observer-config.md", "](../observers/_observer-config.md")
        content = content.replace("](./observer-config.html", "](../observers/_observer-config.html")
    else:  # actual monitor docs
        content = content.replace("](../monitor-config.", "](./_monitor-config.")
        content = content.replace("](../observer-config.", "](../observers/_observer-config.")

    return content


def fix_relative_links_in_observer(content, filename, agent_docs):
    obsesrver_docs_link_pattern = re.compile(r"(\[.*\]\(\.)\/observers(\/.*\))")

    if "observers/_observer-config.md" in filename:
        # Handle relative links to root level docs
        for agent_doc in agent_docs:
            content = content.replace("](./%s" % agent_doc, "](../%s" % agent_doc)

        content = re.sub(obsesrver_docs_link_pattern, r"\1\2", content)
        content = content.replace("../observer-config.md", "./_observer-config.md")
        content = content.replace("../observer-config.html", "./_observer-config.html")
    else:  # actual observer docs
        content = content.replace("](../observer-config.", "](./_observer-config.")
        content = content.replace("](../monitor-config.", "](../monitors/_monitor-config.")

    return content


def fix_relative_links_in_root(content):
    content = content.replace("](./monitor-config.", "](./monitors/_monitor-config.")
    content = content.replace("](./observer-config.", "](./observers/_observer-config.")
    return content


def get_simple_file_names(full_path):
    if not full_path:
        return []

    res = []
    for p in full_path:
        res.append(os.path.basename(p)[:-3])

    return res


def group_files():
    """
    Methods groups file by path
    """
    all_files = {".": [], "monitors": [], "observers": []}

    for item in Path(OUTPUT_AGENT_DOC_PATH).iterdir():
        collect_files_in_groups(item, all_files)

    return all_files


def collect_files_in_groups(path, all_files):
    if path.is_dir():
        for item in path.iterdir():
            collect_files_in_groups(item, all_files)
    else:
        if not str(path).endswith(".md"):
            return
        path_parent = os.path.dirname(path)

        if os.path.relpath(path_parent, OUTPUT_AGENT_DOC_PATH) == os.path.curdir:
            all_files["."].append(path)
        elif os.path.relpath(path_parent, os.path.join(OUTPUT_AGENT_DOC_PATH, "monitors")) == os.path.curdir:
            all_files["monitors"].append(path)
        elif os.path.relpath(path_parent, os.path.join(OUTPUT_AGENT_DOC_PATH, "observers")) == os.path.curdir:
            all_files["observers"].append(path)
        else:
            print("Unknown relative link: %s" % path)
