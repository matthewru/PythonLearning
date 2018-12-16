from clsBook import Book

#Inventory is a class that can load books from a text file to a map and then format and display them.
class Inventory:
    def __init__(self, strBooklist_file = "booklist.txt"):
        self.books = {}
        self.booklist_file_name = strBooklist_file
    
    def add_book(self):
        booklist_file = open(self.booklist_file_name, "r")
        for line in booklist_file:
            record = line.split(",")
            itemnumber = record[0]
            title = record[1]
            author = record[2]
            genre = record[3]
            price = record[4]
            book = Book(itemnumber, record[1], record[2], record[3], float(record[4]))
            self.books.update({itemnumber : book})
        booklist_file.close()
        
    def display(self):
        content = ("%s\n%s\n" % ("Book Inventory".center(40), "=" * 40))
        for itemnumber, book in self.books.items():
            content += "%s\n%s\n" % (book, "=" * 40)
        print(content)


    

        
   
