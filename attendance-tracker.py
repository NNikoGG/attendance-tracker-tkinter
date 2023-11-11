from tkinter import *
from tkinter import ttk
import sqlite3
from tkcalendar import Calendar

# Initialize the main application window
root = Tk()
root.title("Attendance Tracker")
# root.geometry("400x400")

def add_subject():
    return

# Subject Entry
subject_entry = Entry(root)
subject_entry_label = Label(root, text="Add a Subject", width=30)
subject_entry_label.grid(row=0, column=0, padx=5, pady=5)
subject_entry.grid(row=1, column=0, padx=5, pady=5)

# Submit Button for Subject
submit_btn = Button(root, text="Submit", command=add_subject)
submit_btn.grid(row=2, column=0, padx=5, pady=5)


root.mainloop()
