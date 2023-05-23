def is_spam_words(text, spam_words, space_around=False):
    for spam_word in spam_words:
        result = text.lower().find(spam_word)
        if result != -1:
            if space_around:
                if text[result - 1] == ' ':
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


print(is_spam_words('Молох бог ужасен.', ['лох']))
