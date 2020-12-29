import socket
from connection import connection

class testConnection() {
    
    #Tests if connection works and returns result
    def test(self, port) {
        conn = connection()
        conn.connect(self, port)
        
        connected = conn.isConnected()
        conn.disconnect()
        
        return(connected)
    }

}