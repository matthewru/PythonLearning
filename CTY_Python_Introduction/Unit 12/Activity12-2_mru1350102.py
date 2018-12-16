#Prompting for a student name and adding the name to the file
def add_students(students_file):
    name = input("Please enter a student name ")
    students_file.write("%s\n" % name)
    print("%s has been added to the file" % name)

#Opening the file, calling add_students and using a while loop to prompt if they want to add another student
students_file = open("Students.txt", "a+")
add_more = "Yes"
while add_more.lower() == "yes":
    add_students(students_file)
    add_more = input("Would you like to add another student? ")
students_file.close()

#Opening the file to be read and then displaying the contents of the file using the read function
print("Student Name\n------------------")
students_file = open("Students.txt", "r")
print(students_file.read())

students_file.close()

