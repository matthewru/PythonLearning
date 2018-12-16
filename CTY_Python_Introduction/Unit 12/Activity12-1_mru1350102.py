#Prompting for a student name
def add_students(students_file):
    name = input("Please enter a student name ")
    students_file.write("%s\n" % name)
    print("%s has been added to the file" % name)

#Opening the file and using a while loop to prompt if they want to add another student
students_file = open("Students.txt", "w")
add_more = "Yes"
while add_more.lower() == "yes":
    add_students(students_file)
    add_more = input("Would you like to add another student? ")
students_file.close()
