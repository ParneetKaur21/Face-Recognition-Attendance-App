from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
        # Image paths
        img_paths = {
            "img1": r"college_images\smart-attendance.jpg",
            "img2": r"college_images\iStock-182059956_18390_t12.jpg",
            "bg_img": r"college_images\wp2551980.jpg",
            "img_left": r"college_images\AdobeStock_303989091.jpeg"
        }

        # First image
        img = Image.open(img_paths["img1"])
        img = img.resize((700, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=700, height=200)

        # Second image
        img1 = Image.open(img_paths["img2"])
        img1 = img1.resize((700, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=700, y=0, width=700, height=200)

        # Background image
        img3 = Image.open(img_paths["bg_img"])
        img3 = img3.resize((1300, 500), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1300, height=600)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1250, height=600)
        
        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT ATTENDANCE DETAILS", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=7, width=610, height=500)

        img_left = Image.open(img_paths["img_left"])
        img_left = img_left.resize((600, 80), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=600, height=80)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=2, y=85, width=600, height=300)
        
        # Labels and entries
        self.create_label_entry(left_inside_frame, "AttendanceID:", 0, 0, self.var_atten_id)
        self.create_label_entry(left_inside_frame, "Roll:", 0, 2, self.var_atten_roll)
        self.create_label_entry(left_inside_frame, "Name:", 1, 0, self.var_atten_name)
        self.create_label_entry(left_inside_frame, "Department:", 1, 2, self.var_atten_dep)
        self.create_label_entry(left_inside_frame, "Time:", 2, 0, self.var_atten_time)
        self.create_label_entry(left_inside_frame, "Date:", 2, 2, self.var_atten_date)
        
        attendance_label = Label(left_inside_frame, text='Attendance Status:', font=("times new roman", 12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        
        division_combo = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_attendance, font=('times new roman', 12, 'bold'), state="readonly")
        division_combo["values"] = ("Status", "Present", "Absent")
        division_combo.current(0)
        division_combo.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=220, width=580, height=30)

        save_btn = Button(btn_frame, text='Import CSV', command=self.importCsv, width=20, font=('times new roman', 10, 'bold'), bg='blue', fg='white')
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text='Export CSV', command=self.exportCsv, width=19, font=('times new roman', 10, 'bold'), bg='red', fg='white')
        update_btn.grid(row=0, column=1)
        
        update_db_btn = Button(btn_frame, text='Update', width=19, font=('times new roman', 10, 'bold'), bg='light green', fg='white', command=self.updateData)
        update_db_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame, text='Reset', width=20, font=('times new roman', 10, 'bold'), bg='grey', fg='white', command=self.resetData)
        reset_btn.grid(row=0, column=3)
        
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="ATTENDANCE DETAILS", font=("times new roman", 12, "bold"))
        Right_frame.place(x=630, y=7, width=610, height=500)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg='white')
        table_frame.place(x=5, y=5, width=600, height=350)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "std_name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        # Table headings
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("std_name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"  # Removes the space at the beginning

        # Set column widths
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("std_name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def create_label_entry(self, frame, text, row, column, textvariable):
        label = Label(frame, text=text, font=("times new roman", 12, "bold"), bg="white")
        label.grid(row=row, column=column, padx=5, pady=5, sticky=W)
        
        entry = ttk.Entry(frame, width=15, textvariable=textvariable, font=("times new roman", 12, "bold"))
        entry.grid(row=row, column=column + 1, padx=5, pady=5, sticky=W)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for row in rows:
            self.AttendanceReportTable.insert("", END, values=row)

    def importCsv(self):
        global mydata 
        mydata.clear()  # Clear previous data
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)
    
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])
    
    def updateData(self):
        if not self.var_atten_id.get() or not self.var_atten_roll.get() or not self.var_atten_name.get() or not self.var_atten_dep.get() or not self.var_atten_time.get() or not self.var_atten_date.get() or self.var_atten_attendance.get() == "Status":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        selected = self.AttendanceReportTable.focus()
        if not selected:
            messagebox.showerror("Error", "No record selected", parent=self.root)
            return

        selected_index = self.AttendanceReportTable.index(selected)
        mydata[selected_index] = [
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        ]

        self.fetchData(mydata)
        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

    def resetData(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
