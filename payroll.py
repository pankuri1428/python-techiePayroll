from tkinter import *
from tkinter import messagebox
import time
import datetime

root=Tk()
root.title("PAYROLL ") #titlebar title
root.geometry("1350x700+0+0") #for size of window
root.config(bg="black") #for colouring background
#use for writing text
title=Label(root,text="PAYROLL MANAGER",font=("times new roman",30,"bold"),bg="lightgrey",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

     #variables
name=StringVar()
dob=StringVar()
netpay=StringVar()
grosspay=StringVar()
tax=StringVar()
overtime=StringVar()
employer=StringVar()
gender=StringVar()
ni=StringVar()
hours=StringVar()
rate=StringVar()
status=StringVar()
address=StringVar()
salary=StringVar()
payslip=StringVar()

        
        # buttton functions
def iExit():
        qexit=messagebox.askyesno("Payroll System "," Do you want to exit ? ")
        if qexit > 0:
                root.destroy()
                return

def Reset():
        name.set("")
        dob.set("")
        netpay.set("")
        grosspay.set("")
        tax.set("")
        employer.set("")
        ni.set("")
        gender.set("")
        hours.set("")
        rate.set("")
        overtime.set("")
        status.set("")
        address.set("")
        txtpayslip.delete("1.0",END)

def Enterinfo():
        txtpayslip.insert(END,'\t\tpayslip\n\n')
        txtpayslip.insert(END,'Name:   \t\t' + name.get() + "\n\n" )
        txtpayslip.insert(END,'D.O.B:  \t\t' + dob.get() +"\n\n" )
        txtpayslip.insert(END,'NetPay:  \t\t' + netpay.get() + "\n\n")
        txtpayslip.insert(END,'GrossPay: \t\t' + grosspay.get() + "\n\n")
        txtpayslip.insert(END,'Tax:  \t\t' + tax.get() + "\n\n")
        txtpayslip.insert(END,'Employer:  \t\t' + employer.get() + "\n\n")
        txtpayslip.insert(END,'NI Number:  \t\t' + ni.get() + "\n\n")
        txtpayslip.insert(END,'Gender:  \t\t' + gender.get() + "\n\n")
        txtpayslip.insert(END,'Hours worked:  \t\t' + hours.get() + "\n\n")
        txtpayslip.insert(END,'Hours rate:  \t\t' + rate.get() + "\n\n")
        txtpayslip.insert(END,'Overtime:  \t\t' + overtime.get() + "\n\n")
        txtpayslip.insert(END,'Status:  \t\t' + status.get() + "\n\n")
        txtpayslip.insert(END,'Address:  \t\t' + address.get() + "\n\n")
def WeeklyWages():
        HoursWorked=float(hours.get()) 
        HoursRate=float(rate.get())

        paydue = HoursRate *  HoursWorked
        PaymentDue = "₹" , str('%.2f' %(paydue))
        grosspay.set(PaymentDue)

        Tax = paydue*0.2
        Taxables = "₹" , str('%.2f' %(Tax))
        tax.set(Taxables)

        NetPay = paydue - Tax 
        NetPays = "₹" , str('%.2f' %(NetPay))
        netpay.set(NetPays)

        if HoursWorked > 40:
           OvertimeHours = ( HoursWorked - 40) + HoursRate   * 1.5
           overtimehrs = "₹" , str('%.2f' %(OvertimeHours))
           overtime.set(overtimehrs)   

        elif HoursWorked <= 40:
             OvertimePay = ( HoursWorked - 40) + HoursRate   * 1.5
             overtimehrs = "₹" , str('%.2f' %(OvertimePay))
             overtime.set(overtimehrs)   
  
  #frame1
Frame1 = Frame(root,bd=5,relief=RIDGE,bg="white")
Frame1.place(x=10,y=70,width=750,height=620)

        # inner part of frame work begins
title2=Label(Frame1,text="Employee details",font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=20).place(x=0,y=0,relwidth=1)
        
        #name label
lbl_name=Label(Frame1,text="Name",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=10,y=60)
txt_name=Entry(Frame1,textvariable=name,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=170,y=65,width=200) #input field of designation
        
        #dob label
lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=390,y=60)
txt_dob=Entry(Frame1,textvariable=dob,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=520,y=65) #input field of dob
        
        #gender label
