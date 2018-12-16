#This part sets the count values to the default setting of 1.
outer_count = 1
inner_count = 1

#Setting up the loop to nest the inner loop.
for outer_count in range (1, 3):
    for inner_count in range (1, 4):
        print("Outer loop iteration %d and inner loop iteration %d" % (outer_count, inner_count))

#While loop variation

#This part sets the count values to the default setting of 1.
outer_count = 1
inner_count = 1

#Setting up the while loop to nest the inner while loop.
while outer_count < 3:
    while inner_count < 4:
        print("Outer loop iteration %d and inner loop iteration %d" % (outer_count, inner_count))
        inner_count += 1
    inner_count = 1
    outer_count += 1




