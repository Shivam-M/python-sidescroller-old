from tkinter import *
from threading import Thread
from time import sleep
from tools.animator import Animate
# from tools.error import Error
from tools.Player import Player


class Bullet:
    def __init__(self, w, c='red', p=None, g=None):
        self.Velocity = [0.00, 0.00]
        self.Location = [0.00, 0.00]
        self.Colour = c
        self.Window = w
        self.Players = p
        self.GameInstance = g

        self.Shooting = True
        
        self.BulletItem = Label(self.Window, text='-', font=('Arial', 14, 'bold'), fg=self.Colour, bg='#2F3542', width=2, height=1)

        self.setMovement(0)

        self.THREAD_MOVEMENT = Thread(target=self.updateLocation, args=())
        #self.THREAD_AROUND = Thread(target=self.checkSurroundings, args=())

    def checkSurroundings(self):
        while True:
            bulletLocation = self.getLocation()
            playerLocation = self.Players.getLocation()
            if abs(playerLocation[0]-bulletLocation[0]) < 0.001:
                if abs(playerLocation[1]-bulletLocation[1]) > 0.005:
                    print('x', abs(playerLocation[1]-bulletLocation[1]))
                    print('y', abs(playerLocation[0]-bulletLocation[0]))
                    print('t', playerLocation[0])
                    print('t2', bulletLocation[0])
                    print('Shot')
                    self.Shooting = False
                    self.GameInstance.loseLives(self.Players)
                    self.BulletItem.place_forget()
                    self.BulletItem = None
                    break
            sleep(0.01)


    def updateLocation(self):
        while True:
            if self.Shooting:
                currentLocation = self.getLocation()
                self.setLocation(currentLocation[0] + self.getVelocityX(), currentLocation[1])
                self.refresh()
                if self.getLocation()[0] < -0.5 or self.getLocation()[0] > 1.5:
                    break
                sleep(0.01)
            else:
                break

    def setMovement(self, m):
        if m == 0:
            self.setVelocityX(-0.005)
        else:
            self.setVelocityX(+0.005)

    def startShooting(self):
        pass

    def draw(self, x, y):
        self.Location = [x, y]
        self.BulletItem.place(relx=x, rely=y)
        self.THREAD_MOVEMENT.start()
        # self.THREAD_AROUND.start()

    def hide(self):
        self.BulletItem.place_forget()

    def refresh(self):
        self.BulletItem.place(relx=self.getLocation()[0], rely=self.getLocation()[1])

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
    Test = Bullet(root, c='green', p=[])
    button = Button(command=lambda: Test.draw(.45, .8)).pack()
    root.mainloop()
