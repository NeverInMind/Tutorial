import re


def capital_text(s):
    chekc = re.search(' ', s)
    print(s[5])


test = 'test test!test.test?test '

capital_text(test)
