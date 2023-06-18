def make_request(keys, values):
    res = {}
    if len(keys) == len(values):
        res = {keys[i]: values[i] for i in range(len(keys))}
    return res
