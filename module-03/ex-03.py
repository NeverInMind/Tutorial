base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global base_rate
    global price_per_km
    global total_trip
    total_price = base_rate + price_per_km * path
    total_trip += 1
    return total_price
    
trip_price(10)  