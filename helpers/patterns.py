import re

metric_row_pattern = re.compile("- (\**)`([^`]*)`\** \(\*([a-zA-Z]*)\*\)\<br\>[\s]*(.*)[$\n]*")

image_pattern = re.compile("\!\[[^\[\]]*\]\(([^\(\)]*)\)")
image_inline_pattern = re.compile("\[<img src=['\"]([^'\"]+)['\"].*\]\((.*)\)")

link_md_pattern = re.compile("(?P<check_is_image>[^\!]|^)(\[(?P<text>[^\]]+)\]\((?P<link>[^#][^\)]+)\))")
link_inline_pattern = re.compile("<a target\=\"_blank\" href=\"(?P<link>[^\"]*)\">(?P<text>[^\<]*)\<\/a\>")
sfx_link_pattern = re.compile("\[\]\(sfx_link:.+?\)")
sfx_link_inline_pattern = re.compile('<a\s*href="sfx_link:[\w_\-]+"\s*/>')
integrations_link_pattern = re.compile("\[([^\]]+)\]\(https://github\.com/signalfx/integrations.+?\)")
doc_link_pattern = re.compile("\((\.\/docs/([^\/]*).md)\)")
doc_folder_link_pattern = re.compile(".*\[.*\]\(\.\/docs\).*\n?")

sfx_monitor_github_link_pattern = re.compile("https\:\/\/github\.com\/signalfx\/signalfx\-agent\/tree\/master\/docs\/monitors\/(.*)\.md")
integration_github_link_pattern = re.compile("https://github\.com/signalfx/integrations/tree/(master|release)/(?P<monitor>[^\/]*)$")


# patterns for app version
check_sfx_link = re.compile("(?P<check_is_image>.?)\[(?P<text>.*?)\]\((?P<link>[^\(]*?)\)(?P<check_is_sfx_link>\[\]\(sfx_link:(.*?)\))*")