from tkinter import *
import random

window = Tk()

def grabbel():
    if len(items) > 0:
        item = items.pop(random.randrange(len(items)))
        recent.configure(text=f"Gefeliciteerd, je hebt {item} gegrabbeld!")
        totaal.configure(text=f"{str(len(items))} items over")
    elif len(items) <= 0:
        recent.configure(text="de grabbelton is leeg")

items = ["een appel","een pen","een snoepje","1 euro","een blikje cola","een banaan","een stuk papier","een fles water","een python script","een game"]

totaal = Label(window,text=f"{str(len(items))} items over")
totaal.pack()

recent = Label(window,text="")
recent.pack()

grabbelen = Button(window,text="grabbelen",command=grabbel)
grabbelen.pack()

window.mainloop()