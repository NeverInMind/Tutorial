def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    rule_arr = {'81': 'JP', '65': 'SG', '886': 'TW', '380': 'UA'}
    phone_obj = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }
    for phone in list_phones:
        new_ph = sanitize_phone_number(phone)
        check_arr = [new_ph[0:2], new_ph[0:3]]
        if check_arr[0] in rule_arr or check_arr[1] in rule_arr:
            for key in rule_arr:
                result = new_ph.find(key, 0, len(key))
                if result == 0:
                    phone_obj_key = rule_arr[key]
                    require_arr = phone_obj[phone_obj_key]
                    require_arr.append(new_ph)

        else:
            require_arr = phone_obj['UA']
            require_arr.append(new_ph)
    return phone_obj


phones = ['+81 321654987', '+65 132456789', '+886 123456789', '+380 123456789',
          '+398 123654789']
get_phone_numbers_for_countries(phones)
