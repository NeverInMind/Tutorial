def is_valid_pin_codes(pin_codes):
    if pin_codes != []:
        checked_pins = []
        for pin in pin_codes:
            check_count = 0
            for symbol in pin:
                try:
                    if isinstance(int(symbol), int):
                        check_count += 1
                        continue
                except ValueError:
                    break
            if check_count == 4:
                checked_pins.append(pin)
            else:
                break
        if len(set(checked_pins)) < len(pin_codes):
            return False
        else:
            return True
    else:
        return False