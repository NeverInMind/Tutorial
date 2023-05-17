result = None
operand = None
operator = None
wait_for_number = True
while True:
    if wait_for_number == True:
        try:
            i = 1 
            if operator == '+':
                result += operan
            elif operator == '-':
                result -= operand
            elif operator == '/':
                result /= operand
            elif operator == '*':
                result *= operand
            operator = None
            operand = int(input('Enter first number: '))
            while True:
                operator = input('Enter operator: ')
                if operator == '=':
                    print(f'Result: ' + str(result))
                    wait_for_number = False
                    break
                elif operator not in '+-/*':
                    print('It"s not + - / *. Pls try use numbers')
                else:
                    i += 1
                    result = operand
                    break
        except:
            print('It"s not a number. Pls try use + - / *')
    else:
        break
