from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or not(min < quantity < max):
        return []
    arr = []
    while len(arr) != quantity:
        res = randrange(min, max + 1 )
        if res not in arr:
            arr.append(res)
    arr.sort()
    return arr


get_numbers_ticket(1,5,20)
    
        
            
            
                
            
            
    