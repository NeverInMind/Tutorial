def all_sub_lists(data):
    new_list = [[]]
    data_length = len(data)
    if data_length <= 1:
        return new_list
    for item in range(0, len(data)):
        while data_length != 0:
            data_length -= 1
            check_data = data[item:data_length+1]
            if check_data != []:
                new_list.append(check_data)
        data_length = len(data)
    return sorted(new_list, key=len)


test = [1, 2, 3, 4]
all_sub_lists(test)
