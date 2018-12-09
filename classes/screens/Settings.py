from tkinter import *
from classes.game.Switch import Switch
from classes.tools.Animator import Animate


class Settings:
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

        self.SettingsVersion = Label(self.Window, text=self.S_VERSION, font=self.W_FONT2, bg=self.W_BG, fg=self.C_GRAY)
        self.SettingsHelp = Label(self.Window, text=self.S_HELP, font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.SettingsUpdate = Label(self.Window, text=self.S_UPDATE, font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.SettingsLog = Label(self.Window, text=self.S_LOGGING, font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.SettingsCheat = Label(self.Window, text=self.S_CHEAT, font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)

        self.SettingsPosition = Label(self.Window, text=self.S_POSITION, font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.SettingsPage = Label(self.Window, text=self.S_PAGE, font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.SettingsEnemy = Label(self.Window, text=self.S_ENEMY, font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.SettingsPeer = Label(self.Window, text=self.S_PEER, font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)

        self.SettingsPositionSwitch = Switch(self.Window)
        self.SettingsPageSwitch = Switch(self.Window)
        self.SettingsEnemySwitch = Switch(self.Window)
        self.SettingsPeerSwitch = Switch(self.Window)

        self.SettingsHelpSwitch = Switch(self.Window)
        self.SettingsUpdateSwitch = Switch(self.Window)
        self.SettingsLogSwitch = Switch(self.Window)
        self.SettingsCheatSwitch = Switch(self.Window)

    def draw(self):

        self.GameInstance.clearScreen()

        self.GameInstance.GameTitle.config(text='SETTINGS')
        self.GameInstance.GameTitle.place(relx=.05, rely=.1)

        self.SettingsVersion.place(relx=.8, rely=.85)

        self.SettingsHelp.place(relx=.051, rely=.35)
        self.SettingsHelpSwitch.place(0.275, 0.35)

        self.SettingsUpdate.place(relx=.051, rely=.45)
        self.SettingsUpdateSwitch.place(0.275, 0.45)

        self.SettingsLog.place(relx=.051, rely=.55)
        self.SettingsLogSwitch.place(0.275, 0.55)

        self.SettingsCheat.place(relx=.051, rely=.65)
        self.SettingsCheatSwitch.place(0.275, 0.65)

        self.SettingsPosition.place(relx=.38, rely=.35)
        self.SettingsPositionSwitch.place(0.604, 0.35)

        self.SettingsPage.place(relx=.38, rely=.45)
        self.SettingsPageSwitch.place(0.604, 0.45)

        self.SettingsEnemy.place(relx=.38, rely=.55)
        self.SettingsEnemySwitch.place(0.604, 0.55)

        self.SettingsPeer.place(relx=.38, rely=.65)
        self.SettingsPeerSwitch.place(0.604, 0.65)

        self.loadConfiguration()

        Animate(self.Window, .05, .1).scroll()

    def loadConfiguration(self):
        configEntries = ['Show-Help', 'Auto-Update', 'Log-Events', 'Allow-Cheats', 'Show-Position', 'Show-Pages', 'Spawn-Enemies', 'Peer-to-Peer']
        configValues = [0, 0, 0, 0, 0, 0, 0, 0]
        configSwitches = [self.SettingsHelpSwitch, self.SettingsUpdateSwitch, self.SettingsLogSwitch, self.SettingsCheatSwitch, self.SettingsPositionSwitch, self.SettingsPageSwitch, self.SettingsEnemySwitch, self.SettingsPeerSwitch]

        for value in configEntries:
            configValues[configEntries.index(value)] = int(self.GameInstance.Configuration['Settings'][value])
            configSwitches[configEntries.index(value)].set(int(self.GameInstance.Configuration['Settings'][value]))

    def get(self):
        return self.SettingsAssets
