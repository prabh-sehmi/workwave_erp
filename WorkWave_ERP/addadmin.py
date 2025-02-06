from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect
from PIL import Image, ImageTk

class addAdmin:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Add Admin")
        self.root.state("zoomed")
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

        self.mainLabel = Label(self.root, text="Add Admin", font=('Arial', 24, "bold"), bg=self.bg_color,
                               fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.form = Frame(self.root, bg=self.bg_color)
        self.form.pack(pady=10)

        self.lb1 = Label(self.form, text="Name : ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, padx=20, pady=20)
        self.t2 = Entry(self.form, width=35, font=self.font, bg=self.sec_color)
        self.t2.grid(row=0, column=1, padx=20)

        self.lb2 = Label(self.form, text=" Email : ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1, column=0, padx=20, pady=20)
        self.t3 = Entry(self.form, width=35, font=self.font, bg=self.sec_color)
        self.t3.grid(row=1, column=1, padx=20)

        self.lb3 = Label(self.form, text=" Phone No. : ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb3.grid(row=2, column=0, padx=20, pady=20)
        self.t4 = Entry(self.form, width=35, font=self.font, bg=self.sec_color)
        self.t4.grid(row=2, column=1, padx=20)

        self.l5 = Label(self.form, text="Password", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.l5.grid(row=4, column=0, padx=10, pady=10)
        self.t5 = Entry(self.form, font=('', 12), width=47, show='*', bg=self.sec_color)
        self.t5.grid(row=4, column=1, padx=10, pady=10)

        self.l1 = Label(self.form, text="Role ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.l1.grid(row=5, column=0, padx=20, pady=20)
        self.c1 = ttk.Combobox(self.form, values=['SuperAdmin', 'Admin'], state="readonly", width=60)
        self.c1.grid(row=5, column=1, padx=20, pady=20)

        self.btn = Button(self.root, text="Add Admin", font=self.font, command=self.addAdmin, bg=self.text_color,
                          fg="white", activebackground=self.button_hover_color, activeforeground="white")
        self.btn.pack(pady=20)

        self.root.mainloop()


    def reset(self):
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')
        self.t5.delete(0, 'end')
        self.c1.set('')

    def addAdmin(self):
        email=self.t3.get()
        if self.t2.get()=='' and self.t3.get()=='' and self.t4.get()=='' and self.c1.get()=='' and self.t5.get()=='':
            msg.showwarning("Not Running","Enter all fields",parent=self.root)

        else:
            if len(self.t4.get())==10 and self.t4.get().isdigit() :
                if '@' in email and '.' in email:
                    q=("insert into admin values(null,'"+self.t2.get()+"','"+self.t3.get()+"',"+self.t4.get()
                    +",'"+self.t5.get()+"','"+self.c1.get()+"')")
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success","Added Successfully",parent=self.root)
                    self.reset()
                else:
                    msg.showwarning("warning","Invaild email",parent=self.root)
            else:
                msg.showwarning("Not Running","Invalid Mobile Number",parent=self.root)

if __name__=="__main__":
    addAdmin()
