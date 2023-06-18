def sequence_buttons(string):
    vocabul = {'1': '.,?!:',
               '2': 'ABC',
               '3': 'DEF',
               '4': 'GHI',
               '5': 'JKL',
               '6': 'MNO',
               '7': 'PQRS',
               '8': 'TUV',
               '9': 'WXYZ',
               '0': ' '}
    res_string = ''
    for letter in string:
        letter = letter.capitalize()
        for keys, values in vocabul.items():
            res = values.find(letter)
            if res != -1:
                res_string += keys * (res + 1)
    return res_string


test = 'Hello Vovan!;'

sequence_buttons(test)
