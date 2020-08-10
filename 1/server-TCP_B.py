from socket import *
from _thread import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 12345))
serverSocket.listen(10)

serverSocket_second = socket(AF_INET, SOCK_STREAM)
serverSocket_second.bind(("127.0.0.1", 12346))
serverSocket_second.listen(10)


def thread(connection):
    while True:
        x = int(connection.recv(2048).decode("utf-8"))
        y = int(connection.recv(2048).decode("utf-8"))
        connection.send(str.encode(str(x + y)))
        data = connection.recv(2048).decode("utf-8")
        if data == "end connection":
            break
    connection.close()


def decide(temp):
    while True:
        client, addr = temp.accept()
        start_new_thread(thread, (client,))


start_new_thread(decide, (serverSocket,))
start_new_thread(decide, (serverSocket_second,))

