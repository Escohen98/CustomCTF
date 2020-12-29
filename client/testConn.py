import socket
from connection import connection

class testConnection():
    
    #Tests if connection works and returns result
    def test(self, port):
        conn = connection()
        server = conn.connect(port)
        
        connected = conn.isConnected()
        conn.disconnect(server)
        return(connected)