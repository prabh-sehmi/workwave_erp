from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect  # assuming you have a connection module


class ViewLeaveAdmin:
    def __init__(self):
        self.root = Toplevel()
        self.root.state("zoomed")
        self.root.title("Leave Management")
        self.text_color = "#F46036"

        self.conn = connect()  # Establish database connection
        self.cr = self.conn.cursor()

        self.main_label = Label(self.root, text="Leaves", font=('', 28, 'bold'),fg=self.text_color)
        self.main_label.pack()

        self.leave_table = ttk.Treeview(self.root, columns=('id', 'emp_id', 'emp_name', 'date', 'remarks', 'status'))
        self.leave_table.heading('id', text='Serial Number')
        self.leave_table.heading('emp_id', text='Employee ID')
        self.leave_table.heading('emp_name', text='Employee Name')
        self.leave_table.heading('date', text='Date')
        self.leave_table.heading('remarks', text='Remarks')
        self.leave_table.heading('status', text='Status')
        self.leave_table['show'] = 'headings'
        self.leave_table.column('id', width=50, anchor='center')
        self.leave_table.column('emp_id', width=100, anchor='center')
        self.leave_table.column('emp_name', width=100, anchor='center')
        self.leave_table.column('date', width=100, anchor='center')
        self.leave_table.column('remarks', width=200, anchor='center')
        self.leave_table.column('status', width=100, anchor='center')
        self.leave_table.pack(fill='both', padx=20, pady=20)

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('', 12, 'bold'), rowheight=50, foreground="#FF7F66")
        self.style.configure("Treeview", font=('', 14), rowheight=50)

        self.populate_leave_table()  # Fetch and display leave data

        self.leave_table.bind("<Button-3>", self.show_popup_menu)

        self.root.mainloop()

    def populate_leave_table(self):
        try:
            self.cr.execute("SELECT * FROM `leave`")
            leaves_data = self.cr.fetchall()
            for index, leave in enumerate(leaves_data):
                # Replace status values
                leave_values = list(leave)
                if leave_values[5] == 'null':
                    leave_values[5] = 'Not Approved'
                elif leave_values[5] == 'ok':
                    leave_values[5] = 'Approved'
                elif leave_values[5] == 'reject':
                    leave_values[5] = 'Rejected'

                # Insert row with appropriate tag for alternate row coloring
                self.leave_table.insert('', 'end', values=tuple(leave_values))

                # Set background color for alternate rows
                if index % 2 == 0:
                    self.leave_table.tag_configure('evenrow', background='#FFFFFF')
                else:
                    self.leave_table.tag_configure('oddrow', background='#ECECEC')
        except pymysql.Error as e:
            print(e)
            msg.showerror("Error", f"Error fetching leave data: {e}")

    def update_status(self, leave_id, new_status):
        try:
            self.cr.execute("UPDATE `leave` SET status=%s WHERE id=%s", (new_status, leave_id))
            self.conn.commit()
            msg.showinfo("Success", "Status updated successfully",parent=self.root)
            # Refresh table after updating status
            for row in self.leave_table.get_children():
                self.leave_table.delete(row)
            self.populate_leave_table()
        except pymysql.Error as e:
            print(e)
            msg.showerror("Error", f"Error updating status: {e}",parent=self.root)

    def show_popup_menu(self, event):
        item = self.leave_table.identify_row(event.y)
        if item:
            popup_menu = Menu(self.root, tearoff=0)
            popup_menu.add_command(label="Accept",
                                   command=lambda: self.update_status(self.leave_table.item(item, 'values')[0], 'ok'))
            popup_menu.add_command(label="Reject",
                                   command=lambda: self.update_status(self.leave_table.item(item, 'values')[0], 'reject'))
            popup_menu.post(event.x_root, event.y_root)


if __name__ == "__main__":
    view_leave_admin = ViewLeaveAdmin()

