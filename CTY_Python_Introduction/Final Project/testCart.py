from clsCart import Cart
from clsBook import Book

cart = Cart()

cart.checkout()
b1 = Book("1000", "A Visual Encyclopedia", "Chris Woodford", "Science", 23.99)
b2 = Book("1001", "My First Human Body Book", "Patricia J. Wynne and Donald M. Silver", "Science", 3.99)
b3 = Book(floatPrice = 5.25)
cart.add_book(b1)
cart.add_book(b2)
cart.add_book(b3)

cart.display()
cart.checkout()
cart.display()
