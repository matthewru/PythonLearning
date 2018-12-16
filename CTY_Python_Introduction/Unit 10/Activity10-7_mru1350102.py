#Define the super class
class Father:
    def __init__(self, strName = "Father", strAdress = "Father's Adress"):
        self.name = strName
        self.adress = strAdress

    def __str__(self):
        return self.name + " " + "lives" + " " + "at" + " " + self.adress

#Define the subclass
class Son(Father):
    def __init__(self, strName = "Son", strAdress = "Son's Adress", strSchoolName = "Son's School"):
        self.name = strName
        self.adress = strAdress
        self.schoolName = strSchoolName

    def goToSchool(self):
        print("Child is going to %s" % self.schoolName)

#Create subclass object and print the object
sChild = Son()
sChild.goToSchool()
print(sChild)
