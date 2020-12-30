import socket
#from connection import connection

#Login Client
class login():

    def check(self, user, password, s):
        
        if (not user or not password): #Fail-Safe
            #print("Please enter a username and password.")
            return(("Please enter a username and password.", 0))
        elif ("~" in user or ":" in user or "~" in password or "~" in password):
            return (("Bad Character.", 0))
        s.sendall('login~'.encode('utf-8')) 
        
        s.sendall(user.encode('utf-8'))
        s.sendall(password.encode('utf-8'))
        
        rec1 = s.recv(1024).decode()
        rec2 = s.recv(1024).decode()
        return((rec1,rec2))
            #print(rec2)
            #print(rec1) #Flag - Encrypted in rot-13
            #success = (int(rec2) == 1)
            
         
        #conn.disconnect(s)

    # #debugging
    # def run(port):
        # user = input("Username: ")
        # password = input("Password: ")
        # main(user, password, port)
    # #run(12345)
#cd Documents\Python\CustomCTF\client