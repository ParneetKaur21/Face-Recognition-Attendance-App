from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2 
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="dark blue")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        img_top = Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1300, 600), Image.LANCZOS)  # Reduced height
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1300, height=600 )
        #Left Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=30, y=30, width=700, height=500)
        
        #developer_information
        dev_label = Label(main_frame, text='Professional Summary', font=("times new roman", 24, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=0, column=5,sticky=W)

        dev_label = Label(main_frame, text=' A well-organized, creative and goal-oriented under graduate possessing excellent communication, problem-solving and leadership skills with a flair to explore suitable avenues in Computer Science Engineering while developing advanced projects with efficiency and quality. ', font=("times new roman", 14, "bold"), bg="white",wraplength=700, justify='left')
        dev_label.grid(row=1, column=5,sticky=W)
        
        dev_label = Label(main_frame, text='Technical Competencies', font=("times new roman", 24, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=2, column=5,sticky=W)

        dev_label = Label(main_frame, text='C|C++|Python|tkinter|HTML|CSS|Javascript|SQL|Operating System|Data Structures', font=("times new roman", 14, "bold"), bg="white")
        dev_label.grid(row=3, column=5,sticky=W)

        dev_label = Label(main_frame, text='Interpersonal Skills', font=("times new roman", 24, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=4, column=5,sticky=W)

        dev_label = Label(main_frame, text='Ability to work as a leader and at the same time never feel ashamed to work like a team member too| Calm | hardworking| open minded personality| motivating nature  | technologically competent.', font=("times new roman", 14, "bold"), bg="white",wraplength=700, justify='left')
        dev_label.grid(row=5, column=5,sticky=W)
        
        dev_label = Label(main_frame, text='Interests and Hobbies', font=("times new roman", 24, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=6, column=5,sticky=W)

        dev_label = Label(main_frame, text='Video Editing | Dance | Reading Quotes | Teaching ', font=("times new roman", 14, "bold"), bg="white",wraplength=700, justify='left')
        dev_label.grid(row=7, column=5,sticky=W)
        
        dev_label = Label(main_frame, text='Languages Known', font=("times new roman", 24, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=8, column=5,sticky=W)

        dev_label = Label(main_frame, text='English|Hindi|Punjabi', font=("times new roman", 14, "bold"), bg="white",wraplength=700, justify='left')
        dev_label.grid(row=9, column=5,sticky=W)

        
        
        
        
        
        

        #Right Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=750, y=30, width=500, height=500)

        img_top1 = Image.open(r"college_images\developer.jpeg")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)  # Reduced height
        self.photoimg_top1= ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200 )
        
        #developer_information
        dev_label = Label(main_frame, text='Parneet Kaur', font=("times new roman", 24, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=0, column=5,sticky=W)

        dev_label = Label(main_frame, text='Roll number: 2101753', font=("times new roman", 14, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=1, column=5,sticky=W)
        
        dev_label = Label(main_frame, text='#160 posh city, sector - 92,Mohali ', font=("times new roman", 14, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=2, column=5,sticky=W)

        dev_label = Label(main_frame, text='6239895717 ', font=("times new roman", 14, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=3, column=5,sticky=W)
        
        dev_label = Label(main_frame, text='parneetkaurpk.2103@gmail.com', font=("times new roman", 14, "bold"), bg="white", fg="dark blue")
        dev_label.grid(row=4, column=5,sticky=W)

        
        
        

        img_top2 = Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img_top2 = img_top2.resize((500, 300), Image.LANCZOS)  # Reduced height
        self.photoimg_top2= ImageTk.PhotoImage(img_top2)

        f_lbl = Label(main_frame, image=self.photoimg_top2)
        f_lbl.place(x=0, y=200, width=500, height=300 )
        


        





    
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
