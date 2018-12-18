import time
from threading import Thread
from tkinter import *
from random import choice

from classes.game.Enemy import Enemy
from classes.game.Plate import Plate
from classes.game.Slider import Slider
# from classes.game.Blocker import Blocker


class Levels:
    def __init__(self, w, g):

        self.Window = w
        self.GameInstance = g
        self.Colours = ['Red', 'Green', 'Blue', 'Orange', 'Yellow']

        self.W_BG = '#2F3542'
        self.W_FG = '#FFFFFF'

        self.W_FONT = ('MS PGothic', 30, 'bold')
        self.W_FONT2 = ('MS PGothic', 12, 'bold')
        self.W_FONT3 = ('MS PGothic', 10, 'bold')
        self.W_FONT4 = ('MS PGothic', 11, 'bold')

        self.S_VERSION = f'Version A - {self.GameInstance.GameVersion}'

        self.C_RED = '#E74C3C'
        self.C_GREEN = '#2ECC71'
        self.C_ORANGE = '#F39C12'
        self.C_BLUE = '#3498DB'
        self.C_YELLOW = '#F1C40F'
        self.C_GRAY = '#95A5A6'
        self.C_LIGHTGRAY = '#BDC3C7'

        self.ColStr = 'Go to the colour {0}'

        self.ColVar = StringVar()
        self.ColVar.set(self.ColStr)
        self.checkColours = False
        self.activeMode = False
        self.numGames = 0
        self.selectedColour = None
        self.mainEnemy = None
        self.BossReady = False

        # Game Level 1:
        self.whiteFloor = Label(self.Window, bg=self.W_FG, height=3, width=200)

        # Game Level 2:
        self.whiteFloor2 = Label(self.Window, bg=self.W_FG, height=3, width=43)
        self.whiteFloor3 = Label(self.Window, bg=self.W_FG, height=3, width=100)

        # Game Level 3:
        self.whiteFloor4 = Label(self.Window, bg=self.W_FG, height=3, width=20)
        self.whiteFloor5 = Label(self.Window, bg=self.W_FG, height=3, width=100)
        self.whiteFloor6 = Label(self.Window, bg=self.W_FG, height=1, width=10)
        self.whiteFloor7 = Label(self.Window, bg=self.W_FG, height=1, width=8)
        self.whiteFloor8 = Label(self.Window, bg=self.W_FG, height=1, width=14)

        # Game Level 4:
        self.whiteFloor9 = Label(self.Window, bg=self.W_FG, height=3, width=10)
        self.whiteFloor10 = Label(self.Window, bg=self.W_FG, height=3, width=100)
        self.whiteFloor11 = Label(self.Window, bg=self.W_FG, height=3, width=5)
        self.whiteSlider = Slider(self.Window, c=self.W_FG, g=self.GameInstance)
        self.whiteSlider2 = Slider(self.Window, c=self.W_FG, g=self.GameInstance)

        # Game Level 5:
        self.colouredPlate = Plate(self.Window, g=self.GameInstance, c=self.C_BLUE)
        self.colouredPlate2 = Plate(self.Window, g=self.GameInstance, c=self.C_GREEN)
        self.colouredPlate3 = Plate(self.Window, g=self.GameInstance, c=self.C_RED)
        self.colouredPlate4 = Plate(self.Window, g=self.GameInstance, c=self.C_YELLOW)
        self.colouredPlate5 = Plate(self.Window, g=self.GameInstance, c=self.C_ORANGE)
        self.whiteFloor12 = Label(self.Window, bg=self.W_FG, height=3, width=200)
        self.ColourLabel = Label(self.Window, textvariable=self.ColVar, font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG)

        # Game Level 6:
        self.blackFloor = Label(self.Window, bg='#141414', height=3, width=200)

        self.levelAssets = [self.whiteFloor, self.whiteFloor2, self.whiteFloor3, self.whiteFloor4, self.whiteFloor5,
                            self.whiteFloor6, self.whiteFloor7, self.whiteFloor8, self.whiteFloor9, self.whiteFloor10,
                            self.whiteFloor11, self.colouredPlate, self.colouredPlate2, self.colouredPlate3,
                            self.colouredPlate4, self.colouredPlate4, self.ColourLabel, self.whiteFloor12, self.GameInstance.BossItem, self.blackFloor]

    def draw(self, levelNumber=1):
        self.GameInstance.clearScreen()
        if levelNumber == 1:
            self.mainEnemy = Enemy(self.Window, self.GameInstance.Player1, c=self.C_RED, g=self)
            self.mainEnemy.draw(.45, 0.755)
            self.whiteFloor.place(relx=.0, rely=.85)
        elif levelNumber == 2:
            self.mainEnemy.hide()
            self.whiteFloor2.place(relx=.0, rely=.85)
            self.whiteFloor3.place(relx=.70, rely=.85)
        elif levelNumber == 3:
            self.whiteFloor4.place(relx=.0, rely=.85)
            self.whiteFloor5.place(relx=.925, rely=.85)
            self.whiteFloor6.place(relx=.2, rely=.7)
            self.whiteFloor7.place(relx=.4, rely=.6)
            self.whiteFloor8.place(relx=.68, rely=.65)
            try:
                self.levelAssets.remove(self.whiteSlider)
                self.levelAssets.remove(self.whiteSlider2)
            except:
                pass
        elif levelNumber == 4:
            self.whiteFloor9.place(relx=.0, rely=.85)
            self.whiteFloor10.place(relx=.925, rely=.85)
            self.whiteFloor11.place(relx=.47, rely=.85)
            # self.blackBlocker = Blocker(self.Window, self.GameInstance.Player1)
            # self.blackBlocker.draw(.125, .0)
            self.whiteSlider.draw(0.875, .85)
            self.whiteSlider2.draw(0.415, .85)
            self.levelAssets.append(self.whiteSlider)
            self.levelAssets.append(self.whiteSlider2)
        elif levelNumber == 5:
            # self.levelAssets.remove(self.whiteSlider)
            # self.levelAssets.remove(self.whiteSlider2)
            self.colouredPlate.draw(.05, .79)
            self.colouredPlate2.draw(.25, .79)
            self.colouredPlate3.draw(.45, .79)
            self.colouredPlate4.draw(.65, .79)
            self.colouredPlate5.draw(.85, .79)
            self.activeMode = True
            self.chooser()
        elif levelNumber == 6:
            self.blackFloor.place(relx=.0, rely=.85)
            if self.GameInstance.GameMode == 0:
                self.GameInstance.BossItem.place(relx=.75, rely=.31)
                self.Window.config(bg=self.C_RED)
                self.GameInstance.myPlayer().config('#141414')
                self.GameInstance.PlayerPosition.config(bg=self.C_RED, fg='#141414')
                self.GameInstance.PlayerPage.config(bg=self.C_RED, fg='#141414')
                Thread(target=self.bossAI).start()
                # Thread(target=self.stutter).start()
            else:
                Thread(target=self.mpBoss).start()

    def bossAI(self):
        x = .75
        y = .31
        while True:
            if x > 0:
                x -= 0.002
                self.GameInstance.BossItem.place(relx=x, rely=y)
                time.sleep(0.002)
            else:
                break
        while True:
            if x < 0.8:
                x += 0.002
                self.GameInstance.BossItem.place(relx=x, rely=y)
                time.sleep(0.002)
            else:
                break
        while True:
            if y < .36:
                y += 0.002
                self.GameInstance.BossItem.place(relx=x, rely=y)
                time.sleep(0.002)
            else:
                break

    def bossAnim(self):
        self.GameInstance.BossItem.place(relx=.75, rely=.31)
        self.Window.config(bg=self.C_RED)
        self.GameInstance.myPlayer().config('#141414')
        self.GameInstance.PlayerPosition.config(bg=self.C_RED, fg='#141414')
        self.GameInstance.PlayerPage.config(bg=self.C_RED, fg='#141414')
        Thread(target=self.bossAI).start()

    def readyBoss(self):
        return self.BossReady

    def mpBoss(self):
        while True:
            if self.BossReady:
                try:
                    notReady.place_forget()
                except:
                    pass
                self.bossAnim()
                break
            else:
                notReady = Label(self.Window, text='WAIT FOR YOUR TEAMMATE', font=self.W_FONT4, bg=self.W_BG, fg=self.C_BLUE)
                notReady.place(relx=.05, rely=.2)
            time.sleep(0.5)

    def stutter(self):
        while True:
            self.GameInstance.BossItem.place_forget()
            time.sleep(0.004)

    def chooser(self):
        if self.activeMode:
            if self.numGames < 3:
                def sd():
                    self.setDown = False
                self.checkColours = False
                self.colouredPlate.draw(.05, .79)
                self.colouredPlate2.draw(.25, .79)
                self.colouredPlate3.draw(.45, .79)
                self.colouredPlate4.draw(.65, .79)
                self.colouredPlate5.draw(.85, .79)
                self.ColourLabel = Label(self.Window, textvariable=self.ColVar, font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG)
                self.ColourLabel.place(relx=.395, rely=.22)
                self.selectedColour = choice(self.Colours)
                self.ColVar.set(self.ColStr.format(self.selectedColour))
                self.Window.after(3000, lambda: sd())
                self.Window.after(3000, lambda: self.uncheck())

            else:
                self.activeMode = False
                self.whiteFloor12.place(relx=.0, rely=.85)

    def active(self):
        return self.activeMode

    def uncheck(self):
        self.numGames += 1
        self.checkColours = True
        self.Window.after(3000, lambda: (self.ColourLabel.place_forget(), self.chooser()))

    def get(self):
        return self.levelAssets

    def sliders(self):
        return self.whiteSlider, self.whiteSlider2

    def plates(self):
        return self.colouredPlate, self.colouredPlate2, self.colouredPlate3, self.colouredPlate4, self.colouredPlate5

    def colour(self):
        return self.selectedColour
