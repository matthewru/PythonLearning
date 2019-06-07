from tkinter import *


class CheckerSquare(Canvas):

    def __init__(self, master, r, c, game):
        Canvas.__init__(self,master,width=80,height=80,bg="Blanched Almond")
        self.grid(row=r,column=c)
        self.position = (r,c)
        self.isOccupied = False
        self.game = game
        self.bind('<Button-1>', self.square_selected)

    def __str__(self):
        return ("position %s isOccupied %s" % (str(self.position), str(self.isOccupied)))

    def add_checker(self,color, isKing):
        ovalList = self.find_all()
        for oval in ovalList:
            self.delete(oval)
        self.create_oval(10,10,74,74,fill=color)
        if isKing:
            self.create_text(45, 50, text='*', font=("Arial", 60))

    def remove_checker(self):
        ovalList = self.find_all()
        for oval in ovalList:
            self.delete(oval)
        self.isOccupied = False

    def square_selected(self, event):
        self.game.checker_play(self)

    def getTopRight(self):
        if (self.position[0] - 1, self.position[1] + 1) in self.game.squares:
            #print("top right %s" % self.game.squares[(self.position[0] - 1, self.position[1] + 1)])
            return self.game.squares[(self.position[0] - 1, self.position[1] + 1)]
        else:
            return None

    def getBottomRight(self):
        if (self.position[0] + 1, self.position[1] + 1) in self.game.squares:
            #print("bottom right %s" % self.game.squares[(self.position[0] + 1, self.position[1] + 1)])
            return self.game.squares[(self.position[0] + 1, self.position[1] + 1)]
        else:
            return None

    def getBottomLeft(self):
        if (self.position[0] + 1, self.position[1] - 1) in self.game.squares:
            #print("bottom Left %s" % self.game.squares[(self.position[0] + 1, self.position[1] - 1)])
            return self.game.squares[(self.position[0] + 1, self.position[1] - 1)]
        else:
            return None

    def getTopLeft(self):
        if (self.position[0] - 1, self.position[1] - 1) in self.game.squares:
            #print("top left %s" % self.game.squares[(self.position[0] - 1, self.position[1] - 1)])
            return self.game.squares[(self.position[0] - 1, self.position[1] - 1)]
        else:
            return None

    def getTopRightJump(self):
        if (self.position[0] - 2, self.position[1] + 2) in self.game.squares:
            #print("top right jump %s" % self.game.squares[(self.position[0] - 2, self.position[1] + 2)])
            return self.game.squares[(self.position[0] - 2, self.position[1] + 2)]
        else:
            return None

    def getBottomRightJump(self):
        if (self.position[0] + 2, self.position[1] + 2) in self.game.squares:
            #print("bottom right jump %s" % self.game.squares[(self.position[0] + 2, self.position[1] + 2)])
            return self.game.squares[(self.position[0] + 2, self.position[1] + 2)]
        else:
            return None

    def getBottomLeftJump(self):
        if (self.position[0] + 2, self.position[1] - 2) in self.game.squares:
            #print("bottom left jump %s" % self.game.squares[(self.position[0] + 2, self.position[1] - 2)])
            return self.game.squares[(self.position[0] + 2, self.position[1] - 2)]
        else:
            return None

    def getTopLeftJump(self):
        if (self.position[0] - 2, self.position[1] - 2) in self.game.squares:
            #print("top left jump %s" % self.game.squares[(self.position[0] - 2, self.position[1] - 2)])
            return self.game.squares[(self.position[0] - 2, self.position[1] - 2)]
        else:
            return None

    def get_middle_square(self, square):
        middlesquareRow = (self.position[0] + square.position[0])/2
        middlesquareColumn = (self.position[1] + square.position[1])/2
        #print("Middle square at %s" % self.game.squares[(middlesquareRow, middlesquareColumn)])
        return self.game.squares[(middlesquareRow, middlesquareColumn)]

    def __eq__(self, square):
        return square is not None and square.position == self.position

