#Importing and setting up the program with the turtle module
import turtle
pent = turtle.Pen()

#The function for the program
def draw_pentagon(length):
    for count in range(0, 5):
        pent.forward(length)
        pent.left(72)

#Finally calling the function
draw_pentagon(50)
            
