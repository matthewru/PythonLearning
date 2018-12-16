#functions
def total_motel_price(total_travel_distance, travel_distance_per_day, motel_cost_per_night):
    return int(total_travel_distance / travel_distance_per_day) * motel_cost_per_night
    
def total_gas_price(total_travel_distance, car_miles_per_gallon, gas_price_per_gallon):
    return (total_travel_distance / car_miles_per_gallon) * gas_price_per_gallon

def print_total_cost(motel_cost, gas_cost):
    print("The total cost of the trip is $%.2f" % (motel_cost + gas_cost))

#input

total_travel_distance = int(input("What's the total travel distance (in miles)? "))
total_driving_hours_per_day = float(input("How long will you drive per day (in hours)? "))
miles_per_hour = int(input("How fast will you go during the trip (in miles per hour)? "))
travel_distance_per_day = int(total_driving_hours_per_day) * int(miles_per_hour)
car_miles_per_gallon = int(input("How far can you travel with one gallon of gas in your car (in miles)? "))
gas_price_per_gallon = float(input("How much does gas cost per gallon? "))
motel_cost_per_night = float(input("How much does the motel cost per night? "))


#calling function

print(total_travel_distance)
print(car_miles_per_gallon)
print(gas_price_per_gallon)
print( total_gas_price(total_travel_distance, car_miles_per_gallon, gas_price_per_gallon))
#print(travel_distance_per_day)
#print( int(total_travel_distance / travel_distance_per_day))

print( total_motel_price(total_travel_distance, travel_distance_per_day, motel_cost_per_night))

motel_cost = total_motel_price(total_travel_distance, travel_distance_per_day, motel_cost_per_night)
gas_cost = total_gas_price(total_travel_distance, car_miles_per_gallon, gas_price_per_gallon)
print_total_cost(motel_cost, gas_cost)

