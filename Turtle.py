from tkinter import *

class Block:
    def __init__(self, mastert):
#        self.scrn =
        self.ent = Entry(mastert)
        self.but = Button(mastert, text="Преобразовать")
        self.lab = Label(mastert, bg='black', fg='white', relief=GROOVE)
        self.lab2 = Label(mastert, bg='black', fg='white', relief=RAISED)
        self.textb = Text(mastert, relief=SUNKEN)
        self.but['command'] = self.str_to_sort
        self.ent.pack(fill=BOTH)
        self.but.pack(fill=BOTH)
        self.lab.pack(fill=BOTH)
        self.lab2.pack(fill=BOTH)
        self.textb.pack(fill=BOTH)

    def str_to_sort(self):
        s = self.ent.get()
        s = s.split()
        s.sort()
        self.lab['text'] = ' '.join(s)
        self.lab2['text'] = ''.join(s)

root = Tk()
root2 = Tcl()

first_block = Block(root)
second_block = Block(root2)

root.mainloop()

