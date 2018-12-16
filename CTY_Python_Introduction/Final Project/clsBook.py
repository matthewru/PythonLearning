#The class book has the attributes: item number, title, author, genre, and price,
#which are printed using a __str__ method
class Book:
    def __init__(self, strItemnumber = "0", strTitle = "None", strAuthor = "None", strGenre = "None", floatPrice = 0.00):
        self.itemnumber = strItemnumber
        self.title = strTitle
        self.author = strAuthor
        self.genre = strGenre
        self.price = floatPrice

    def __str__(self):
        return "Item number:%s\nTitle:%s\nAuthor:%s\nGenre:%s\nPrice:$%.2f" % (self.itemnumber, self.title, self.author, self.genre, self.price)
