from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from tkinter.tix import Form
from tkinter.filedialog import askopenfilename
import cv2
from connection import connect
from PIL import Image, ImageTk
import random


class addemployee:

    def __init__(self):
        self.root = Toplevel()
        self.root.title("Add Employee")
        self.root.state("zoomed")
        self.font = ("Arial", 14)
        self.root['background'] = '#FFFFFF'

        self.font = ("Arial", 14, "bold")
        self.conn = connect()
        self.cr = self.conn.cursor()

        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"
        self.text_color = "#F46036"
        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        # Left Frame for Image
        self.left_frame = Frame(self.root, bg=self.bg_color)
        self.left_frame.pack(side=LEFT, padx=20, pady=20, fill=Y)

        # Load and resize image
        image = Image.open("images/img.png")  # Change to your image file path
        image = image.resize((480, 270))  # Resize image as per your requirement
        photo = ImageTk.PhotoImage(image)

        # Create label to display image
        self.image_label = Label(self.left_frame, image=photo, bg=self.bg_color)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(padx=20, pady=20)  # Pack image label on the left side

        # Right Frame for Form
        self.right_frame = Frame(self.root, bg=self.bg_color)
        self.right_frame.pack(side=LEFT, padx=20, pady=20, fill=BOTH, expand=True)

        self.mainLabel = Label(self.right_frame, text="Add Employee", font=("Arial", 24, "bold"),
                               bg=self.bg_color, fg=self.text_color)
        self.mainLabel.pack(pady=20)

        # Form
        self.form = Frame(self.right_frame, bg=self.bg_color)
        self.form.pack(pady=10)

        self.lb1 = Label(self.form, text=" Name ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = Entry(self.form, font=self.font, width=35, bg=self.sec_color)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = Label(self.form, text="Father Name ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = Entry(self.form, font=self.font, width=35, bg=self.sec_color)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = Label(self.form, text=" Email ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = Entry(self.form, font=self.font, width=35, bg=self.sec_color)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = Label(self.form, text=" Mobile ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = Entry(self.form, font=self.font, width=35, bg=self.sec_color)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = Label(self.form, text=" Address ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = Entry(self.form, font=self.font, width=35, bg=self.sec_color)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.lb6 = Label(self.form, text=" Category ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = ttk.Combobox(self.form, font=self.font, width=35, values=self.values())
        self.txt6.grid(row=5, column=1, padx=10, pady=10)

        self.lb7 = Label(self.form, text=" Department ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7 = ttk.Combobox(self.form, font=self.font, width=35, values=self.values1())
        self.txt7.grid(row=6, column=1, padx=10, pady=10)

        self.lb9 = Label(self.form, text=" Image ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb9.grid(row=8, column=0, padx=10, pady=10)
        self.txt9 = Entry(self.form, font=self.font, width=35, bg=self.sec_color)
        self.txt9.grid(row=8, column=1, padx=10, pady=10)

        self.btn1 = Button(self.form, text='select', width=10, font=self.font, command=self.selectImage,
                           bg=self.bg_color, fg=self.text_color)
        self.btn1.grid(row=8, column=2, padx=10, pady=10)

        self.lb10 = Label(self.form, text=" Password ", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb10.grid(row=9, column=0, padx=10, pady=10)
        self.txt10 = Entry(self.form, font=self.font, width=35, show='*', bg=self.sec_color)
        self.txt10.grid(row=9, column=1, padx=10, pady=10)

        # Add button at the bottom
        self.btn = Button(self.right_frame, text='Add', width=20, font=self.font, command=self.addemployee,
                          bg=self.text_color, fg="white", activebackground=self.button_hover_color,
                          activeforeground="white")
        self.btn.pack(padx=40,pady=40)

        self.root.mainloop()

    def addemployee(self):

        name = self.txt1.get()
        father_name = self.txt2.get()
        email = self.txt3.get()
        mobile = self.txt4.get()
        address = self.txt5.get()
        category = self.txt6.get()
        department = self.txt7.get()
        image = self.txt9.get()
        password=self.txt10.get()
        print(name, father_name, email, mobile,address,category,department,image,password)
        if (name == '' or father_name == '' or email == '' or mobile == '' or
                address == '' or category == '' or department == ''  or
                image == '' or password == ''):
            msg.showwarning("Warning", " Enter all field")
        else:
            if '@' in self.txt3.get() and '.' in self.txt3.get():
                if len(self.txt4.get()) == 10 and self.txt4.get().isdigit():
                    q = ("insert into employee values(null, '" + self.txt1.get() + "','" + self.txt2.get() + "','" + self.txt3.get() +
                                "','" + self.txt4.get() + "','" + self.txt5.get() + "','" + self.txt6.get() + "','" + self.txt7.get() +
                                "','" + self.txt9.get() + "','" + self.txt10.get() + "')")

                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success", "Employee added successfully",parent=self.root)
                    self.txt1.delete(0,"end")
                    self.txt2.delete(0, "end")
                    self.txt3.delete(0, "end")
                    self.txt4.delete(0, "end")
                    self.txt5.delete(0, "end")
                    self.txt6.delete(0, "end")
                    self.txt7.delete(0, "end")
                    self.txt9.delete(0, "end")
                    self.txt10.delete(0, "end")
                else:
                    msg.showwarning("Warning", " Enter valid Mobile Number",parent=self.root)
            else:
                msg.showwarning("Warning", " Enter valid  Email",parent=self.root)

    def values(self):
        q = "select name from category"
        self.cr.execute(q)
        result = self.cr.fetchall()

        l = []
        for i in result:
            l.append(i[0])
        return l

    def values1(self):
        q = "select name from department"
        self.cr.execute(q)
        result = self.cr.fetchall()

        l1 = []
        for j in result:
            l1.append(j[0])
        return l1


    def selectImage(self):
        name = self.txt1.get()
        if len(name) != 0:
            path = askopenfilename(parent=self.root)
            # print(path)
            image = cv2.imread(path)

            cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            faces = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=5)

            if len(faces) == 0:
                msg.showwarning("Warning", " Image is not valid" ,parent=self.root)
            else:
                # Clear previous data in the entry widget
                self.txt9.delete(0, 'end')

                # Generate a random number for the image name
                random_number = random.randint(10000, 99999)
                img_name = f"{name}_{random_number}.png"
                name = f"employeeImage/{img_name}"
                cv2.imwrite(name, image)
                self.txt9.insert(0, img_name)
                msg.showinfo("Success", " Image is Valid",parent=self.root)
        else:
            msg.showwarning("Warning", " Enter Name",parent=self.root)


if __name__ == "__main__":
    addemployee()
