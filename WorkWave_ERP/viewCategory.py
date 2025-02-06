from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
import pymysql
class viewCategory:
    def __init__(self):
        self.root = Toplevel()
        self.root.state('zoomed')
        self.text_color = "#F46036"

        self.conn = connect()
        self.cr = self.conn.cursor()

        self.ml=Label(self.root,text="View Category",font=('',36,'bold'),fg=self.text_color)
        self.ml.pack(padx=10,pady=10)

        self.searchFrame=Frame(self.root)
        self.searchFrame.pack(padx=10,pady=10)

        self.searchLabel = Label(self.searchFrame, text="Search", font=('', 14))
        self.searchLabel.grid(row=0, column=0, padx=10, pady=10)
        self.searchField = Entry(self.searchFrame, font=('', 14, 'bold'))
        self.searchField.grid(row=0, column=1, padx=10, pady=10)

        self.searchBtn = Button(self.searchFrame, text="Search", font=('', 12, ''),width=10,command=self.searchBtn)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=10)

        self.refreshBtn = Button(self.searchFrame, text="Refresh", font=('', 12, ''),width=10,command=self.refreshData)
        self.refreshBtn.grid(row=0, column=3, padx=10, pady=10)

        self.deleteBtn = Button(self.searchFrame, text="Delete", font=('',12,''),width=10,command=self.deleteBtn)
        self.deleteBtn.grid(row=0, column=4, padx=10, pady=10)

        self.categoryTable=ttk.Treeview(self.root,columns=('name','description'))
        self.categoryTable.heading('name',text='Category')
        self.categoryTable.heading('description',text='About')
        self.categoryTable['show']='headings'

        self.categoryTable.column('name',width=10,anchor='center')
        self.categoryTable.column('description',width=10,anchor='center')

        self.style=ttk.Style()
        self.style.configure("Treeview.Heading",font=('',12,'bold'),rowheight=50,foreground="#FF7F66")
        self.style.configure("Treeview",font=('',14),rowheight=50)

        self.categoryTable.pack(fill='both', padx=20, pady=20)
        self.categoryInfo()
        self.categoryTable.bind("<Double-1>",self.openUpdateWindow)


        self.root.mainloop()

    def categoryInfo(self):
        q="Select * from category"
        self.cr.execute(q)
        result=self.cr.fetchall()
        for row in self.categoryTable.get_children():
            self.categoryTable.delete(row)
        for i in range(len(result)):
            self.categoryTable.insert('',index=i,values=result[i])

    def refreshData(self):
        self.searchField.delete(0,'end')
        self.categoryInfo()

    def searchBtn(self):
        data=self.searchField.get()
        q=f"select * from category where name like'%{data}%' "
        self.cr.execute(q)
        result=self.cr.fetchall()
        for row in self.categoryTable.get_children():
            self.categoryTable.delete(row)
        for i in range(len(result)):
            self.categoryTable.insert('',index=i,values=result[i])

    def deleteBtn(self):
        row=self.categoryTable.selection()
        if len(row)==0:
            msg.showwarning("Invalid","Please select a row you want to delete",parent=self.root)
        else:
            row_id=self.categoryTable.selection()[0]
            item=self.categoryTable.item(row_id)
            data=item['values']
            confirm=msg.askyesno("","Are you sure you want to Delete Category?",parent=self.root)
            if confirm :
                q=f"delete from category where name='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success ","Deleted Successfully",parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success","Deletion Aborted",parent=self.root)

    def openUpdateWindow(self,event):
        row=self.categoryTable.selection()
        row_id=row[0]
        items=self.categoryTable.item(row_id)
        data=items['values']

        self.root1=Toplevel()
        self.root1.geometry("700x500")

        self.ml=Label(self.root1,text="Category",font=('',36,'bold'))
        self.ml.pack(padx=20,pady=20)

        self.updateForm=Frame(self.root1)
        self.updateForm.pack(padx=20,pady=20)

        font=('',14)

        '''self.lb1 = Label(self.updateForm, text="Id", font=font)
        self.txt1 = Entry(self.updateForm, font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')'''

        self.l2 =Label(self.updateForm,text="Name", font=font)
        self.txt2 = Entry(self.updateForm, font=font)
        self.l2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0,data[0])
        self.txt2.configure(state='readonly')

        self.l3 = Label(self.updateForm,text="description",font=font)
        self.l3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = Entry(self.updateForm, font=font)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0,data[1])
        self.updateBtn = Button(self.root1, text="Update Admin", font=('', 12), width=10,
                                command=self.updateCategory)
        self.updateBtn.pack(padx=10, pady=10)
        self.root1.mainloop()

    def updateCategory(self):
        if self.txt2.get() == '' and self.txt3.get() == '':
            msg.showerror("Not Running","Please Enter all fields")
        else:
            #id=self.txt1.get()
            name = self.txt2.get()
            description = self.txt3.get()
            q = f"update category set description='{description}' where name='{name}'"
            self.cr.execute(q)
            self.conn.commit()
            msg.showinfo("Success","Updated",parent=self.root)
            self.root1.destroy()
            self.refreshData()
if __name__ == '__main__':
    viewCategory = viewCategory()