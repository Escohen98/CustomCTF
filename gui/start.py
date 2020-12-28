from tkinter import * 
import time

window = Tk() #Open window
window.title('Capture the Flag')
window.geometry("300x300")

port = 0

def setPort(port):
    port = port

def getPort():
    return port
    
#To hide buttons
def hide(events, screen):
    for event in events:
        event.destroy()
    show(screen)

#home screen
def home():
    var = StringVar()
    label = Label(window, textvariable=var, height=3, font=64)
    start = Button(window, text = "Start", font=32, padx = 10, command=lambda: hide([start, label], 'menu'))
    #start['command'] = hide([start, label])

    var.set("Welcome to the CTF!")
    label.pack()
    start.pack(pady=100)

#Must enter port before moving to menu screen
def portScreen():
    print("Coming Soon")

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
    if(port == 0): #Change to isConnected
        var = StringVar()
        label = Label(window, textvariable=var, font=128, padx=10, width=10)
        var.set("Port not found!")
        back = Button(window, text = "Back", font=32, padx=10, widt=10, command= lambda: hide([label, back], 'menu'))
        
        label.pack(pady=(100,0))
        back.pack(pady=(100,0))
    else:
        print('Coming Soon')
    
def loginScreen():
    if(port == 0): #Change to isConnected
        var = StringVar()
        label = Label(window, textvariable=var, font=128, padx=10, width=10)
        var.set("Port not found!")
        back = Button(window, text = "Back", font=32, padx=10, widt=10, command= lambda: hide([label, back], 'menu'))
        
        label.pack(pady=(100,0))
        back.pack(pady=(100,0))
    else:
        print('Coming Soon')

def flagScreen():
    if(port == 0): #Change to isConnected
        var = StringVar()
        label = Label(window, textvariable=var, font=128, padx=10, width=10)
        var.set("Port not found!")
        back = Button(window, text = "Back", font=32, padx=10, widt=10, command= lambda: hide([label, back], 'menu'))
        
        label.pack(pady=(100,0))
        back.pack(pady=(100,0))
    else:
        print('Coming Soon')

#Shows the given screen
def show(screen):
    print("Screen: ", screen)
    if (screen == 'home'):
        home()
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