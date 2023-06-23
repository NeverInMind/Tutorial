def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as pf:
        pf.write(additional_info)
        with open(path, 'r') as ph:
            ph.seek(start_pos)
            res = ph.read(count_chars)
            return res


file_operations('.\output-12.txt', 'New data', 2, 3)
