from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import tkinter as tk
from connection import connect
from tkinter.filedialog import askopenfilename
import cv2
import random


class viewemployee:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("View Course")
        self.root.state("zoomed")
        self.font = ("", 14)
        self.text_color = "#F46036"

        self.conn = connect()
        self.cr = self.conn.cursor()

        self.mainLabel = Label(self.root, text="View Employee", font=("", 32, 'bold'),fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.form = Frame(self.root)
        self.form.pack(pady=10)

        self.searchLabel = Label(self.form, text="Search", font=self.font)
        self.searchLabel.grid(row=0, column=0, padx=20, pady=20)
        self.searchField = Entry(self.form, width=35, font=self.font)
        self.searchField.grid(row=0, column=1, padx=20, pady=20)

        self.searchBtn = Button(self.form, text="Search", font=self.font, command=self.searchemployee)
        self.searchBtn.grid(row=0, column=2, padx=20, pady=20)
        self.refreshBtn = Button(self.form, text="Refresh", font=self.font, command=self.refreshData)
        self.refreshBtn.grid(row=0, column=3, padx=20, pady=20)
        self.deleteBtn = Button(self.form, text="Delete", font=self.font, command=self.deleteemployee)
        self.deleteBtn.grid(row=0, column=4, padx=20, pady=20)

        self.employeetable = ttk.Treeview(self.root, column=(
            'employee_id', 'name', 'father_name', 'email', 'mobile', 'address', 'category', 'department', 'image',))
        self.employeetable.heading('employee_id', text="ID", anchor="center",
                                   command=lambda: self.sort_column('employee_id'))
        self.employeetable.heading('name', text="Name", anchor="center", command=lambda: self.sort_column('name'))
        self.employeetable.heading('father_name', text="Father Name", anchor="center",
                                   command=lambda: self.sort_column('father_name'))
        self.employeetable.heading('email', text="Email", anchor="center", command=lambda: self.sort_column('email'))
        self.employeetable.heading('mobile', text="Mobile", anchor="center", command=lambda: self.sort_column('mobile'))
        self.employeetable.heading('address', text="Address", anchor="center",
                                   command=lambda: self.sort_column('address'))
        self.employeetable.heading('category', text="Category", anchor="center",
                                   command=lambda: self.sort_column('category'))
        self.employeetable.heading('department', text="Department", anchor="center",
                                   command=lambda: self.sort_column('department'))
        self.employeetable.heading('image', text="Image", anchor="center", command=lambda: self.sort_column('image'))

        self.employeetable['show'] = 'headings'

        self.employeetable.column('employee_id', width=50, anchor="center")
        self.employeetable.column('name', width=150, anchor="center")
        self.employeetable.column('father_name', width=150, anchor="center")
        self.employeetable.column('email', width=200, anchor="center")
        self.employeetable.column('mobile', width=100, anchor="center")
        self.employeetable.column('address', width=200, anchor="center")
        self.employeetable.column('category', width=100, anchor="center")
        self.employeetable.column('department', width=100, anchor="center")
        self.employeetable.column('image', width=100, anchor="center")

        self.employeetable.pack( fill='both', padx=20, pady=20)

        self.getemployeeinfo()

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('', 12, 'bold'), rowheight=50, foreground="#FF7F66")
        self.style.configure("Treeview", font=('', 14), rowheight=50)

        self.employeetable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def getemployeeinfo(self):
        q = "select id,name,father_name,email,mobile,address,category,department,image from employee"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.employeetable.get_children():
            self.employeetable.delete(row)

        for i in range(len(result)):
            self.employeetable.insert('', index=i, values=result[i])

    def openUpdateWindow(self, event):
        row = self.employeetable.selection()
        row_id = row[0]
        items = self.employeetable.item(row_id)
        data = items['values']

        self.root1 = Toplevel()
        self.root1.geometry("900x900")

        self.mainlabel1 = Label(self.root1, text="Update Employee", font=('', 24, 'bold'))
        self.mainlabel1.pack(pady=20)

        self.updateForm = Frame(self.root1)

        font = ('', 14)

        self.lb1 = Label(self.updateForm, text=" ID ", font=font)
        self.txt1 = Entry(self.updateForm, font=font,width=30)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text=" Name ", font=font)
        self.txt2 = Entry(self.updateForm, font=font,width=30)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.updateForm, text=" Father Name ", font=font)
        self.txt3 = Entry(self.updateForm, font=font,width=30)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.updateForm, text=" Email ", font=font)
        self.txt4 = Entry(self.updateForm, font=font,width=30)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.updateForm, text=" Mobile ", font=font)
        self.txt5 = Entry(self.updateForm, font=font,width=30)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[4])

        self.lb6 = Label(self.updateForm, text=" Address ", font=font)
        self.txt6 = Entry(self.updateForm, font=font,width=30)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[5])

        self.lb7 = Label(self.updateForm, text=" Category ", font=font)
        self.txt7 = ttk.Combobox(self.updateForm, font=font, values=self.values(),width=28)
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7.grid(row=6, column=1, padx=10, pady=10)
        self.txt7.insert(0, data[6])

        self.lb8 = Label(self.updateForm, text=" Department ", font=font)
        self.txt8 = ttk.Combobox(self.updateForm, font=font, values=self.values1(),width=28)
        self.lb8.grid(row=7, column=0, padx=10, pady=10)
        self.txt8.grid(row=7, column=1, padx=10, pady=10)
        self.txt8.insert(0, data[7])

        # self.lb10 = Label(self.updateForm, text=" Image ", font=font)
        # self.txt10 = Entry(self.updateForm, font=font)
        # self.lb10.grid(row=9, column=0, padx=10, pady=10)
        # self.txt10.grid(row=9, column=1, padx=10, pady=10)
        # self.txt10.insert(0, data[8])

        self.lb9 = Label(self.updateForm, text=" Image ", font=self.font)
        self.lb9.grid(row=8, column=0, padx=10, pady=10)
        self.txt9 = Entry(self.updateForm, font=self.font,width=30)
        self.txt9.grid(row=8, column=1, padx=10, pady=10)
        self.btn1 = Button(self.updateForm, text='select', width=10, font=self.font, command=self.selectImage)
        self.btn1.grid(row=8, column=2, padx=10, pady=10)
        self.txt9.insert(0, data[8])
        self.updateForm.pack(pady=10)

        self.updateBtn = Button(self.root1, text="Update", font=('', 12), width=10, command=self.updateemployee)
        self.updateBtn.pack(pady=20)

        self.root1.mainloop()

    def updateemployee(self):
        id = self.txt1.get()
        name = self.txt2.get()
        father_name = self.txt3.get()
        email = self.txt4.get()
        mobile = self.txt5.get()
        address = self.txt6.get()
        category = self.txt7.get()
        department = self.txt8.get()
        image = self.txt9.get()

        if (len(name) == 0 or len(father_name) == 0 or len(email) == 0 or len(mobile) == 0 or len(address) == 0 or
                len(category) == 0 or len(department) == 0 or len(image) == 0):
            msg.showwarning("Warning", "Please enter all fields", parent=self.root)
        else:
            if '@' in self.txt4.get() and '.' in self.txt4.get():
                if len(self.txt5.get()) == 10 and self.txt5.get().isdigit():
                    q = (
                        f"update employee set name='{name}', father_name='{father_name}',  mobile='{mobile}',email='{email}',address='{address}',department='{department}',category='{category}',image='{image}' WHERE id='{id}'")
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success", "Employee has been updated", parent=self.root)
                    self.root1.destroy()
                    self.refreshData()
                else:
                    msg.showwarning("Warning", "Please enter valid Mobile Number", parent=self.root)
            else:
                msg.showwarning("Warning", "Please enter valid Email ", parent=self.root)

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

    def refreshData(self):
        self.searchField.delete(0, 'end')
        self.getemployeeinfo()

    def searchemployee(self):
        data = self.searchField.get()
        q = f"select id,name,father_name,email,mobile,address,category,department,image from employee where name like '%{data}%' or address like '%{data}%'"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.employeetable.get_children():
            self.employeetable.delete(row)

        for i in range(len(result)):
            self.employeetable.insert('', index=i, values=result[i])

    def deleteemployee(self):
        row = self.employeetable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "Please select the Item", parent=self.root)
        else:
            row_id = row[0]
            items = self.employeetable.item(row_id)
            data = items['values']

            confirm = msg.askyesno("", "Are you sure you want to Delete ?", parent=self.root)
            if confirm:
                q = f"delete from employee where employee_id='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "Employee has been deleted", parent=self.root)
                self.refreshData()
            else:
                msg.showwarning("Success", "Deletion Aborted", parent=self.root)

    def selectImage(self):
        name = self.txt2.get()
        if len(name) != 0:
            path = askopenfilename(parent=self.root)
            # print(path)
            image = cv2.imread(path)

            cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            faces = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=5)

            if len(faces) == 0:
                msg.showwarning("Warning", " Image is not valid", parent=self.root1)
            else:
                # Clear previous data in the entry widget
                self.txt9.delete(0, 'end')

                # Generate a random number for the image name
                random_number = random.randint(10000, 99999)
                img_name = f"{name}_{random_number}.png"
                name = f"employeeImage/{img_name}"
                cv2.imwrite(name, image)
                self.txt9.insert(0, img_name)
                msg.showinfo("Success", " Image is Valid", parent=self.root1)
        else:
            msg.showwarning("Warning", " Enter Name", parent=self.root1)


if __name__ == "__main__":
    viewemployee()
