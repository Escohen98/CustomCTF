# Capture the Flag for Informatics 310: Information Assurance and Cyber Security at the University of Washington

## Setup
+ Install Python 3.7 or greater
+ Update pip `python3 -m pip install --upgrade pip`(if this errors, do `python -m pip install --upgrade pip`)
+ Install tkinter if not already installed `pip3 install tk`(if this errors do `pip install tk`)
+ Open client and server settings.config and adjust based on needs
+ Run Server (python3 ./server/server.py) and Client (python3 ./client/start.py)

## Challenge
<details> 
  
  <summary> Steps to Reproduce </summary> 
  
    1. Nmap to find the port<br>
    2. Use the port to access the client<br>
    3. Ping server with response that has hidden credentials<br>
    4. Sniff network to find unencrypted information<br>
    5. Login to account<br>
    6. Download encrypted message<br>
    7. Decrypt the message<br>
    8. Enter flag
  
</details>
  
<details>  
  
  <summary> Easter Egg </summary>
  
    1. Find flag_client file
    2. chmod into source code
    3. Find special flag
    4. Enter into flag
  
</details>

## Notes
* Technically a user could modify source code to get credentials without monitoring the network.
* The ping is actually a layer 2 TCP request instead of a layer 3 ICMP. The purpose is to add an unencrypted payload to the packets.

Copyright © Eric Cohen 2021
