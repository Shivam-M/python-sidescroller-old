from tkinter import *
from classes.tools.Animator import Animate


class Customize:
    def __init__(self, w, g):

        self.SettingsAssets = []
        self.Window = w
        self.GameInstance = g

        self.W_BG = '#2F3542'
        self.W_FG = '#FFFFFF'

        self.W_FONT = ('MS PGothic', 30, 'bold')
        self.W_FONT2 = ('MS PGothic', 12, 'bold')
        self.W_FONT3 = ('MS PGothic', 10, 'bold')
        self.W_FONT4 = ('MS PGothic', 11, 'bold')

        self.S_VERSION = f'Version A - {self.GameInstance.GameVersion}'
        self.S_HELP = 'SHOW HELP'
        self.S_UPDATE = 'AUTO-UPDATE'
        self.S_LOGGING = 'LOG EVENTS'
        self.S_CHEAT = 'ALLOW CHEATS'
        self.S_LIVES = '3 LIVES REMAINING'
        self.S_POSITION = 'SHOW POSITION'
        self.S_PAGE = 'SHOW PAGE'
        self.S_ENEMY = 'SPAWN ENEMIES'
        self.S_PEER = 'PEER-TO-PEER'

        self.C_RED = '#E74C3C'
        self.C_GREEN = '#2ECC71'
        self.C_ORANGE = '#F39C12'
        self.C_BLUE = '#3498DB'
        self.C_YELLOW = '#F1C40F'
        self.C_GRAY = '#95A5A6'
        self.C_LIGHTGRAY = '#BDC3C7'

    def draw(self):

        self.GameInstance.clearScreen()

        self.GameInstance.GameTitle.config(text='CUSTOMIZE')
        self.GameInstance.GameTitle.place(relx=.05, rely=.1)

        Animate(self.Window, .05, .1).scroll()
