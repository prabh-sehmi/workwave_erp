from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect

class ViewAdmin:
    def __init__(self):
        self.root=Toplevel()
        self.root.state("zoomed")

        self.conn=connect()
        self.cr=self.conn.cursor()
        self.text_color = "#F46036"

        self.mainLabel=Label(self.root,text="View Admin",font=('',28,'bold'),fg=self.text_color)
        self.mainLabel.pack()

        self.searchFrame=Frame(self.root)
        self.searchFrame.pack(pady=10)

        self.searchLabel=Label(self.searchFrame,text="Search",font=('',14))
        self.searchLabel.grid(row=0,column=0,padx=10,pady=10)
        self.searchField=Entry(self.searchFrame,font=('',14,'bold'))
        self.searchField.grid(row=0,column=1,padx=10,pady=10)

        self.searchBtn=Button(self.searchFrame,text="Search",font=('',12),width=10,command=self.searchAdmin)
        self.searchBtn.grid(row=0,column=2,padx=10,pady=10)
        self.refreshBtn = Button(self.searchFrame, text="Refresh", font=('', 12), width=10,command=self.refreshData)
        self.refreshBtn.grid(row=0, column=3, padx=10, pady=10)
        self.deletebtn = Button(self.searchFrame, text="Delete Admin", font=('', 12), width=10,command=self.deleteAdmin)
        self.deletebtn.grid(row=0, column=4, padx=10, pady=10)

        self.adminTable=ttk.Treeview(self.root,columns=('id','name','email','mobile','role'))
        self.adminTable.heading('id',text='Admin Id')
        self.adminTable.heading('name',text='Name')
        self.adminTable.heading('email',text='E-Mail')
        self.adminTable.heading('mobile',text='Mobile')
        self.adminTable.heading('role',text='Role')
        self.adminTable['show']='headings'
        self.adminTable.column('id',width=10,anchor='center')
        self.adminTable.column('name', width=10, anchor='center')
        self.adminTable.column('email',width=10,anchor='center')
        self.adminTable.column('mobile',width=10,anchor='center')
        self.adminTable.column('role',width=10,anchor='center''')

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('', 12, 'bold'), rowheight=50, foreground="#FF7F66")
        self.style.configure("Treeview", font=('', 14), rowheight=50)

        self.adminTable.pack(fill='both',padx=20,pady=20)
        self.getAdminInfo()
        self.adminTable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def openUpdateWindow(self,event):
        row=self.adminTable.selection()
        row_id=row[0]
        items=self.adminTable.item(row_id)
        data=items['values']

        self.root1=Toplevel()#Creates a new window
        self.root1.geometry("700x500")

        self.mainLabel1=Label(self.root1,text="Update Admin",font=('',24,'bold'))
        self.mainLabel1.pack(pady=10,padx=10)

        self.updateForm= Frame(self.root1)
        self.updateForm.pack(pady=10,padx=10)

        font=('',14)

        self.lb1=Label(self.updateForm,text="Admin Id",font=font)
        self.txt1=Entry(self.updateForm,font=font)
        self.lb1.grid(row=0,column=0,padx=10,pady=10)
        self.txt1.grid(row=0,column=1,padx=10,pady=10)
        self.txt1.insert(0,data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text="Admin Name", font=font)
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0,data[1])

        self.lb3 = Label(self.updateForm, text="Admin Email", font=font)
        self.txt3 = Entry(self.updateForm, font=font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0,data[2])

        self.lb4 = Label(self.updateForm, text="Admin Mobile", font=font)
        self.txt4 = Entry(self.updateForm, font=font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0,data[3])

        self.lb5 = Label(self.updateForm, text="Admin Role", font=font)
        self.txt5 = ttk.Combobox(self.updateForm, font=font,values=['Super Admin','Admin'],state='readonly')
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.set(data[4])

        self.updateForm.pack(pady=10)
        self.updateBtn = Button(self.root1, text="Update Admin", font=('', 12), width=10,
                                command=self.updateAdmin)
        self.updateBtn.pack(padx=10, pady=10)

        self.root1.mainloop()

    def updateAdmin(self):
        id=self.txt1.get()
        name=self.txt2.get()
        email=self.txt3.get()
        mobile=self.txt4.get()
        role=self.txt5.get()
        print(name,email,mobile,role)

        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(role) == 0:
            msg.showerror("Not Working","Need to fill all fields",parent=self.root)
        else:
            if mobile.isdigit() and len(mobile)==10 :
                if '@' in email and '.' in email :
                    q = f"update admin set name='{name}',email='{email}',mobile='{mobile}',role='{role}' where id='{id}'"
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success","Admin Updated",parent=self.root)
                    self.root1.destroy()
                    self.refreshData()
                else:
                    msg.showwarning("Not working","Email Format Invalid",parent=self.root)
            else:
                msg.showwarning("Not Running ","Invalid Mobile Number",parent=self.root)

    def getAdminInfo(self):
        q="select id,name,email,mobile,role from admin"
        self.cr.execute(q)

        result=self.cr.fetchall()

        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        for i in range(len(result)):
            self.adminTable.insert('',index=i,values=result[i])

    def searchAdmin(self):
        data=self.searchField.get()
        q=f"select id,name,email,mobile,role from admin where name like '%{data}%'"
        print(q)
        self.cr.execute(q)
        result=self.cr.fetchall()
        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        for i in range(len(result)):
            self.adminTable.insert('',index=i,values=result[i])

    def refreshData(self):
        self.searchField.delete(0,'end')
        self.getAdminInfo()

    def deleteAdmin(self):
        row = self.adminTable.selection()
        if len(row)==0:
            msg.showwarning("Warning","Please select the Item",parent=self.root)
        else:
            row_id=self.adminTable.selection()[0]
            items=self.adminTable.item(row_id)
            data=items['values']
            #print(data)
            confirm=msg.askyesno("","Are you sure you want to delete ?",parent=self.root)
            if confirm:
                q=f"delete from admin where id='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success","Deleted Successfully",parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success","Deletion Aborted",parent=self.root)



if __name__ == "__main__":
    ViewAdmin()