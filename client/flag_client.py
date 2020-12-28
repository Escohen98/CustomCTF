import socket
from connection import connection

#Flag Client

#Connect to server
conn = connection()
s = conn.connect(12345)

success = False;
s.sendall('flag'.encode('utf-8')) 
while not success: #Loops through until successful login
    flag = input("Flag: ")
    if not flag:
        print("Please enter a value: ")
        continue
    s.sendall(flag.encode('utf-8'))

    rec1 = s.recv(1024).decode()
    rec2 = s.recv(1024).decode()
    
    #print(rec2)
    print(rec1)
    success = (int(rec2) == 1)
conn.disconnect(s)