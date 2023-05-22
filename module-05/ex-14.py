import re


def find_all_phones(text):
    pattern = r"\+{1}[0-9]{3}\([0-9]{2}\)[0-9]{3}-[0-9]{1}-[0-9]{3}" \
        r"|\+{1}[0-9]{3}\([0-9]{2}\)[0-9]{3}-[0-9]{2}-[0-9]{2}"
    result = re.findall(pattern, text)
    return result
