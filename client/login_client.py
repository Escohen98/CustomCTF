import socket

#Login Client

#Connect to server
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))

success = False;
while not success: #Loops through until successful login
    s.sendall('login'.encode('utf-8')) 
    user = input("Username: ")
    password = input("Password: ")
    s.sendall(user.encode('utf-8'))
    s.sendall(password.encode('utf-8'))
    
    print(s.recv(1024).decode()) #Flag - Encrypted in rot-13
    success = (int(s.recv(1024).decode() == 1)
    
s.close()