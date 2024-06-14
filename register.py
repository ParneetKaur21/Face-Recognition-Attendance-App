from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import messagebox

class Register:
    def __init__(self, root):
        self.root = root 
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")


        #variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA= StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Load the background image
        self.bg = Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\gradient-connection-background_23-2150462053.jpg")
        # Resize the background image to fit the window
        self.bg = self.bg.resize((1530, 790), Image.LANCZOS)
        # Convert the background image to PhotoImage
        self.bg = ImageTk.PhotoImage(self.bg)
        # Create a label to display the background image
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame for the left image with a black border
        self.left_frame = Frame(self.root, bd=5, bg='black')
        self.left_frame.place(x=100, y=80, width=360, height=510)

        # Load the left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\gradient.jpg")
        left_lbl = Label(self.left_frame, image=self.bg1)
        left_lbl.place(x=0, y=0, width=350, height=500)

        # Add a welcome message on the left image
        welcome_lbl = Label(left_lbl, text="Welcome to\nRegistration Page", font=("Brush Script MT", 22, "bold"), bg="white", fg="darkblue")
        welcome_lbl.place(x=20, y=200, width=310, height=100)

        # Start the blinking effect for the border
        self.blink_border()
        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=460, y= 80, width=700, height=510)

        register_lbl=Label(frame, text="Register Here",font=("times new roman", 20, "bold"), fg="darkblue", bg="white")
        register_lbl.place(x=20, y=20)
        
        #labels and entries 
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130,width=250)

        #last name
        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)
        
        l_name_entry=ttk.Entry(frame,textvariable=self.var_lname,  font=("times new roman", 15, "bold"))
        l_name_entry.place(x=370, y=130,width=250)

        #contact number
        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)
        
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,  font=("times new roman", 15, "bold"))
        contact_entry.place(x=50, y=200,width=250)

        #email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)
        
        email_entry=ttk.Entry(frame,textvariable=self.var_email,  font=("times new roman", 15, "bold"))
        email_entry.place(x=370, y=200,width=250)

        #security question select 
        securityQ = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white")
        securityQ.place(x=50, y=240)
        
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_securityQ, font=('times new roman', 15, 'bold'),state="readonly")
        self.combo_security["values"] = ("Select", "Your favorite game", "Your pet name", "Your Hobby")
        self.combo_security.current(0)
        self.combo_security.place(x=50, y=270, width=250)





        #security_ans
        Security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        Security_A.place(x=370, y=240)
        
        email_entry=ttk.Entry(frame,textvariable=self.var_securityA,  font=("times new roman", 15, "bold"))
        email_entry.place(x=370, y=270,width=250)
        
        #password 
        password = Label(frame, text="Enter Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=50, y=310)
        
        password_entry=ttk.Entry(frame,textvariable=self.var_pass,  font=("times new roman", 15, "bold"))
        password_entry.place(x=50, y=340,width=250)

        #confirm passwrd
        conf_pass = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        conf_pass.place(x=370, y=310)
        
        confirm_pass_entry=ttk.Entry(frame,textvariable=self.var_confpass,  font=("times new roman", 15, "bold"))
        confirm_pass_entry.place(x=370, y=340,width=250)
        
        #checkbutton 
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check, text="I Agree the terms and conditions",font=("times new roman",12, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50, y=380)

        #buttons 
        registernowbtn=Button(frame,command=self.register_data,text="Register Now", font=("times new roman", 15,"bold"),borderwidth=0, fg="white", bg="darkblue",activeforeground="white", activebackground="darkblue")
        registernowbtn.place(x=50, y=430,width=150,height=40)

        #buttons 
        loginnowbutton=Button(frame,text="Login Now", font=("times new roman", 15,"bold"),borderwidth=0, fg="white", bg="#d42222",activeforeground="white", activebackground="#d42222")
        loginnowbutton.place(x=250, y=430,width=150,height=40)
    

    #functions 
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_contact.get()=="" or self.var_lname.get()=="" or self.var_securityA.get()=="":
            messagebox.showerror("Error","All fields are required")

        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm Password must be same!")
        
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree the terms and conditions")
        else:
            messagebox.showinfo("Success","Welcome to face recognition!")



        

 







    def blink_border(self):
        current_color = self.left_frame.cget("bg")
        next_color = "white" if current_color == "darkblue" else "darkblue"
        self.left_frame.config(bg=next_color)
        self.root.after(1000, self.blink_border)  # Blink every 1000 milliseconds (1 second)

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
