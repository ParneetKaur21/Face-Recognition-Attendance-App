from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import messagebox

class Register:
    def __init__(self, root):
        self.root = root 
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        # Load the background image
        self.bg = Image.open(r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\gradient-connection-background_23-2150462053.jpg")
        # Resize the background image to fit the window
        self.bg = self.bg.resize((1530, 790), Image.LANCZOS)
        # Convert the background image to PhotoImage
        self.bg = ImageTk.PhotoImage(self.bg)
        # Create a label to display the background image
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Load the left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\parne\OneDrive\Desktop\Face Recognition System\college_images\gradient.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=100, y=80, width=350, height=500)

        # Add a welcome message on the left image
        welcome_lbl = Label(left_lbl, text="Welcome to\nRegistration Page", font=("Brush Script MT", 22, "bold"), bg="white", fg="darkblue")
        welcome_lbl.place(x=20, y=200, width=310, height=100)

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
