from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect(('127.0.0.1', 1234))
    print("Successfully connected to the server.")
except ConnectionRefusedError as CRE:
    print("can't connect to server.\nplease try again.\nError : ", CRE)
    exit(0)

while True:
    try:
        message = input("Client : ")
        clientSocket.send(message.encode())
        if message == "good bye":
            print("connection closed.")
            exit(0)
        if not message:
            print("EOF detected.\ndisconnecting...")
            clientSocket.close()
            print("disconnected.")
            exit(0)
        message = clientSocket.recv(2048).decode()
        if not message:
            print("EOF detected.\ndisconnecting...")
            clientSocket.close()
            print("disconnected.")
            exit(0)
        if message.lower() == "good bye":
            print("Connection closed by server.\n")
            exit(0)
        else:
            print("Server : ", message)
    except KeyboardInterrupt as KI:
        print("Program interrupted.\nConnection Closed\nError : ", KI)
        clientSocket.close()
        exit(0)
    except error as Err:
        print("Connection forcibly closed.\nplease try again.\nError : ", Err)
        clientSocket.close()
        exit(0)
    except EOFError as EOFErr:
        print("EOF detected.\ndisconnecting...")
        clientSocket.close()
        print("disconnected")
        exit(0)
    except ConnectionResetError as CRE:
        print("Connection forcibly closed by server.\nError : ", CRE)
        clientSocket.close()
        exit(0)