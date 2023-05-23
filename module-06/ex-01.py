def real_len(text):
    rule = ['\n', '\f', '\r', '\t', '\v']
    for symb in rule:
        text = text.replace(symb, '')
    return len(text)
    
        
    
    