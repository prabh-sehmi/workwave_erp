from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
from PIL import Image,ImageTk
from customtkinter import ctk_tk
from adminlogin import adminLogin
from attendance import attendance
from employeelogin import employeelogin
from datetime import datetime

class mainwindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main Window")
        self.root.state("zoomed")
        self.frame=Frame(self.root)
        button_style = {
            "font": ("Helvetica", 14,"bold"),
            "bg": "#FF7F66",
            "fg": "#FFF6E5",
            "activebackground": "#AFCC2F",
            "activeforeground": "white",
            "relief": "raised",
            "borderwidth": 0,
            "highlightthickness": 0

        }


        img=Image.open("images/mainImage.jpeg")
        width=int(self.root.winfo_screenwidth())
        height=int(self.root.winfo_screenheight())
        print(width,height)
        img=img.resize((width,height))
        bg=ImageTk.PhotoImage(img)
        c=Canvas(self.root,width=width,height=height)
        c.pack(fill='both',expand=True)
        c.create_image(0,0,image=bg,anchor='nw')



        c.create_text(790 + 13, 35 + 43, text="WorkWave ERP System", font=("Arial", 44, "bold"), fill="#6BBFBF")
        c.create_text(790+10, 35+40, text="WorkWave ERP System", font=("Arial", 44, "bold"), fill="#208C81")

        self.adLogBtn = Button(self.root, text="Admin Side", width=17, height=2, command=lambda: adminLogin(),**button_style)
        a_window=c.create_window(300,410,anchor="nw",window=self.adLogBtn)
        self.epLogBtn = Button(self.root, text="Employee Side", width=17, height=2, command=lambda: employeelogin(),**button_style)
        e_window = c.create_window(300, 480, anchor="nw", window=self.epLogBtn)
        self.back = Button(self.root, text="Exit", width=13, height=2, command=lambda: self.root.destroy(),**button_style,)
        x_window = c.create_window(1700, 50, anchor="nw", window=self.back)
        # Camera Button
        self.cameraBtn = Button(self.root, text="Camera", width=23, height=1, command=lambda :attendance(),
                                **button_style)
        x_window = c.create_window(225, 550, anchor="nw", window=self.cameraBtn)



        self.root.mainloop()

        self.root.mainloop()


if __name__ == "__main__":
    mainwindow = mainwindow()