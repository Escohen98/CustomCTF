#!./server.py

import socket
import os
import threading

s = socket.socket() #Socket object
def checkCreds(c,user, password): #checks if credentials are valid and sends result to client
    if not user or not password: #Ensure server doesn't crash on forced exit
        return(True)
    elif (user == 'spy' and password == 'pwnd'):
        c.sendall('It looks like the Spy has encrypted the message.\nPGS{eraqrmibhf_ng_erq_fdhner}'.encode('utf-8'))
        c.sendall('1'.encode('utf-8')) #Because I am too lazy to figure out how to send a boolean
        return(True)
    else: #Not necessary but I'm not risking it breaking again.
        c.sendall('Invalid username or password.'.encode('utf-8'))
        c.sendall('0'.encode('utf-8'))
        return(False)
    
def checkFlag(c,flag):
    if not flag: #Ensure server doesn't crash on forced exit
        return(True)
    if (flag == 'CTF{rendezvous_at_red_square}'):
        c.sendall('You win!'.encode('utf-8'))
        c.sendall('1'.encode('utf-8')) #Because I am too lazy to figure out how to send a boolean
        return(True)
    else: 
        c.sendall('Incorrect.'.encode('utf-8'))
        c.sendall('0'.encode('utf-8'))
        return(False)


def multi_threaded_client(c):
    while True:
        part = c.recv(1234).decode() #Either send file or login. 
        if (part == 'send'): #Part 1 - Download Files
            print(os.getcwd())
            #THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) #Cross-Platform compatibility
            #my_file = os.path.join(THIS_FOLDER, 'tosend.png') 
            file = open('tosend.pcap', 'rb') #Testing with png. Replace with pcap
            print('Sending File...')
            bits = file.read(1024)
            while bits: #Sends over file in pieces
                print('Sending...')
                c.sendall(bits)
                bits = file.read(1024)
            file.close()
            c.shutdown(socket.SHUT_WR) #Necessary to end buffer
        elif(part == 'login'): #Part 2 - Input Login Credentials
            auth = False
            while not auth:
                user = c.recv(1234).decode() #Receiving Username
                password = c.recv(1234).decode() #Receiving Password
                if(checkCreds(c,user, password)): #Breaks if true
                    auth = True
        elif (part == 'flag'): #Part 3 - Enter flag
            #Coming Soon.
            while True:
                flag = c.recv(1234).decode() #Receiving Flag
                if(checkFlag(c,flag)):
                    break
        else: #Should only have 3 options, but failsafe kill command
            print("Invalid. Shutting Down...")
            c.close()
            break

host = socket.gethostname() #Local Machine
port = 12345

try:
    s.bind((host, port)) #Binding host and port to socket
except socket.error as e:
    print(str(e))
x = 5
s.listen(x) #waiting for a connection can fail up to x times 
#ThreadCount = 0
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    threading.Thread(target=multi_threaded_client, args=(c,  ), daemon=True).start() #Starts the new thread
    #ThreadCount += 1
    #print('Thread Number: ' + str(ThreadCount))
s.close()