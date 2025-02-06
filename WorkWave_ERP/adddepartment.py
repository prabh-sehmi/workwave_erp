from tkinter import *
import tkinter.messagebox as msg
from connection import connect
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class addDepartment:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Add Department")
        self.root.state("zoomed")
        self.font= ("Arial", 16,'bold')
        self.root['background'] = '#FFFFFF'

        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"
        self.text_color = "#F46036"

        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        self.conn=connect()
        self.cr = self.conn.cursor()

        # Load and resize image
        image = Image.open("images/img.png")  # Change to your image file path
        image = image.resize((280, 140))  # Resize image as per your requirement
        photo = ImageTk.PhotoImage(image)

        # Create label to display image
        self.image_label = Label(self.root, image=photo, bg=self.bg_color)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(side=TOP, fill=Y, padx=20, pady=20)  # Pack image label on the left side

        self.mainLabel = Label(self.root, text="Add Department", font=('Arial', 24, "bold"),bg=self.bg_color, fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.form = Frame(self.root,bg=self.bg_color)
        self.form.pack(pady=10)

        self.lb1 = Label(self.form, text=" Department Name : ",font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, padx=20, pady= 20)
        self.t1 = Entry(self.form, width=35, font=self.font,bg=self.sec_color)
        self.t1.grid(row=0, column=1, padx=20)

        self.lb2 = Label(self.form, text=" Email : ", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1, column=0, padx=20, pady=20)
        self.t2 = Entry(self.form, width=35, font=self.font,bg=self.sec_color)
        self.t2.grid(row=1, column=1, padx=20)

        self.lb3 = Label(self.form, text=" Phone No. : ", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb3.grid(row=2, column=0, padx=20, pady=20)
        self.t3 = Entry(self.form, width=35, font=self.font,bg=self.sec_color)
        self.t3.grid(row=2, column=1, padx=20)

        # self.lb4 = Label(self.form, text=" HOD ID : ", font=self.font)
        # self.lb4.grid(row=3, column=0, padx=20, pady=20)
        # self.t4 = Entry(self.form, width=35, font=self.font)
        # self.t4.grid(row=3, column=1, padx=20)

        self.l1 = Label(self.form, text="HOD Name", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.l1.grid(row=5, column=0, padx=20, pady=20)
        self.c1 = ttk.Combobox(self.form, values= self.fetchhod(), state="readonly", width=60)
        self.c1.grid(row=5, column=1, padx=20, pady=20)

        self.btn = Button(self.root, text="Add Department", font=self.font, command=self.addDepartment,bg=self.text_color, fg="white", activebackground=self.button_hover_color, activeforeground="white")
        self.btn.pack(pady=20)



        self.root.mainloop()

    def reset(self):
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t1.delete(0, 'end')
        self.c1.set('')


    def addDepartment(self):
        if self.t1.get()=='' or self.t2.get()=='' or self.t1.get()=='' or self.c1.get()=='' :
            msg.showwarning("Warning", "Please Enter all field",parent=self.root)
        else:
            hod_id=self.getHodName(self.c1.get())
            if len(self.t3.get())==10 and self.t3.get().isdigit():
                if '@' in self.t2.get() and '.' in self.t2.get():
                    q=f"insert into department values ('{self.t1.get()}','{self.t2.get()}','{self.t3.get()}','{hod_id}')"
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success", "Department added successfully",parent=self.root)
                    self.reset()
                else:
                    msg.showwarning("Warning", " Enter vaild Email",parent=self.root)
            else:
                msg.showwarning("Warning", " Enter vaild Phone Number",parent=self.root)
    def getHodName(self,name):
        name=name
        q=f"select id from hod where name='{name}'"
        self.cr.execute(q)
        row=self.cr.fetchall()
        for i in row:
            return i[0]
    def fetchhod(self):
        q=" select * from hod "
        self.cr.execute(q)
        result = self.cr.fetchall()
        list=[]
        for i in result :
            list.append(i[1])

        return list


if __name__ == '__main__':
    addDepartment()