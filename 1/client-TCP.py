from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)


print('Connecting to server')
try:
    clientSocket.connect(("127.0.0.1", 12345))
    print("connected")
except error as e:
    print("Connection failed.\nTry again.\nError: ", end="\0")
    print(str(e))

Response = clientSocket.recv(2048).decode("utf-8")

if Response == "Server is busy.":
    print("server is busy.\n please try again later.")

else:
    try:
        while True:
            num1 = input("Enter first number : ")
            num2 = input("Enter second number : ")
            clientSocket.send(str.encode(num1))
            clientSocket.send(str.encode(num2))
            Response = clientSocket.recv(1024)
            print("Sum is :", Response.decode("utf-8"))
            temp = input("Do you want to end the connection? [y/n] ")
            if temp.lower() == "y":
                clientSocket.send(str.encode("end connection"))
                break
            elif temp.lower() == "n":
                clientSocket.send(str.encode("wait"))
    except:
        print("Connection Closed.\nRequest timed out.")
clientSocket.close()

