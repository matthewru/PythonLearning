#This is the default adress map (key: name, value: contact) for all of the contacts
contact_map = {}

#This function adds a contact to the adress book
def add_contact():
    add_more = "Yes"
    while add_more == "Yes":
        name = input("What is the name of your contact? ")
        contact = input("What is %s's contact? " % name)
        contact_map[name] = contact
        add_more = input("Would you like to add another contact (Yes or No)? ")

#This function displays all contacts in the adress book
def display_contact():
    if len(contact_map) == 0:
        print("No contacts found in your adress book.")
    else:
        for name, contact in contact_map.items():
            print("%s's contact is %s." % (name, contact))

#This function searches for a specific contact in the adress book      
def search_contact():
    find_more = "Yes"
    while find_more == "Yes":
        name = input("Who's contact would you like to find? ")
        if name in contact_map.keys():
            print("%s's contact is %s." % (name, contact_map[name]))
        else:
            print("No such contact was found in the address book")
        find_more = input("Would you like to find another contact (Yes or No)? ")

#This function deletes a certain contact from the adress book
def del_contact():
    del_more = "Yes"
    while del_more == "Yes":
        name = input("What is the name of the contact to be deleted? ")
        if name in contact_map.keys():
            confirmation = input("Are you sure you want to delete %s? " % name)
            if confirmation == "Yes":
                del(contact_map[name])
                print("%s has successfully been deleted" % name)
        else:
            print("No such contact was found in the address book")
        del_more = input("Would you like to delete another contact (Yes or No)? ")

#This function displays the main menu
def main_menu():
    print("Select an option...")
    print("1 - Add/Update contact...")
    print("2 - Display all contacts...")
    print("3 - Search...")
    print("4 - Delete contact...")
    print("5 - Quit")
    return int(input())
    
###########################################################################################################

#This main body of the program chooses which function to call based on the user's input
print("Address book to store friends contact")
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")
option = main_menu()
while option != 5:
    if option == 1:
        add_contact()
    elif option == 2:
        display_contact()
    elif option == 3:
        search_contact()
    elif option == 4:
        del_contact()
    option = main_menu()
    
