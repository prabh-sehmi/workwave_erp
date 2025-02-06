from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect

class viewleaveemployee:
    def __init__(self, employee_id):
        self.employee_id = employee_id
        # Other initialization code...
        self.root = Toplevel()
        self.root.state("zoomed")

        self.conn = connect()
        self.cr = self.conn.cursor()

        self.mainLabel = Label(self.root, text="Leaves", font=('', 28, 'bold'))
        self.mainLabel.pack()

        self.leavetable = ttk.Treeview(self.root, columns=('id', 'emp_id', 'date', 'remarks', 'status'))
        self.leavetable.heading('id', text='Serial Number')
        self.leavetable.heading('emp_id', text='Employee ID')
        self.leavetable.heading('date', text='Date')
        self.leavetable.heading('remarks', text='Remarks')
        self.leavetable.heading('status', text='Status')
        self.leavetable['show'] = 'headings'
        self.leavetable.column('id', width=50, anchor='center')
        self.leavetable.column('emp_id', width=100, anchor='center')
        self.leavetable.column('date', width=100, anchor='center')
        self.leavetable.column('remarks', width=200, anchor='center')
        self.leavetable.column('status', width=100, anchor='center')

        self.leavetable.pack(fill='both', padx=20, pady=20)
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('', 12, 'bold'), rowheight=50, foreground="#FF7F66")
        self.style.configure("Treeview", font=('', 14), rowheight=50)

        self.populate_leave_table()  # Fetch and display leave data



        self.root.mainloop()

    def populate_leave_table(self):
        try:
            employee_id = self.employee_id
            q = f"SELECT id,emp_id,emp_name,date, status  FROM `leave` WHERE emp_id = '{employee_id}'"
            self.cr.execute(q)

            result = self.cr.fetchall()
            print(result)
            for row in self.leavetable.get_children():
                self.leavetable.delete(row)

            for i in range(len(result)):
                self.leavetable.insert('', index=i, values=result[i])
        except pymysql.Error as e:
            print(e)
            msg.showerror("Error", f"Error fetching leave data: {e}", parent=self.root)


if __name__ == "__main__":
    employee_id = 2  # Replace with the actual employee ID
    viewleaveemployee_instance = viewleaveemployee(employee_id)


