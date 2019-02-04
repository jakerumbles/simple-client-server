#Name: Jake Edwards
#Date: 2/1/2019
#Professor: Dr. Glendowne
#Class: CSC 435-001

import socket
import sys
from _thread import *

print("Server has started")
print("Written by Jake Edwards")

host = '127.0.0.1'
port = 1234

#Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    #bind to port onto the local host
    try:
        server.bind((host, port))
    except socket.error as e:
        print(str(e))
        sys.exit()

    #Tell server to listen on the binded port
    server.listen(5)
    print("Server listening on port " + str(port))

    def client_thread(conn):
        print("Connection established with: " + str(addr))
        
        while True:
            #Reveive data from client
            data = conn.recv(1024)
            num = data.decode()
            if not data:
                break
            print('Client sent ' + str(num))

            #Send confirmation back to client
            msg = 'Number ' + num + ' recieved'
            conn.sendall(msg.encode())
        conn.close()

    #Tell server to accept incoming connections
    #conn is new socket that will be used for this connection.  addr is the address bound to the socket on the other end of the connection
    while True:
        conn, addr = server.accept()
        start_new_thread(client_thread, (conn,))



    
    
