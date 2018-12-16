from tkinter import *
from threading import Thread
from time import sleep


class Blocker:
    def __init__(self, w, p, c='red', g=None):
        self.Velocity = [0.00, 0.00]
        self.Location = [0.00, 0.00]
        self.Colour = c
        self.Window = w
        self.GameInstance = g
        self.Player = p

        self.BlockerItem = Label(self.Window, text='❰ ❱', font=('Arial', 6, 'bold'), fg='white', bg='white', width=200, height=100)
        self.BlockerActive = True

        self.THREAD_MOVEMENT = Thread(target=self.updateLocation, args=())

    def updateLocation(self):
        while True:
            while self.BlockerActive:
                try:
                    currentLocation = self.getLocation()
                    playerLocation = self.Player.getLocation()
                    self.setLocation(playerLocation[0] + 0.1, currentLocation[1])
                    self.refresh()
                    sleep(0.01)
                except:
                    break
            else:
                break

    def draw(self, x, y):
        self.Location = [x, y]
        self.BlockerItem.place(relx=x, rely=y)
        self.THREAD_MOVEMENT.start()

    def place_forget(self):
        try:
            self.BlockerActive = False
            self.BlockerItem.place_forget()
            self.BlockerItem = None
        finally:
            pass

    def hide(self):
        self.BlockerItem.place_forget()

    def refresh(self):
        self.BlockerItem.place(relx=self.getLocation()[0], rely=self.getLocation()[1])

    def getLocation(self):
        return self.Location

    def setLocation(self, x, y):
        self.Location = [x, y]


if __name__ == '__main__':
    root = Tk()
    root.config(bg='#141414')
    root.geometry('400x200')
    Test = Blocker(root, c='#FFFFFF', p=None)
    button = Button(command=lambda: Test.draw(.8, .8)).pack()
    root.mainloop()
