import random

print("Think of a number between 0 and 100")
number = int(input("Hit enter when you have it "))

wrong = True
highBoundary = 100
lowBoundary = 0
guesses = 0

while wrong:
    guess = random.randint(lowBoundary, highBoundary)
    guesses += 1

    print("I guess %d" % guess)
    reply =  input("Is this high, low, or correct?")
    if reply == "low":
        lowBoundary = guess
    elif reply == "high":
        highBoundary = guess
    elif reply == "correct":
        print("I knew it!")
        print("It took me %d guesses" % guesses)
        wrong = False