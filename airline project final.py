
import tkinter as tk
import time
import random
from tkinter import messagebox
import pymysql
import datetime
def Create_user():
    con=pymysql.connect(host="localhost",user="root",password="1986")
    cur=con.cursor()
    s='create database if not exists airline'
    cur.execute(s)

    if cur.rowcount==1:
        cur.execute("use airline")
        q="create table if not exists login(Name varchar(30),User_name varchar(30),Password varchar(20),Mobile char(10))"
        cur.execute(q)
        cur.execute("delete from login")
        s1='insert into login values("Geetika Jain","geetika02","1986","9871565454")'
        cur.execute(s1)
        con.commit()
        con.close()

def about():
    print()
    print("="*100)
    print(" "*30," AIRLINE TICKETING SYSTEM ")
    print("="*100)
    print('Airline Ticketing System is Project designed to manage all operation')
    print("related to ticket booking. The primary goal of an this project is to ensure efficient Ticket Booking")
    print("cancellation, Printing ticket, Modification of passenger details, Addition, Modification, ")
    print("Deletion, Display Flight Details.")
    print()
    print(" "*45,"Project Designed and Developed by : Geetika Jain- XII-A")
    print("="*100)
    #time.sleep(5)
    main_menu()

def close_window():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def sign_in():
    Create_user()
    con=pymysql.connect(host="localhost",user="root",password="1986",database='airline')
    cur=con.cursor()
    s='select * from Login'
    cur.execute(s)
    d=cur.fetchone()
    username = username_entry.get()
    password = password_entry.get()
    if username.lower()==d[1] and password==d[2]:
        messagebox.showinfo("Login", "Credentials verified")
        root.destroy()
        about()
    else:
        messagebox.showinfo("Login Error", "User ID or Password Invalid, Try Again")

def main_menu():
    print()
    while True:
        print()
        print("M A I N - M E N U ")
        print("--------------------")
        print()
        print("1. FLight Menu")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Print Ticket")
        print("5. Exit")
        ch=int(input("Enter your choice [1,2,3,4,5]"))
        if ch==1:
            Flight_menu()
        elif ch==2:
            print()
            Book_Ticket()
        elif ch==3:
            Cancel_Ticket()
        elif ch==4:
            Print_Ticket()
        elif ch==5:
            print("Shutding down...")
            time.sleep(5)
            print("Thank you")
            break

def Flight_menu():
    print()
    while True:
        print()
        print("F L I G H T - M E N U ")
        print("--------------------")
        print()
        print("1. Add New Flight Detials ")
        print("2. Modify Flight Detials")
        print("3. Delete Flight Detials")
        print("4. Show Flight Details")
        print("5. Back to Main Menu")
        ch=int(input("Enter your choice [1,2,3,4,5]"))
        if ch==1:
            Add_Flight()
        elif ch==2:
            Mod_Flight()
        elif ch==3:
            Remove_Flight()
        elif ch==4:
            Show_Flight()
        elif ch==5:
            break

def Add_Flight():
    print()
    print("Adding Flight Detials")
    print("======================")
    print()
    flno=input("Enter Flight No")
    fname=input("Enter name of the Airline")
    source=input("Enter Source")
    dest=input("Enter Destination")
    km=int(input("Enter total distance"))
    price=int(input("Enter Ticket Price Economy class"))
    seats=int(input("Enter total no of seats"))
    dtime=input("Enter Departure time")
    atime=input("Enter Arival Time")
    ttime=input("Enter total Fligh Duration ")
    con=pymysql.connect(host="localhost",user="root",password="1986",database='airline')
    cur=con.cursor()
    s='''create table IF NOT EXISTS Flight(flno char(10) primary key,f_name varchar(20),source varchar(20),destination
varchar(20),distancekm int,t_price decimal(10,2),t_seats int,dep_time varchar(10),Arr_time varchar(10),Total_time varchar(10))'''
    print(s)
    cur.execute(s)
    q="insert into Flight values('{}','{}','{}','{}',{},{},{},'{}','{}','{}')".format(flno,fname,source,dest,km,price,seats,dtime,atime,ttime)
    cur.execute(q)
    con.commit()
    print(cur.rowcount,"Row Inserted")
    con.close()

