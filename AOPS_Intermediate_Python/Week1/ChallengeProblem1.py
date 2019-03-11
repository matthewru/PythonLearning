# Python Class 1889
# Lesson 1 Problem 1 Part (b)
# Author: madmathninja (272729)

numAnswered = int(input("Enter the number of questions answered: "))
numCorrect = int(input("Enter the number of questions correct: "))
numBlank = 25 - numAnswered
numWrong = numAnswered - numCorrect
score = (numCorrect * 6) + (numBlank * 1.5) + (numWrong * 0)
print("The student's score is: " + str(score))