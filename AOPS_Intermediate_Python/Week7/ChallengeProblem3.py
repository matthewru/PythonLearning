from tkinter import *

class clickCounter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.clicks = 0
        self.cButton = Button(self, text="+1 Click",command=self.click)
        self.cButton.grid(row=4, column=1)
        self.clickLabel = Label(self, text="%d clicks so far" % self.clicks)
        self.clickLabel.grid(row=0, column=0)

    def click(self):
        self.clicks += 1
        self.clickLabel['text'] = "%d clicks so far" % self.clicks

root = Tk()
cF = clickCounter(root)
cF.mainloop()
