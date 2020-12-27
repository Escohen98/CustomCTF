import socket

#Login Client

#Connect to server
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))

success = False;
s.sendall('login'.encode('utf-8')) 
while not success: #Loops through until successful login
    
    user = input("Username: ")
    password = input("Password: ")
    if not user or not password:
        print("Please enter a username and password.")
        continue
    s.sendall(user.encode('utf-8'))
    s.sendall(password.encode('utf-8'))
    
    rec1 = s.recv(1024).decode()
    rec2 = s.recv(1024).decode()
    
    #print(rec2)
    print(rec1) #Flag - Encrypted in rot-13
    success = (int(rec2) == 1)
    
 
s.close()

#cd Documents\Python\CustomCTF\client