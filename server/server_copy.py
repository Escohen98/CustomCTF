#!./server.py

import socket

def checkCreds(user, password): #checks if credentials are valid and sends result to client
    if (user == 'spy' and password == 'pwnd'):
        c.sendall('1'.encode('utf-8')) #Because I am too lazy to figure out how to send a boolean
        return(True)
    c.sendall('1'.encode('utf-8'))
    return(False)

s = socket.socket() #Socket object
host = socket.gethostname() #Local Machine
port = 12345
s.bind((host, port)) #Binding host and port to socket
x = 5
s.listen(x) #waiting for a connection can fail up to x times 
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    output = 'Connection Successfully Established!'
    
    part = c.recv(1234).decode() #Either send file or login. 
    if (part == 'send'): #Part 1 - Download File
        file = open('tosend.png', 'rb') #Testing with png. Replace with pcap
        print('Sending File...')
        bits = file.read(1024)
        while bits: #Sends over file in pieces
            print('Sending...')
            s.send(bits)
            bits = file.read(1024)
        file.close()
        s.shutdown(socket.SHUT_WR) #Necessary to end buffer
    elif(part == 'login'): #Part 2 - Input Login Credentials
        auth = False;
        while True:
            user = c.recv(1234).decode() #Receiving Username
            password = c.recv(1234).decode() #Receiving Password
            if(checkCreds(user, password)): #Breaks if true
                break
    elif (part == 'flag'): #Part 3 - Enter flag
        #Coming Soon.
        print('Coming Soon.')
    else: #Should only have 3 options, but failsafe kill command
        print("Invalid. Shutting Down...")
        c.close()
        break
    c.sendall(output.encode('utf-8')) 
   # inpt = c.recv(1234).decode()
   # print(inpt)
        
   # if (inpt == 'kill'):
   #     print('Server shutting down ...')
   #     c.close()
   #     break