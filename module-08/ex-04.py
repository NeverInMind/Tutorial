from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > quantity or quantity < max:
        return []
    arr = []
    check = len(arr)
    while check != quantity:
        res = randrange(min, max)
        if res not in arr:
            arr.append(res)
    arr.sort()
    return arr


get_numbers_ticket(1,5,20)
    
        
            
            
                
            
            
    