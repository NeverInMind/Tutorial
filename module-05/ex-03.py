def sanitize_phone_number(phone):
    rule = ['(', ')', '-', ' ', '+']
    for item in rule:
        phone = phone.replace(item, '')
    return phone