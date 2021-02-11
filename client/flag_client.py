#Copyright © Eric Cohen 2021
import socket
from connection import connection

#Flag Client
class flagCheck:

    #success = False;
    #while not success: #Loops through until successful login
    def check(self, flag, s):
        #Connect to server
        if not flag:
            print("Please enter a value: ")
            return ["Please enter a value",0]
        elif ("~" in flag or ":" in flag):
            return (("Bad Character.", 0))
        elif(type(flag) == type(1)): #Stops injections / timeout
            str(flag)
         #picoCTF{H@ppy_3@st3r!}
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
        except socket.timeout:
            rec1 = 'Server Timed out. Please try again.'
            rec2 = '0'

        print(f"rec1: {rec1}")
        print(f"rec2: {rec2}")

        return [rec1, rec2]
