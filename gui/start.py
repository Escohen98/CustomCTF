from tkinter import * 
import time

window = Tk() #Open window
window.title('Capture the Flag')
window.geometry("300x300")
#To hide buttons
def hide(events):
    for event in events:
        print(type(event))
        event.destroy()

#home screen
def home():
    var = StringVar()
    label = Label(window, textvariable=var, relief=RAISED, height=3, font=64)
    start = Button(window, text = "Start", font=32, padx = 10, command=lambda: hide([start, label]))
    #start['command'] = hide([start, label])

    var.set("Welcome to the CTF!")
    label.pack()
    start.pack(pady=100)

#Menu Screen    
def menu():
    print('Coming Soon')
    
def downloadScreen():
    print('Coming Soon')
    
def loginScreen():
    print('Coming Soon')

def flagScreen():
    print('Coming Soon')


home()
#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )

window.mainloop()  