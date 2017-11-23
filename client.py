import socket
host = '192.168.100.101'
port = 5000
mySocket = socket.socket()
mySocket.connect((host, port))
message = input(" -> ")
while message != 'q':
    flag = 1
    while (flag):
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        print ('Received from server: ' + data)
        message = input("->")
mySocket.close()
