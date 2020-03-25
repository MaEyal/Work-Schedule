import about
from Edit_Emp import edit_em
from EditSchedule import edit_sc
from Generate import generate
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

#Generate new schedule
def gen_sch():
    root.withdraw()
    global win
    win = Toplevel()
    win.title("Generate Schedule")
    win.geometry('880x460')
    generate(win)
    win.protocol("WM_DELETE_WINDOW", close_win)


#Edit existing schedule
def edit_schedule():
    root.withdraw()
    global win
    win = Toplevel()
    win.title("Edit Schedule")
    win.geometry('650x450')
    edit_sc(win)
    win.protocol("WM_DELETE_WINDOW", close_win)


#Edit employees window
def edit_e():
    root.withdraw()
    global win
    win = Toplevel()
    win.title("Edit Employees")
    win.geometry('420x420')
    edit_em(win)
    win.protocol("WM_DELETE_WINDOW", close_win)

#closses windows for all options except 'about'
def close_win():
    win.destroy()
    root.deiconify()

root.title("Work Schedule Generator")
root.geometry('200x300')
headline = Label(root, text = 'Work Schedule Generator', padx=5, pady=5, font = "Ariel 11 underline bold")
headline.grid(row =2, column = 1)
btn1 = Button(root, text = "Generate Schedule",  width = 18, height = 2, font = "Ariel 11", command = gen_sch)
btn2 = Button(root, text = "Load Current Schedule",  width = 18, height = 2, font = "Ariel 11", command = edit_schedule)
btn3 = Button(root, text = "Edit Employee List",  width = 18, height = 2, font = "Ariel 11", command = edit_e)
btn4 = Button(root, text = "About",  width = 18, height = 2, command = about.about, font = "Ariel 11")

btn1.grid(row = 4, column = 1, padx = 10, pady =10)
btn2.grid(row = 5, column = 1, padx = 10, pady =10)
btn3.grid(row = 6, column = 1, padx = 10, pady =10)
btn4.grid(row = 7, column = 1, padx = 10, pady =10)

root.mainloop()