def Mod_Flight():
    print()
    print("Modify Flight Details")
    print("======================")
    print()
    flno=input("Enter Flight No to Modify")
    con=pymysql.connect(host="localhost",user="root",password="1986",database='airline')
    cur=con.cursor()
    s="select * from flight where flno='"+flno+"'"
    cur.execute(s)
    d=cur.fetchone()
    if d==None:
        print("Sorry Flight Detials not found")

    else:
        print(d)
        print("Enter new Flight details to modify or old to retain")
        cur.execute("delete from flight where flno='"+flno+"'")
        con.commit()
        fname=input("Enter Airline name")
        source=input("Enter Source")
        dest=input("Enter Destination")
        km=int(input("Enter total distance"))
        price=int(input("Enter Ticket Price Economy class"))
        seats=int(input("Enter total no of seats"))
        dtime=input("Enter Departure time")
        atime=input("Enter Arival Time")
        ttime=input("Enter total Fligh Duration ")
        q="insert into Flight values('{}','{}','{}','{}',{},{},{},'{}','{}','{}')".format(flno,fname,source,dest,km,price,seats,dtime,atime,ttime)
        cur.execute(q)
        con.commit()
        print(cur.rowcount,"Row Updated")
        con.close()

def Remove_Flight():
    print()
    print("Delete Flight Detials")
    print("======================")
    print()
    flno=input("Enter Flight No to Delete")
    con=pymysql.connect(host="localhost",user="root",password="1986",database='airline')
    cur=con.cursor()
    s="select * from flight where flno="+flno
    cur.execute(s)
    d=cur.fetchone()
    if d==None:
        print("Sorry Flight Detials not found")
    else:
        print(d)
        q="Delete from Flight where flno="+flno
        ch=input("Do You really want to delete")
        if ch.lower()=="y":
            cur.execute(q)
            con.commit()
            print(cur.rowcount," Rows Deleted ")
            con.close()

def Show_Flight():
    print()
    print("Show Flight Detials")
    print("======================")
    print()
    print("1... Show Single Flight Information")
    print("2... Show All Flight Detials",end=" ")
    ch=int(input())
    print()
    con=pymysql.connect(host="localhost",user="root",password="1986",database='airline')
    cur=con.cursor()
    if ch==1:
        fno=input("Enter Flight No")
        s="select * from flight where flno='{}'".format(fno)
        cur.execute(s)
        print(cur.fetchone())
    else:
        s="select * from flight";
        cur.execute(s)
        d=cur.fetchall()
    for i in d:
        for j in i:
            print(j,end=" ")
        print("\n")
    con.close()

def Book_Ticket():
    print("Ticket Booking Menu")
    print("===================")
    print()
    con=pymysql.connect(host="localhost",user="root",password="1986",database='airline')
    cur=con.cursor()
    a=input("Enter Source City")
    b=input("Enter Destination City")
    q="select * from flight where source='{}' and destination='{}'".format(a,b)
    cur.execute(q)
    rec=cur.fetchall()
    if rec==None:
        print("No Flights Availiable in the given route")
    else:
        for i in rec:
            for j in i:
                print(j,end=" ")
            print()
        fno=input("Choose Flight Number from above to book ticket")
        dot=input("Enter Date of Travel")
        nop=int(input("Enter Number of Passenger"))
        bi=random.randint(111,99999999)
        bid='B'+str(bi)
        pn=random.randrange(1,9999999999)
        pnr='E'+str(pn)

        q="create table if not exists "+bid+"(booking_id char(10),pnr char(11), name varchar(30),age int,seat_no char(6))"
        cur.execute(q)

        q2="create table if not exists booking(bid char(10) primary key,source varchar(20),destination varchar(20),dateoftravel date, total_fare int(11),nop int,fname varchar(30), flno char(15) not NULL, pnr varchar(11))"
        cur.execute(q2)

        passenger=[]
        seat=[]
        s=0
        for i in range(1,nop+1):
            nm=input("Enter Passenger Name")
            age=int(input("Enter Passenger Age"))
            passenger.append([nm,age])
            s=s+1
            sno='A '+str(s)
            seat.append(sno)
        q3="select * from flight where flno='{}'".format(fno)
        cur.execute(q3)
        data=cur.fetchone()
        print(data)
        fnm=data[1]
        fno=data[0]
        tp=data[5]
        totalp=nop*tp
        gst=totalp*18/100
        fpay=totalp+gst
        print()
        print("Payment Options are [1.. Netbanking 2 Credit / Debit Card, 3.. UPI]")
        print()
        opt=int(input("Enter payment option "))
        if opt==1:
            print()
            userid=input("Enter Netbanking Login ID")
            passw=input("Enter Login Password")
            print()
            print("="*100)
            print("You have sucessfully paid Rs. ",fpay, "Using Netbanking payment option")
            print("="*100)
        elif opt==2:
            print()
            print()
            card=input("Enter Debit/ Credit Card No in xxxx-xxxx-xxxx-xxxx format :")
            cname=input("Enter Name of the Card Holder")
            exp=input("Enter Card Expiry date MM/YY format")
            cvv=int(input("Enter 3 digit CVV Number"))
            print()
            print("="*100)
            print("You have sucessfully paid Rs. ",fpay, "Using Card no ending with "+card[-4:])
            print("="*100)

        elif opt==3:
            print()
            upi=input("Enter UPI ID")
            passw=input("Enter Password")
            print()
            print("="*100)
            print("You have sucessfully paid Rs. ",fpay, "Using UPI ID ",upi)
            print("="*100)

        for i in range(0,len(passenger)):
            q4="insert into "+bid+" values('{}','{}','{}',{},'{}')".format(bid,pnr,passenger[i][0],passenger[i][1],seat[i])
            cur.execute(q4)
            q5="insert into booking values('{}','{}','{}','{}',{},{},'{}','{}','{}')".format(bid,a,b,dot,fpay,nop,fnm,fno,pnr)
        cur.execute(q5)
        con.commit()
        con.close()

