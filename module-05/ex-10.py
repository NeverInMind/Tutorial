import re


def find_word(text, word):
    re_check = re.search(word, text)
    if re_check is not None:
        result = True
        result_span = re_check.span()
        result_str = re_check.group()
        sample = {
            'result': result,
            'first_index': result_span[0],
            'last_index': result_span[1],
            'search_string': result_str,
            'string': re_check.string
        }
    else:
        sample = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': result_str,
            'string': re_check.string
        }
    return sample
