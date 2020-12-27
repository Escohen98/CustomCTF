import socket
import os

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
    if (part == 'send'): #Part 1 - Download Files
        print(os.getcwd)
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) #Cross-Platform compatibility
        my_file = os.path.join(THIS_FOLDER, 'tosend.png') 
        file = open(r''+ my_file, 'rb') #Testing with png. Replace with pcap
        print('Sending File...')
        bits = file.read(1024)
        while bits: #Sends over file in pieces
            print('Sending...')
            s.send(bits)
            bits = file.read(1024)
        file.close()
        s.shutdown(socket.SHUT_WR) #Necessary to end buffer
c.close()