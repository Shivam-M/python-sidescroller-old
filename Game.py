import configparser
import os
from threading import Thread, active_count
from time import sleep
from tkinter import *

from classes.screens.Customize import Customize
from classes.screens.Settings import Settings
from classes.screens.Update import Update

from classes.tools.Error import Error
from classes.tools.Logger import Logger

from classes.game.Player import Player
from classes.game.Network import Host, Join
from classes.game.Slider import Slider
from classes.game.Enemy import Enemy

# TODO: Move update functions into a separate class
# TODO: Add all settings assets into an array
# TODO: Saving & exiting buttons on settings screen
# TODO: General optimizations (performance, network)
# TODO: Add client-server connection option as opposed to the current peer-to-peer
# TODO: Player customization (colours, name-tags)
# TODO: Complete Coin class


class Game:
    def __init__(self):
        self.W_BG = '#2F3542'
        self.W_FG = '#FFFFFF'
        self.W_SIZE = '600x300'
        self.W_SIZE = '800x300'
        self.W_TITLE = 'PLACEHOLDER'

        self.W_FONT = ('MS PGothic', 30, 'bold')
        self.W_FONT2 = ('MS PGothic', 12, 'bold')
        self.W_FONT3 = ('MS PGothic', 10, 'bold')
        self.W_FONT4 = ('MS PGothic', 11, 'bold')

        self.GameMode = 0
        self.GameVersion = 0.53
        self.GamePage = 1
        self.GameLives = 3
        self.GameCooldown = 20
        self.GameState = 'host'

        self.S_GAME = 'PLACEHOLDER'
        self.S_SINGLEPLAYER = 'SINGLE-PLAYER'
        self.S_MULTIPLAYER = 'MULTI-PLAYER'
        self.S_CUSTOMIZE = 'CUSTOMIZE'
        self.S_SETTINGS = 'SETTINGS'
        self.S_EXITGAME = 'EXIT GAME'
        self.S_UPDATEGAME = 'UPDATE GAME'

        self.S_VERSION = f'Version A - {self.GameVersion}'
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

        self.CFG_HELP = 0
        self.CFG_UPDATE = 0
        self.CFG_LOGGING = 0
        self.CFG_CHEATS = 0
        self.CFG_POSITION = 0
        self.CFG_PAGES = 0

        self.Configuration = configparser.ConfigParser()
        self.Configuration.read('config/game/game-config.ini')

        self.whiteFloor = None
        self.whiteFloor2 = None
        self.whiteFloor3 = None
        self.whiteFloor4 = None
        self.whiteFloor5 = None
        self.whiteFloor6 = None
        self.whiteFloor7 = None
        self.whiteFloor8 = None
        self.whiteFloor9 = None
        self.whiteFloor10 = None
        self.whiteFloor11 = None
        self.whiteFloor12 = None
        self.whiteFloor13 = None
        self.whiteFloor14 = None
        self.whiteFloor15 = None
        self.whiteFloor16 = None
        self.whiteFloor17 = None

        self.Slider = None
        self.Slider2 = None

        self.allFloors = [self.whiteFloor, self.whiteFloor2, self.whiteFloor3,
                          self.whiteFloor4, self.whiteFloor5, self.whiteFloor6,
                          self.whiteFloor7, self.whiteFloor8, self.whiteFloor9,
                          self.whiteFloor10, self.whiteFloor11, self.Slider, self.Slider2]

        self.threadBypass = False

        self.GameWindow = Tk()
        self.GameWindow.geometry(self.W_SIZE)
        self.GameWindow.title(self.W_TITLE)
        self.GameWindow.config(bg=self.W_BG)

        self.GameTitle = Label(self.GameWindow, text=self.S_GAME, font=self.W_FONT, bg=self.W_BG, fg=self.W_FG)
        self.GameTitle.place(relx=.05, rely=.1)

        # gamePhoto = PhotoImage(file="../assets/images/download.png", master=self.GameWindow)
        # gamePhoto = gamePhoto.subsample(3)
        # gamePhoto2 = PhotoImage(file="../assets/images/download1.png", master=self.GameWindow)
        # gamePhoto2 = gamePhoto2.subsample(3)
        # self.otherImg = Button(self.GameWindow, image=gamePhoto2, bd=0, command=lambda: (self.otherImg.place_forget(), self.CoinItem.place(relx=.75, rely=.3)))
        # self.CoinItem = Button(self.GameWindow, image=gamePhoto, bd=0, command=lambda: (self.CoinItem.place_forget(), self.otherImg.place(relx=.75, rely=.3)))
        # self.CoinItem.place(relx=.75, rely=.3)

        self.GameSingleplayer = Button(self.GameWindow, text=self.S_SINGLEPLAYER, font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG, bd=0, command=lambda: self.startGame(0))
        self.GameSingleplayer.place(relx=.05, rely=.3)
        self.GameMultiplayer = Button(self.GameWindow, text=self.S_MULTIPLAYER, font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG, bd=0, command=lambda: self.startGame(1))
        self.GameMultiplayer.place(relx=.05, rely=.4)
        self.GameCustomize = Button(self.GameWindow, text=self.S_CUSTOMIZE, font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG, bd=0, command=lambda: self.customizeScreen())
        self.GameCustomize.place(relx=.05, rely=.5)
        self.GameSettings = Button(self.GameWindow, text=self.S_SETTINGS, font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG, bd=0, command=lambda: self.changeSettings())
        self.GameSettings.place(relx=.05, rely=.6)
        self.GameExitGame = Button(self.GameWindow, text=self.S_EXITGAME, font=self.W_FONT2, bg=self.W_BG, fg=self.C_RED, bd=0, command=lambda: self.exitGame())
        self.GameExitGame.place(relx=.05, rely=.7)
        self.GameUpdate = Button(self.GameWindow, text=self.S_UPDATEGAME, font=self.W_FONT2, bg=self.W_BG, fg=self.C_GREEN, bd=0, command=lambda: self.updateGame())
        self.GameUpdate.place(relx=.05, rely=.8)

        self.GameLivesRemaining = Label(self.GameWindow, text=self.S_LIVES, font=self.W_FONT4, bg=self.W_BG, fg=self.C_RED)

        self.currentLocation = StringVar()
        self.PlayerPosition = Label(self.GameWindow, textvariable=self.currentLocation, font=self.W_FONT3, bg=self.W_BG, fg=self.C_GRAY)

        self.currentPage = StringVar()
        self.PlayerPage = Label(self.GameWindow, textvariable=self.currentPage, font=self.W_FONT3, bg=self.W_BG, fg=self.C_GREEN)

        self.GameAssets = [self.GameTitle, self.GameSingleplayer, self.GameMultiplayer, self.GameCustomize, self.GameSettings, self.GameExitGame, self.GameUpdate]

        self.THREAD_PRINT = Thread(target=self.printThreads, args=()).start()
        self.THREAD_WINDOW = Thread(target=self.GameWindow.mainloop())

    def drawStart(self):
        global keyPressedL, keyPressedR

        keyPressedR = False
        keyPressedL = False

        def handleKeyPress(event):
            global keyPressedL, keyPressedR
            if event.keysym == 'Left':
                keyPressedL = True
                self.myPlayer().setVelocityX(-0.0025)
            elif event.keysym == 'Right':
                keyPressedR = True
                self.myPlayer().setVelocityX(+0.0025)
            elif event.keysym == 'Up':
                if not self.myPlayer().isJumping():
                    if keyPressedL:
                        self.myPlayer().jump(0)
                    elif keyPressedR:
                        self.myPlayer().jump(1)
                    else:
                        self.myPlayer().jump(2)

        def handleKeyRelease(event):
            global keyPressedL, keyPressedR
            if event.keysym == 'Left':
                keyPressedL = False
                if not keyPressedR:
                    if self.myPlayer().isJumping():
                        self.myPlayer().setVelocityX(0)
            elif event.keysym == 'Right':
                keyPressedR = False
                if not keyPressedL:
                    if not self.myPlayer().isJumping():
                        self.myPlayer().setVelocityX(0)

        def evStopL(event):
            global keyPressedL, keyPressedR
            keyPressedL = False
            if not keyPressedR:
                self.myPlayer().setVelocityX(0)

        def evStopR(event):
            global keyPressedL, keyPressedR
            keyPressedR = False
            if not keyPressedL:
                self.myPlayer().setVelocityX(0)

        self.clearScreen()
        self.GameWindow.bind('<Up>', handleKeyPress)
        self.GameWindow.bind('<Right>', handleKeyPress)
        self.GameWindow.bind('<Left>', handleKeyPress)
        self.GameWindow.bind('<KeyRelease-Left>', evStopL)
        self.GameWindow.bind('<KeyRelease-Right>', evStopR)

        self.PlayerPage.place(relx=.825, rely=.05)

        self.drawPage(1)
        self.GameWindow.after(1, lambda: self.GameLivesRemaining.place(relx=.41, rely=.15))
        self.GameWindow.after(3000, lambda: self.GameLivesRemaining.place_forget())

        self.Player1 = Player(self.GameWindow, 'white')
        self.Player1.draw(.05, .5)

        if self.GameState == 'host':
            arguments = (self.Player1, )
        else:
            arguments = (self.Player2, )

        gThread = Thread(target=self.moveDown, args=arguments)
        uThread = Thread(target=self.updateLocation, args=arguments)
        cThread = Thread(target=self.changeLocation, args=arguments)
        pThread = Thread(target=self.showLocation, args=arguments)
        bThread = Thread(target=self.checkBoundary, args=arguments)

        allThreads = [gThread, uThread, cThread, pThread, bThread]

        for thread in allThreads:
            thread.start()

    def updateGame(self):

        Update(self.GameWindow, self).draw()

    def printThreads(self):
        while True:
            Logger.log(f'Current number of threads: {active_count()}')
            if active_count() > 30:
                if not self.threadBypass:
                    threadLimit = Error(text='Thread count exceeded 30 threads [warning level] - to carry on running the program and ignore any other warnings, click \'Ignore\', to close the program, click \'Exit\'. The program '
                                             'will force close at 80 threads', options=['Ignore', 'Exit'])
                    threadLimit.show()
                    if threadLimit.outcome() == 'Ignore':
                        self.threadBypass = True
                    elif threadLimit.outcome() == 'Exit':
                        self.GameWindow.destroy()
                        exit(69)
            if active_count() > 80:
                Logger.log('Force shutdown - exceeded 80 threads.', 'ERROR')
                self.GameWindow.destroy()
            sleep(5)

    def getPlayer(self):
        return self.Player1

    def clearFloors(self):
        try:
            for floor in self.allFloors:
                floor.place_forget()
        except Exception as e:
            pass

    def myPlayer(self):
        if self.GameState == 'host':
            return self.Player1
        elif self.GameState == 'join':
            return self.Player2

    def drawPage(self, n):
        self.currentPage.set('GAME PAGE: ' + str(n))
        self.clearFloors()
        n = 4
        if n == 1:
            self.whiteFloor = Label(self.GameWindow, bg=self.W_FG, height=3, width=200)
            self.whiteFloor.place(relx=.0, rely=.85)
        elif n == 2:
            self.whiteFloor2 = Label(self.GameWindow, bg=self.W_FG, height=3, width=43)
            self.whiteFloor2.place(relx=.0, rely=.85)

            self.whiteFloor3 = Label(self.GameWindow, bg=self.W_FG, height=3, width=100)
            self.whiteFloor3.place(relx=.70, rely=.85)
        elif n == 3:
            self.whiteFloor4 = Label(self.GameWindow, bg=self.W_FG, height=3, width=20)
            self.whiteFloor4.place(relx=.0, rely=.85)

            self.whiteFloor5 = Label(self.GameWindow, bg=self.W_FG, height=3, width=100)
            self.whiteFloor5.place(relx=.925, rely=.85)

            self.whiteFloor6 = Label(self.GameWindow, bg=self.W_FG, height=1, width=10)
            self.whiteFloor6.place(relx=.2, rely=.7)

            self.whiteFloor7 = Label(self.GameWindow, bg=self.W_FG, height=1, width=8)
            self.whiteFloor7.place(relx=.4, rely=.6)

            self.whiteFloor8 = Label(self.GameWindow, bg=self.W_FG, height=1, width=14)
            self.whiteFloor8.place(relx=.68, rely=.65)
        elif n == 4:
            self.whiteFloor9 = Label(self.GameWindow, bg=self.W_FG, height=3, width=10)
            self.whiteFloor9.place(relx=.0, rely=.85)

            self.whiteFloor10 = Label(self.GameWindow, bg=self.W_FG, height=3, width=100)
            self.whiteFloor10.place(relx=.925, rely=.85)

            self.whiteFloor11 = Label(self.GameWindow, bg=self.W_FG, height=3, width=5)
            self.whiteFloor11.place(relx=.47, rely=.85)

            self.Slider = Slider(self.GameWindow, c='white', g=self)
            self.Slider.draw(0.875, .85)

            self.Slider2 = Slider(self.GameWindow, c='white', g=self)
            self.Slider2.draw(0.415, .85)

        self.allFloors = [self.whiteFloor, self.whiteFloor2, self.whiteFloor3,
                          self.whiteFloor4, self.whiteFloor5, self.whiteFloor6,
                          self.whiteFloor7, self.whiteFloor8, self.whiteFloor9,
                          self.whiteFloor10, self.whiteFloor11, self.Slider, self.Slider2]

    def Log(self, m, p='INFO'):
        if self.Configuration['Settings']['Log-Events'] == '1':
            Logger.log(m, p)

    def moveDown(self, p):
        while True:
            if p.gravity():
                if self.GamePage == 1:
                    playerLocation = p.getLocation()
                    if playerLocation[1] < .79:
                        p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                elif self.GamePage == 2:
                    playerLocation = p.getLocation()
                    if playerLocation[1] < .79:
                        p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    elif playerLocation[1] <= 1.10 and 0.39 < playerLocation[0] < 0.68:
                        p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    if .97 > playerLocation[0] > .70 and playerLocation[1] > 0.79:
                        p.setLocation(playerLocation[0], 0.79)
                elif self.GamePage == 3:
                    playerLocation = p.getLocation()
                    if 0.28 >= playerLocation[0] >= 0.20:
                        if playerLocation[1] < .64:
                            p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                        elif playerLocation[1] > 0.7:
                            p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    elif 0.39 >= round(playerLocation[0], 2) >= 0.29:
                        p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    elif 0.48 >= round(playerLocation[0], 2) >= 0.39:
                        if playerLocation[1] < .54:
                            p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                        elif playerLocation[1] > 0.6:
                            p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    elif 0.66 >= playerLocation[0] >= 0.49:
                        p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    elif 0.79 >= playerLocation[0] >= 0.67:
                        if playerLocation[1] < .59:
                            p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                        elif playerLocation[1] > 0.65:
                            p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    elif 0.92 >= playerLocation[0] >= 0.80:
                        p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    else:
                        if playerLocation[1] < .79:
                            p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    if .99 > playerLocation[0] > .92 and playerLocation[1] > 0.79:
                        p.setLocation(playerLocation[0], 0.79)
                elif self.GamePage == 4:
                    playerLocation = p.getLocation()
                    if 0.09 >= playerLocation[0] >= 0.00:
                        if playerLocation[1] < .79:
                            p.setLocation(playerLocation[0], playerLocation[1] + 0.005)
                    elif 0.30 >= playerLocation[0] >= 0.10:
                        if self.underSlider(p):
                            pass
                sleep(0.005)
            else:
                sleep(0.005)

    def underSlider(self, p):
        # TODO: Add GameSliders array
        pass

    @staticmethod
    def changeLocation(p):
        while True:
            playerLocation = p.getLocation()
            playerLocation[0] = playerLocation[0] + p.getVelocityX()
            sleep(0.005)

    def loseLives(self, p):
        self.GameLives -= 1
        if self.GameLives == 0:
            self.GamePage = 0
            self.clearScreen()
            t = Label(self.GameWindow, text='GAME OVER', font=self.W_FONT, bg=self.W_BG, fg=self.C_RED)
            t.place(relx=.049, rely=.2)
            self.GamePage = 1
            self.drawPage(1)
            p.setLocation(0.05, .5)
        else:
            self.GameLivesRemaining.config(text=f'{self.GameLives} LIVES REMAINING')
            self.GameWindow.after(1, lambda: self.GameLivesRemaining.place(relx=.41, rely=.15))
            self.GameWindow.after(3000, lambda: self.GameLivesRemaining.place_forget())
            self.GamePage = 1
            self.drawPage(1)
            p.setLocation(0.05, .5)

    def checkBoundary(self, p):
        while True:
            playerLocation = p.getLocation()
            if playerLocation[1] > 0.85:
                self.loseLives(p)
            if playerLocation[0] <= -0.02:
                if self.GamePage > 1:
                    self.drawPage(self.GamePage - 1)
                    self.GamePage -= 1
                    p.setLocation(0.95, playerLocation[1])
            elif playerLocation[0] >= 1.01:
                self.drawPage(self.GamePage + 1)
                self.GamePage += 1
                p.setLocation(0.05, playerLocation[1])

            sleep(0.01)

    def updateLocation(self, p):
        while True:
            if self.GameMode == 1:
                self.Session.send(';' + str(self.GamePage) + ';' + str(round(p.getLocation()[0], 2)) + ';' + str(round(p.getLocation()[1], 2)))
                self.Player2.refresh()
                self.Player1.refresh()
            else:
                p.refresh()
            sleep(0.001)

    def startGame(self, t):
        self.setGamemode(t)
        if t == 0:
            self.drawStart()
            Test2 = Enemy(self.GameWindow, self.Player1, c=self.C_RED, g=self)
            Test2.draw(.45, 0.755)
            # Test3 = Enemy(self.GameWindow, self.Player1, c=self.C_RED, g=self)
            # Test3.draw(.7, 0.755)
        else:
            self.clearScreen()
            b = Button(self.GameWindow, text='HOST', command=lambda: (b.place_forget(), b2.place_forget(), self.host()))
            b.pack()
            b2 = Button(self.GameWindow, text='JOIN', command=lambda: (b.place_forget(), b2.place_forget(), self.join()))
            b2.pack()

    def host(self):
        self.GameState = 'host'
        self.Player2 = Player(self.GameWindow, self.C_BLUE)
        self.Player2.draw(.1, .5)
        self.Session = Host(self.Player2, self)
        self.drawStart()
        self.Session.run()

    def join(self):
        self.GameState = 'join'
        self.Player2 = Player(self.GameWindow, self.C_BLUE)
        self.Player2.draw(.1, .5)
        self.Session = Join(self.Player2, self)
        self.drawStart()
        self.Session.connect()
        self.Session.startlisten()

    def getPage(self):
        return self.GamePage

    def exitGame(self):
        self.GameWindow.destroy()

    def runGame(self):
        self.THREAD_WINDOW.start()

    def restartGame(self):
        pass

    def showConsole(self):
        pass

    def clearScreen(self):
        for GameAsset in self.GameAssets:
            GameAsset.place_forget()

    def changeSettings(self):
        Settings(self.GameWindow, self).draw()

    def customizeScreen(self):
        Customize(self.GameWindow, self).draw()

    def setGamemode(self, g):
        self.restartGame()
        self.GameMode = g

    def showLocation(self, p):
        while True:
            if self.Configuration['Settings']['Show-Position'] == '1':
                self.PlayerPosition.place(relx=.05, rely=.05)
                self.currentLocation.set(f'L: {p.getLocation()[0]:.2f}, {p.getLocation()[1]:.2f} | X: {p.getVelocityX()}')
            sleep(0.01)


if __name__ == '__main__':
    Test = Game()
    Test.runGame()
