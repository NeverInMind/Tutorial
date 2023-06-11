def read_employees_from_file(path):
    pf = open(path, 'r')
    lines = pf.readlines()
    new_arr = []
    for i in lines:
        new_arr.append(i.split('\n')[0])
    pf.close()


file_path = ".\ex-02.txt"
read_employees_from_file(file_path)
