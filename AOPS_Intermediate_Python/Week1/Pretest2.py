grades = {}

def student_data():

    file = open("studentdata.txt", "r")

    for line in file:
        data = line.split(" ")
        name = data[0]
        score = int(data[1])
        if name in grades.keys():
            grades[name].append(score)
        else:
            grades[name] = []
            grades[name].append(score)

    file.close()

student_data()

exists = True

while exists:
    name = input("Enter name: ")
    if name in grades.keys():
        print("The average for %s is: %.1f" % (name, sum(grades.get(name))/len(grades.get(name))))
    else:
        exists = False



