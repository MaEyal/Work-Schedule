from tkinter import *

def about():
    aboutwin = Toplevel()
    aboutwin.title("About Schedule Generator")
    aboutwin.geometry('200x200')
    about_label1 = Label(aboutwin, text = "Schedule generator was created by:", anchor = 'center')
    about_label2 = Label(aboutwin, text = "Eyal Magen", anchor = 'center')
    about_label3 = Label(aboutwin, text = "eyal517@gmail.com", anchor = 'center')
    about_label1.pack()
    about_label2.pack()
    about_label3.pack()