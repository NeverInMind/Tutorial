def is_spam_words(text, spam_words, space_around=False):
    for spam_word in spam_words:
        result = text.lower().find(spam_word)
        if result != -1:

            return result
        else:
            return False


print(is_spam_words("Ты лох.", ["лох"]))
