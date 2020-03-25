from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import EmployeeData
import Classes
from Edit_Emp import values
import copy



def generate(gen_win):
    def generate_scheudle(new_emp_list, shifts, weekly_rest):
        def checks():
            #checking if the employee is not already in current shift, previous shift or next shift
            if shifts_sorted[x].shift_num%2 == 0:
                shifts_check = []
                i = -4
                while i < 6:
                    if shifts_sorted[x].shift_num + i > 41:
                        pass
                    else:
                        shifts_check.append(weekly_rest[shifts_sorted[x].shift_num + i])
                    i += 1
                if new_emp_list[count].employee_number in shifts_check:
                    return False
            else:
                shifts_check = []
                i = -5
                while i < 5:
                    if shifts_sorted[x].shift_num + i > 41:
                        pass
                    else:
                        shifts_check.append(weekly_rest[shifts_sorted[x].shift_num + i])
                    i += 1
                if new_emp_list[count].employee_number in shifts_check:
                    return False

            #Checking if the employee has not yet exceeded the limitation of 7 nights per 2 weeks
            if (shifts_sorted[x].shift_num%6 == 4 or shifts_sorted[x].shift_num%6 ==5) and new_emp_list[count].last_week_nights + 1 == 8:
                return False
            if new_emp_list[count].num_of_shifts == 0:
                return False
            return True

        def sort_by_weeklyshifts(elem):
            return elem.weekly_rest_num

        def sort_by_amount(elem):
            return elem.num_of_shifts


        new_emp_list = sorted(new_emp_list, key = sort_by_weeklyshifts)
        shifts_sorted = []
        for x in range(42):
            shifts_sorted.append(Classes.Shift(x,len(shifts[x]),copy.deepcopy(shifts[x])))
        shifts_sorted = sorted(shifts_sorted, key = sort_by_amount)

        for x in range(0,42,2):
            if weekly_rest[shifts_sorted[x].shift_num] == 0:
                found = False
                count = 0
                while found == False and count < len(new_emp_list):
                    if new_emp_list[count].employee_number in shifts_sorted[x].list_of_employees:
                        if checks():
                            weekly_rest[shifts_sorted[x].shift_num]= new_emp_list[count].employee_number
                            new_emp_list[count].num_of_shifts -= 1
                            found = True
                            if (shifts_sorted[x].shift_num%6 == 4 or shifts_sorted[x].shift_num%6 ==5):
                                new_emp_list[count].last_week_nights += 1
                            new_emp_list[count].weekly_rest_num -= 1
                            while count<len(new_emp_list)-1 and new_emp_list[count].weekly_rest_num <= new_emp_list[count+1].weekly_rest_num:
                                temp = new_emp_list[count]
                                new_emp_list[count] = new_emp_list[count+1]
                                new_emp_list[count+1] = temp
                                count += 1
                    count += 1

        for x in range(1,42,2):
            if weekly_rest[shifts_sorted[x].shift_num] == 0:
                found = False
                count = 0
                while found == False and count < len(new_emp_list):
                    if new_emp_list[count].employee_number in shifts_sorted[x].list_of_employees:
                        if checks():
                            weekly_rest[shifts_sorted[x].shift_num]= new_emp_list[count].employee_number
                            new_emp_list[count].num_of_shifts -= 1
                            found = True
                            if (shifts_sorted[x].shift_num%6 == 4 or shifts_sorted[x].shift_num%6 ==5):
                                new_emp_list[count].last_week_nights += 1
                        while count < len(new_emp_list) - 1 and new_emp_list[count].weekly_rest_num <= new_emp_list[
                            count + 1].weekly_rest_num:
                            temp = new_emp_list[count]
                            new_emp_list[count] = new_emp_list[count + 1]
                            new_emp_list[count + 1] = temp
                            count += 1
                    count +=1

        ###########################################################################################
        new_schedule = Toplevel()
        new_schedule.geometry('650x400')
        headline_personal = Label(new_schedule, font='Ariel 14 bold underline', justify='center', text="Schedule")
        headline_personal.grid(row=0, pady=5)


        # main frame for hand picking shifts
        frame_body = Frame(new_schedule, relief='groove', width=500, height=500)
        frame_body.grid(row=2, padx=10, pady=10)

        # frame for the days of the week on top
        frame_body_head = Frame(frame_body, relief='groove')
        frame_body_head.grid(row=0, column=1)
        lbl_sun = Label(frame_body_head, text="Sunday").grid(row=0, column=1, padx=10, pady=10)
        lbl_mon = Label(frame_body_head, text="Monday").grid(row=0, column=2, padx=10, pady=10)
        lbl_teu = Label(frame_body_head, text="Tuesday").grid(row=0, column=3, padx=10, pady=10)
        lbl_wed = Label(frame_body_head, text="Wednesday").grid(row=0, column=4, padx=10, pady=10)
        lbl_thu = Label(frame_body_head, text="Thursday").grid(row=0, column=5, padx=10, pady=10)
        lbl_fri = Label(frame_body_head, text="Friday").grid(row=0, column=6, padx=10, pady=10)
        lbl_sat = Label(frame_body_head, text="Saturday").grid(row=0, column=7, padx=10, pady=10)

        # frame for days and positions
        frame_body_left = Frame(frame_body, relief='groove')
        frame_body_left.grid(row=2, column=0, sticky='w')
        lbl_mor = Label(frame_body_left, text="Morning:").grid(row=0, column=0, padx=10, pady=10)
        lbl_after = Label(frame_body_left, text="Afternoon:").grid(row=2, column=0, padx=10, pady=10)
        lbl_eve = Label(frame_body_left, text="Night:").grid(row=4, column=0, padx=10, pady=10)
        for x in range(0, 5, 2):
            lbl_incharge = Label(frame_body_left, text="Incharge")
            lbl_patrol = Label(frame_body_left, text="Patrol")
            lbl_incharge.grid(row=x, column=1, padx=2, pady=2)
            lbl_patrol.grid(row=x + 1, column=1, padx=2, pady=2)

        # Creates and places a weekly restrictions table for the supervisor to hand pick
        frame_body_main = Frame(frame_body, relief='groove')
        frame_body_main.grid(row=2, column=1)

        row1 = 0
        column1 = 0
        for x in range(0, 42,2):
            def emp_lbl(y):
                if weekly_rest[y]-1<0:
                    return " "
                else:
                    return emp_list[weekly_rest[y]-1].name
            incharge_lbl = Label(frame_body_main, text = emp_lbl(x), width = 10, anchor = 'center')
            incharge_lbl.grid(row=row1, column=column1, padx=2, pady=5)
            incharge_lbl = Label(frame_body_main, text=emp_lbl(x+1), width = 10, anchor = 'center')
            incharge_lbl.grid(row=row1+1, column=column1, padx=2, pady=5)
            row1 += 2
            if row1 % 6 == 0:
                row1 = 0
                column1 += 1


        cnl_btn = Button(new_schedule, text = "cancel", command = new_schedule.destroy)
        cnl_btn.grid(row = 4, column = 0, pady = 15)
        export_btn = Button(new_schedule, text = "Save & Export", command = lambda : EmployeeData.save_export(weekly_rest, emp_list))
        export_btn.grid(row =3, column = 0, pady= 10)


        ###########################################################################################




    # insterting the employees restrictions to the variable shifts
    def personal_rest():

            def close_win():
                combo.configure(state='normal')
                select_btn.config(state='normal')
                emp_rest.destroy()


            combo.configure(state='disabled')
            select_btn.config(state = 'disabled')
            # saving the shifts input on an employee to the master list of restrictions
            def save_shifts():

                weekly_counter = 0
                for x in range(21):
                    if combo_shifts[x].get() == 'Yes':
                        if emp_list[employee_number-1].saturdays == 3 and (x>15 and x<20):
                            continue
                        if employee_number not in  shifts[x*2+1]:
                            shifts[x*2+1].append(employee_number)
                            weekly_counter += 1
                            if (emp_list[employee_number-1].incharge == True):
                                shifts[x*2].append(employee_number)
                                weekly_counter += 1
                    else:
                        if employee_number in shifts[x*2+1]:
                            shifts[x*2+1].remove(employee_number)
                            if (emp_list[employee_number-1].incharge == True):
                                shifts[x*2].remove(employee_number)
                emp_list[employee_number-1].weekly_rest_num = weekly_counter
                combo.configure(state = 'normal')
                select_btn.config(state='normal')
                emp_rest.destroy()



            emp_rest = Toplevel()
            emp_rest.geometry('600x300')
            emp_rest.title("Personal Employee Restrictions")
            employee_number = int(combo.get().split(':')[0])
            headline_personal = Label(emp_rest, font = 'Ariel 14 bold underline', justify='center', text=combo.get()[2:])
            headline_personal.grid(row=0, pady=5)

            # frame for the days of the week on top
            frame_body = Frame(emp_rest, relief='groove')
            frame_body.grid(row=1, pady=10, padx=10)
            frame_body_head = Frame(frame_body, relief = 'groove')
            frame_body_head.grid(row = 0, column = 1)
            lbl_sun = Label(frame_body_head, text="Sunday").grid(row=0, column=1, padx=10, pady=10)
            lbl_mon = Label(frame_body_head, text="Monday").grid(row=0, column=2, padx=10, pady=10)
            lbl_teu = Label(frame_body_head, text="Tuesday").grid(row=0, column=3, padx=10, pady=10)
            lbl_wed = Label(frame_body_head, text="Wednesday").grid(row=0, column=4, padx=10, pady=10)
            lbl_thu = Label(frame_body_head, text="Thursday").grid(row=0, column=5, padx=10, pady=10)
            lbl_fri = Label(frame_body_head, text="Friday").grid(row=0, column=6, padx=10, pady=10)
            lbl_sat = Label(frame_body_head, text="Saturday").grid(row=0, column=7, padx=10, pady=10)

            # frame for the comboboxes
            frame_body_left = Frame(frame_body, relief='groove')
            frame_body_left.grid(row=1, column=0, sticky='w')
            lbl_mor = Label(frame_body_left, text="Morning:").grid(row=0, column=0, padx=10, pady=10)
            lbl_after = Label(frame_body_left, text="Afternoon:").grid(row=2, column=0, padx=10, pady=10)
            lbl_eve = Label(frame_body_left, text="Night:").grid(row=4, column=0, padx=10, pady=10)

            frame_body_right = Frame(frame_body)
            frame_body_right.grid(row=1, column=1)

            combo_shifts = []
            row2 = 0
            column2 = 0
            for x in range(21):
                shift_box = Combobox(frame_body_right, values='" " Yes', width = 5)
                shift_box.current(0)
                combo_shifts.append(shift_box)
                combo_shifts[x].grid(row= row2, column=column2, padx=7, pady=8)
                if int(combo.get().split(':')[0]) in shifts[x*2+1] or int(combo.get().split(':')[0]) in shifts[x*2]:
                    combo_shifts[x].current(1)
                row2 += 1
                if row2%3 == 0:
                    row2 = 0
                    column2 +=1

            save_btn = Button(emp_rest, text = 'save', command = save_shifts)
            save_btn.grid(row = 2, pady = 8)
            emp_rest.protocol("WM_DELETE_WINDOW", close_win)


    # Checking the restrictions of maximum 3 consecutive Saturdays and up to 7 nights per week
    # For the hand picked restrictions
    def check_restrictions():
        new_emp_list = copy.deepcopy(emp_list)
        weekly_rest = []
        for x in range(42):
            weekly_rest.append(int(restrictions[x].get().split(':')[0]))
            if (x%6 == 4 or x%6 == 5) and int(restrictions[x].get().split(':')[0]) != 0:
                if new_emp_list[int(restrictions[x].get().split(':')[0]) - 1].last_week_nights + 1 == 8:
                    messagebox.showerror('Restrictions Error',
                                         new_emp_list[int(restrictions[x].get().split(':')[0]) - 1].name + " cannot work more than"
                                                                                                " 7 nights per 2 weeks")
                    return
                else:
                    new_emp_list[int(restrictions[x].get().split(':')[0]) - 1].last_week_nights += 1
            elif (x>31 and x<40) and (int(restrictions[x].get().split(':')[0]) != 0):
                if new_emp_list[int(restrictions[x].get().split(':')[0]) - 1].saturdays + 1 == 4:
                    messagebox.showerror('Restrictions Error', new_emp_list[int(
                        restrictions[x].get().split(':')[0]) - 1].name + " cannot work more than 3 consecutive Saturdays")
                    return
            if int(restrictions[x].get().split(':')[0]) > 0:
                if new_emp_list[int(restrictions[x].get().split(':')[0])-1].num_of_shifts > 0:
                    new_emp_list[int(restrictions[x].get().split(':')[0]) - 1].num_of_shifts -= 1
            else:
                pass
        for x in range(4):
            if int(last_week[x].get().split(':')[0]) == 0:
                messagebox.showerror('Restrictions Error', " Last Saturday shifts fields must be filled")
                return
            weekly_rest.append(int(last_week[x].get().split(':')[0]))
        generate_scheudle(new_emp_list, shifts, weekly_rest)




    #main part of generating the schedule
    emp_list = EmployeeData.importList()



    headline = Label(gen_win, text="Generate New Schedule", font="Ariel 14 bold underline", justify = 'center')
    headline.grid(row=0, pady=10)
    select_emp = Label(gen_win, text = "Restrictions", font = "Ariel 12 bold underline")
    select_emp.grid(row = 1, column = 0, padx = 10, pady = 10)


    #main frame for hand picking shifts
    frame_body = Frame(gen_win, relief = 'groove', width = 500, height = 500)
    frame_body.grid(row =2, padx = 10, pady = 10)

    #frame for the days of the week on top
    frame_body_head = Frame(frame_body, relief = 'groove')
    frame_body_head.grid(row =0, column = 1)
    lbl_sun = Label(frame_body_head, text="Sunday").grid(row=0, column=1, padx=10, pady=10)
    lbl_mon = Label(frame_body_head, text="Monday").grid(row=0, column=2, padx=10, pady=10)
    lbl_teu = Label(frame_body_head, text="Tuesday").grid(row=0, column=3, padx=10, pady=10)
    lbl_wed = Label(frame_body_head, text="Wednesday").grid(row=0, column=4, padx=10, pady=10)
    lbl_thu = Label(frame_body_head, text="Thursday").grid(row=0, column=5, padx=10, pady=10)
    lbl_fri = Label(frame_body_head, text="Friday").grid(row=0, column=6, padx=10, pady=10)
    lbl_sat = Label(frame_body_head, text="Saturday").grid(row=0, column=7, padx=10, pady=10)

    #frame for days and positions
    frame_body_left = Frame(frame_body, relief = 'groove')
    frame_body_left.grid(row = 2, column = 0, sticky = 'w')
    lbl_mor = Label(frame_body_left, text="Morning:").grid(row=0, column=0, padx=10, pady=10)
    lbl_after = Label(frame_body_left, text="Afternoon:").grid(row=2, column=0, padx=10, pady=10)
    lbl_eve = Label(frame_body_left, text="Night:").grid(row=4, column=0, padx=10, pady=10)
    for x in range(0,5,2):
        lbl_incharge = Label(frame_body_left, text = "Incharge")
        lbl_patrol = Label(frame_body_left, text = "Patrol")
        lbl_incharge.grid(row = x, column = 1, padx = 2, pady = 2)
        lbl_patrol.grid(row = x+1, column = 1, padx =2, pady =2)


    #Creates and places a weekly restrictions table for the supervisor to hand pick
    frame_body_main = Frame(frame_body, relief = 'groove')
    frame_body_main.grid(row = 2, column = 1)
    restrictions = []
    row1 = 0
    column1 = 0
    for x in range(0, 42,2):
        combo_shift = Combobox(frame_body_main, state='readonly', width=7)
        combo_shift.configure(value=values(emp_list))
        restrictions.append(combo_shift)
        restrictions[x].grid(row= row1, column=column1, padx=2, pady=5)
        combo_shift2 = Combobox(frame_body_main, state='readonly', width=7)
        combo_shift2.configure(value=values(emp_list))
        restrictions.append(combo_shift2)
        restrictions[x+1].grid(row=row1+1, column=column1, padx=2, pady=5)
        restrictions[x].current(0)
        restrictions[x+1].current(0)
        row1 += 2
        if row1%6 == 0:
            row1 = 0
            column1 +=1

    frame_body_right = Frame(frame_body)
    frame_body_right.grid(row = 2, column = 2, padx = 5)
    headline2 = Label(frame_body_right, font='Ariel 12 bold underline', text="Saturday shifts:")
    headline2.grid(row=0, pady = 12, padx = 5)

    frame_left = Frame(frame_body_right)
    frame_left.grid(row=1, column=0)
    frame_right = Frame(frame_body_right, height = 300, width = 200)
    frame_right.grid(row=1, column=1)

    # frame for days and positions
    lbl_after = Label(frame_left, text="Afternoon:").grid(row=0, column=0, padx=10, pady=10)
    lbl_eve = Label(frame_left, text="Night:").grid(row=2, column=0, padx=10, pady=10)
    for x in range(0, 3, 2):
        lbl_incharge = Label(frame_left, text="Incharge")
        lbl_patrol = Label(frame_left, text="Patrol")
        lbl_incharge.grid(row=x, column=1, padx=2, pady=2)
        lbl_patrol.grid(row=x + 1, column=1, padx=2, pady=2)
    last_week = []
    for x in range(4):
        combo_last_week = Combobox(frame_right, width=8, value = values(emp_list))
        combo_last_week.grid(row=x, padx = 10, pady = 4)
        combo_last_week.current(0)
        last_week.append(combo_last_week)


    #This bit is for the personal restrictions that the employees themselves have sent
    #creating a shifts variable, a list of lists that in it there would be the the employees willing work each shift
    shifts = []
    for x in range(42):
        shifts.append([])








    frame_btm = Frame(gen_win, width = 500, height = 500)
    frame_btm.grid(row =3, pady=30)

    combo = Combobox(frame_btm, state='readonly')
    combo.configure(value=values(emp_list))
    choose_emp = Label(frame_btm, text="Choose employee: ")
    choose_emp.grid(row=0, padx=20, column=0, sticky = 'w')
    combo.grid(row=0, column=1, padx=20)
    combo.current(0)
    select_btn = Button(frame_btm, text="Select", command = personal_rest)
    select_btn.grid(row=0, column=2, padx=20, sticky = 'e')

    next_btn = Button(gen_win, text = "Generate Schedule", command = check_restrictions)
    next_btn.grid(row =4, column = 0, sticky = 'e', padx = 20)















