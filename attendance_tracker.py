from tkinter import *
from tkinter import ttk
import sqlite3
from tkcalendar import Calendar

# Initialize the main application window
root = Tk()
root.title("Attendance Tracker")
# root.geometry("400x400")

# Creating a database
conn = sqlite3.connect("attendance_tracker.db")

# Creating a cursor
c = conn.cursor()

# Creating a table

c.execute("""CREATE TABLE IF NOT EXISTS attendance (
		subject text
		)""")




def add_subject():
	# Creating a database
	conn = sqlite3.connect("attendance_tracker.db")

	# Creating a cursor
	c = conn.cursor()

	# Inserting the values into the table
	c.execute("INSERT INTO attendance VALUES (:subject)",
		   {
				'subject': subject_entry.get()
		   	})
	
	# Commit changes
	conn.commit()
	
	# Close connection
	conn.close()
	
    # Clear the text boxes
	subject_entry.delete(0, END)
	


def show():
	# Creating a database
	conn = sqlite3.connect("attendance_tracker.db")

	# Creating a cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM attendance")
	records = c.fetchall()

	# Display results in GUI
	print_records = ''
	for record in records:
		print_records += str(record[0]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(column=0, row=12, columnspan=2,)

	# Commit changes
	conn.commit()
	
	# Close connection
	conn.close()

# Subject Entry
subject_entry = Entry(root)
subject_entry_label = Label(root, text="Add a subject", width=30)
subject_entry_label.grid(row=0, column=0, padx=5, pady=5)
subject_entry.grid(row=1, column=0, padx=5, pady=5)

# Submit Button for Subject
submit_btn = Button(root, text="Submit", command=add_subject)
submit_btn.grid(row=2, column=0, padx=10, pady=10, columnspan=2, ipadx=25)

# Show Button for Subject
show_btn = Button(root, text="Show Subjects", command=show)
show_btn.grid(row=3, column=0, padx=10, pady=10, columnspan=2, ipadx=25)


# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
