from tkinter import *

root = Tk()
root.title("TITLE HERE")

def isChecked():
    if a.get() == 1 and b.get() == 0:
        root.geometry("1280x720")
    elif a.get() == 0 and b.get() == 1:
        root.geometry("1920x1080")
    elif a.get() == 0 and b.get() == 0:
        root.geometry("400x400")
    elif a.get() == 1 and b.get() == 1:
        root.geometry("4000x400")

a = IntVar()
b = IntVar()

cb1 = Checkbutton(root, text="720p", variable=a, onvalue=1, offvalue=0, command=isChecked).pack
cb2 = Checkbutton(root, text="1080p", variable=b, onvalue=1, offvalue=0, command=isChecked).pack

cb1.grid(row=0,column=0)
cb2.grid(row=1, column=0)

root.geometry("400x400")
root.mainloop()