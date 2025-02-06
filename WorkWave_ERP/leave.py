from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from tkcalendar import DateEntry  # Import DateEntry widget from tkcalendar
import pymysql
from connection import connect


class LeaveApplication:
    def __init__(self,employee_id):
        self.employee_id=employee_id
        self.root = Toplevel()
        self.root.title("Leave Application")
        self.root.geometry("1000x700")
        self.root['background'] = '#FFFFFF'
        self.text_color = "#F46036"

        self.font = ("Arial", 20, "bold")
        self.conn = connect()
        self.cr = self.conn.cursor()

        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"

        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        self.mainLabel = Label(self.root, text="Leave Application", font=('Arial', 24, 'bold'), bg=self.bg_color, fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.leaveForm = Frame(self.root, bg=self.bg_color)
        self.leaveForm.pack()

        self.lb1 = Label(self.leaveForm, text="Employee ID", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, pady=10, padx=20)

        self.t1 = Entry(self.leaveForm, font=self.font, width=30)
        self.t1.grid(row=0, column=1, pady=10, padx=20)
        self.t1.insert(END,self.employee_id[0])
        self.t1.configure(state='readonly')

        self.lb11 = Label(self.leaveForm, text="Employee Name", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb11.grid(row=1, column=0, pady=10, padx=20)

        self.t11 = Entry(self.leaveForm, font=self.font, width=30)
        self.t11.grid(row=1, column=1, pady=10, padx=20)
        self.t11.insert(END, self.employee_id[2])
        self.t11.configure(state='readonly')

        self.lb2 = Label(self.leaveForm, text="Date", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=2, column=0, pady=10, padx=20)

        # Replace Entry with DateEntry for calendar date selection
        self.t2 = DateEntry(self.leaveForm, font=self.font, width=30, background='darkblue', foreground='white',
                            borderwidth=2, date_pattern='Y-m-d')
        self.t2.grid(row=2, column=1, pady=10, padx=20)

        self.lb3 = Label(self.leaveForm, text="Remarks", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb3.grid(row=3, column=0, pady=10, padx=20)
        # Replace Entry with Text for larger text box
        self.t3 = Text(self.leaveForm, font=self.font, width=30, height=5)
        self.t3.grid(row=3, column=1, pady=10, padx=20)

        self.submitButton = Button(self.root, text="Submit", width=15, font=self.font, command=self.submitLeave, bg=self.text_color, fg="white", activebackground=self.button_hover_color, activeforeground="white")
        self.submitButton.pack(pady=20)

        # Bind hover effects to the submit button
        self.submitButton.bind("<Enter>", self.on_enter)
        self.submitButton.bind("<Leave>", self.on_leave)

        self.root.mainloop()

    def submitLeave(self):
        emp_id = self.t1.get()
        emp_name = self.t11.get()
        date = self.t2.get()
        remarks = self.t3.get("1.0", "end-1c")

        try:
            if len(date)!=0 or len(remarks)!=0:
                sql_insert_leave = "INSERT INTO `leave` VALUES (null, %s, %s, %s, %s, 'pending')"
                self.cr.execute(sql_insert_leave, (emp_id, emp_name, date, remarks))
                self.conn.commit()
                msg.showinfo("Leave Application", "Leave submitted successfully.",parent=self.root)
                self.t1.delete(0,'end')
                self.t11.delete(0,'end')
                self.t2.delete(0,'end')
                self.t3.delete('1.0','end-1c')
            else:
                msg.showerror("Error", "Please enter date and remarks.")
        except Exception as e:
            self.conn.rollback()
            print(e)
            msg.showerror("Error", f"An error occurred: {e}",parent=self.root)
    def on_enter(self, event):
        # Change background color when mouse enters button
        self.submitButton.config(bg=self.button_hover_color)

    def on_leave(self, event):
        # Restore background color when mouse leaves button
        self.submitButton.config(bg=self.button_color)

if __name__ == "__main__":
    leave_application = LeaveApplication((2,"jas"),)





