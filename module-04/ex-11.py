def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_number = False
    for ch in password:
        if 'a' <= ch <= 'z':
            has_lower = True
        if 'A' <= ch <= 'Z':
            has_upper = True
        if '0' <= ch <= '9':
            has_number = True
    if len(password) == 8 and has_upper and has_lower and has_number:
        return True
    else:
        return False