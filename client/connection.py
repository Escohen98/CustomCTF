class connection:
    conn = False

    def isConnected(): #Returns whether or not the client is connected
        return conn
        
    def connect():
        conn = True
        
    def disconnect():
        conn = False
        
    
    
    