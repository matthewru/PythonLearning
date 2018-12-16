from clsDiceGame import DiceGame

#This main part of the program executes the roll method using the object dice.
#It also prompts the user if they want to play again by using a while loop.
dice = DiceGame()
answer = "Yes"
while answer == "Yes":
    dice.roll()
    answer = input("Would you like to roll again (Yes or No)? ")
    