class CheckerPiece:

    def __init__(self, square, game, player):
        self.square = square
        self.isKing = False
        self.game = game
        self.player = player

    def move(self, square):
        self.square.remove_checker()
        self.square = square
        self.square.position = square.position
        if self.game.currentPlayer == self.game.redPlayer:
            if self.square.position[0] == 7:
                self.isKing = True
        if self.game.currentPlayer == self.game.whitePlayer:
            if self.square.position[0] == 0:
                self.isKing = True
        self.square.add_checker(self.player.color, self.isKing)

    def capture(self, square):
        square.remove_checker()
        del self.game.squares[square.position]

class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = []

    def get_checker_piece(self, square):
        for piece in self.pieces:
            if piece.square == square:
                return piece
        return None

    def has_checker(self, square):
        return self.get_checker_piece(square) is not None

class CheckerBoard:

    def __init__(self):
        self.board = {}

        for row in range(8):
            for column in range(8):
                coords = (row,column)
                if coords in [(0, 1), (0, 3), (0, 5), (0, 7), (1, 0), (1, 2), (1, 4), (1, 6), (2, 1), (2, 3), (2, 5), (2, 7)]:
                    self.board[coords] = 0
                elif coords in [(5, 0), (5, 2), (5, 4), (5, 6), (6, 1), (6, 3), (6, 5), (6, 7), (7, 0), (7, 2), (7, 4), (7, 6)]:
                    self.board[coords] = 1
                else:
                    self.board[coords] = None
        self.currentPlayer = 0

    def get_piece(self, coords):
        return self.board[coords]

    def get_player(self):
        return self.currentPlayer

