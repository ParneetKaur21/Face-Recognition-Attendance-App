from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2 
import os

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        title_lbl = Label(self.root, text="Help Desk", font=("times new roman", 35, "bold"), bg="white", fg="dark blue")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        img_top = Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1300, 600), Image.LANCZOS)  # Reduced height
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1300, height=600 )

        help_label = Label(f_lbl, text='Email : parneetkaurpk.2103@gmail.com', font=("times new roman", 12, "bold"), bg="white")
        help_label.grid(row=550, column=260,padx=500,pady=180)
        



    
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
