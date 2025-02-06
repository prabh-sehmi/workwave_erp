from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect
from PIL import Image, ImageTk

class adminProfile:
    def __init__(self,data):
        self.data = data
        self.root = Toplevel()
        self.root.title(" Admin Profile")
        self.root.geometry('700x700')
        self.font = ("Arial", 16,'bold')
        self.root['background'] = '#FFFFFF'

        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"
        self.text_color = "#F46036"
        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        self.conn = connect()
        self.cr = self.conn.cursor()

        # Load and resize image
        image = Image.open("images/img.png")  # Change to your image file path
        image = image.resize((280, 140))  # Resize image as per your requirement
        photo = ImageTk.PhotoImage(image)

        # Create label to display image
        self.image_label = Label(self.root, image=photo, bg=self.bg_color)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(side=TOP, fill=Y, padx=20, pady=20)  # Pack image label on the left side

        self.mainLabel = Label(self.root, text=" Admin Profile", font=('Arial', 24, "bold"), bg=self.bg_color,
                               fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.form = Frame(self.root, bg=self.bg_color)
        self.form.pack(pady=10)
        self.id=self.data[0]
        self.lb1 = Label(self.form, text="Name : ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, padx=20, pady=20)
        self.t2 = Entry(self.form, width=35, font=self.font, bg=self.sec_color)
        self.t2.grid(row=0, column=1, padx=20)
        self.t2.insert(0,self.data[2])

        self.lb2 = Label(self.form, text=" Email : ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1, column=0, padx=20, pady=20)
        self.t3 = Entry(self.form, width=35, font=self.font, bg=self.sec_color)
        self.t3.grid(row=1, column=1, padx=20)
        self.t3.insert(0, self.data[1])

        self.lb3 = Label(self.form, text=" Phone No. : ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb3.grid(row=2, column=0, padx=20, pady=20)
        self.t4 = Entry(self.form, width=35, font=self.font, bg=self.sec_color)
        self.t4.grid(row=2, column=1, padx=20)
        self.t4.insert(0, self.data[3])


        self.btn = Button(self.root, text=" Admin  Profile ", font=self.font, command=self.addAdmin, bg=self.text_color,
                          fg="white", activebackground=self.button_hover_color, activeforeground="white")
        self.btn.pack(pady=20)

        self.root.mainloop()


    def reset(self):
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')

    def addAdmin(self):
        id = self.id
        name = self.t2.get()
        email = self.t3.get()
        mobile = self.t4.get()


        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 :
            msg.showerror("Not Working", "Need to fill all fields", parent=self.root)
        else:
            if mobile.isdigit() and len(mobile) == 10:
                if '@' in email and '.' in email:
                    q = f"update admin set name='{name}',email='{email}',mobile='{mobile}' where id='{id}'"
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success", "Admin Updated", parent=self.root)
                else:
                    msg.showwarning("Not working", "Email Format Invalid", parent=self.root)
            else:
                msg.showwarning("Not Running ", "Invalid Mobile Number", parent=self.root)



if __name__=="__main__":
    adminProfile('1')
