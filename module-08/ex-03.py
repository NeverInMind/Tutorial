from datetime import datetime


def get_str_date(date):
    res = datetime.strptime(date , "%Y-%m-%d %H:%M:%S.%fZ")
    res = res.strftime('%A %d %B %Y')
    print(res)
    
    
    
get_str_date('2021-05-27 17:08:34.149Z')