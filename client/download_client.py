import socket
import time
import json

class downloader():
    #Download Client
    def download(self, s):
        with open("./settings.json") as f:
            data = json.load(f)
        s.sendall('send'.encode('utf-8'))
        filepath = data["file"]["path"]+data["file"]["name"]
        f = open(filepath, 'wb')
        print('\nReceiving...')
        bits = s.recv(1024)
        while bits: #Importing File
            print('Receiving...')
            if not bits:
                break
            f.write(bits)
            bits = s.recv(1024)
        f.close()

# connected = False; #Checks if client is connected to server
# while not connected: #Loops until connected to server
    # try: #Attempting Connection
        # s = socket.socket()
        # s.settimeout(5.0)
        # host = socket.gethostname()
        # port = int(input('Enter port: '))
        # s.connect((host, port))
        # s.sendall('send'.encode('utf-8'))
        # f = open('torecv.png', 'wb') #Opening File Buffer
        # download(s)
        # connected = True
    # except Exception as err: #If fail to connect, notify user
        # print('Incorrect Socket. Please try again.')
        # time.sleep(1)
# print(s.recv(1024).decode())

# s.close()

    #cd Documents\Python\CustomCTF\client
