def format_ingredients(items):
    str = ''
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        for i in items:
            if items.index(i) == len(items) - 1:
                str += i
            else:
                str += i + ' and '
    else:
        for i in items:
            if items.index(i) == len(items) - 1:
                str += ' and ' + i
            elif items.index(i) == len(items) - 2:
                str += i
            else:
                str+= i + ", "
    return str