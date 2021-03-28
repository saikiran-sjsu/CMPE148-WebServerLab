#import socket module
from socket import *
import sys  # In order to terminate the program
serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start #Fill in end
    try:
        message =  connectionSocket.recv(1024)# Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =  f.read() # Fill in start #Fill in end
    # Send one HTTP header line into socket
    # Fill in start
        connectionSocket.send(b'\nHTTP/1.1 200 OK\n\n')
    # Fill in end
    # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i], 'utf-8'))
            connectionSocket.send("".encode())
        connectionSocket.close()
    except IOError:
    # Send response message for file not found
    # Fill in start  #Fill in end
    # Close client socket
    # Fill in start
        connectionSocket.send(b'\nHTTP/1.1 404 Not Found\n\n')
        connectionSocket.close()
        break
    # Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data