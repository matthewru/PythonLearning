from clsInventory import Inventory
from clsCart import Cart

#This function takes books from the inventory based on the user's selection,
#and places them in the shopping cart
def add_to_cart(inventory, cart):
    books = inventory.books
    add_more = "Yes"
    while add_more.lower() == "yes":
        itemnumber = input("Which book would you like to purchase? ")
        if itemnumber in books.keys():
            cart.add_book(books[itemnumber])
        else:
            print("Please select a valid book number")
        add_more = input("Would you like to buy another book (Yes or No)? ")

#This function displays the main menu
def main_menu():
    print("1 - Display Books")
    print("2 - Add to Cart")
    print("3 - Show Cart")
    print("4 - Checkout")
    print("5 - Quit")
    return int(input("Select an option: "))
    
###########################################################################################################

#This main body of the program chooses which function to call based on the user's input
inventory = Inventory("booklist.txt")
inventory.add_book()
cart = Cart()

option = main_menu()
while option != 5:
    if option == 1:
        inventory.display()
    elif option == 2:
        add_to_cart(inventory, cart)
    elif option == 3:
        cart.display()
    elif option == 4:
        cart.checkout()
    option = main_menu()
print("\nThank you for shopping with us!")