class CheckersGame(Frame):

    def __init__(self, master):
        Frame.__init__(self,master, bg='white')
        self.grid()
        self.colors = ('red', 'white')
        self.board = CheckerBoard()
        self.squares = {}
        for row in range(8):
            for column in range(8):
                self.squares[(row,column)] = CheckerSquare(self, row, column, self)
                self.squares[(row, column)]['highlightthickness'] = 4
                self.squares[(row, column)]['highlightbackground'] = 'white'
                if (row,column) in [(0, 1), (0, 3), (0, 5), (0, 7),
                                                  (1, 0), (1, 2), (1, 4), (1, 6),
                                                  (2, 1), (2, 3), (2, 5), (2, 7),
                                                  (5, 0), (5, 2), (5, 4), (5, 6),
                                                  (6, 1), (6, 3), (6, 5), (6, 7),
                                                  (7, 0), (7, 2), (7, 4), (7, 6)]:
                    self.squares[(row,column)].isOccupied = True
        for coord in self.squares:
            if coord in [(0, 1), (0, 3), (0, 5), (0, 7),
                         (1, 0), (1, 2), (1, 4), (1, 6),
                         (2, 1), (2, 3), (2, 5), (2, 7),
                         (3, 0), (3, 2), (3, 4), (3, 6),
                         (4, 1), (4, 3), (4, 5), (4, 7),
                         (5, 0), (5, 2), (5, 4), (5, 6),
                         (6, 1), (6, 3), (6, 5), (6, 7),
                         (7, 0), (7, 2), (7, 4), (7, 6)]:
                self.squares[coord]['bg'] = "dark green"
        self.players = []
        self.selected_Checker = None
        self.setup_players()
        self.currentPlayer = self.redPlayer
        self.rowconfigure(8, minsize=3)
        self.turnSquare = CheckerSquare(self,9,2, self)
        self.turnSquare.add_checker(self.colors[self.board.get_player()], False)
        self.turnSquare["bg"] = "gray79"
        self.turnSquare.unbind("<Button 1>")
        self.turnLabel = Label(self, text="Turn:", font=('Arial', 18), bg='white')
        self.turnLabel.grid(row=9, column=1)
        self.update_display()

    def update_display(self):
        for row in range(8):
            for column in range(8):
                rc = (row, column)
                piece = self.board.get_piece(rc)
                if piece is not None:
                    self.squares[rc].add_checker(self.colors[piece], False)

    def setup_players(self):
        self.redPlayer = Player("red")
        self.whitePlayer = Player("white")
        for coord in self.board.board:
            if self.board.board[coord] == 0:
                self.redPlayer.pieces.append(CheckerPiece(self.squares[coord], self, self.redPlayer))
            if self.board.board[coord] == 1:
                self.whitePlayer.pieces.append(CheckerPiece(self.squares[coord], self, self.whitePlayer))


    def switch_turn(self):
        if self.currentPlayer == self.redPlayer:
            self.currentPlayer = self.whitePlayer
            self.turnSquare.remove_checker()
            self.turnSquare.add_checker(self.whitePlayer.color, False)
        else:
            self.currentPlayer = self.redPlayer
            self.turnSquare.remove_checker()
            self.turnSquare.add_checker(self.redPlayer.color, False)

    def is_a_step(self, square):
        #print("square is %s" % square)
        if self.selected_Checker.isKing:
            if square == self.selected_Checker.square.getBottomRight() \
                    and self.selected_Checker.square.getBottomRight().isOccupied == False:
                return True
            if square == self.selected_Checker.square.getBottomLeft() \
                    and self.selected_Checker.square.getBottomLeft().isOccupied == False:
                return True
            if square == self.selected_Checker.square.getTopRight() \
                    and self.selected_Checker.square.getTopRight().isOccupied == False:
                return True
            if square == self.selected_Checker.square.getTopLeft() \
                    and self.selected_Checker.square.getTopLeft().isOccupied == False:
                return True
        else:
            if self.currentPlayer == self.redPlayer:
                if square == self.selected_Checker.square.getBottomRight() \
                        and self.selected_Checker.square.getBottomRight().isOccupied == False:
                    return True
                if square == self.selected_Checker.square.getBottomLeft()\
                        and self.selected_Checker.square.getBottomLeft().isOccupied == False:
                    return True
            elif self.currentPlayer == self.whitePlayer:
                if square == self.selected_Checker.square.getTopRight() \
                        and self.selected_Checker.square.getTopRight().isOccupied == False:
                    return True
                if square == self.selected_Checker.square.getTopLeft() \
                        and self.selected_Checker.square.getTopLeft().isOccupied == False:
                    return True

    def is_a_jump(self, square):
        if square is None:
            return False
        #print("square is %s" % square)
        if self.selected_Checker.isKing:
            if self.currentPlayer == self.redPlayer:
                if square == self.selected_Checker.square.getBottomRightJump() \
                        and self.selected_Checker.square.getBottomRightJump().isOccupied == False \
                        and self.whitePlayer.has_checker(self.selected_Checker.square.getBottomRight()):
                    return True
                elif square == self.selected_Checker.square.getBottomLeftJump() \
                        and self.selected_Checker.square.getBottomLeftJump().isOccupied == False \
                        and self.whitePlayer.has_checker(self.selected_Checker.square.getBottomLeft()):
                    return True
                elif square == self.selected_Checker.square.getTopRightJump() \
                        and self.selected_Checker.square.getTopRightJump().isOccupied == False \
                        and self.whitePlayer.has_checker(self.selected_Checker.square.getTopRight()):
                    return True
                elif square == self.selected_Checker.square.getTopLeftJump() \
                        and self.selected_Checker.square.getTopLeftJump().isOccupied == False \
                        and self.whitePlayer.has_checker(self.selected_Checker.square.getTopLeft()):
                    return True
            if self.currentPlayer == self.whitePlayer:
                if square == self.selected_Checker.square.getBottomRightJump() \
                        and self.selected_Checker.square.getBottomRightJump().isOccupied == False \
                        and self.redPlayer.has_checker(self.selected_Checker.square.getBottomRight()):
                    return True
                elif square == self.selected_Checker.square.getBottomLeftJump() \
                        and self.selected_Checker.square.getBottomLeftJump().isOccupied == False \
                        and self.redPlayer.has_checker(self.selected_Checker.square.getBottomLeft()):
                    return True
                elif square == self.selected_Checker.square.getTopRightJump() \
                        and self.selected_Checker.square.getTopRightJump().isOccupied == False \
                        and self.redPlayer.has_checker(self.selected_Checker.square.getTopRight()):
                    return True
                elif square == self.selected_Checker.square.getTopLeftJump() \
                        and self.selected_Checker.square.getTopLeftJump.isOccupied == False \
                        and self.redPlayer.has_checker(self.selected_Checker.square.getTopLeft()):
                    return True
        else:
            if self.currentPlayer == self.redPlayer:
                if square == self.selected_Checker.square.getBottomRightJump() \
                        and self.selected_Checker.square.getBottomRightJump().isOccupied == False \
                        and self.whitePlayer.has_checker(self.selected_Checker.square.getBottomRight()):
                    return True
                elif square == self.selected_Checker.square.getBottomLeftJump() \
                        and self.selected_Checker.square.getBottomLeftJump().isOccupied == False \
                        and self.whitePlayer.has_checker(self.selected_Checker.square.getBottomLeft()):
                    return True
            elif self.currentPlayer == self.whitePlayer:
                if square == self.selected_Checker.square.getTopRightJump() \
                        and self.selected_Checker.square.getTopRightJump().isOccupied == False \
                        and self.redPlayer.has_checker(self.selected_Checker.square.getTopRight()):
                    return True
                elif square == self.selected_Checker.square.getTopLeftJump() \
                        and self.selected_Checker.square.getTopLeftJump().isOccupied == False \
                        and self.redPlayer.has_checker(self.selected_Checker.square.getTopLeft()):
                    return True

    def can_jump(self):
        potentialJumps = []
        timescanJump = 0
        if self.selected_Checker.isKing:
            potentialJumps.append(self.selected_Checker.square.getBottomRightJump())
            potentialJumps.append(self.selected_Checker.square.getBottomLeftJump())
            potentialJumps.append(self.selected_Checker.square.getTopRightJump())
            potentialJumps.append(self.selected_Checker.square.getTopLeftJump())
        else:
            if self.currentPlayer == self.redPlayer:
                potentialJumps.append(self.selected_Checker.square.getBottomRightJump())
                potentialJumps.append(self.selected_Checker.square.getBottomLeftJump())
            elif self.currentPlayer == self.whitePlayer:
                potentialJumps.append(self.selected_Checker.square.getTopRightJump())
                potentialJumps.append(self.selected_Checker.square.getTopLeftJump())
        for square in potentialJumps:
            if self.is_a_jump(square):
                timescanJump += 1
        if timescanJump > 0:
            return True
        elif timescanJump == 0:
            return False

    def checker_play(self, square):
        #if checker is defined True: highlight black
        if self.selected_Checker is None:
            #print("first click")
            square['highlightthickness'] = 4
            square['highlightbackground'] = "black"
            checker = self.currentPlayer.get_checker_piece(square)
            if checker is not None:
                self.selected_Checker = checker
        #end of first click
        #if checker is set
        else:
        #second click start
            #print("second click")

            if self.is_a_step(square):
                #print("is a step")
                for tile in self.squares.values():
                    tile['highlightbackground'] = 'white'
                square['highlightbackground'] = 'black'
                self.selected_Checker.move(square)
                self.switch_turn()
                self.selected_Checker = None
            elif self.is_a_jump(square):
                #print("is a jump")
                square['highlightbackground'] = 'black'
                orig_square = self.selected_Checker.square
                self.selected_Checker.move(square)
                self.selected_Checker.capture(orig_square.get_middle_square(square))
                if self.can_jump():
                    self.showMessage("You must continue to jump!")
                    return
                else:
                    self.clearMessage()
                    self.switch_turn()
                    self.selected_Checker = None
                    return
            else:
                checker = self.currentPlayer.get_checker_piece(square)
                if checker is not None:
                    self.selected_Checker = checker
                    for tile in self.squares.values():
                        tile['highlightbackground'] = 'white'
                    square['highlightbackground'] = 'black'
        #end of second click
        #set checker variable to none

    def showMessage(self, message):
        self.msgLabel = Label(self, text=message, font=("Arial", 15), bg='white')
        self.msgLabel.grid(row=9, column=5, columnspan=3)

    def clearMessage(self):
        self.msgLabel.destroy()

def play_Checkers():
    root = Tk()
    root.title("Checkers")
    CG = CheckersGame(root)
    CG.mainloop()

play_Checkers()

