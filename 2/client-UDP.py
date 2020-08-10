from socket import *


clientSocket = socket(AF_INET6, SOCK_DGRAM)

while True:
    message = input("Write your message :")
    if message[0:4] == "POST":
        clientSocket.sendto(message.encode(), ('localhost', 1234))
        data, addr = clientSocket.recvfrom(2048)
        data = data.decode()
        if data == "done":
            print("your message has been posted on the channel.")
    elif message[0:3] == "GET":
        clientSocket.sendto(message.encode(), ('localhost', 1234))
        while True:
            rec, addr = clientSocket.recvfrom(2048)
            rec = rec.decode()
            if rec == "done":
                print("End of messages.")
                break
            else:
                print(rec)

    else:
        print("invalid message.")

