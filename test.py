from tkinter import *

# loading Python Imaging Library
from PIL import ImageTk, Image

# To get the dialog box to open when required
from tkinter import filedialog


def open_img():
    # Select the Imagename  from a folder
    x = openfilename()

    # opens the image
    img = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    img = img.resize((1280, 720), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # create a label
    panel = Label(root, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=2)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='"pen')
    return filename


# Create a window
root = Tk()

a = IntVar()
b = IntVar()
c = Checkbutton(root, text = "720p", variable = a).pack
c.place(relx=0.5, rely=0.04, anchor=CENTER)
c1 = Checkbutton(root, text = "1080p", variable = b).pack
c1.place(relx=0.5, rely=0.04, anchor=CENTER)

# Set Title as Image Loader
root.title("VINTOOL")


# Allow Window to be resizable
root.resizable(width=False, height=False)


# Create a button and place it into the window using grid layout
btn = Button(root, text='open image', command=open_img)
btn.place(relx=0.5, rely=0.02, anchor=CENTER)

root.geometry("1280x720")
root.mainloop()


