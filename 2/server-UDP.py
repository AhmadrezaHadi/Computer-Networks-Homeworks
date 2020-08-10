from socket import *


serverSocket = socket(AF_INET6, SOCK_DGRAM)
serverSocket.bind(('localhost', 1234))


messages = []

while True:
    data, addr = serverSocket.recvfrom(2048)
    data = data.decode()
    if data[0:3] == "GET":
        for message in messages:
            serverSocket.sendto(message.encode(), (addr[0], addr[1]))
    elif data[0:4] == "POST":
        tempMessage = "ip : " + str(addr[0]) + " with port : " + str(addr[1]) + " posted : " + data[4:]
        messages.append(tempMessage)
        print(messages)
    serverSocket.sendto("done".encode(), (addr[0], addr[1]))