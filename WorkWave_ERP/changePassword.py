from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect

class Main:
    def __init__(self,email):
        self.email = email
        self.root = Tk()
        self.root.title("Change Password")
        self.root.geometry('1000x750')
        self.conn = connect()
        self.cr = self.conn.cursor()
        self.text_color = "#F46036"

        self.ml = Label(self.root, text="Change Password", font=('', 36, 'bold'), anchor='center',fg=self.text_color)
        self.ml.pack(pady=20, padx=20)
        self.form = Frame(self.root)
        self.form.pack(pady=20, padx=20)

        self.l4=Label(self.form,text="Enter Email",font=('',16,''),fg=self.text_color)
        self.l4.grid(row=0,column=0,pady=20,padx=20)
        self.t4=Entry(self.form,font=('',16))
        self.t4.grid(row=0,column=1,pady=20,padx=20)
        self.t4.insert(END,self.email)
        self.t4.configure(state='readonly')

        self.l1=Label(self.form, text="Enter Old Password", font=('',16,''),fg=self.text_color)
        self.t1=Entry(self.form, font=('',16),show='*')
        self.l1.grid(row=1, column=0,pady=20,padx=20)
        self.t1.grid(row=1,column=1,pady=20, padx=20)


        self.l2 = Label(self.form,text="Enter New Password", font=('',16),fg=self.text_color)
        self.t2=Entry(self.form, font=('',16),show='*')
        self.l2.grid(row=2,column=0,pady=20,padx=20)
        self.t2.grid(row=2,column=1,pady=20,padx=20)

        self.l3 = Label(self.form,text="Confirm New Password", font=('',16),width=35,fg=self.text_color)
        self.t3 = Entry(self.form,font=('',16),show='*')
        self.l3.grid(row=3,column=0,pady=20,padx=20)
        self.t3.grid(row=3,column=1,pady=20, padx=20)

        self.b1 = Button(self.root, text="Confirm", font=('',16,'bold'),width=20,command=self.changePassword,bg=self.text_color,fg='white')
        self.b1.pack(pady=20, padx=20)


        self.root.mainloop()
    def changePassword(self):
        email=self.t4.get()
        password=self.t1.get()
        q = f"SELECT id,email,name,mobile,role  FROM admin WHERE email = '{email}' and password = '{password}'"
        self.cr.execute(q)
        result = self.cr.fetchone()
        if result is None:
            msg.showwarning("Error", "Email and password do not match",parent=self.root)
        else:
            if self.t2.get()==self.t3.get():
                q = f"update admin set password = '{self.t2.get()}' where email='{email}' and password = '{password}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "Password Updated",parent=self.root)



if __name__ == '__main__':
    main = Main('jas@gmail.com')