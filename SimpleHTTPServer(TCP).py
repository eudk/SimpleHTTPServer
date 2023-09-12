import threading
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('The server is ready')
def handleClient(connectionSocket, addr):
    print (str(addr) + ' connected')
    sentence = connectionSocket.recv(1024).decode()
    httpResponse = "HTTP/1.0 200 OK\n\n<html><body>hello world </body></html >\n"

    connectionSocket.send(httpResponse.encode())
    connectionSocket.close()
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
