import os, shutil, urllib.request, zipfile
from tkinter import *

from classes.tools.Animator import Animate


class Update:
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
        self.W_FONT5 = ('MS PGothic', 4, 'bold')
        self.W_FONT6 = ('MS PGothic', 18, 'bold')

        self.S_INFO = 'Information: Current files and program data will be stored in a backup folder in the above directory.'

        self.C_RED = '#E74C3C'
        self.C_GREEN = '#2ECC71'
        self.C_ORANGE = '#F39C12'
        self.C_BLUE = '#3498DB'
        self.C_YELLOW = '#F1C40F'
        self.C_GRAY = '#95A5A6'
        self.C_LIGHTGRAY = '#BDC3C7'

        self.CONFIG_PROGRAM_GITHUB = 'https://github.com/Shivam-M/Game-S'

        def getFolderSize(d=os.getcwd()):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(d):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            return total_size

        self.currentVersion = Label(self.Window, text='Current Version:', font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.currentSize = Label(self.Window, text='Current Size:', font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.latestVersion = Label(self.Window, text='Latest Version:', font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)
        self.latestSize = Label(self.Window, text='Latest Size:', font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY)

        self.currentVersionV = Label(self.Window, text=('Version ' + str(self.GameInstance.GameVersion)), font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG)
        self.currentSizeV = Label(self.Window, text=f'{getFolderSize() / 1000} KB', font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG)
        self.latestVersionV = Label(self.Window, text='Version 1.01', font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG)
        self.latestSizeV = Label(self.Window, text='-- KB', font=self.W_FONT2, bg=self.W_BG, fg=self.W_FG)

        self.updateInformation = Label(self.Window, text=self.S_INFO, font=self.W_FONT3, bg=self.W_BG, fg=self.C_BLUE)
        self.unfilledBar = Label(self.Window, text=' ', font=self.W_FONT5, bg=self.C_GRAY, fg=self.C_GRAY, width=180)
        self.filledBar = Label(self.Window, text=' ', font=self.W_FONT5, bg=self.W_FG, fg=self.W_FG, width=40)
        self.percentageValue = Label(self.Window, text='0%', font=self.W_FONT2, bg=self.W_BG, fg=self.C_LIGHTGRAY, anchor='e')
        self.updateProgress = Label(self.Window, text='UPDATING GAME...', font=self.W_FONT6, bg=self.W_BG, fg=self.C_LIGHTGRAY, anchor='e')
        self.updateButton = Button(self.Window, text='UPDATE GAME', font=self.W_FONT2, fg=self.W_BG, bg=self.C_LIGHTGRAY, bd=0, command=lambda: (self.updateButton.place_forget(), self.performUpdate(), self.updateProgress.place(relx=.045, rely=.77)))

    def draw(self):

        self.GameInstance.clearScreen()

        self.GameInstance.GameTitle.config(text='UPDATE')
        self.GameInstance.GameTitle.place(relx=.05, rely=.1)

        self.currentVersion.place(relx=.05, rely=.35)
        self.currentSize.place(relx=.54, rely=.35)
        self.latestVersion.place(relx=.05, rely=.45)
        self.latestSize.place(relx=.54, rely=.45)

        self.currentVersionV.place(relx=.28, rely=.35)
        self.currentSizeV.place(relx=.82, rely=.35)
        self.latestVersionV.place(relx=.28, rely=.45)
        self.latestSizeV.place(relx=.82, rely=.45)

        self.updateInformation.place(relx=.05, rely=.55)
        self.unfilledBar.place(relx=.05, rely=.88)
        self.filledBar.place(relx=.05, rely=.88)
        self.percentageValue.place(relx=.91, rely=.8)
        self.updateProgress.place(relx=.049, rely=.77)
        self.updateButton.place(relx=.05, rely=.78)

        Animate(self.Window, .05, .1).scroll()

    def performUpdate(self):

        os.chdir('../../')
        t = self.CONFIG_PROGRAM_GITHUB.split('/')
        cwd = str(os.getcwd())
        cwd = cwd.replace(os.sep, '/')
        counter = 0
        folder = []
        x = len(cwd) - 1
        while True:
            if cwd[x] != '/':
                counter += 1
                x = len(cwd) - counter
                folder.insert(0, cwd[x])
                continue
            else:
                break
        folder.remove('/')
        folder = "".join(folder)
        os.chdir('../')
        shutil.make_archive(folder + '-BACKUP', 'zip', folder)
        urllib.request.urlretrieve(self.CONFIG_PROGRAM_GITHUB + '/archive/master.zip', folder + '-NEW.zip')
        zip = zipfile.ZipFile(folder + '-NEW.zip')

        try:
            shutil.rmtree(folder, ignore_errors=True)
        except PermissionError:
            pass
        zip.extractall()

        def getFolderSize(d='..'):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(d):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            return total_size

        self.latestSizeV.config(text=(str((getFolderSize(os.getcwd() + '/' + t[4] + '-master')) / 1000) + ' KB'))

        for file in os.listdir(os.getcwd() + '/' + t[4] + '-master'):
            os.rename(os.getcwd() + '/' + t[4] + '-master/' + file, os.getcwd() + '/' + folder + '/' + file)

        zip.close()
        try:
            shutil.rmtree(t[4] + '-master', ignore_errors=True)
            shutil.rmtree(folder + '-NEW.zip', ignore_errors=True)
        except PermissionError:
            pass
        try:
            os.remove(folder + '-NEW.zip')
        except:
            pass
