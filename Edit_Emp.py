from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import EmployeeData
import Classes


def update_combo():
    global emp_list
    emp_list = EmployeeData.importList()
    combo.configure(value = values(emp_list))

def values(emp_list):
    y = ["0: Employee name"]
    for x in emp_list:
        y.append(str(x.employee_number) + ": " + x.name)
    return y



#Adding a new employee

def add_em():

    def add():
        try:
            k = int(weekly_shifts_entry.get())
            if len(name_entry.get()) > 0:
                EmployeeData.add_employee(name_entry.get(),weekly_shifts_entry.get())
                update_combo()
                win_add.destroy()
            else:
                messagebox.showerror('Saving Error', 'Invalid input')
        except:
            messagebox.showerror('Saving Error', 'Invalid input')

    win_add = Toplevel()
    win_add.geometry('300x250')
    win_add.title("Add Employee")
    frame_head = Frame(win_add)
    frame_head.pack()
    frame_body = Frame(win_add)
    frame_body.pack()
    headline = Label(frame_head, text="Add new employee", font="Ariel 14 bold underline").grid(row=0, column=0, pady=10)
    name_lbl = Label(frame_body, text="Employee name: ").grid(row=1, column=0, padx=10, pady=10)
    weekly_shifts_lbl = Label(frame_body, text="Number of weekly shifts: ").grid(row=2, column=0, padx=10, pady=10)
    name_entry = Entry(frame_body)
    name_entry.grid(row=1, column=1)
    weekly_shifts_entry = Entry(frame_body)
    weekly_shifts_entry.grid(row=2, column=1)
    add_btn = Button(frame_body, text="Add employee", command=add).grid(row=5, column=0, padx=10, pady=10)



def open_edit(edit_win):
    def del_emp():
        EmployeeData.delete_employee(int(combo.get().split(':')[0]))
        update_combo()
        cancel_op()
    def check_changes():
        try:
            int(weekly_shifts_entry.get())
            int(last_week_entry.get())
            int(saturdays_entry.get())
            return True
        except:
            messagebox.showerror('Saving Error', 'Invalid input')
            return False

    def save_changes():
        if check_changes() == True:
            changes = Classes.Employee(combo.get()[2:],weekly_shifts_entry.get(),last_week_entry.get(),
            saturdays_entry.get(),combo.get().split(':')[0],True if incharge_combo.get() == 'Yes' else False)
            EmployeeData.edit_employee(changes)
            update_combo()
            cancel_op()
        else:
            pass

    #After a choice of an employee, destroyes the text fields when canceling changes
    def cancel_op():
        num_value.destroy()
        weekly_shifts_entry.destroy()
        last_week_entry.destroy()
        saturdays_entry.destroy()
        incharge_combo.destroy()
        save_btn.destroy()
        cancel_btn.destroy()
        del_btn.destroy()
        combo.current(0)
        select_employee.configure(state = 'normal')

    #checking and openning the data of the chosen employee
    if combo.get().split(':')[0] > '0':
        select_employee.configure(state = 'disabled')
        emp_num = int(combo.get().split(':')[0])
        num_value = Label(edit_win, text=emp_list[emp_num - 1].employee_number)
        num_value.grid(row=3, column=1)
        weekly_shifts_entry = Entry(edit_win, justify='center')
        weekly_shifts_entry.grid(row=4, column=1)
        weekly_shifts_entry.insert(0, emp_list[emp_num - 1].num_of_shifts)
        last_week_entry = Entry(edit_win, justify='center')
        last_week_entry.grid(row=5, column=1)
        last_week_entry.insert(0, emp_list[emp_num - 1].last_week_nights)
        saturdays_entry = Entry(edit_win, justify='center')
        saturdays_entry.grid(row=6, column=1)
        saturdays_entry.insert(0, emp_list[emp_num - 1].saturdays)
        incharge_combo = Combobox(edit_win, values='Yes No', state='readonly', width = '17')
        incharge_combo.grid(row=7, column=1)
        incharge_combo.current(0 if emp_list[emp_num - 1].incharge == True else 1)
        save_btn = Button(edit_win, text="Save", command = save_changes)
        save_btn.grid(row=8, column=2)
        cancel_btn = Button(edit_win, text = "Cancel", command = cancel_op)
        cancel_btn.grid(row = 8, column = 1)
        del_btn = Button(edit_win, text = "Delete", command = del_emp)
        del_btn.grid(row = 8, column = 0)

    else: #Alert if no employee was chosen
        messagebox.showerror('Loading Error', 'Invalid employee')









def edit_em(edit_win):
    #Combobox for a choice of employees
    global combo
    global select_employee
    headline = Label(edit_win, text = "Edit Employees List", font = "Ariel 14 bold underline")
    headline.grid(row = 0, column = 1, pady = 10)
    combo = Combobox(edit_win, state = 'readonly')
    update_combo()
    choose_emp = Label(edit_win, text = "Choose employee: ")
    choose_emp.grid(row = 2 , column = 0, padx = 5)
    combo.grid(row = 2, column = 1)
    combo.current(0)
    select_employee = Button(edit_win, text = "Select", command = lambda: open_edit(edit_win))
    select_employee.grid(row = 2, column = 2)

    #Skeleton structure for the employee details
    num_lbl = Label(edit_win, text="Employee number: ").grid(row=3, column=0, padx=5, pady=10)
    weekly_shifts_lbl = Label(edit_win, text="Number of weekly shifts: ").grid(row=4, column=0, padx=5, pady=10)
    last_week_lbl = Label(edit_win, text="Last week's nights: ").grid(row=5, column=0, padx=10, pady=5)
    saturdays_lbl = Label(edit_win, text="Consecutive Saturdays: ").grid(row=6, column=0, padx=5, pady=10)
    incharge_lbl = Label(edit_win, text="Incharge: ").grid(row=7, column=0, padx=5, pady=10)
    add_btn = Button(edit_win, text="Add employee", command = add_em).grid(row=9, column=1, padx=5, pady=10)









