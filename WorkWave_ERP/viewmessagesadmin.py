from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect


class viewmessagesadmit:
    def __init__(self):
        self.root = Toplevel()
        self.root.state("zoomed")
        self.text_color = "#F46036"

        self.conn = connect()
        self.cr = self.conn.cursor()
        self.mainLabel = Label(self.root, text="Messages", font=('', 28, 'bold'),fg=self.text_color)
        self.mainLabel.pack()

        self.messagestable = ttk.Treeview(self.root, columns=('id', 'emp_id_B','title', 'date', 'description'))
        self.messagestable.heading('id', text='ID')
        self.messagestable.heading('title', text='Meeting Title')
        self.messagestable.heading('description', text='Description')
        self.messagestable.heading('date', text='Date')
        # self.messagestable.heading('time', text='Time')
        self.messagestable.heading('emp_id_B', text='Employee ID')
        self.messagestable['show'] = 'headings'

        self.messagestable.column('id', width=50, anchor='center')
        self.messagestable.column('title', width=200, anchor='center')
        self.messagestable.column('description', width=300, anchor='center')
        self.messagestable.column('date', width=100, anchor='center')
        # self.messagestable.column('time', width=100, anchor='center')
        self.messagestable.column('emp_id_B', width=100, anchor='center')

        self.messagestable.pack( fill='both', padx=20, pady=20)
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('', 12, 'bold'), rowheight=50, foreground="#FF7F66")
        self.style.configure("Treeview", font=('', 14), rowheight=50)

        self.populate_messages_table()

        self.root.mainloop()


    def populate_messages_table(self):
        try:
            self.cr.execute("SELECT * FROM message ORDER BY date DESC")
            messages_data = self.cr.fetchall()

            for message in messages_data:
                (id_, title, description, date,  emp_id_B) = message
                self.messagestable.insert('', 'end', values=(id_, title, description, date,  emp_id_B))

            # Configure alternate row colors
            for index, _ in enumerate(messages_data):
                if index % 2 == 0:
                    self.messagestable.tag_configure('evenrow', background='#ECECEC')
                else:
                    self.messagestable.tag_configure('oddrow', background='#FFFFFF')

        except pymysql.Error as e:
            msg.showerror("Error", f"Error fetching messages data: {e}",parent=self.root)


if __name__ == "__main__":
    viewmessagesadmit()
