def capital_text(s):
    s = s.strip().capitalize()
    check_rule = ['!', '?', '.']
    change = False
    for i in range(0, len(s)):
        check_let = s[i]
        if check_let != " " and change:
            s = s[:i] + check_let.upper() + s[i+1:]
            change = False
        if check_let in check_rule:
            change = True
            continue
    return s


test = ' alert. boss! oh'
capital_text(test)
