def encode(data):
    if not data:
        return []
    count = 1
    cur = data[0]
    while count < len(data) and data[count] == cur:
        count += 1
    return [cur, count] + encode(data[count:])
