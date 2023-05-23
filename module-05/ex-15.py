import re


def find_all_links(text):
    result = []
    pattern = r"https?://(?![a-zA-Z0-9_]*\.\.)[a-zA-Z0-9_.]+"
    iterator = re.finditer(pattern, text)
    for match in iterator:
        result.append(match.group())
    return result