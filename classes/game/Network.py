import socket
import select
import random
from threading import Thread

from classes.tools.Logger import Logger


class Host:
    def __init__(self, t, gi):
        self.connectionIP = '0.0.0.0'
        self.connectionPort = 6969

        self.otherPlayer = t
        self.randomID = random.randint(1000, 999999)
        self.gameInstance = gi

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        Logger.log(f'Hosting on: {s.getsockname()[0]} - use this to connect locally.', 'SERVER')
        s.close()

        self.LIST = []
        self.connectedUsers = {}
        self.gameSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gameSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        self.THREAD_LISTEN = Thread(target=self.listen, args=())

    def run(self):
        self.gameSocket.bind((self.connectionIP, self.connectionPort))
        self.gameSocket.listen(10)
        self.LIST.append(self.gameSocket)
        self.THREAD_LISTEN.start()

    def send(self, m):
        try:
            for connectedSocket in self.LIST:
                if connectedSocket != self.gameSocket:
                    connectedSocket.send(str.encode(str(self.randomID) + m))
        except Exception as error:
            Logger.error(error)

    def listen(self):
        while True:
            try:
                read_sockets, write_sockets, error_sockets = select.select(self.LIST, [], [])
                for sock in read_sockets:
                    if sock == self.gameSocket:
                        sockfd, address = self.gameSocket.accept()
                        self.LIST.append(sockfd)
                        Logger.log(f'Client [{address[0]}:{address[1]}] connected to the server.', 'CONNECT')
                    else:
                        try:
                            receivedData = sock.recv(40, ).decode()
                        except:
                            try:
                                try:
                                    disconnected_user = self.connectedUsers[address]
                                    del self.connectedUsers[address]
                                except:
                                    disconnected_user = '[undefined]'
                                Logger.log(f'Client [{address[0]}:{address[1]}] ({disconnected_user}) disconnected from the server.', 'DISCONNECT')
                            except Exception as error:
                                Logger.error(error)
                            sock.close()
                            self.LIST.remove(sock)
                            continue
                        if receivedData:
                            arguments = receivedData.split(';')
                            if arguments[0] != str(self.randomID):
                                if arguments[1] == str(self.gameInstance.getPage()):
                                    if arguments[1] != '5':
                                        if arguments[1] != '6':
                                            self.otherPlayer.show()
                                            self.otherPlayer.setLocation(round(float(arguments[2]), 2), round(float(arguments[3]), 2))
                                        else:
                                            self.gameInstance.currentLevel.BossReady = True
                                    else:
                                        self.otherPlayer.hide()
                                else:
                                    self.otherPlayer.hide()
            except Exception as error:
                Logger.error(error)


class Join:
    def __init__(self, t, gi, i):
        self.connectionIP = i
        self.connectionPort = 6969

        self.randomID = random.randint(1000, 999999)

        self.otherPlayer = t
        self.gameInstance = gi

        self.gameSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gameSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.gameSocket.settimeout(3)

        self.THREAD_LISTEN = Thread(target=self.listen, args=())

    def connect(self):
        try:
            self.gameSocket.connect(('127.0.0.1', 6969))
            self.gameSocket.settimeout(None)
            return True
        except Exception as e:
            Logger.error(e)
            return False

    def startlisten(self):
        self.THREAD_LISTEN.start()

    def listen(self):
        while True:
            try:
                data = self.gameSocket.recv(40,).decode()
            except Exception as e:
                Logger.error(e)
                break
            if data:
                arguments = data.split(';')
                if arguments[0] != str(self.randomID):
                    if arguments[1] == str(self.gameInstance.getPage()):
                        if arguments[1] != '5':
                            if arguments[1] != '6':
                                self.gameInstance.getPlayer().show()
                                self.gameInstance.getPlayer().setLocation(round(float(arguments[2]), 2), round(float(arguments[3]), 2))
                            else:
                                self.gameInstance.currentLevel.BossReady = True
                        else:
                            self.gameInstance.getPlayer().hide()
                    else:
                        self.gameInstance.getPlayer().hide()

    def send(self, m):
        self.gameSocket.send(str.encode(str(self.randomID) + m))


if __name__ == '__main__':
    pass
