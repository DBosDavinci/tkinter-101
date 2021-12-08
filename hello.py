from tkinter import *

window = Tk()

window.title("hello")
window.config(bg='red')
window.geometry('200x200')

label = Label(window, text="Hello\nTkinter!",font=('Helvetica bold',15),bd=1,relief= "sunken",width=12,height=6,background="yellow",foreground="green").place(relx= 0.5,rely= 0.5,anchor= CENTER)

window.mainloop()