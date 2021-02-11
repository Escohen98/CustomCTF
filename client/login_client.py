#Copyright © Eric Cohen 2021
import socket
#From connection import connection

#Login Client
class login():

    def check(self, user, password, s):

        if (not user or not password): #Fail-Safe
            return(("Please enter a username and password.", 0))
        elif ("~" in user or ":" in user or "~" in password or "~" in password):
            return (("Bad Character.", 0))
        s.sendall(f'login~{user}:{password}'.encode('utf-8'))
        rec = s.recv(1024).decode().split(":")

        return(rec)
