#Total Cost function that calculates the total cost based on the number of nights and what room you stay in
def calculate_cost(number_of_nights, room_type):
    if room_type == 'Single':
        return round((number_of_nights * 50.00), 2)
    elif room_type == 'Double':
        return round((number_of_nights * 75.00), 2)
    elif room_type == 'Deluxe':
        return round((number_of_nights * 200.00), 2)
    elif room_type == 'Penthouse':
        return round((number_of_nights * 300.00), 2)
    
#Prompts user for how long they stay and how many people are staying
number_of_nights = int(input("How many nights are you staying? "))

number_of_guests = int(input("How many people are staying? "))

#This code finds out which room the guests will stay in
if number_of_guests == 1:
    room_type = 'Single'
elif number_of_guests == 2:
    room_type = 'Double'
elif number_of_guests > 2:
    room_type = input("Would you like a Deluxe Suite or a Penthouse Suite? ")
        if room_type != 'Penthouse' or 'Deluxe':
            print("Please specify a valid room")

#Finally, this prints out the total cost of the stay
print(calculate_cost(number_of_nights, room_type))
