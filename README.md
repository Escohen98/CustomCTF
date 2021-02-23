# Capture the Flag for Informatics 310: Information Assurance and Cyber Security at the University of Washington

## Setup
+ Install Python 3.7 or greater
+ Update pip `python3 -m pip install --upgrade pip`(if this errors, do `python -m pip install --upgrade pip`)
+ Install tkinter if not already installed `pip3 install tkinter`(if this errors do `pip install tkinter`)
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
1. Find flag\_client file
2. chmod into source code
3. Find special flag
4. Enter into flag

## Notes
* Technically a user could modify source code to get credentials without monitoring the network.

Copyright © Eric Cohen 2021
