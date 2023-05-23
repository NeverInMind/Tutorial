def is_check_name(fullname, first_name):
    prefix = fullname.split(' ')
    if first_name == prefix[0]:
        return True
    else:
        return False
