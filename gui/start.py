from tkinter import * 

window = Tk() #Open window
window.title('Capture the Flag')
window.geometry("300x300")

var = StringVar()
label = Label(window, textvariable=var, relief=RAISED, height=3)
start = Button(window, text = "Start")

var.set("Welcome to the CTF!")
label.pack()
start.pack()
#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )

window.mainloop()  