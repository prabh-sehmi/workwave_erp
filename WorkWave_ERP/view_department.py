from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect

class viewdepartment:

    def __init__(self):
        self.root = Toplevel()
        self.root.state("zoomed")
        self.text_color = "#F46036"

        self.conn = connect()
        self.cr = self.conn.cursor()

        self.mainLabel = Label(self.root, text="View Department", font=('', 28, 'bold'),fg=self.text_color)
        self.mainLabel.pack()

        self.searchFrame = Frame(self.root)
        self.searchFrame.pack(pady=10)

        self.searchLabel = Label(self.searchFrame, text="Search", font=('', 14))
        self.searchLabel.grid(row=0, column=0, padx=10, pady=10)
        self.searchField = Entry(self.searchFrame, font=('', 14, 'bold'))
        self.searchField.grid(row=0, column=1, padx=10, pady=10)

        self.searchBtn = Button(self.searchFrame, text="Search", font=('', 12), width=10, command=self.searchhod)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=10)
        self.refreshBtn = Button(self.searchFrame, text="Refresh", font=('', 12), width=10, command=self.refreshData)
        self.refreshBtn.grid(row=0, column=3, padx=10, pady=10)
        self.deletebtn = Button(self.searchFrame, text="Delete HOD", font=('', 12), width=10, command=self.deletehod)
        self.deletebtn.grid(row=0, column=4, padx=10, pady=10)

        self.hodTable = ttk.Treeview(self.root, columns=('name', 'email', 'mobile', 'hod_id'),
                                     style='Custom.Treeview')
        self.hodTable.heading('hod_id', text='HOD Name')
        self.hodTable.heading('name', text='Name')
        self.hodTable.heading('email', text='E-Mail')
        self.hodTable.heading('mobile', text='Mobile')
        self.hodTable['show'] = 'headings'
        self.hodTable.column('hod_id', width=100, anchor='center')
        self.hodTable.column('name', width=200, anchor='center')
        self.hodTable.column('email', width=200, anchor='center')
        self.hodTable.column('mobile', width=150, anchor='center')


        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Custom.Treeview.Heading", font=('', 14, 'bold'), background=self.text_color, foreground='white',
                             relief='flat')
        self.style.configure("Custom.Treeview", font=('', 12), background='#D3D3D3', fieldbackground='#D3D3D3',
                             relief='flat')

        self.hodTable.pack(fill='both', padx=20, pady=20)
        self.gethodInfo()
        self.hodTable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def openUpdateWindow(self,event):
        row=self.hodTable.selection()
        row_id=row[0]
        items=self.hodTable.item(row_id)
        data=items['values']

        self.root1=Toplevel()#Creates a new window
        self.root1.geometry("700x500")

        self.mainLabel1=Label(self.root1,text="Update Department",font=('',24,'bold'))
        self.mainLabel1.pack(pady=10,padx=10)

        self.updateForm= Frame(self.root1)
        self.updateForm.pack(pady=10,padx=10)

        font=('',14)



        self.lb2 = Label(self.updateForm, text="Department Name", font=font)
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0,data[0])
        self.txt2.configure(state='readonly')

        self.lb3 = Label(self.updateForm, text="Department Email", font=font)
        self.txt3 = Entry(self.updateForm, font=font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0,data[1])

        self.lb4 = Label(self.updateForm, text="Department Mobile", font=font)
        self.txt4 = Entry(self.updateForm, font=font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0,data[2])

        self.lb5 = Label(self.updateForm, text="HOD Name", font=font)
        self.txt5 = ttk.Combobox(self.updateForm, font=font,values= self.fetchhod())
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[3])



        self.updateForm.pack(pady=10)
        self.updateBtn = Button(self.root1, text="Update HOD", font=('', 12), width=10,
                                command=self.updatehod)
        self.updateBtn.pack(padx=10, pady=10)

        self.root1.mainloop()

    def fetchhod(self):
        q=" select * from hod "
        self.cr.execute(q)
        result = self.cr.fetchall()
        list=[]
        for i in result :
            list.append(i[1])

        return list
    def getHodName(self,name):
        name=name
        q=f"select id from hod where name='{name}'"
        self.cr.execute(q)
        row=self.cr.fetchall()
        for i in row:
            return i[0]

    def updatehod(self):
        name=self.txt2.get()
        email=self.txt3.get()
        mobile=self.txt4.get()
        qualifications=self.txt5.get()
        hod_id = self.getHodName(qualifications)
        print(name,email,mobile,qualifications)

        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(qualifications) == 0:
            msg.showerror("Not Working","Need to fill all fields",parent=self.root)
        else:
            if mobile.isdigit() and len(mobile)==10 :
                if '@' in email and '.' in email :
                    q = f"update department set email='{email}',mobile='{mobile}',hod_id='{hod_id}' where name='{name}'"
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success","HOD Updated",parent=self.root)
                    self.root1.destroy()
                    self.refreshData()
                else:
                    msg.showwarning("Not working","Email Format Invalid",parent=self.root)
            else:
                msg.showwarning("Not Running ","Invalid Mobile Number",parent=self.root)

    def gethodInfo(self):
        q=f"select department.name,department.email,department.mobile,hod.name from department inner join hod on department.hod_id=hod.id"

        self.cr.execute(q)

        result=self.cr.fetchall()

        for row in self.hodTable.get_children():
            self.hodTable.delete(row)

        for i in range(len(result)):
            self.hodTable.insert('',index=i,values=result[i])

    def searchhod(self):
        data=self.searchField.get()
        q=f"select department.name,department.email,department.mobile,hod.name from department inner join hod on department.hod_id=hod.id where department.name like '%{data}%'"
        print(q)
        self.cr.execute(q)
        result=self.cr.fetchall()
        for row in self.hodTable.get_children():
            self.hodTable.delete(row)

        for i in range(len(result)):
            self.hodTable.insert('',index=i,values=result[i])

    def refreshData(self):
        self.searchField.delete(0,'end')
        self.gethodInfo()

    def deletehod(self):
        row = self.hodTable.selection()
        if len(row)==0:
            msg.showwarning("Warning","Please select the Item",parent=self.root)
        else:
            row_id=self.hodTable.selection()[0]
            items=self.hodTable.item(row_id)
            data=items['values']
            #print(data)
            confirm=msg.askyesno("","Are you sure you want to delete ?",parent=self.root)
            if confirm:
                q=f"delete from department where name='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success","Deleted Successfully",parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success","Deletion Aborted",parent=self.root)



if __name__ == "__main__":
    viewdepartment()