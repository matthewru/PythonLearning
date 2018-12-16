#This function calculates the total cost based on the number of balloons
def calculate_cost (number_of_balloons):
    if number_of_balloons <= 50:
        return round(number_of_balloons * 1.00, 2)
    elif number_of_balloons > 50 and number_of_balloons <= 100:
        return round(50 * 1.00, 2) + round(((number_of_balloons - 50) * 0.5), 2)
    elif number_of_balloons > 100:
        return round((((number_of_balloons - 100) * 0.25) + round(50 * 1.00, 2) + round((50 * 0.5), 2)), 2)
    
#Prompts the user for the number of balloons purchased
number_of_balloons = int(input("How many balloons are you buying? "))

#Finally, this prints out the total cost of the balloons
print(calculate_cost(number_of_balloons))
