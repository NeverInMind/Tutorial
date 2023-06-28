from datetime import date


def get_days_in_month(month, year):
    if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
        days =29
        return days
    
    elif(month==2) :
        days =28
        return days
    
    elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
        days =31
        return days
    
    else :
        days =30
        return days
    


        
    
get_days_in_month(2, 2020)