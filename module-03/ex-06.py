def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        space_amount = (length - len(string)) // 2
        return string.rjust(len(string) + space_amount, ' ')