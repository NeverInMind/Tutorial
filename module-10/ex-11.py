from collections import UserString


class NumberString(UserString):
    def number_count(self):
        len = 0
        for item in self:
            if item.isnumeric():
                len +=1
        return len
        
        
            
                
                
            
                
        