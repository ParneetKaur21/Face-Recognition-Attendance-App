from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2 
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        img_top = Image.open(r"college_images\facialrecognition.png")
        img_top = img_top.resize((1300, 250), Image.LANCZOS)  # Reduced height
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1300, height=250 )
        
        #button

        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="dark green", fg="white")
        b1_1.place(x=0,y=300,width=1300,height=45)


        img_bottom = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1300, 250), Image.LANCZOS)  # Reduced height
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=340, width=1300, height=250 )
        
    def train_classifier(self):
        data_dir= ("data")
        path =[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #list comprehension
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray Scale Image
            imageNp=np.array(img,'uint8') #datatype in array is uint8
            id=int(os.path.split(image)[1].split('.')[1])
            #C:\Users\parne\OneDrive\Desktop\Face Recognition System\data\user.5.1.jpg
            #0
            #we will be using numpy as it gives 88% array conversion of image performance for more information we can say that image
            #is in pixels so we need to divide an image to grids so numpy is recommended to convert an image in array
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #=========train the classifier And Save======
        #clf.train(faces,ids)
        #clf=cv2.face.LBPHFaceRecognizer()
        #clf.write("classifier.xml")
        #cv2.destroyAllWindows()
        #messagebox.showinfo("Result","Training data sets completed!!!!")

        try:
            # Train the classifier and save
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.train(faces, ids)
            recognizer.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training data sets completed!!!!")
        except Exception as e:
            print(f"Error during training: {e}")
            messagebox.showerror("Error", f"Training failed: {e}")


        








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()