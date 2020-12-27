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
    if not flag:
        print("Please enter a value: ")
        continue
    s.sendall(flag.encode('utf-8'))

    rec1 = s.recv(1024).decode()
    rec2 = s.recv(1024).decode()
    
    #print(rec2)
    print(rec1)
    success = (int(rec2) == 1)
s.close()