def Cancel_Ticket():
    con=pymysql.connect(host="localhost",user="root",password="1986",database='airline')
    c=con.cursor()
    print()
    print("-"*100)
    print("\t\t\t Ticket Cancellation Menu")
    print("-"*100)
    print()
    print()
    t=input("\t\t\t Enter booking id ")
    q1="select * from booking where bid='{}'".format(t)
    c.execute(q1)
    b=c.fetchone()
    

    if c.rowcount>=1:
        print()
        print("="*100)
        dt = datetime.date.today()
        print(" Today's Date ",dt,end=" ")
        print(" Booking ID : ",b[0],end=" ")
        print(" \t Travel Date",b[3])
        print("-"*100)
        print()
        print(" Flight :\t", b[6], "\tFlight No :",b[7],"\tPNR No",b[8])
        print()
        print()
        print(" From ",b[1]," \t\t To :",b[2])
        print()
        ch=input("Please confirm [Y/ N] to cancel")
        if ch.lower()=='y':
            q="update flight set t_seats=t_seats+{} where flno='{}'".format(b[5],b[7])
            c.execute(q)
            c.execute("delete from booking where bid='{}'".format(t))
            con.commit()
            print()
            print()
            print("Cacellation done, your Money Will be credited to respective account")
            print("Thanks for choosing our services")
    else:
        print("Enter valid booking ID")

def Print_Ticket():
    con=pymysql.connect(host="localhost",user="root",password="1986",database='airline')
    cur=con.cursor()
    pn=input("Enter Pnr No : ")
    q1="select * from booking where pnr='{}'".format(pn)
    print(q1)
    cur.execute(q1)
    data=cur.fetchone()
    if data==None:
        print("Invalid PNR No")
    else:
        q2="select * from "+data[0]
        cur.execute(q2)
        d=cur.fetchall()
        nop=data[5]
        source=data[1]
        dest=data[2]
        tf=data[4]
        flno=data[7]
        pnr=data[8]
        fname=data[6]
        dot=data[3]

        print("="*100)
        print('Pnr/Booking Ref No.',pnr,end=' ')
        print(' '*20,'Date of Travel: ',dot)
        print("="*100)
        print()
        x="select * from flight where flno='{}'".format(flno)
        cur.execute(x)
        y=cur.fetchone()
        
        at=y[8]
        dt=y[7]
        td=y[9]
        print("%5s"%"Sl.no%25s"%"Passenger%20s"%"source%30s"%"Destination%17s"%"Seat No.")
        
        print()
        c=1
        for i in d:
            print("%5s"%c,end="")
            print("%20s"%i[2],end="")
            print("%20s"%source,end="")
            print("%20s"%dest,end="")
            print("%20s"%i[4],end="")
            c=c+1
            print()

        print()
        print()
        print("Flight NO",flno," "*10,"Departure time",dt," "*10,"Total Duration",td)
        print()
        print("Flight Name",fname," "*20,"Arival Time",at)
        print()
        print("Total Fare : ",tf)
        print("="*100)
        
    
   


root = tk.Tk()
root.title("Login Window")
root.geometry("400x200")
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()
label_username = tk.Label(frame, text="Username:")
label_username.pack()
username_entry = tk.Entry(frame)
username_entry.pack()
label_password = tk.Label(frame, text="Password:")
label_password.pack()
password_entry = tk.Entry(frame, show="*")
password_entry.pack()
username_entry.focus_set()
signup_button = tk.Button(frame, text="Sign in", command=sign_in)
signup_button.pack(pady=10)
exit_button = tk.Button(frame, text=" Exit ", command=close_window)
exit_button.pack()
root.mainloop()
