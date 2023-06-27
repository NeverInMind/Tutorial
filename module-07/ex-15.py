def flatten(data):
    new_arr = []
    if data == []:
        return new_arr
    if type(data[0]) == list:
        first_list = flatten(data[0])
        second_list = flatten(data[1:])
        new_arr = first_list + second_list
        return new_arr
    else:
        first_list = data[:1]
        second_list = flatten(data[1:])
        new_arr = first_list + second_list
        return new_arr
