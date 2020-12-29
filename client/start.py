from tkinter import * 
from testConn import testConnection
from download_client import downloader

window = Tk() #Open window
window.title('Capture the Flag')
window.geometry("300x300")
window.resizable(width=False, height=False)
connTest = testConnection()

PORT = 0

#Changes global port
def setPort(port):
    global PORT
    PORT = port

#Gets global port
def getPort():
    return(PORT)
    
#Checks if port is valid 
def checkPort(port):
    if(connTest.test(port)): 
        return(True)
    return(False)
    
#Message when entering a screen with the incorrect port
def portNotFound():
    var = StringVar()
    label = Label(window, textvariable=var, font=128, padx=10, width=10)
    var.set("Port not found!")
    back = Button(window, text = "Back", font=32, padx=10, widt=10, command= lambda: hide([label, back], 'menu'))
    
    label.pack(pady=(100,0))
    back.pack(pady=(100,0))

#To hide screens
def hide(events, screen):
    for event in events:
        event.destroy()
    show(screen)

#home screen
def home():
    var = StringVar()
    label = Label(window, textvariable=var, height=3, font=64)
    start = Button(window, text = "Start", font=32, padx = 10, command=lambda: hide([start, label], 'port'))
    #start['command'] = hide([start, label])

    var.set("Welcome to the CTF!")
    label.pack()
    start.pack(pady=100)

#Must enter port before moving to menu screen
def portScreen():
    submit = Button(window, text = "Submit", font=32, padx = 10, command=lambda: portScreenTransition(int(eP.get()),[lP, eP, submit]))
    lP = Label(window, text="Port:")
    eP = Entry(window, bd = 2)
    
    submit.pack(side = BOTTOM, pady=(20,20))
    lP.pack(side = LEFT, padx=(75,0))
    eP.pack(side = RIGHT, padx=(0,75))
    #print("Coming Soon")

#Too many middleman functions ... but be an easier way.
def portScreenTransition(port, entries):
    if(checkPort(port)):
        setPort(port)
        print(PORT)
        hide(entries,'menu')
    else:
        print("Invalid port message here")
#Menu Screen    
def menu():
    var = StringVar()
    label = Label(window, textvariable=var, height=3, font=64)
    var.set("Pick your challenge!")
    dB = Button(window, text = "Download", font=32, padx=10, width=10, command = lambda: hide([label, dB, lB, fB],'download'))
    lB = Button(window, text = "Login", font=32, padx=10, width=10, command=lambda: hide([label, dB, lB, fB],'login'))
    fB = Button(window, text = "Flag", font=32, padx=10, width=10, command=lambda: hide([label, dB, lB, fB],'flag'))
  
    label.pack()
    dB.pack(pady=(50,10))
    lB.pack(pady=10)
    fB.pack(pady=10)
    
def downloadScreen():
    print(getPort())
    portCheck = checkPort(getPort())
    if(portCheck): #Change to isConnected
        var = StringVar()
        label = Label(window, textvariable=var, height=3, font=64)
        download = Button(window, text = "Download", font=32, padx = 10, pady = 10, command=lambda: hide([download, label], 'menu'))
        var.set("Click to download the pcap file")
        label.pack()
        download.pack(pady=100)
    else:
        portNotFound()
    
def toDownload():
    downloader().download()
    
def loginScreen():
    if(checkPort(getPort())): #Change to isConnected
        print("Coming Soon")
    else:
        portNotFound()

def flagScreen():
    if(checkPort(getPort())): #Change to isConnected
        print("Coming Soon")
    else:
        portNotFound()

#Shows the given screen
def show(screen):
    print("Screen: ", screen)
    if (screen == 'home'):
        home()
    elif (screen == 'port'):
        portScreen()
    elif (screen == 'menu'):
        menu()
    elif (screen == 'download'):
        downloadScreen()
    elif (screen == 'login'):
        loginScreen()
    elif (screen == 'flag'):
        flagScreen()

show('home')
#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )

window.mainloop()  