def write_employees_to_file(employee_list, path):
    pf = open(path, 'w')
    for i in employee_list:
        for x in i:
            pf.write(f'{x}\n')
    pf.close()


file_path = ".\ex-02.txt"

new_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

write_employees_to_file(new_list, file_path)
