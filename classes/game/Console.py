from tkinter import *
from threading import Thread
from time import sleep


class Console:
    def __init__(self, g=None):
        self.GameInstance = g

        self.C_GRAY = '#95A5A6'
        self.C_LIGHTGRAY = '#BDC3C7'
        self.C_RED = '#E74C3C'

        self.ConsoleWindow = Tk()
        self.ConsoleWindow.geometry('250x150+90+90')
        self.ConsoleWindow.config(bg='#141414')
        self.ConsoleWindow.overrideredirect(1)

        self.LocationLabel = Label(self.ConsoleWindow, text='LOCATION', font='Verdana 10 bold', bg='#141414', fg='#FFFFFF')
        self.LocationLabel.place(relx=.05, rely=.1)

        self.ThreadsLabel = Label(self.ConsoleWindow, text='THREADS', font='Verdana 10 bold', bg='#141414', fg='#FFFFFF')
        self.ThreadsLabel.place(relx=.08, rely=.3)

        self.CheatsLabel = Label(self.ConsoleWindow, text='CHEATS', font='Verdana 10 bold', bg='#141414', fg='#FFFFFF')
        self.CheatsLabel.place(relx=.12, rely=.5)

        self.TickratesLabel = Label(self.ConsoleWindow, text='TICKRATE', font='Verdana 10 bold', bg='#141414', fg='#FFFFFF')
        self.TickratesLabel.place(relx=.07, rely=.7)

        self.LocationValue = Label(self.ConsoleWindow, text='X: 0.00 | Y: 0.00', font='Verdana 10 bold', bg='#141414', fg=self.C_GRAY)
        self.LocationValue.place(relx=.45, rely=.1)

        self.ThreadsValue = Label(self.ConsoleWindow, text='14 THREADS', font='Verdana 10 bold', bg='#141414', fg=self.C_GRAY)
        self.ThreadsValue.place(relx=.45, rely=.3)

        self.CheatsValue = Label(self.ConsoleWindow, text='ACTIVE - ALL', font='Verdana 10 bold', bg='#141414', fg=self.C_GRAY)
        self.CheatsValue.place(relx=.45, rely=.5)

        self.TickratesValue = Label(self.ConsoleWindow, text='U: 200 | D: REAL', font='Verdana 10 bold', bg='#141414', fg=self.C_GRAY)
        self.TickratesValue.place(relx=.45, rely=.7)

        self.exitBar = Button(self.ConsoleWindow, text=' ', font='Verdana 10 bold', bg=self.C_RED, bd=0, width=50, height=1, fg=self.C_RED, command=lambda: self.ConsoleWindow.destroy())
        self.exitBar.place(relx=.0, rely=-0.1)

        self.exitBar2 = Button(self.ConsoleWindow, text=' ', font='Verdana 10 bold', bg=self.C_RED, bd=0, width=50, height=1, fg=self.C_RED, command=lambda: self.ConsoleWindow.destroy())
        self.exitBar2.place(relx=.0, rely=0.9)

        self.ConsoleWindow.mainloop()


if __name__ == '__main__':
    T = Console()
