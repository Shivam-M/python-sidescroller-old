from tkinter import *
from classes.game.Switch import Switch
from classes.tools.Animator import Animate


class Over:
    def __init__(self, w, g, i=3):

        self.OverAssets = []
        self.Window = w
        self.GameInstance = g
        self.Reasons = [
            'RAN OUT OF LIVES',
            'RAN OUT OF TIME',
            'TEAMMATE DISCONNECTED',
            'UNKNOWN ERROR OCCURRED'
        ]

        self.W_BG = '#2F3542'
        self.W_FG = '#FFFFFF'

        self.W_FONT = ('MS PGothic', 30, 'bold')
        self.W_FONT2 = ('MS PGothic', 12, 'bold')
        self.W_FONT3 = ('MS PGothic', 10, 'bold')
        self.W_FONT4 = ('MS PGothic', 11, 'bold')
        self.W_FONT5 = ('Tahoma', 25, 'bold')
        self.W_FONT6 = ('Tahoma', 15, 'bold')

        self.S_VERSION = f'Version A - {self.GameInstance.GameVersion}'
        self.S_OVER = 'GAME OVER'
        self.S_ALIVE = 'TIME ALIVE:'
        self.S_LEVEL = 'CURRENT LEVEL:'
        self.S_CHECKPOINT = 'CHECKPOINT:'
        self.S_REASON = self.Reasons[i]
        
        self.C_RED = '#E74C3C'
        self.C_GREEN = '#2ECC71'
        self.C_ORANGE = '#F39C12'
        self.C_BLUE = '#3498DB'
        self.C_YELLOW = '#F1C40F'
        self.C_GRAY = '#95A5A6'
        self.C_LIGHTGRAY = '#BDC3C7'

        self.GameOverLabel = Label(self.Window, text=self.S_OVER, font=self.W_FONT5, bg=self.W_BG, fg=self.C_RED)
        self.GameReasonLabel = Label(self.Window, text=self.S_REASON, font=self.W_FONT6, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.AliveTimeLabel = Label(self.Window, text=self.S_ALIVE, font=self.W_FONT3, bg=self.W_BG, fg=self.C_GRAY)
        self.LevelLabel = Label(self.Window, text=self.S_LEVEL, font=self.W_FONT3, bg=self.W_BG, fg=self.C_GRAY)
        self.CheckpointLabel = Label(self.Window, text=self.S_CHECKPOINT, font=self.W_FONT3, bg=self.W_BG, fg=self.C_GRAY)

    def draw(self):

        self.GameInstance.clearScreen()

        self.GameOverLabel.place(relx=.05, rely=.25)
        self.GameReasonLabel.place(relx=.32, rely=.29)
        self.AliveTimeLabel.place(relx=.053, rely=.45)
        self.LevelLabel.place(relx=.054, rely=.55)
        self.CheckpointLabel.place(relx=.054, rely=.65)

        Animate(self.Window, .05, .1).scroll()
