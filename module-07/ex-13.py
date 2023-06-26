def get_employees_by_profession(path, profession):
    new_arr = []
    with open(path, 'r')as pf:
        res = pf.readlines()
        for item in res:
            new = item.strip()
            finder = new.find(profession)
            if finder != -1:
                new = new.replace(profession, '').strip()
                new_arr.append(new)
    result = " ".join(new_arr)
    return result


get_employees_by_profession('.\output-13.txt', 'courier')
