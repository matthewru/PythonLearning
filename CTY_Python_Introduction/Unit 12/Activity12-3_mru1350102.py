#Prompting for a student name and adding the name to the file
def add_students(students_file):
    name = input("Please enter a student name ")
    student_id = input("Please enter the student's id number ")
    course = input("Please enter what course they are enrolled in ")
    students_file.write("%s, %s, %s\n" % (name, student_id, course))
    print("%s has been added to the file" % name)

def format_text(text):
    return text.center(30, " ")

#Opening the file to be read and then displaying the contents of the file using the read function
def display_students():
    print("%s%s%s" % (format_text("Student Name"), format_text("ID Number"), format_text("Course Name")))
    print("%s" % "-".center(100, "-"))
    students_file = open("Students.txt", "r")
    for line in students_file:
        word = line.split(", ")
        print("%s%s%s" % (format_text(word[0]), format_text(word[1]), format_text(word[2])))
    students_file.close()
        
#Opening the file, calling add_students and using a while loop to prompt if they want to add another student
display_students()

students_file = open("Students.txt", "a+")
add_more = input("Would you like to add a student? ")
while add_more.lower() == "yes":
    add_students(students_file)
    add_more = input("Would you like to add another student? ")
students_file.close()
display_students()
