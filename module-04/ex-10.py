from random import randint


def get_random_password():
    password = ''
    for i in range(1,9):
        symbol = randint(40, 126)
        password += str(chr(symbol))
    return password
    
    
    
        
        
        
    