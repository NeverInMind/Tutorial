def token_parser(s):
    s = s.replace(" ", "")
    leks_list = ['+', '-', '/', '*', '(', ')']
    find_list = []
    number_set = ''
    for item in range(0, len(s)):
        if item == len(s)-1:
            find_list.append(s[item])
        if s[item] in leks_list:
            if number_set != '':
                find_list.append(number_set)
                number_set = ''
            find_list.append(s[item])
        else:
            number_set += s[item]
    return find_list


test = "(2+ 3) *4 - 5 * 3"
print(token_parser(test))
