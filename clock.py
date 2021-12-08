import time
from tkinter import *

def updateTime():
    now = time.strftime("%H:%M:%S")
    label.configure(text=now)
    window.after(1000, updateTime)

window = Tk()
window.title("clock")

label = Label(window,text="",font=('Comic Sans MS',40),background="cyan")
label.pack()

updateTime()

window.mainloop()