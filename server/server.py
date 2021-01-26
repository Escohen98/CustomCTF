#!./server.py
#If you're here, that means you know something
#that hasn't been taught yet
#Congratulations!! Here's your special code: h4v3_4_c00k13

import socket
import os
import threading
import json

#Builds JSON. Can't make global due to threads.
def getJSON() {
    with open('./settings.json') as f:
        data = json.load(f)
    return(data)
}

s = socket.socket() #Socket object
def checkCreds(c,user, password): #checks if credentials are valid and sends result to client
    data = getJSON()
    if not user or not password: #Ensure server doesn't crash on forced exit
        return(True)
    elif (user == data["login"]["user"] and password == data["login"]["pass"]):
        c.sendall('It looks like the Spy\n has encrypted the message.\n\nPGS{eraqrmibhf_ng_erq_fdhner}:1'.encode('utf-8'))
        return(True)
    else: #Not necessary but I'm not risking it breaking again.
        c.sendall('Invalid username or password.:0'.encode('utf-8'))
        return(False)

def checkFlag(c,flag):
    print(f"flag: {flag}")
    if not flag: #Ensure server doesn't crash on forced exit
        c.sendall('Please enter a value.:0'.encode('utf-8'))
        return(False)
    elif (flag == 'CTF{rendezvous_at_red_square}'):
        c.sendall('You win!:1'.encode('utf-8'))
        return(True)
    c.sendall('Incorrect.:0'.encode('utf-8'))
    return(False)



#Moving the buffer stream to its own file.
def upload(c):
    data = getJSON() #Probably could put this in multi_thread, but lazy
    print(os.getcwd())
    #THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) #Cross-Platform compatibility
    #my_file = os.path.join(THIS_FOLDER, 'tosend.png')
    file = open(data["file"]["path"]+data["file"]["name"], 'rb') #Testing with png. Replace with pcap
    print('Sending File...')
    bits = file.read(1024)
    while bits: #Sends over file in pieces
        print('Sending...')
        c.sendall(bits)
        bits = file.read(1024)
    file.close()
    print("Done.")
    c.shutdown(socket.SHUT_WR) #Necessary to end buffer
    break

def multi_threaded_client(c):
    while True:
        partSplit = c.recv(1234).decode().split("~") #Necessary for flag and login
        part = partSplit[0] #The whicever screen is in use
        extrasplit = '' #Prevent an unnecessary error
        if(len(partSplit) == 2):
            extrasplit = partSplit[1]
        print(f"part: {part}")
        if (part == 'send'): #Part 1 - Download Files
            upload(c);
        elif(part == 'login'): #Part 2 - Input Login Credentials
            auth = False
            #while not auth:
            split = extrasplit.split(":") #username:password
            checkCreds(c,split[0], split[1]) #Breaks if true
            break
        elif (part == 'flag'): #Part 3 - Enter flag
            #flag = c.recv(1234).decode() #Receiving Flag
            checkFlag(c,extrasplit)
            break
        else: #Should only have 3 options, but failsafe kill command
            print(part)
            print("Invalid Page. Thread Shutting Down...")
            c.close()
            break

host = socket.gethostname() #Local Machine
port = getJSON()["port"]

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
