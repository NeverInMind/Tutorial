def prepare_data(data):
    data.remove(min(data))
    data.remove(max(data))
    data.sort()
    return data