# coding: utf8
import socket
from socket import error as SocketError

hote = 'localhost'
port = 8888

mainCo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mainCo.connect((hote, port))
    print('Connected succesfully')
except SocketError as ex:
    pass

n = 0
toSend = str(n).encode()
mainCo.send(toSend)
receiveMsg = mainCo.recv(1024)

while (receiveMsg != 'Welcome'):
    n += 1
    toSend = str(n).encode()
    mainCo.send(toSend)
    receiveMsg = mainCo.recv(1024)
    print(receiveMsg.decode() + ' : ' + str(n))
    
print('[+] Password found : ' + n)
print('[+] Closing connection...')