lbl_gender=Label(Frame1,text="Gender",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=10,y=120)
txt_gender=Entry(Frame1,textvariable=gender,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=170,y=125,width=200) #input field of gender
        
        #status label
lbl_status=Label(Frame1,text="Status",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=390,y=120)
txt_status=Entry(Frame1,textvariable=status,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=520,y=125) #input field of status
    
       # employer label
lbl_employer=Label(Frame1,text="Employer",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=10,y=170)
txt_employer=Entry(Frame1,textvariable=employer,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=170,y=175,width=200) #input field of name

        #NI number label
lbl_ni=Label(Frame1,text="NI number",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=390,y=170)
txt_ni=Entry(Frame1,textvariable=ni,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=520,y=175) #input field of doj
       
        #=====Row3
        #hours worked label
lbl_hours=Label(Frame1,text="Hours worked",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=10,y=220)
txt_hours=Entry(Frame1,textvariable=hours,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=170,y=220,width=200) #input field of age
        
        #hourly rate label
lbl_rate=Label(Frame1,text="Hourlyrate",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=390,y=220)
txt_rate=Entry(Frame1,textvariable=rate,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=520,y=225) #input field of experience
       
        #=====Row4
        #tax  label
lbl_tax=Label(Frame1,text="Tax",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=10,y=270)
txt_tax=Entry(Frame1,textvariable=tax,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=170,y=275,width=200) #input field of gender
        
        #overtime  label
lbl_overtime=Label(Frame1,text="Overtime",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=390,y=270)
txt_overtime=Entry(Frame1,textvariable=overtime,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=520,y=275) #input field of proofid
        
        #=====Row5 
        #net pay label
lbl_netpay=Label(Frame1,text="Net Pay",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=10,y=320)
txt_netpay=Entry(Frame1,textvariable=netpay,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=170,y=325,width=200) #input field of email
        
        #grosspay label
lbl_grosspay=Label(Frame1,text="Gross Pay",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=390,y=320)
txt_grosspay=Entry(Frame1,textvariable=grosspay,font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=520,y=325) #input field of contact
        
      
        #=====Row7
        #address label
lbl_address=Label(Frame1,text="Address",font=("times new roman",18,"bold"),bg="white",fg="black").place(x=10,y=370)
txt_address=Text(Frame1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
txt_address.place(x=170,y=380,width=490,height=150) #input field of address
       #button 1
btn_reset=Button(Frame1,text="Reset",font=("times new roman",15),bg="gray",fg="black",command=Reset).place(x=240,y=560,height=30,width=120)
        #button 2
btn_payslip=Button(Frame1,text="Payslip",font=("times new roman",15),bg="gray",fg="black",command=Enterinfo).place(x=400,y=560,height=30,width=120)

        #button 3
btn_exit=Button(Frame1,text="Exit",font=("times new roman",15),bg="gray",fg="black",command=iExit).place(x=550,y=560,height=30,width=120)



        #frame 2
Frame2=Frame(root,bd=3,relief=RIDGE,bg="white")
Frame2.place(x=770,y=70,width=580,height=130)
         # inner part of frame2 work begins
title3=Label(Frame2,text="Employee Salary",font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=20).place(x=0,y=0,relwidth=1)
        #button1
#btn_payslip=Button(Frame2,text="Payslip",font=("times new roman",15),bg="gray",fg="black",command=Enterinfo).place(x=100,y=70,height=30,width=120)

btn_salary=Button(Frame2,text=" Your Salary ",font=("times new roman",15),bg="gray",fg="black",command=WeeklyWages).place(x=230,y=70,height=30,width=200)
       
               #frame 3
Frame3=Frame(root,bd=5,relief=RIDGE,bg="white")
Frame3.place(x=770,y=210,width=580,height=480)
#inner part of frame begins
title4=Label(Frame3,text="Pay slip",font=("times new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=20).place(x=0,y=0,relwidth=1)
#payslip label

txtpayslip=Text(Frame3,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
txtpayslip.place(x=10,y=50,width=550,height=400) #input field of payslip


root.mainloop()