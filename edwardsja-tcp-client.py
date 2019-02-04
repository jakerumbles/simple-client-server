#Name: Jake Edwards
#Date: 2/1/2019
#Professor: Dr. Glendowne
#Class: CSC 435-001

import socket
import random
import sys

server = '127.0.0.1'
port = 1234

#Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    #Connect to server
    try:
        client.connect((server, port))
    except Exception as e:
        print(e)
        print("Program closing...")
        sys.exit()

    #Send a number to server
    rand = str(random.randint(1, 10_001))
    client.send(rand.encode())
    print("Number sent!")

    #Recieve confirmation from server
    confirmation = client.recv(4096)
    print(confirmation.decode())





