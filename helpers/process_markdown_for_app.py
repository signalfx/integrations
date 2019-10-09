#!/usr/bin/env python3

import re

from helpers.helpers import sanitize_link
from helpers.patterns import check_sfx_link, image_inline_pattern

def link_sub(m):
    prefix = m.group('check_is_image')
    
    # Don't process images
    if prefix == "!":
        return m.group(0)
    
    # Don't process sfx_links
    if m.group('check_is_sfx_link'):
        return m.group(0)

    # Don't process image links
    if re.search(image_inline_pattern, m.group(0)):
        return m.group(0)

    return prefix + "<a target=\"_blank\" href=\"" + m.group('link') + "\">" + m.group('text') + "</a>"

def process_links(contents):
    # Convert all links to open in new tab except sfx_links

    contents = re.sub(check_sfx_link, link_sub, contents)

    return contents

def process_markdown_for_app(markdown):
    markdown = process_links(markdown)
    return markdown
