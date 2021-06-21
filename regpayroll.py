import sys
from tkinter import*
from tkinter import messagebox
import datetime
import time

class login:
    def _init_(self,root):
        self.root=root
        self.root.title("login System")
        self.root.geometry("1000x630+100+50")
        self.root.resizable(False,False)
        #===BG===#
        self.bg=PhotoImage(file="C:\\Users\\hp\\OneDrive\\Desktop\\python basics\\python\\registration.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=100,y=0,relwidth=1,relheight=1)
        
        #===login Frame===
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=10,y=20,height=600,width=450)

        title=Label(Frame_login,text="Register here",font=("Impact",25,"bold"),fg="black",bg="white").place(x=50,y=50)
        #label1
        desc=Label(Frame_login,text="Accountant Employee Registration Area",font=("Goudy old style",10,"bold"),fg="black",bg="white").place(x=50,y=100)
        lbl_user=Label(Frame_login,text="Username",font=("Impact",15),fg="gray",bg="white").place(x=50,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightyellow")
        self.txt_user.place(x=50,y=180,width=350,height=25)
        #label2
        lbl_phone=Label(Frame_login,text="Phone Number",font=("Impact",15),fg="gray",bg="white").place(x=50,y=220)
        self.txt_phone=Entry(Frame_login,font=("times new roman",15),bg="lightyellow")
        self.txt_phone.place(x=50,y=260,width=350,height=25)

        #label2
        lbl_pass=Label(Frame_login,text="Password",font=("Impact",15),fg="gray",bg="white").place(x=50,y=300)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightyellow")
        self.txt_pass.place(x=50,y=340,width=350,height=25)

        #label2
        lbl_email=Label(Frame_login,text="Email",font=("Impact",15),fg="gray",bg="white").place(x=50,y=380)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightyellow")
        self.txt_pass.place(x=50,y=420,width=350,height=25)

        
        #button1
        register_btn=Button(self.root,text="REGISTER",fg="white",bg="black",font=("times new roman",12)).place(x=150,y=500,width=180,height=40)
        
        

root=Tk()
obj=login(root)
root.mainloop()