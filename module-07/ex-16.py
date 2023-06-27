def decode(data):
    new_arr = []
    if len(data) > 0:
        list1 = list(data[0]) * data[1]
        list2 = list(decode(data[2:]))
        new_arr = list1 + list2
    return new_arr
