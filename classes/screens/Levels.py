from tkinter import *

from classes.game.Enemy import Enemy
from classes.game.Slider import Slider
from classes.game.Blocker import Blocker


class Levels:
    def __init__(self, w, g):

        self.Window = w
        self.GameInstance = g

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

        self.levelAssets = [self.whiteFloor, self.whiteFloor2, self.whiteFloor3, self.whiteFloor4, self.whiteFloor5,
                            self.whiteFloor6, self.whiteFloor7, self.whiteFloor8, self.whiteFloor9, self.whiteFloor10,
                            self.whiteFloor11]

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
            self.Window.config(bg='#2F3542')
            try:
                self.levelAssets.remove(self.whiteSlider)
                self.levelAssets.remove(self.whiteSlider2)
            except:
                pass
        elif levelNumber == 4:
            # self.Window.config(bg='#141414')
            self.whiteFloor9.place(relx=.0, rely=.85)
            self.whiteFloor10.place(relx=.925, rely=.85)
            self.whiteFloor11.place(relx=.47, rely=.85)
            self.blackBlocker = Blocker(self.Window, self.GameInstance.Player1)
            self.blackBlocker.draw(.125, .0)
            self.whiteSlider = Slider(self.Window, c=self.W_FG, g=self.GameInstance)
            self.whiteSlider2 = Slider(self.Window, c=self.W_FG, g=self.GameInstance)
            self.whiteSlider.draw(0.875, .85)
            self.whiteSlider2.draw(0.415, .85)
            self.levelAssets.append(self.whiteSlider)
            self.levelAssets.append(self.whiteSlider2)
        elif levelNumber == 5:
            self.levelAssets.remove(self.whiteSlider)
            self.levelAssets.remove(self.whiteSlider2)

    def get(self):
        return self.levelAssets
