# Work-Schedule
A work schedule generator

A work schedule generator for a friend who asked me to create it.
This is a schedule generator for a specific place that has 2 people in a shift, one in charge and one patrol. It abides by certain legal
limitation such as: An employee is not allowed to work more than 3 consecutive saturdays and not allowed to work more than 7 nights
per 2 weeks. And also abides by preferred limitations such as not having only 8 hours between shifts (legal yet uncomfortable).

Each employee has a standard number of shifts he\she should be assigned to during the week (full time\part time). Every week the employees 
sends to the supervisor in which shifts they can put assigned to next week and the generator assigns the shifts accroding to these
limitations.

The idea is pretty simple:
After inputting the emplyees requested shifts by the supervisor. The generator assigns the shift that the least employees can work at
with the employee that "opened" the least weekly options, thus assigning the more "problematic" employees with the more "problematic"
shifts. Leaving the the more flexiable employees for the later time.

After receiving a generated schedule, the generator exports it to an excel file, then the supervisor may go to the "Edit schedule" tab
and manually insert changes if needed.

Since the progrem is not flexiable (ex: one of the employees is sick, the supervisor might need to ask an employee to work an extra
shift that week. The supervisor may either input in the employee details that he will work more shifts and generting it with more
standard shifts for this employee), the supervisor may instert manual changes to the schedule that are not restricted to legal
and logical limitations such as having only an 8 hour break between shifts, putting someone who's not qualified to be incharge or
working more than the premitted Saturdays and night.
