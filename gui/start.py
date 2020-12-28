from tkinter import * 
import time

window = Tk() #Open window
window.title('Capture the Flag')
window.geometry("300x300")
#To hide buttons
def hide(events, screen):
    for event in events:
        print(type(event))
        event.destroy()
    show(screen)

#home screen
def home():
    var = StringVar()
    label = Label(window, textvariable=var, relief=RAISED, height=3, font=64)
    start = Button(window, text = "Start", font=32, padx = 10, command=lambda: hide([start, label], 'menu'))
    #start['command'] = hide([start, label])

    var.set("Welcome to the CTF!")
    label.pack()
    start.pack(pady=100)

#Menu Screen    
def menu():
    var = StringVar()
    label = Label(window, textvariable=var, relief=RAISED, height=3, font=64)
    var.set("Pick your challenge!")
    dB = Button(window, text = "Download", font=32, padx=10, width=10, command = lambda: hide([label, dB, lB, fB],'download'))
    lB = Button(window, text = "Login", font=32, padx=10, width=10, command=lambda: hide([label, dB, lB, fB],'login'))
    fB = Button(window, text = "Flag", font=32, padx=10, width=10, command=lambda: hide([label, db, lb, fb],'flag'))
  
    label.pack()
    dB.pack(pady=(50,10))
    lB.pack(pady=10)
    fB.pack(pady=10)
    
def downloadScreen():
    print('Coming Soon')
    
def loginScreen():
    print('Coming Soon')

def flagScreen():
    print('Coming Soon')

#Shows the given screen
def show(screen):
    if (screen == 'home'):
        home()
    elif (screen == 'menu'):
        menu()
    elif (screen == 'download'):
        downloadScreen()
    elif (screen == 'login'):
        loginScreen()
    elif (screen == flag):
        flagScreen()


show('home')
#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )

window.mainloop()  