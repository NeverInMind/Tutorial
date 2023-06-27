from datetime import date


def get_days_in_month(month, year):
    start = date(year, month, 1).isoweekday()
    print(start)

    


        
    
get_days_in_month(2, 2023)