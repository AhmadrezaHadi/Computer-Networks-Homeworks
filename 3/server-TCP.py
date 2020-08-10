from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

try:
    serverSocket.bind(('127.0.0.1', 1234))
except error as e:
    print("Server failed to start\nError : ", e)

serverSocket.listen(5)
client, addr = serverSocket.accept()
print("Connected to the client successfully.")
while True:
    try:
        message = client.recv(2048).decode('utf-8')
        if not message:
            print("EOF detected.\ndisconnecting...")
            client.close()
            print("disconnected.")
            exit(0)
        if message.lower() == "good bye":
            client.close()
            print("Connection closed by the client.")
            exit(0)
        else:
            print("Client : ", message)
            message = input("Server : ")
            client.send(message.encode())
            if message.lower() == "good bye":
                print("connection closed.\n")
                exit(0)
    except KeyboardInterrupt as KI:
        print("Program interrupted.\nConnection Closed\nError : ", KI)
        serverSocket.close()
        exit(0)
    except ConnectionAbortedError as CAE:
        print("Connection Aborted.\nError : ", CAE)
        serverSocket.close()
        exit(0)
    except ConnectionResetError as CRE:
        print("Connection forcibly closed by client.\nError : ", CRE)
        serverSocket.close()
        exit(0)
    except EOFError as EOFErr:
        print("EOF detected.\ndisconnecting...")
        serverSocket.close()
        print("disconnected")
        exit(0)