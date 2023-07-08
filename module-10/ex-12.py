class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id.startswith('01'):
        id_list.append(employee_id)
        return id_list
    else:
        raise IDException

        
    
        
test = '01sdasdad'
res = test.startswith('01')
print(res)
