#prompts the user (whole numbers)
print("Enter one course")
course_1 = input()
print("Enter it's grade")
grade_1 = input()
print("Enter another course")
course_2 = input()
print("Enter it's grade")
grade_2 = input()
print("Enter a final course")
course_3 = input()
print("Enter it's grade")
grade_3 = input()

#Calculates total and average
total = int(grade_1) + int(grade_2) + int(grade_3)
average = int(total) / 3

#Formatting               
space = " "
extra_space_length = 25
line_1 = "-" * 45
line_2 = "=" * 45
print("%s Report Card %s" % (space * 15, space * 15))
print("%s Course Name %s Course Grade" % (space * 4, space * 10))
print("%s" % line_1)
print("")
print("%s %s %s %s" % (space * 4, course_1 , space * (extra_space_length - len(course_1)), grade_1))
print("%s %s %s %s" % (space * 4, course_2 , space * (extra_space_length - len(course_2)), grade_2))
print("%s %s %s %s" % (space * 4, course_3 , space * (extra_space_length - len(course_3)), grade_3))
print("%s" % line_2)
print("%s Total %s %d" % (space * 4, space * (extra_space_length - len("Total")), total))
print("%s Average %s %.1f" % (space * 4, space * (extra_space_length - len("Average")), average))

    
