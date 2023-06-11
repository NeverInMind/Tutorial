def add_employee_to_file(record, path):
    pf = open(path, 'a')
    pf.write(f'{record}\n')
    pf.close()
