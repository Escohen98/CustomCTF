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
    
    response = int(s.recv(1024).decode())
    if (response == 1): 
        print('It looks like the Spy has encrypted the message.')
        print('PGS{eraqrmibhf_ng_erq_fdhner}') #Flag - Encrypted in rot-13
        success = True;
    else:
        print("Invalid username or password")
s.close()