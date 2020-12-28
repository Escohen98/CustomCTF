import socket
from connection import connection

#Login Client

def main(port):
    #Connect to server
    conn = connection()
    s = conn.connect(port)

    success = False;
    s.sendall('login'.encode('utf-8')) 
    while not success: #Loops through until successful login
        
        user = input("Username: ")
        password = input("Password: ")
        if not user or not password: #Fail-Safe
            print("Please enter a username and password.")
            continue
        s.sendall(user.encode('utf-8'))
        s.sendall(password.encode('utf-8'))
        
        rec1 = s.recv(1024).decode()
        rec2 = s.recv(1024).decode()
        
        #print(rec2)
        print(rec1) #Flag - Encrypted in rot-13
        success = (int(rec2) == 1)
        
     
    conn.disconnect(s)


def run(port):
    main(port)
run(12345)
#cd Documents\Python\CustomCTF\client