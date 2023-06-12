import re


def is_integer(s):

    if len(s) == 0:
        return False
    else:
        s = s.strip()
        check_symb = re.search('\+|\-', s)
        if check_symb is not None:
            if s[1:].isdigit():
                return True
        else:
            return False


test = 'abc'
print(is_integer(test))
