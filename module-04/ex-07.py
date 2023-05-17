points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    distance = 0.0
    counter = 0
    global points
    for i in coordinates:
        if counter ==  len(coordinates) - 1:
            break
        if coordinates[counter] > coordinates[counter + 1]:
            first_el = coordinates[counter + 1]
            second_el = coordinates[counter]
        else:
            second_el = coordinates[counter + 1]
            first_el = coordinates[counter]     
        cord_tup = (first_el, second_el)
        counter += 1
        distance += points[cord_tup]
    return distance

    
    
        
    
    
    
        
        
        
            
        
            
        
    