import random
count = 1
even_total = 0
odd_total = 0

#Generate 10 random integer numbers within the range of 1 and 25
for count in range(1, 11):
    number = random.randint(1, 25)
    #Print the numbers
    print(number)
    #Check whether a number is even or odd
    if number % 2 == 0:
        #Calculate the sum of the even numbers
        even_total += number
    elif number % 2 == 1:
        #Calculate the sum of the odd numbers
        odd_total += number

#Print the sum of the even and odd integers
print("The sum of the even numbers is: %d" % even_total)
print("The sum of the odd numbers is : %d" % odd_total)
