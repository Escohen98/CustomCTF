# CustomCTF

##Setup
+ Install Python 3.7 or greater
+ Update pip `python -m pip install --upgrade pip`
+ Install tkinter if not already installed `python -m pip install --upgrade pip`
+ Open client and server settings.config and adjust based on needs
+ Run Server (python3 ./server/server.py) and Client (python3 ./client/start.py)

## Steps to Reproduce:
1. Nmap to find the port
2. Use the port to access the client
3. Ping server with response that has hidden credentials.
3. Sniff network to find unencrypted information
4. Login to account
5. Download encrypted message
6. Decrypt the message
7. Enter flag

## Easter Egg
1. Find server file
2. chmod into server source code
3. Find special code
4. Enter into flag

##Notes
* Technically a user could modify source code to get credentials without monitoring the network.

Copyright © Eric Cohen 2021
