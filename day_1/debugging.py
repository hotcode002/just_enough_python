floors = 10
current_floor = 0 # This is just a starting point
user_floor = 0 # This is just a starting point

user_floor = 6

difference = user_floor - current_floor

if difference < 0 : 
    current_floor = user_floor
    print ( " Move down ")
    
if difference > 0 : 
    current_floor = user_floor
    print ( " Move up ")    

user_floor = 3

difference = user_floor - current_floor

if difference < 0 : 
    current_floor = user_floor
    print ( " Move down ")
    
elif difference > 0 : 
    current_floor = user_floor
    print ( " Move up ")    