from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect  # Assuming connect is a function to establish database connection
import sqlite3
import csv
from tkinter.filedialog import asksaveasfilename


class getattendance:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("View Attendance")
        self.root.state("zoomed")
        self.font = ("Arial", 12)

        self.conn = connect()  # Establish database connection
        self.cr = self.conn.cursor()

        self.mainLabel = Label(self.root, text="View Attendance", font=("", 32, 'bold'))
        self.mainLabel.pack(pady=20)

        # Attendance table
        self.attendance_table = ttk.Treeview(self.root, columns=(
        'id', 'employee_id', 'name', 'date', 'time'))
        self.attendance_table.heading('id', text="ID")
        self.attendance_table.heading('employee_id', text="Employee ID")
        self.attendance_table.heading('name', text="Employee Name")
        self.attendance_table.heading('date', text="Date")
        self.attendance_table.heading('time', text="Time")
        # self.attendance_table.heading('department', text="Department")
        # self.attendance_table.heading('category', text="Category")
        self.attendance_table['show'] = 'headings'
        self.attendance_table.pack(expand=True, fill='both', padx=20, pady=20)

        # Configure column widths
        self.attendance_table.column('id', width=50, anchor='center')
        self.attendance_table.column('employee_id', width=100, anchor='center')
        self.attendance_table.column('name', width=150, anchor='center')
        self.attendance_table.column('date', width=100, anchor='center')
        self.attendance_table.column('time', width=100, anchor='center')
        # self.attendance_table.column('department', width=150, anchor='center')
        # self.attendance_table.column('category', width=100, anchor='center')

        self.get_attendance_info()
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('', 12, 'bold'), rowheight=50, foreground="#FF7F66")
        self.style.configure("Treeview", font=('', 14), rowheight=50)

        # Configure row heights
        self.attendance_table.tag_configure('evenrow', background='#ECECEC')
        self.attendance_table.tag_configure('oddrow', background='#FFFFFF')
        # self.attendance_table.configure(font=self.font)

        # Button to export data to CSV
        self.export_button = Button(self.root, text="Export to CSV", command=self.export_to_csv, font=self.font)
        self.export_button.pack(pady=10)

        self.root.mainloop()

    def get_attendance_info(self):
        try:
            q = "select * from attendance"
            self.cr.execute(q)

            result = self.cr.fetchall()

            for row in self.attendance_table.get_children():
                self.attendance_table.delete(row)

            for i in range(len(result)):
                self.attendance_table.insert('', index=i, values=result[i])
        except sqlite3.Error as e:
            msg.showerror("Error", f"Database Error: {e}")

    def export_to_csv(self):
        try:

            # Fetch data from the attendance table, excluding the 'Type' field
            q = "select * from attendance"
            self.cr.execute(q)
            data = self.cr.fetchall()

            # Ask user to choose the file path
            file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

            # Check if the user cancelled the dialog
            if not file_path:
                return

            # Open the CSV file for writing
            with open(file_path, "w", newline="") as csvfile:
                csvwriter = csv.writer(csvfile)

                # Write the header row
                csvwriter.writerow(['ID', 'Employee ID', 'Employee Name', 'Date', 'Time'])

                # Write data rows
                csvwriter.writerows(data)

            msg.showinfo("Success", f"Data exported to {file_path}")
        except sqlite3.Error as e:
            msg.showerror("Error", f"Database Error: {e}")
        except Exception as e:
            msg.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    getattendance()
