from tkinter import *
from threading import Thread
from time import sleep

from classes.game.Player import Player


class Tracer:
    def __init__(self, w, c='red', p=None, g=None):
        self.Velocity = [0.00, 0.00]
        self.Location = [0.00, 0.00]
        self.Colour = c
        self.Window = w
        self.Players = p
        self.GameInstance = g

        self.Shooting = True
        
        self.TracerItem = Label(self.Window, text='-', font=('Arial', 14, 'bold'), fg=self.Colour, bg='#2F3542', width=2, height=1)

        self.setMovement(0)

        self.THREAD_MOVEMENT = Thread(target=self.updateLocation, args=())
        # self.THREAD_AROUND = Thread(target=self.checkSurroundings, args=())

    def checkSurroundings(self):
        while True:
            TracerLocation = self.getLocation()
            playerLocation = self.Players.getLocation()
            if abs(playerLocation[0]-TracerLocation[0]) < 0.001:
                if abs(playerLocation[1]-TracerLocation[1]) > 0.005:
                    print('x', abs(playerLocation[1]-TracerLocation[1]))
                    print('y', abs(playerLocation[0]-TracerLocation[0]))
                    print('t', playerLocation[0])
                    print('t2', TracerLocation[0])
                    print('Shot')
                    self.Shooting = False
                    self.GameInstance.loseLives(self.Players)
                    self.TracerItem.place_forget()
                    self.TracerItem = None
                    break
            sleep(0.01)

    def updateLocation(self):
        PLoc = self.Players.getLocation()
        TLoc = self.getLocation()
        Gradient = (TLoc[1] - PLoc[1]) / (TLoc[0] - PLoc[0])
        Gradient = (PLoc[1] - TLoc[1]) / (PLoc[0] - TLoc[0])
        orig = TLoc[1]
        Gradient *= -1
        print(Gradient)
        while True:
            sleep(0.2)
            orig -= 0.001
            self.setLocation(orig, orig * Gradient)
            self.refresh()
            print((orig, orig * Gradient))

    def setMovement(self, m):
        if m == 0:
            self.setVelocityX(-0.005)
        else:
            self.setVelocityX(+0.005)

    def startShooting(self):
        pass

    def draw(self, x, y):
        self.Location = [x, y]
        self.TracerItem.place(relx=x, rely=y)
        self.THREAD_MOVEMENT.start()
        # self.THREAD_AROUND.start()

    def hide(self):
        self.TracerItem.place_forget()

    def refresh(self):
        self.TracerItem.place(relx=self.getLocation()[0], rely=self.getLocation()[1])

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
    root.geometry('400x200')
    P = Player(root)
    P.draw(0.7, .8)
    Test = Tracer(root, c='green', p=P)
    button = Button(command=lambda: Test.draw(.85, .3)).pack()
    root.mainloop()
