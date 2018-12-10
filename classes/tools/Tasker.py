from threading import Thread
from time import sleep


class DELAYED_TASK:
    def __init__(self, f, a=(), t=5):
        self.temporaryDelay = t
        self.threadRunning = True
        self.runningThread = Thread(target=self.execute)
        self.temporaryThread = Thread(target=f, args=a)

    def run(self):
        self.runningThread.start()

    def execute(self):
        sleep(self.temporaryDelay)
        self.temporaryThread.start()


class REPEATED_TASK:
    def __init__(self, f, a=(), t=5, c=True):
        self.temporaryDelay = t
        self.temporaryCondition = c
        self.threadFunction = f
        self.threadArguments = a
        self.threadRunning = True
        self.runningThread = Thread(target=self.execute)
        self.temporaryThread = Thread(target=f, args=a)

    def run(self):
        self.runningThread.start()

    def execute(self):
        while self.temporaryCondition:
            while self.threadRunning:
                self.temporaryThread = Thread(target=self.threadFunction, args=self.threadArguments)
                self.temporaryThread.start()
                sleep(self.temporaryDelay)
            else:
                break

    def stop(self):
        self.threadRunning = False


if __name__ == '__main__':
    def p():
        print('This is a test.')
    nd = REPEATED_TASK(p, t=2)
    nd.run()
