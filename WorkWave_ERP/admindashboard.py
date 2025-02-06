from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
from PIL import Image, ImageTk
from viewadmin import ViewAdmin
from addadmin import addAdmin
from viewCategory import viewCategory
from addCategory import AddCategory
from changePassword import Main
from addhod import addhod
from viewhod import viewhod
from admin_profile import adminProfile
from viewleaveadmin import ViewLeaveAdmin
from viewmessagesadmin import viewmessagesadmit
from getattendanceadmin import getattendance
from addemployee import addemployee
from viewemployee import viewemployee
from adddepartment import addDepartment
from view_department import viewdepartment
class adminDashboard:
    def __init__(self,adminDetails):

        self.adminDetails = adminDetails
        print(adminDetails)
        self.root = Toplevel()
        self.root.state('zoomed')
        self.root.title('Welcome to Admin Dashboard')
        button_style = {
            "font": ("Helvetica", 14, "bold"),
            "bg": "#FF7F66",
            "fg": "#FFF6E5",
            "activebackground": "#AFCC2F",
            "activeforeground": "white",
            "relief": "raised",
            "borderwidth": 0,
            "highlightthickness": 0

        }
        # Add background image
        img = Image.open("images/adminDashboard.jpeg")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        img = img.resize((width, height))
        bg = ImageTk.PhotoImage(img)
        c = Canvas(self.root, width=width, height=height)
        c.pack(fill='both', expand=True)
        c.create_image(0, 0, image=bg, anchor='nw')

        # Add title text
        c.create_text(890 + 13, 35 + 43, text=f"Welcome {self.adminDetails[2]} to your dashboard",
                      font=("Arial", 44, "bold"), fill="#F46036")
        c.create_text(890 + 10, 35 + 40, text=f"Welcome {self.adminDetails[2]} to your dashboard",
                      font=("Arial", 44, "bold"), fill="#F46036")

        viewattendanceBtn = Button(self.root, text="View Record", width=15, height=2,
                               command=lambda: getattendance(), **button_style)
        viewattendanceBtn.place(x=400, y=200)

        self.mainMenu = Menu(self.root)
        self.root.configure(menu=self.mainMenu)

        if (adminDetails[4]=="SuperAdmin"):
            self.adminSubMenu = Menu(self.mainMenu,tearoff=0)
            self.mainMenu.add_cascade(label="Manage Admin",menu=self.adminSubMenu)
            self.adminSubMenu.add_command(label="Add Admin",command= lambda: addAdmin())
            self.adminSubMenu.add_command(label="View Admin",command= lambda : ViewAdmin())



        self.adminSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Manage Category", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add Category", command=lambda: AddCategory())
        self.adminSubMenu.add_command(label="View Category", command=lambda: viewCategory())

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Manage HOD", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add HOD", command=lambda: addhod())
        self.adminSubMenu.add_command(label="View HOD", command=lambda: viewhod())

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Manage Department", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add Department", command=lambda: addDepartment())
        self.adminSubMenu.add_command(label="View Department", command=lambda: viewdepartment())

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Manage Employee", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add Employee", command=lambda: addemployee())
        self.adminSubMenu.add_command(label="View Employee", command=lambda: viewemployee())

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Manage Leaves",command=lambda: ViewLeaveAdmin())

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="View Messages", command=lambda: viewmessagesadmit())

        self.profileSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Profile", menu=self.profileSubMenu)
        self.profileSubMenu.add_command(label="Change Password", command=lambda: Main(adminDetails[1]))
        self.profileSubMenu.add_command(label="Manage Profile", command=lambda: adminProfile(adminDetails))
        self.profileSubMenu.add_command(label="Logout", command=lambda: self.root.destroy())

        # self.mainLabel=Label(self.root,text=f"Welcome {self.adminDetails[2]} to your Dashboard",font=('',28,'bold'))
        # self.mainLabel.pack(pady=20,padx=20)

        # self.root.mainloop()


        self.root.mainloop()

    def createFile(self):
        print("created")
if __name__ == "__main__":
    admin=adminDashboard(adminDetails=(1, 'gagan445@gmail.com', 'Gagan', '99209929233', 'SuperAdmin'))