from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
from changeemployeepassword import changePassword
from leave import LeaveApplication
from viewleaveemployee import viewleaveemployee
from messages import messages
from attendance import attendance
from PIL import Image, ImageTk
from datetime import datetime

class employeedashboard:
    def __init__(self, employeedetails):
        self.employeedetails = employeedetails

        self.root = Toplevel()
        self.root.state("zoomed")
        self.root.title("Welcome to Employee Dashboard")
        self.font = ("Arial", 10)

        # self.mainLabel = Label(self.root, text=f"Welcome {self.employeedetails[2]} to your dashboard",
        #                        font=('', 24, 'bold'))
        # self.mainLabel.pack(pady=20)
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

        # Load background image
        img = Image.open("images/erpImage.png")
        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        print(width, height)
        img = img.resize((width, height))
        bg = ImageTk.PhotoImage(img)
        c = Canvas(self.root, width=width, height=height)
        c.pack(fill='both', expand=True)
        c.create_image(0, 0, image=bg, anchor='nw')

        # # Create label for background image
        # bg_label = Label(self.root, image=bg_photo)
        # bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        c.create_text(890 + 13, 35 + 43, text=f"Welcome {self.employeedetails[2]} to your dashboard",font=("Arial", 44, "bold"), fill="#6BBFBF")
        c.create_text(890 + 10, 35 + 40, text=f"Welcome {self.employeedetails[2]} to your dashboard", font=("Arial", 44, "bold"), fill="#208C81")

        self.mainMenu = Menu(self.root)
        self.root.configure(menu=self.mainMenu)

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Manage Change Password", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Change Password", command=lambda: changePassword(employeedetails[1]))


        self.adminSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Manage Leave Application", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Leave Application", command=lambda: LeaveApplication(employeedetails))
        self.adminSubMenu.add_command(label="View Leave",command=lambda: viewleaveemployee(employeedetails[0]))

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Manage Send Message", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Send Message", command=lambda: messages(employeedetails[0]))

        logoutBtn = Button(self.root, text="Logout", width=15, height=2, command=lambda: self.root.destroy(),**button_style)
        logoutBtn.place(x=1700, y=60)

        self.root.mainloop()
if __name__ == "__main__":
    employee = employeedashboard(employeedetails=(2, 'Jatin', 'fwe', 'j@gmail.com','9876543210', 'fdgcbc', 'Computer ', 'Computer Science', 'tyu','0000'))
