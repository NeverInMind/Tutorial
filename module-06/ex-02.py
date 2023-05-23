articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    global articles_dict
    new_art_arr = []
    for art in articles_dict:
        find_obj  = art.get('title') + ' ' + art.get('author')
        if letter_case:
            result = find_obj.find(key)
            
        else:
            result = find_obj.lower().find(key.lower())
        if result != -1:
            new_art_arr.append(art)
    return new_art_arr

    
    
        
    
        
        
        
            
        
        
            
        
        
            
        
        
            
        
            
    