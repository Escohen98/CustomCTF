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
    msg1 = s.recv(1024).decode()
    msg2 = s.recv(1024).decode()
    print(msg1)
    print(msg2)
    msg1 = ''
    msg2 = ''
    #response = (msg2) == 1)

s.close()

#cd Documents\Python\CustomCTF\client