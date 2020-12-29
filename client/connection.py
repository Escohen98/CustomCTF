import socket 

class connection():
    conn = False
    @staticmethod #or put 'self' as an argument
    def isConnected(): #Returns whether or not the client is connected
        return connection.conn
           
    def connect(self, port):
        server = socket.socket()
        server.settimeout(5.0)
        host = socket.gethostname() #Might not be a bad idea to put into a config file
        server.connect((host,port))
        self.conn = True
        return(s)
            
    def disconnect(self, server):
        server.shutdown(socket.SHUT_RDWR)
        server.close()
        print ("Closed.")
        connection.conn = False
    
        
    
    
    