dataList = []

#Function to display the count, minimum, maximum, range, and the average of the data set
def display_statistics():
    print("Your data list is %d numbers long" % len(dataList))
    print("The minimum is %d and the maximum is %d" % (min(dataList), max(dataList)))
    print("The range of the data list is %d" % (max(dataList) - min(dataList)))
    print("The average of the data list is %.2f" % round(sum(dataList)/len(dataList), 2))

#The main program checks if the input is an integer and prompts the user if they want to continue
add_more = "Yes"
while add_more == "Yes":
    strNum = input("What number would you like to add? ")
    if str.isdigit(strNum) == True:
        dataList.append(int(strNum))
        add_more = input("Do you want to add another number? ")
    else:
        print("Please add a valid integer number")
    
display_statistics()
