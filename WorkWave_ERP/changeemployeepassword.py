from tkinter import *
import tkinter.messagebox as msg
from connection import connect
from PIL import Image, ImageTk
import pymysql
import tkinter.ttk as ttk
class changePassword:
    def __init__(self,email):
        self.email=email
        self.root = Toplevel()
        self.root.title("Employee Change Password")
        self.root.geometry("1000x750")
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


        self.mainLabel = Label(self.root, text="Change Password", font=('', 32,"bold"),bg=self.bg_color, fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.form = Frame(self.root,bg=self.bg_color)
        self.form.pack(pady=10)

        self.lb1 = Label(self.form, text="Enter Email", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, padx=20, pady=20)

        self.txt1 = Entry(self.form, font=self.font,bg=self.sec_color,width=27)
        self.txt1.grid(row=0, column=1, padx=20, pady=20)
        self.txt1.insert(END,self.email)
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.form, text="Enter Old Password", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1, column=0, padx=20, pady=20)
        self.txt2 = Entry(self.form,  font=self.font, show='*',bg=self.sec_color,width=27)
        self.txt2.grid(row=1, column=1, padx=20, pady=20)

        self.lb3 = Label(self.form, text="Enter New Password", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb3.grid(row=2, column=0, padx=20, pady=20)
        self.txt3 = Entry(self.form,  font=self.font,show='*',bg=self.sec_color,width=27)
        self.txt3.grid(row=2, column=1, padx=20, pady=20)

        self.lb4 = Label(self.form, text="Enter Confirm Password", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb4.grid(row=3, column=0, padx=20, pady=20)
        self.txt4 = Entry(self.form,  font=self.font,show='*',bg=self.sec_color,width=27)
        self.txt4.grid(row=3, column=1, padx=20, pady=20)

        self.b1 = Button(self.root, text="Confirm", font=('', 16, 'bold'), width=20, command=self.changePassword,
                         bg=self.text_color, fg='white')
        self.b1.pack(pady=20, padx=20)

        # Make window responsive
        self.root.pack_propagate(0)
        self.root.geometry("800x700")
        self.root.minsize(200, 100)


        self.root.mainloop()

    def changePassword(self):
        email = self.txt1.get()
        password = self.txt2.get()
        q = (f"select employee_id,name,father_name,email,mobile,address,department,image FROM employee Where email = '{email}' and password = '{password}'")
        self.cr.execute(q)
        result = self.cr.fetchone()

        if result is None:
            msg.showwarning("Warning", "Email and Password do not match",parent=self.root)
        else:
            if self.txt3.get() == self.txt4.get():
                q = f"update employee set password = '{self.txt3.get()}' where email = '{email}' and password = '{password}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "Password Updated",parent=self.root)
                self.txt1.delete(0, "end")
                self.txt2.delete(0, "end")
                self.txt3.delete(0, "end")
                self.txt4.delete(0, "end")



if __name__ == "__main__":
    changePassword('jas@gmail.com')