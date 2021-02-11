#Copyright © Eric Cohen 2021
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
        try:
            while bits: #Importing File
                print('Receiving...')
                if not bits:
                    break
                f.write(bits)
                bits = s.recv(1024)
            print("Done.")
        except:
            print("Bad.")
        f.close()
