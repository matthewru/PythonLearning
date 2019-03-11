import random

number = random.randint(0, 100)

wrong = True
guesses = 0

while wrong:
    guess = int(input("Enter your guess: "))
    guesses += 1
    if guess > number:
        print("Sorry, %d is too high" % guess)
    elif guess < number:
        print("Sorry, %d is too low" % guess)
    elif guess == number:
        print("Good job! %d is my number." % guess)
        print("It took you %d guesses." % guesses)
        wrong = False