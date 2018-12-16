#Setting variables for the count and the height of the tree
count = 1
height = 10

#Loop system to create tree using stars and spaces
for count in range (1, (height + 1)):
    print(" " * (height - count) + "*" * (2 * count - 1))
for count in range (1, 4):
    print(" " * (height - 2) + "*" * 3)

