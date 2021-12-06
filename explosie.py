import tkinter

window = tkinter.Tk()

window.title("My First Window")
window.geometry('50x50')
window.configure(bg='white')
print(6)
count = 2

def updateWindow():
    global count
    size = 50 * count
    window.geometry(f'{size}x{size}')
    if count == 2:
        window.configure(bg='yellow')
        print(5)
    elif count == 3:
        window.configure(bg='orange')
        print(4)
    elif count == 4:
        window.configure(bg='red')
        print(3)
    elif count == 5:
        window.configure(bg='purple')
        print(2)
    elif count == 6:
        window.configure(bg='black')
        print(1)
    count+=1

def explosion():
    print("BOOM!")
    window.destroy()

window.after(2000, updateWindow)
window.after(4000, updateWindow)
window.after(6000, updateWindow)
window.after(8000, updateWindow)
window.after(10000, updateWindow)
window.after(12000, explosion)

window.mainloop()