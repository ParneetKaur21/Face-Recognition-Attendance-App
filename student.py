from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2 
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #========variables=========
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id= StringVar()
        self.var_std_name = StringVar()
        self.var_div= StringVar()
        self.var_roll = StringVar()
        self.var_gen = StringVar()
        self.var_dob= StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        self.var_com_search = StringVar()
        self.var_search = StringVar()

        # First image
        img = Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\face-recognition.png")
        img = img.resize((500, 100), Image.LANCZOS)  # Reduced height
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=100)

        # Second image
        img1 = Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\smart-attendance.jpg")
        img1 = img1.resize((500, 100), Image.LANCZOS)  # Reduced height
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=100)

        # Third image
        img2 = Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((500, 100), Image.LANCZOS)  # Reduced height
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=100)

        # bg-image
        img3 = Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\wp2551980.jpg")
        img3 = img3.resize((1300, 500), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1300, height=600)  # Adjusted position

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1250, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT DETAILS", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=610, height=500)  # Increased height

        img_left = Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((600, 80), Image.LANCZOS)  # Reduced height
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=600, height=80)

        # current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=3, y=70, width=600, height=90)  # Reduced height

        # department
        dep_label = Label(current_course_frame, text='Department', font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=('times new roman', 12, 'bold'), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # course
        course_label = Label(current_course_frame, text='Course', font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=('times new roman', 12, 'bold'), width=17, state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # YEAR
        year_label = Label(current_course_frame, text='Year', font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=('times new roman', 12, 'bold'), width=17, state="readonly")
        year_combo["values"] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024", "2024-2025")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text='Semester', font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=('times new roman', 12, 'bold'), width=17, state="readonly")
        semester_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # class student information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=3, y=160, width=600, height=290)  # Adjusted position and height

        # StudentId
        studentId_label = Label(class_Student_frame, text='StudentID:', font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id, width=15, font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_Student_frame, text='Student Name:', font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name, width=15, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # class division
        class_division_label = Label(class_Student_frame, text='Class Division:', font=("times new roman", 12, "bold"), bg="white")
        class_division_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        division_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_div, font=('times new roman', 12, 'bold'), width=13, state="readonly")
        division_combo["values"] = ("A", "B", "C")
        division_combo.current(0)
        division_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_Student_frame, text='Roll No:', font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll, width=15, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_Student_frame, text='Gender:', font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gen, font=('times new roman', 12, 'bold'), width=13, state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_Student_frame, text='DOB:', font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=15, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Email
        email_label = Label(class_Student_frame, text='Email:', font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email, width=15, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Phone No
        phone_label = Label(class_Student_frame, text='Phone No:', font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone, width=15, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text='Address:', font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address, width=15, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(class_Student_frame, text='Teacher Name:', font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher, width=15, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0, padx=5, pady=5)

        radiobtn2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1, padx=5, pady=5)

        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=580,height=30)

        save_btn = Button(btn_frame,text='Save',command=self.add_data,width='20',font=('times new roman',10,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text='Update',command=self.update_data,width='19',font=('times new roman',10,'bold'),bg='light green',fg='white')
        update_btn.grid(row=0,column=1)
        
        delete_btn = Button(btn_frame,text='delete',command=self.delete_data,width='19',font=('times new roman',10,'bold'),bg='red',fg='white')
        delete_btn.grid(row=0,column=2)
        
        reset_btn = Button(btn_frame,text='Reset',command=self.reset_data,width='20',font=('times new roman',10,'bold'),bg='grey',fg='white')
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=230,width=580,height=30)

        take_photo_sample_btn = Button(btn_frame1,command=self.generate_data_set,text='Take Photo Sample',width='40',font=('times new roman',10,'bold'),bg='#4287f5',fg='white')
        take_photo_sample_btn.grid(row=1,column=0)

        update_photo_btn = Button(btn_frame1,text='Update Photo Sample',width='40',font=('times new roman',10,'bold'),bg='#20e344',fg='white')
        update_photo_btn.grid(row=1,column=1)




        
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT DETAILS", font=("times new roman", 12, "bold"))
        Right_frame.place(x=650, y=10, width=580, height=500)  # Increased height

        img_right = Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\AdobeStock_303989091.jpeg")
        img_right = img_right.resize((580, 80), Image.LANCZOS)  # Reduced height
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=570, height=80)

        # Search System
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=3, y=70, width=570, height=70)  # Reduced height

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white", fg="red")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=10, state="readonly")
        search_combo["values"] = ("Roll_No", "Phone_no", "Std_id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10,command=self.search_data, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        showAll_btn = Button(search_frame, text="Show All", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        # table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=3, y=130, width=560, height=320)  # Adjusted position and height

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)  # Increased width

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
    # Function to add data
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Cgc@1234#", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gen.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Function to fetch data
    # Function to fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Cgc@1234#", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            # Ensure that the table is visible by packing it into the GUI
            self.student_table.pack(fill=BOTH, expand=1)
        conn.close()

    # Function to get cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gen.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # Function to update data
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Cgc@1234#", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, semester=%s, std_name=%s, `div`=%s, roll=%s, gen=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo_sample=%s WHERE std_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gen.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Function to delete data
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Cgc@1234#", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE std_id=%s"
                    value = (self.var_std_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student details have been deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Function to reset data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gen.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")



#================generate photo sample========================
    def generate_data_set(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Cgc@1234#", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                my_result = my_cursor.fetchall()
                id=0
                for x in my_result:
                    id += 1
                    my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, semester=%s, std_name=%s, `div`=%s, roll=%s, gen=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo_sample=%s WHERE std_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gen.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

            # ===Load predefined data on face frontals from openscv===
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
 
                def face_cropped(img):
                            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            faces = face_classifier.detectMultiScale(gray,1.3,5)
                            if len(faces)==0:
                                return None
                            #scaling factor = 1.3
                            #Minimum Neighbour = 5

                            for(x,y,w,h) in faces:
                                return img[y:y+h, x:x+w]
                                
                        
                cap=cv2.VideoCapture(0)
                img_id=0 
                while True:
                        ret, my_frame=cap.read()
                        if ret and face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)
                        
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break 
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    def search_data(self):
        if self.var_com_search.get() == "Select" or self.var_search.get() == "":
            messagebox.showerror("Error", "Select a valid search criteria and enter search value")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Cgc@1234#", database="face_recognizer")
                my_cursor = conn.cursor()
                if self.var_com_search.get() == "roll":
                    my_cursor.execute("SELECT * FROM student WHERE roll LIKE %s", ('%' + self.var_search.get() + '%',))
                elif self.var_com_search.get() == "phone":
                    my_cursor.execute("SELECT * FROM student WHERE phone LIKE %s", ('%' + self.var_search.get() + '%',))
                elif self.var_com_search.get() == "std_id":
                    my_cursor.execute("SELECT * FROM student WHERE id LIKE %s", ('%' + self.var_search.get() + '%',))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                else:
                    messagebox.showinfo("Info", "No matching records found")
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")

            




    
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
