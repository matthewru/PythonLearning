from clsInventory import Inventory

#Cart, the subclass of Inventory which can add a book, checkout, and display all the cart's contents
class Cart(Inventory):
    def __init__(self):
        super(Cart, self).__init__()

    def add_book(self, bBook):
        itemnumber = bBook.itemnumber
        self.books.update({itemnumber : bBook})
        
    def checkout(self):
        if bool(self.books) == False:
            print("\nYour cart is empty.\n")
        else:
            totalPrice = 0
            for itemnumber, book in self.books.items():
                totalPrice += book.price
            print("\nYour total price is $%.2f" % totalPrice) 
            print("Thank you for your business!\n")
            self.books.clear()

    def display(self):
        if bool(self.books) == False:
            print("\nYour cart is empty.\n")
        else:
            content = ("\n%s\n%s\n" % (("You have %d books in your cart" % len(self.books.keys())).center(40), "=" * 40))
            for itemnumber, book in self.books.items():
                content += "%s\n%s\n" % (book, "=" * 40)
            print(content)
