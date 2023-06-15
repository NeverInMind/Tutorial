def data_preparation(list_data):
    total_list = []
    for item in list_data:
        print(item)
        if len(item) > 2:
            max_value = max(item)
            min_value = min(item)
            item.remove(max_value)
            item.remove(min_value)
        for items in item:
            total_list.append(items)
    total_list.sort(key=None, reverse=True)
    return total_list


test_list = [[1, 2, 3], [3, 4], [5, 6]]
data_preparation(test_list)
