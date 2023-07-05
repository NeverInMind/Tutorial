import random

def get_random_winners(quantity, participants):
    keys = list(participants.keys())
    random.shuffle(keys)
    if quantity > len(keys):
        return []
    winners = random.sample(keys, k=quantity)
    return winners
    
    
    