import sys
from tkinter import*
from tkinter import messagebox
import datetime
import time
import sql.connector as connector

class login:
    def _init_(self,root):
        self.root=root
        self.root.title("login System")
        self.root.geometry("1199x700+100+50")
        self.root.resizable(False,False)
        #===BG===#
        self.bg=PhotoImage(file="C:\\Users\\hp\\OneDrive\\Desktop\\login2.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #===login Frame===
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=40,y=250,height=340,width=500)

        title=Label(Frame_login,text="Login here",font=("Impact",25,"bold"),fg="black",bg="white").place(x=90,y=30)
        #label1
        desc=Label(Frame_login,text="Accountant Employee Login Area",font=("Goudy old style",10,"bold"),fg="black",bg="white").place(x=90,y=70)
        lbl_email=Label(Frame_login,text="Email",font=("Impact",15),fg="gray",bg="white").place(x=90,y=100)
        self.txt_email=Entry(Frame_login,font=("times new roman",15),bg="lightyellow")
        self.txt_email.place(x=90,y=140,width=350,height=25)
        #label2
        lbl_pass=Label(Frame_login,text="password",font=("Impact",15),fg="gray",bg="white").place(x=90,y=180)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightyellow")
        self.txt_pass.place(x=90,y=220,width=350,height=25)

        lbl_register=Label(Frame_login,text="Don't have an account ? ",font=("Impact",15),fg="gray",bg="white").place(x=90,y=260)
        register_btn=Button(self.root,text="Register Here ",fg="black",bg="white",bd=0,font=("Goudy old style",12,'bold')).place(x=350,y=510,width=130,height=35)
        
        #button1
        login_btn=Button(self.root,text="LOGIN",command=self.login,fg="white",bg="black",font=("times new roman",12)).place(x=200,y=570,width=180,height=40)

    def clear(self):
        self.txt_email.delete(0,END),
        self.txt_pass.delete(0,END)
    def insert_user(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            con=connector.connect(host="localhost",user="root",password= "" ,database="logindatabase")
            cur=con.cursor()
            cur.execute(" select * from login where email=%s and password=%s",(self.txt_email.get(),self.txt_pass.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("ERROR","INVALID EMAIL ID AND PASSWORD ",parent=self.root)
            else:
                messagebox.showinfo("SUCCESS","REGISTRATION COMPLETED!!",parent=self.root)    
            

root=Tk()
obj=login(root)
root.mainloop()