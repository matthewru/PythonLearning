import turtle
import random
shape = turtle.Pen()


#Function for the spiral shapes or the odd number sided shapes
def spiral_graphic(number_of_sides):
    for count in range(0, 30):
        shape.color((random.random(), random.random(), random.random()))
        shape.forward(count * 3)
        shape.left((360/number_of_sides))

#Function for the rotated shape or the even number sided shapes
def rotation_shape(number_of_sides):
    for count in range(0, 24):
        for count in range(0, (number_of_sides)):
            shape.color((random.random(), random.random(), random.random()))
            shape.forward(50)
            shape.left((360/number_of_sides))
        shape.left(15)
        
#The logic to choose whether it's a spiral or a shape rotation     
for count in range(0,4):
    shape.reset()
    number_of_sides = random.randint(3,8)
    if number_of_sides % 2 == 0:
        rotation_shape(number_of_sides)
    elif number_of_sides % 2 == 1:
        spiral_graphic(number_of_sides)


