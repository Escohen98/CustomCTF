import socket
from connection import connection

#Flag Client
class flagCheck:

    #success = False;
    #while not success: #Loops through until successful login
    def check(self, flag, s): 
        #Connect to server
        #flag = input("Flag: ")
        if not flag:
            print("Please enter a value: ")
            return ["Please enter a value",0]
        elif ("~" in flag or ":" in flag):
            return (("Bad Character.", 0))
        elif(type(flag) == type(1)): #Stops injections / timeout
            str(flag)
         #s.sendall(flag.encode('utf-8'))

        try:
            print("here")
            s.sendall(f'flag~{flag}'.encode('utf-8')) 
        except socket.timeout:
            rec1 = 'Server Timed out. Please try again.'
            rec2 = '0'
            return [rec1, rec2]
        #Need to resolve socket timeout issue.
        try:
            rec = s.recv(1024).decode('utf-8').split(":")
            rec1 = rec[0]
            rec2 = rec[1]
           # rec1 = s.recv(1024).decode('utf-8') #Response
           # rec2 = s.recv(1024).decode('utf-8') #Response Code 
        except socket.timeout:
            rec1 = 'Server Timed out. Please try again.'
            rec2 = '0'
        
        #print(rec2)
        print(f"rec1: {rec1}")
        print(f"rec2: {rec2}")
        #success = (int(rec2) == 1)
        return [rec1, rec2]