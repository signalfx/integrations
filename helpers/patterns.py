import re

metric_row_pattern = re.compile("- (\**)`([^`]*)`\** \(\*([a-zA-Z]*)\*\)\<br\>[\s]*(.*)[$\n]*")

image_pattern = re.compile("\!\[[^\[\]]*\]\(([^\(\)]*)\)")
image_inline_pattern = re.compile("\[<img src=['\"]([^'\"]+)['\"].*\]\((.*)\)")

sfx_link_pattern = re.compile("\[\]\(sfx_link:.+?\)")
sfx_link_inline_pattern = re.compile('<a\s*href="sfx_link:[\w_\-]+"\s*/>')
integrations_link_pattern = re.compile("\[([^\]]+)\]\(https://github\.com/signalfx/integrations.+?\)")
doc_link_pattern = re.compile("\((\.\/docs/([^\/]*).md)\)")
doc_folder_link_pattern = re.compile(".*\[.*\]\(\.\/docs\).*\n?")
