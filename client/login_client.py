import socket
#from connection import connection

#Login Client
class login():

    def check(self, user, password, s):

        #success = False;
        s.sendall('login'.encode('utf-8')) 
        #while not success: #Loops through until successful login 
        if not user or not password: #Fail-Safe
            #print("Please enter a username and password.")
            return(("Please enter a username and password.", 0))
            #continue
        s.sendall(user.encode('utf-8'))
        s.sendall(password.encode('utf-8'))
        
        rec1 = s.recv(2048).decode()
        rec2 = s.recv(2048).decode()
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