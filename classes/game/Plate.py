from tkinter import *


class Plate:
    def __init__(self, w, c='red', g=None):
        self.Velocity = [0.00, 0.00]
        self.Location = [0.00, 0.00]
        self.Colour = c
        self.Window = w
        self.GameInstance = g

        self.PlateItem = Label(self.Window, text='          ', font=('Arial', 6, 'bold'), fg=self.Colour, bg=self.Colour, width=14, height=1)
        self.PlateHidden = False

    def draw(self, x, y):
        self.PlateHidden = False
        self.Location = [x, y]
        self.PlateItem.place(relx=x, rely=y)

    def place_forget(self):
        try:
            self.PlateHidden = True
            self.PlateItem.place_forget()
        finally:
            pass

    def isHidden(self):
        return self.PlateHidden

    def cget(self, s):
        return self.PlateItem.cget(s)

    def hide(self):
        self.PlateItem.place_forget()

    def show(self):
        self.PlateHidden = False
        self.PlateItem.place(relx=self.Location[0], rely=self.Location[1])

    def refresh(self):
        self.PlateItem.place(relx=self.getLocation()[0], rely=self.getLocation()[1])

    def setVelocityX(self, v):
        self.Velocity[0] = v

    def setVelocityY(self, v):
        self.Velocity[1] = v

    def getVelocityX(self):
        return self.Velocity[0]

    def getVelocityY(self):
        return self.Velocity[1]

    def getLocation(self):
        return self.Location

    def setLocation(self, x, y):
        self.Location = [x, y]


if __name__ == '__main__':
    root = Tk()
    root.config(bg='#141414')
    root.geometry('400x200')
    Test = Plate(root, c='#FFFFFF')
    button = Button(command=lambda: Test.draw(.5, .8)).pack()
    root.mainloop()
