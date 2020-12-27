import socket

#Flag Client

#Connect to server
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))

success = False;
s.sendall('flag'.encode('utf-8')) 
while not success: #Loops through until successful login
    flag = input("Flag: ")
    s.sendall(flag.encode('utf-8'))
    #msg1 = 
    #msg2 = 
    print(s.recv(1024).decode('utf-8'))
    #print(s.recv(1024).decode('utf-8'))
    #msg1 = ''
    #msg2 = ''
    #response = (msg2) == 1)

s.close()

#cd Documents\Python\CustomCTF\client