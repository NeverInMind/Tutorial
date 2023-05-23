import re


def replace_spam_words(text, spam_words):
    for spam_word in spam_words:
        text = re.sub(spam_word, '*' * len(spam_word), text, flags=re.I)
    return text


replace_spam_words('Молох бог ужасен.', 'лох')
