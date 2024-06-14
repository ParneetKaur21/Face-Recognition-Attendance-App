from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import messagebox

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        
        # Load the image
        self.bg = Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\gradient-connection-background_23-2150462053.jpg")
        
        # Resize the image to fit the window
        self.bg = self.bg.resize((1530, 790), Image.LANCZOS)
        
        # Convert the image to PhotoImage
        self.bg = ImageTk.PhotoImage(self.bg)
        
        # Create a label to display the image
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame with a border and initial border color
        self.frame = Frame(self.root, bg="black", bd=2, relief=RIDGE, highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frame.place(x=480, y=120, width=340, height=450)
        
        # Start the blinking effect
        self.blink_state = True
        self.blink_border()

        img1=Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\login.jpg")
        img1=img1.resize((100, 100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=600, y=145,width=100,height=100)

        get_str=Label(self.frame, text="Get Started", font=("times new roman",18, "bold"),fg="white", bg="black")
        get_str.place(x=100, y=115)

        #label
        usename_lbl=Label(self.frame, text="Username", font=("times new roman",15,"bold"),fg="white", bg="black")
        usename_lbl.place(x=60, y=160)

        self.txtuser=ttk.Entry(self.frame, font=("times new roman",15,"bold"))
        self.txtuser.place(x=30, y=190, width=270)

        password_lbl=Label(self.frame, text="Password", font=("times new roman",15,"bold"),fg="white", bg="black")
        password_lbl.place(x=60, y=225)

        self.password=ttk.Entry(self.frame, font=("times new roman",15,"bold"))
        self.password.place(x=30, y=260, width=270)

        #==========Icon Image==========
        img2=Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\login.jpg")
        img2=img2.resize((35, 35),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=510, y=279,width=35,height=35)
        

        img3=Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\passwordpa.jpg")
        img3=img3.resize((35, 35),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=510, y=349,width=35,height=35)
        
        #login button
        loginbtn=Button(self.frame,command=self.login,text="Login",font=("times new roman", 15,"bold"), bd=3, fg="white", bg="#33acf2",activeforeground="white", activebackground="#33acf2")
        loginbtn.place(x=110, y=300,width=120, height=40)

        #register button
        registerbtn=Button(self.frame,text="New User Register", font=("times new roman", 10,"bold"),borderwidth=0, fg="white", bg="black",activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350,width=160)

        #forgot pass
        forgot_pass_btn=Button(self.frame,text="Forgot Password",font=("times new roman", 10,"bold"), borderwidth=0, fg="white", bg="black",activeforeground="white", activebackground="black")
        forgot_pass_btn.place(x=10, y=380,width=160)



    def login(self):
        if self.txtuser.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="Parneet Kaur" and self.password.get()=="2101753":
            messagebox.showinfo("Success","Welcome to Face Recognition Attendance Application!!!")
        else:
            messagebox.showerror("Error","Invalid Username and Password")



    def blink_border(self):
        # Toggle the border color between white and red
        if self.blink_state:
            self.frame.config(highlightbackground="white", highlightcolor="white")
        else:
            self.frame.config(highlightbackground="black", highlightcolor="black")
        self.blink_state = not self.blink_state
        # Toggle the border color every 2000ms (2 seconds)
        self.root.after(1000, self.blink_border)



        

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
