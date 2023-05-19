def formatted_numbers():
    res_arr = ['|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')]
    for i in range(0, 16):
        res_arr.append('|{:<10d}|{:^10x}|{:>10b}|'.format(i, i, i))
    return res_arr


for el in formatted_numbers():
    print(el)
