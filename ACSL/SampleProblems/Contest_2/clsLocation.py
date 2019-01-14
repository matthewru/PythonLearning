class Location:

    def __init__(self, row = 0, column = 0):
        self.row = row
        self.column = column

    def __str__(self):
        return "Location(" + str(self.row) + ", " + str(self.column) + ")"

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.row == other.row and self.column == other.column
        return False