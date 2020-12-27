import socket
import time
import os
import tqdm

#Download Client

connected = False; #Checks if client is connected to server
while not connected: #Loops until connected to server
    try: #Attempting Connection
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host = socket.gethostname()
        port = int(input('Enter port: '))
        s.connect((host, port))
        s.sendall('send'.encode('utf-8'))
        time.sleep(2)
        f = open('torecv.png', 'wb') #Opening File Buffer
        code = 50;
        connected = True
    except Exception as err: #If fail to connect, notify user
        print('Incorrect Socket. Please try again.')
        time.sleep(1)
print(s.recv(1024).decode())

print('Receiving...')
bits = s.recv(1024) 
while (bits): #Importing File
    print('Receiving...')
    f.write(bits)
    bits = s.recv(1024)
f.close()


#inpt = input('Kill? ')
#if (inpt == 'yes'):
#    s.sendall('kill'.encode('utf-8'))

s.close()