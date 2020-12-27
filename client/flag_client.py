import socket

#Flag Client

#Connect to server
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))

success = False;
while not success: #Loops through until successful login
    s.sendall('flag'.encode('utf-8')) 
    flag = input("Flag: ")
    s.sendall(flag.encode('utf-8'))

    response = int(s.recv(1024).decode())
    if (response == 1): 
        print(s.recv(1024).decode())
        success = True;
    else:
        print(s.recv(1024).decode())
s.close()