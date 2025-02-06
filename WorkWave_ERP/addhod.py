from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect
from PIL import Image, ImageTk

class addhod:
    def __init__(self):
        self.root=Toplevel()
        self.root.title("Add Hod")
        self.root.state("zoomed")
        self.root['background'] = '#FFFFFF'
        self.font = ("Arial", 14, "bold")

        self.conn=connect()
        self.cr= self.conn.cursor()
        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"
        self.text_color = "#F46036"
        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        # Load and resize image
        image = Image.open("images/img.png")  # Change to your image file path
        image = image.resize((380, 240))  # Resize image as per your requirement
        photo = ImageTk.PhotoImage(image)

        # Create label to display image
        self.image_label = Label(self.root, image=photo, bg=self.bg_color)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(side=TOP, fill=Y, padx=20, pady=20)  # Pack image label on the left side

        self.mainLabel=Label(self.root,text="Add Hod",font=('Arial',24,'bold'),bg=self.bg_color, fg=self.text_color)
        self.mainLabel.pack(pady=10,padx=10)

        self.form=Frame(self.root,bg=self.bg_color)
        self.form.pack()


        self.l2 = Label(self.form, text="Name",font=self.font,bg=self.bg_color, fg=self.text_color)
        self.l2.grid(row=1, column=0, padx=10, pady=10)
        self.t2 = Entry(self.form, font=self.font,bg=self.sec_color,width=27)
        self.t2.grid(row=1, column=1, padx=10, pady=10)

        self.l3 = Label(self.form, text="E-Mail",font=self.font,bg=self.bg_color, fg=self.text_color)
        self.l3.grid(row=2, column=0, padx=10, pady=10)
        self.t3 = Entry(self.form, font=self.font,bg=self.sec_color,width=27)
        self.t3.grid(row=2, column=1, padx=10, pady=10)

        self.l4 = Label(self.form, text="Mobile Number",font=self.font,bg=self.bg_color, fg=self.text_color)
        self.l4.grid(row=3, column=0, padx=10, pady=10)
        self.t4 = Entry(self.form, font=self.font,bg=self.sec_color,width=27)
        self.t4.grid(row=3, column=1, padx=10, pady=10)

        self.l5 = Label(self.form, text="Qualifications",font=self.font,bg=self.bg_color, fg=self.text_color)
        self.l5.grid(row=4, column=0, padx=10, pady=10)
        self.t5 = Entry(self.form,font=self.font,bg=self.sec_color,width=27)
        self.t5.grid(row=4, column=1, padx=10, pady=10)

        self.btn = Button(self.root, text='Add', width=20, font=self.font, command=self.addhod,
                          bg=self.text_color, fg="white", activebackground=self.button_hover_color,
                          activeforeground="white")
        self.btn.pack(padx=40, pady=40)
        self.root.mainloop()
    def reset(self):
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')
        self.t5.delete(0, 'end')


    def addhod(self):
        email=self.t3.get()
        if self.t2.get()=='' and self.t3.get()=='' and self.t4.get()=='' and self.t5.get()=='':
            msg.showwarning("Not Running","Enter all fields",parent=self.root)

        else:
            if len(self.t4.get())==10 and self.t4.get().isdigit() :
                if '@' in email and '.' in email:
                    q=("insert into hod values (null,'"+self.t2.get()+"','"+self.t3.get()+"',"+self.t4.get()
                    +",'"+self.t5.get()+"')")
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success","Added Successfully",parent=self.root)
                    self.reset()
                else:
                    msg.showwarning("warning","Invaild email",parent=self.root)
            else:
                msg.showwarning("Not Running","Invalid Mobile Number",parent=self.root)
if __name__=="__main__":

    addhod()
