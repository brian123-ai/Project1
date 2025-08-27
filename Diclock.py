'''
PROBLEM STATEMENT:
Build a simple digitl clock that displays the current time and updates every second.
'''

import time

from tkinter import Label, Tk

app = Tk()
app.title("Digital Clock")
app.geometry("400x200") 
app.resizable(0, 0)
app.configure(bg="black")

clock_label = Label(app, font=("Arial", 48), bg="black", fg="white",relief="flat")

clock_label.place(x=50, y=50)

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

update_clock()
app.mainloop()
