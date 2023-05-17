def first(size, *string):
    return(size + len(string))


def second(size, **string2):
        i = 0
        for second_part in string2.items():
            i += 1
        return(size + i)
