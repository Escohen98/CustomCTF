import socket
from connection import connection

class testConnection():
    
    #Tests if connection works and returns result
    def test(self, port):
        conn = connection()
        connected = False
        print("Connecting...")
        server = conn.connect(port)
        
        connected = conn.isConnected()
        if(connected):
            conn.disconnect(server)
        return(connected)