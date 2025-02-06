from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import pymysql
from connection import connect
from employeedashboard import employeedashboard
class employeelogin:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Employee Login")
        self.root['background'] = '#FFFFFF'

        self.font = ("Arial", 20, "bold")
        self.conn = connect()
        self.cr = self.conn.cursor()

        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"
        self.text_color = "#6BBFBF"
        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        # Load and resize image
        image = Image.open("images/Login.jpg")  # Change to your image file path
        image = image.resize((380, 240))  # Resize image as per your requirement
        photo = ImageTk.PhotoImage(image)

        # Create label to display image
        self.image_label = Label(self.root, image=photo, bg=self.bg_color)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(side=TOP, fill=Y, padx=20, pady=20)  # Pack image label on the left side


        self.mainLabel = Label(self.root,text="Employee Login",font=('Arial',24,'bold'),bg=self.bg_color, fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.loginForm = Frame(self.root,bg=self.bg_color)

        self.lb1=Label(self.loginForm,text="Enter Email",font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0,column=0,pady=20,padx=20)

        self.t1= Entry(self.loginForm,font=self.font,bg=self.sec_color,width=20)
        self.t1.grid(row=0,column=1,pady=20,padx=20)

        self.lb2=Label(self.loginForm,text="Enter Password",font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1,column=0,pady=20,padx=20)

        self.t2= Entry(self.loginForm,font=self.font,bg=self.sec_color,width=20,show='*')
        self.t2.grid(row=1,column=1,pady=20,padx=20)

        self.loginForm.pack(pady=10)

        self.loginButton = Button(self.root,text="Login",width=15,font=self.font,command=self.checkAdmin,bg=self.button_color, fg="white", activebackground=self.button_hover_color, activeforeground="white")
        self.loginButton.pack(pady=20)

        # Make window responsive
        self.root.pack_propagate(0)
        self.root.geometry("800x700")
        self.root.minsize(200, 100)  # Set minimum window size

        self.root.mainloop()

    def checkAdmin(self):
        email = self.t1.get()
        password = self.t2.get()

        q = f"SELECT id,email,name,mobile FROM employee WHERE email = '{email}' and password = '{password}'"
        self.cr.execute(q)
        result = self.cr.fetchone()
        if result is None:
            msg.showwarning("Not Found","Enter a valid e-mail or password",parent=self.root)
        else:
            print(result)
            msg.showinfo("Found","Login Successful",parent=self.root)
            self.root.destroy()
            # adminDashboard(adminDetails= result)
            employeedashboard(employeedetails=result)
if __name__ == "__main__":
    employeelogin()