import datetime
from tkinter import *
from PIL import Image, ImageTk
import cv2
from deepface import DeepFace
import os
import tkinter.messagebox as msg
from connection import connect
import email_varification
import tkinter
from tkinter import PhotoImage


class attendance:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Employee ERP || Attendance")
        self.root.state("zoomed")

        self.font = ('Times New Roman', 14)
        self.font1 = ('Times New Roman', 16, 'bold')

        self.mainBackground = "white"
        self.frameBackground = "#F46036"

        self.root.configure(bg=self.mainBackground)
        self.conn = connect()
        self.cr = self.conn.cursor()

        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        print(width, height)
        # 1280,800
        self.root.columnconfigure(1, weight=1)  # Expand the right column

        self.frame = Frame(self.root, pady=10, padx=10, bg=self.mainBackground, width=int(width), height=int(height))
        self.frame.pack(expand=True, fill='both')
        self.frame.pack_propagate(0)

        width_1 = int(self.frame.winfo_screenwidth() / 2)
        height_2 = int(self.frame.winfo_screenheight() - 200)

        # print(width_1,height_2)
        # 1280,600

        self.frame1 = Frame(self.frame, highlightthickness=4, highlightbackground='black', width=int(width_1),
                            height=int(height_2), bg=self.frameBackground, padx=10, pady=10)
        self.frame1.grid(row=0, column=0, padx=12, pady=35)
        self.frame1.grid_propagate(0)

        self.frame2 = Frame(self.frame, highlightthickness=4, bg=self.frameBackground, highlightbackground='black',
                            width=width_1, height=height_2)
        self.frame2.grid(row=0, column=1, pady=35)
        self.frame2.grid_propagate(0)

        self.mainLabel1 = Label(self.frame1, text="EMPLOYEE ERP", font=("Times New Roman", 20, 'bold'), fg='black',
                                bg=self.frameBackground,
                                )
        self.mainLabel1.pack(padx=30, pady=10)
        self.frm = Frame(self.frame1, bg=self.mainBackground)
        self.frm.pack(pady=10, padx=30)
        self.lb1 = Label(self.frm, text='Employee ID:', font=self.font, bg=self.mainBackground)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = Entry(self.frm, font=self.font, width=25, highlightthickness=4, highlightbackground='black')
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = Label(self.frm, text='Employee Name:', font=self.font, bg=self.mainBackground)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = Entry(self.frm, font=self.font, width=25, highlightbackground='black', highlightthickness=4)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = Label(self.frm, text='Date:', font=self.font, bg=self.mainBackground)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = Entry(self.frm, font=self.font, width=25, highlightthickness=4, highlightbackground='black')
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = Label(self.frm, text='Timing:', font=self.font, bg=self.mainBackground)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = Entry(self.frm, font=self.font, width=25, highlightthickness=4, highlightbackground='black')
        self.txt4.grid(row=3, column=1, padx=10, pady=10)


        self.btn = Button(self.frame1, text='Submit', font=self.font, width=20, relief=tkinter.SOLID,
                          borderwidth=2, command=self.getSubmit)

        self.btn.pack(pady=42, padx=25)

        self.btn.bind("<Enter>", self.on_enter_btn)
        self.btn.bind("<Leave>", self.on_leave_btn)

        # __________________________________________________________________________________________________-

        self.displayFrame = Frame(self.frame2, width=self.frame2.winfo_width(), padx=40, pady=40,
                                  height=int(self.frame2.winfo_screenheight()) - 350)
        self.displayFrame.pack(pady=10, expand=True, fill='both', padx=10)
        self.displayFrame.pack_propagate(0)

        width_2 = int(self.displayFrame.winfo_screenheight() - 200)
        height_2 = int(self.displayFrame.winfo_screenheight() - 500)

        self.label = Label(self.displayFrame)
        self.label.pack(anchor=NE)

        self.camLabel = Label(self.displayFrame)
        self.camLabel.pack(anchor=NW)

        self.btnFrame = Frame(self.frame2, width=int(width_2 / 3 * 4), bg=self.frameBackground, height=height_2)
        self.btnFrame.pack(pady=20, padx=20)
        self.btnFrame.pack_propagate(0)
        self.cameraButton = Button(self.btnFrame, text='Open Camera',
                                   font=self.font, width=18, relief=tkinter.SOLID, command=self.openCamera,
                                   anchor='center', bg=self.mainBackground)
        self.cameraButton.grid(row=0, column=0, pady=20, padx=15)

        self.cameraClose = Button(self.btnFrame, text="Capture ",
                                  font=self.font, width=18, relief=tkinter.SOLID, bg=self.mainBackground)
        self.cameraClose.grid(row=0, column=2, pady=20, padx=15)

        self.imageButton = Button(self.btnFrame, text="Close Button",
                                  font=self.font, width=18, relief=tkinter.SOLID, bg=self.mainBackground)
        self.imageButton.grid(row=0, column=3, pady=20, padx=15)

        self.cameraButton.bind("<Enter>", self.on_enter_btn)
        self.cameraButton.bind("<Leave>", self.on_leave_btn)

        self.cameraClose.bind("<Enter>", self.on_enter_btn)
        self.cameraClose.bind("<Leave>", self.on_leave_btn)

        self.imageButton.bind("<Enter>", self.on_enter_btn)
        self.imageButton.bind("<Leave>", self.on_leave_btn)

        self.root.mainloop()

    def openCamera(self):
        self.cap = cv2.VideoCapture(0)
        self.show_frames()
        self.cameraClose.configure(command=self.closeCamera, text='Close Camera')
        self.imageButton.configure(command=self.recface, text='Capture')
        # self.imageButton = Button(self.btnFrame, text='Capture', font=('arial', 20), width=16, command=self.recface)
        # self.imageButton.grid(row=0, column=1, pady=20, padx=10)

    def closeCamera(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.camLabel.configure(image='')
        self.cameraButton.configure(command=self.openCamera, text='Open Camera')
        # self.imageButton.destroy()

    def recface(self):
        image_list = os.listdir('employeeImage')
        # print(image_list)
        for img in image_list:
            print(img)
            try:
                result = DeepFace.verify(img1_path=self.frame, img2_path=f"employeeImage/{img}",
                                         model_name='VGG-Face')
                print(result)
                if result['verified'] == True:
                    msg.showinfo("Success", "Deep Face Result is verified, please wait...", parent=self.root)
                    self.getValues(img)
                    break
                elif result['verified'] == False:
                    msg.showerror("warning", "Deep Face Result is verification is failed", parent=self.root)
                    # self.getValues(img)
                    break

            except:
                msg.showerror("warning", "Something went Wrong, Face not Found, Please Try Again..", parent=self.root)
                print('Face not Found')

    #
    def getValues(self, img):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select * from employee where image='{img}'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        print(data)
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')
        self.txt1.insert(0, data[0][0])
        self.txt2.insert(0, data[0][1])
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(current_date, current_time)
        self.txt3.insert(0, current_date)
        self.txt4.insert(0, current_time)
        # self.txt5.insert(0,self.center_id[0][0])

    def getSubmit(self):
        criminal_id = self.txt1.get()
        # center_id = self.txt5.get()
        criminal_name = self.txt2.get()
        date = self.txt3.get()
        time = self.txt4.get()
        # description = self.txt6.get('1.0', 'end-1c')

        conn = connect()
        cr = conn.cursor()
        q = f"insert into attendance values(null,'{criminal_id}','{criminal_name}','{date}','{time}')"
        print(q)
        cr.execute(q)
        conn.commit()
        self.sendRemarks(criminal_id)
        msg.showinfo("success", "Attendance has been Marked..", parent=self.root)
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        # self.txt5.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')
        # self.txt6.delete('1.0', 'end-1c')

    def sendRemarks(self, criminal_id):
        q = f"select * from employee where id='{criminal_id}'"
        self.cr.execute(q)
        criminals_data = self.cr.fetchone()
        date = self.txt3.get()
        time = self.txt4.get()

        message = f'''
            Employee Name - {criminals_data[1]} has been identified at {time} on {date}.

            Here are Employee Details -
            Employee Name - {criminals_data[1]}
            Employee Mobile - {criminals_data[4]}
            Employee Email - {criminals_data[3]}
            Location - {criminals_data[5]}


        '''
        subject = "Employee Attendance Report"

        x = email_varification.sendEmail(to=criminals_data[3], message=message, subject=subject)
        if x:
            msg.showinfo("Sent", "Mail has been sent", parent=self.root)
        else:
            msg.showwarning('Warn', 'Mail not sent', parent=self.root)

    def show_frames(self):
        # Get the latest frame and convert into Image
        flag, self.frame = self.cap.read()
        if flag:
            self.frame = cv2.resize(self.frame, (720, 480))
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.frame = cv2.flip(self.frame, 1)
            img = Image.fromarray(self.frame)
            # Convert image to PhotoImage
            self.frame2 = ImageTk.PhotoImage(image=img)
            self.camLabel.imgtk = self.frame2
            self.camLabel.configure(image=self.frame2)
            # Repeat after an interval to capture continiously
            self.camLabel.after(20, self.show_frames)

    def on_leave_btn(self, event):
        self.btn.configure(bg=self.frameBackground, fg='black')

    def on_enter_btn(self, event):
        self.btn.configure(bg=self.mainBackground, fg='Black')


if __name__ == '__main__':
    attendance()
