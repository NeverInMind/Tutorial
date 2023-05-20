import re


def find_all_words(text, word):
    result = re.findall(word, text, flags=re.I)
    return result


text = 'Python also pythOn and this also PyThoN'

find_all_words(text, 'Python')
