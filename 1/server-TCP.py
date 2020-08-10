from socket import *
from _thread import *

threadCount = 0

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 12345))
serverSocket.listen(10)


def thread(connection):
    global threadCount
    try:
        while True:
            x = int(connection.recv(2048).decode("utf-8"))
            y = int(connection.recv(2048).decode("utf-8"))
            connection.send(str.encode(str(x + y)))
            data = connection.recv(2048).decode("utf-8")
            if data == "end connection":
                threadCount -= 1
                break
    except:
        threadCount -= 1
        print("connection closed with a client.")
    connection.close()


while True:
    client, addr = serverSocket.accept()

    if threadCount == 4:
        client.send(str.encode("Server is busy."))
        client.close()
    else:
        print("successfully connected to a client.")
        client.send(str.encode("Server available."))
        client.settimeout(10)
        start_new_thread(thread, (client,))
        threadCount += 1
