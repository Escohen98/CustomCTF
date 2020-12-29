import socket 
import time

class connection():
    conn = False
    @staticmethod #or put 'self' as an argument
    def isConnected(): #Returns whether or not the client is connected
        return connection.conn
           
    def connect(self, port):
        server = socket.socket()
        server.settimeout(5.0)
        host = socket.gethostname() #Might not be a bad idea to put into a config file
        print(f"host: {host} type: {type(host)}")
        print(f"port: {port} type: {type(port)}")
        server.connect((host,port))
        connection.conn = True
        return(server)
            
    def disconnect(self, server):
        server.shutdown(socket.SHUT_RDWR)
        server.close()
        print("Test connection closed.")
        connection.conn = False
    
        
    
    
    