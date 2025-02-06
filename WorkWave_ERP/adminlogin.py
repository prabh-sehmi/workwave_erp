from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from PIL import Image, ImageTk  # Import PIL modules for image handling
import pymysql
from connection import connect
from admindashboard import adminDashboard

class adminLogin:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Admin Login")
        self.root['background'] = '#FFFFFF'

        self.font=("Arial", 20, "bold")
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
        image = image.resize((380,240))  # Resize image as per your requirement
        photo = ImageTk.PhotoImage(image)

        # Create label to display image
        self.image_label = Label(self.root, image=photo, bg=self.bg_color)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(side=TOP, fill=Y, padx=20, pady=20)  # Pack image label on the left side

        self.mainLabel = Label(self.root, text="Admin Login", font=('Arial', 24, 'bold'), bg=self.bg_color, fg="#6BBFBF")
        self.mainLabel.pack(pady=20)

        self.loginForm = Frame(self.root, bg=self.bg_color)

        self.lb1 = Label(self.loginForm, text="Enter Email", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.t1 = Entry(self.loginForm, font=self.font,bg=self.sec_color,width=20)
        self.t1.grid(row=0, column=1, pady=10, padx=20, sticky="e")

        self.lb2 = Label(self.loginForm, text="Enter Password", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.t2 = Entry(self.loginForm, font=self.font, show='*',bg=self.sec_color,width=20)
        self.t2.grid(row=1, column=1, pady=10, padx=20, sticky="e")

        self.loginForm.pack(pady=10)

        self.loginButton = Button(self.root, text="Login", font=self.font, command=self.checkAdmin, bg='#6BBFBF', fg="white", activebackground=self.button_hover_color, activeforeground="white",width=10)
        self.loginButton.pack(pady=20)

        # Bind hover effects to the login button
        self.loginButton.bind("<Enter>", self.on_enter)
        self.loginButton.bind("<Leave>", self.on_leave)

        # Make window responsive
        self.root.pack_propagate(0)
        self.root.geometry("800x700")
        self.root.minsize(200, 100)  # Set minimum window size

        self.root.mainloop()

    def checkAdmin(self):
        email = self.t1.get()
        password = self.t2.get()

        q = f"SELECT id,email,name,mobile,role  FROM admin WHERE email = '{email}' and password = '{password}'"
        self.cr.execute(q)
        result = self.cr.fetchone()
        if result is None:
            msg.showwarning("Not Found", "Enter a valid e-mail or password",parent=self.root)
        else:
            print(result)
            msg.showinfo("Found", "Login Successful")
            self.root.destroy()
            adminDashboard(adminDetails=result)

    def on_enter(self, event):
        # Change background color when mouse enters button
        self.loginButton.config(bg=self.button_hover_color)

    def on_leave(self, event):
        # Restore background color when mouse leaves button
        self.loginButton.config(bg=self.button_color)


if __name__ == "__main__":
    admin = adminLogin()

