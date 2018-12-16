#This part of the program creates a for loop that counts numbers up to 10 but midway through it asks the user if it wants to continue.
for count in range (1, 11):
    print(str(count))
    if count == 6:
        ask = input("Would you like to continue? ")
        if ask == 'No':
            break;

#This part of the program has the same functionality as the previous one, except this one uses a for loop and the variable "number"
number = 1

while number <= 10:
    print(number)
    if number == 6:
        ask = input("Would you like to continue? ")
        if ask == 'No':
            break;
    number += 1
    
