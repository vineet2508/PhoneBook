import splashwin
from Tkinter import *
import tkMessageBox
import sqlite3

con=sqlite3.Connection('phonebook2')
cur=con.cursor()
cur.execute("create table if not exists maindb(contactid integer primary key autoincrement,fname varchar(20),mname varchar(20),lname varchar(20),cname varchar(30),address varchar(40),city varchar(20),pincode varchar(6),websiteurl varchar(50),dob date)")
cur.execute("create table if not exists phonedb(contactid integer ,ctype varchar(10),pno varchar(10),primary key(contactid,pno),foreign key (contactid) REFERENCES maindb(contactid))")
cur.execute("create table if not exists emaildb(contactid integer ,etype varchar(10),email varchar(40),primary key(contactid,email),foreign key (contactid) REFERENCES maindb(contactid))")
con.commit()
#Gui
root=Tk()
root.title("PhoneBook ")
root.geometry("650x700")
root.config(bg='light blue')

img=PhotoImage(file='logo.gif')
Label(root,image=img).place(x=220,y=0)
Label(root,text="First Name",font="Arial 12 ").place(x=70,y=200)
Label(root,text="Middle  Name",font="Arial 12 ").place(x=70,y=225)
Label(root,text="Last Name",font="Arial 12 ").place(x=70,y=250)
Label(root,text="Company Name",font="Arial 12 ").place(x=70,y=275)
Label(root,text="Address",font="Arial 12 ").place(x=70,y=300)
Label(root,text="city",font="Arial 12 ").place(x=70,y=325)
Label(root,text="Pincode",font="Arial 12 ").place(x=70,y=350)
Label(root,text="Website URL",font="Arial 12 ").place(x=70,y=375)
Label(root,text="Date of Birth",font="Arial 12 ").place(x=70,y=400)
e1=Entry(root,font="Arial 12 ")
e1.place(x=240,y=200)
e2=Entry(root,font="Arial 12 ")
e2.place(x=240,y=225)
e3=Entry(root,font="Arial 12 ")
e3.place(x=240,y=250)
e4=Entry(root,font="Arial 12 ")
e4.place(x=240,y=275)
e5=Entry(root,font="Arial 12 ")
e5.place(x=240,y=300)
e6=Entry(root,font="Arial 12 ")
e6.place(x=240,y=325)
e7=Entry(root,font="Arial 12 ")
e7.place(x=240,y=350)
e8=Entry(root,font="Arial 12 ")
e8.place(x=240,y=375)
e9=Entry(root,font="Arial 12 ")
e9.place(x=240,y=400)
Label(root,text='Select Phone Type :',font='Aerial 14',foreground='blue').place(x=1,y=430)
v1=IntVar()
r1=Radiobutton(root,text='Office',variable=v1,value=1).place(x=290,y=430)
r2=Radiobutton(root,text='Home',variable=v1,value=2).place(x=430,y=430)
r3=Radiobutton(root,text='Mobile',variable=v1,value=3).place(x=560,y=430)
Label(root,text="Phone Number",font="Aerial 12").place(x=70,y=460)
e10=Entry(root,font="Arial 12")
e10.place(x=240,y=460)
Label(root,text='Select Email Type :',font='Aerial 14',foreground='blue').place(x=1,y=490)
v2=IntVar()
r4=Radiobutton(root,text='Office',variable=v2,value=4).place(x=290,y=490)
r5=Radiobutton(root,text='Personal',variable=v2,value=5).place(x=430,y=490)
Label(root,text="Email Id",font="Aerial 12").place(x=70,y=520)
e11=Entry(root,font="Arial 12")
e11.place(x=240,y=520)

#save function
def indata():
    if len(e1.get()) == 0:
        tkMessageBox.showinfo('information','Your name is blank !!')
    elif len(e10.get()) == 0:
        tkMessageBox.showinfo('information','Your Phone number is blank!!')
    else:
        cur.execute("insert into maindb(fname,mname,lname,cname,address,city,pincode,websiteurl,dob) values (?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()))
        cur.execute("insert into phonedb(contactid,ctype,pno)values((select max(contactid)from maindb),?,?)",(v1.get(),e10.get()))
        cur.execute("insert into emaildb(contactid,etype,email)values((select max(contactid)from maindb),?,?)",(v2.get(),e11.get()))
        con.commit()
        print ("Data Inserted")
        tkMessageBox.showinfo('saved','Data Saved successfully')

        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)

#search function
def search():
    
    root1=Tk()
    root1.config(bg='light blue')

    def ser(e=0):
        
        cur.execute("select fname,mname,lname from maindb where fname like ? or mname like ? or lname like ?",(('%'+e12.get()+'%'),('%'+e12.get()+'%'),('%'+e12.get()+'%')))
        o=cur.fetchall()
        lb.delete(0,END)
        for i in range(len(o)):
            k=o[i][0]+' '+o[i][1]+' '+o[i][2]
            lb.insert(END,k)
        
    def close1():
        root1.destroy()
        
    root1.geometry("650x700")
    root1.title("Search")
    Label(root1,text="Searching PhoneBook",font="Aerial 20",relief='ridge').place(x=150,y=0)
    Label(root1,text="Enter name : ",font="Aerial 10 ").place(x=50,y=50)
    Button(root1,text="Close",font="Aerial 10",command=close1).place(x=250,y=670)
    e12=Entry(root1,font="Aerial 10")
    e12.place(x=220,y=50)
    lb=Listbox(root1,font='Aerial 14',height=25,width=100,selectmode= SINGLE)
    lb.place(x=1,y=79)
    x=cur.execute("select contactid,fname,mname,lname from maindb order by fname").fetchall()
    for i in x:
        lb.insert(END,i[1]+' '+i[2]+' '+i[3])
    
        
    lb2=Listbox(root1,font='Aerial 14',height=25,width=100)
    def selectitem(e=1):
        try:
            s=(lb.get(lb.curselection()))
        except:
            print('minor warning')
        v= s.split(),'spli'
        #print v
        k=str(v[0][0])
        #print k
        cid=cur.execute("select contactid from maindb where fname=?",(k,)).fetchall()
        #print x[k]
        #print 'cid ', cid[0][0]
##        idd=cid[0]
##        print idd,'idd',type(idd)
        def delete():
            cur.execute("delete from maindb where contactid=?",(cid[0][0],))
            cur.execute('delete from phonedb where contactid=?',(cid[0][0],))
            cur.execute('delete from emaildb where contactid=?',(cid[0][0],))
            con.commit()
            close1()
            tkMessageBox.showinfo('delete','Data deleted successfully')
            
        Button(root1,text="Delete Contact",font="Aerial 10 bold",command=delete,bg='Red',relief='ridge').place(x=380,y=50)
        print (cid,'cid')
        print (cid[0],'cid[0]')
        cur.execute('select * from maindb where contactid=?',(cid[0][0],))
        M=cur.fetchall()
        print (M)
        cur.execute('select * from phonedb where contactid=?',(cid[0][0],))
        P=cur.fetchall()
        cur.execute('select * from emaildb where contactid=?',(cid[0][0],))
        E=cur.fetchall()
        #print P[0][1]
        
        lb2.place(x=1,y=79)
        lb2.insert(END,"First Name : "+M[0][1])
        lb2.insert(END,"Middle Name : "+M[0][2])
        lb2.insert(END,"Last Name : "+M[0][3])
        lb2.insert(END,"Company Name : "+M[0][4])
        lb2.insert(END,"Address : "+M[0][5])
        lb2.insert(END,"City : "+M[0][6])
        lb2.insert(END,"Pincode : "+M[0][7])
        lb2.insert(END,"Website URL : "+M[0][8])
        lb2.insert(END,"Date of Birth : "+M[0][9])
        lb2.insert(END,"Phone details.....")
        #print v1.get()
        if(v1.get()==1):
            val='office'
        elif (v1.get()==2):
            val='Home'
        else:
            val='Mobile'
        lb2.insert(END,val+' : '+P[0][2])
        lb2.insert(END,"Email  details.....")
        #print v2.get()
        if(v2.get()==4):
            val='office'
        else :
            val='Personal'
        lb2.insert(END,val+' : '+E[0][2])
    
    e12.bind("<KeyRelease>",ser)
    root1.bind("<<ListboxSelect>>",selectitem)
    
    root1.mainloop()
#edit function
def edit():
    root2=Tk()
    root2.config(bg='light blue')

    def ser(e=0):
        lb.delete(0,END)
        cur.execute("select fname,mname,lname from maindb where fname like ? or mname like ? or lname like ?",(('%'+e13.get()+'%'),('%'+e13.get()+'%'),('%'+e13.get()+'%')))
        o=cur.fetchall()
        for i in range(len(o)):
            k=o[i][0]+' '+o[i][1]+' '+o[i][2]
            lb.insert(END,k)
    def close1():
        root2.destroy()
    root2.geometry("650x700")
    root2.title("Search")
    Label(root2,text="Updating PhoneBook",font="Aerial 20",relief='ridge',bg='Green').place(x=150,y=0)
    Label(root2,text="Enter name for updating : ",font="Aerial 10 ").place(x=50,y=50)
    Button(root2,text="Close",font="Aerial 10",command=close1).place(x=250,y=670)
    e13=Entry(root2,font="Aerial 10")
    e13.place(x=220,y=50)
    lb=Listbox(root2,font='Aerial 14',height=25,width=100,selectmode= BROWSE)
    lb.place(x=1,y=79)
    x=cur.execute("select contactid,fname,mname,lname from maindb order by fname").fetchall()
 #   print x
 
    for i in x:
        lb.insert(END,i[1]+' '+i[2]+' '+i[3])
    def selectitem(event):
        s=(lb.get(lb.curselection()))
        v= s.split(),'spli'
        #print v
        k=str(v[0][0])
        #print k
        cid=cur.execute("select contactid from maindb where fname=?",(k,)).fetchall()
        root3=Tk()
        root3.title("Updating PHONEBOOK ")
        root3.geometry("650x700")
        root3.config(bg='light blue')
        print (cid[0])
        cur.execute('select * from maindb where contactid=?',(cid[0][0],))
        M=cur.fetchall()
        cur.execute('select * from phonedb where contactid=?',(cid[0][0],))
        P=cur.fetchall()
        cur.execute('select * from emaildb where contactid=?',(cid[0][0],))
        E=cur.fetchall()
        print (M[0][1],'printing the details')
        Label(root3,text="UPDATING",font="Aerial 25 bold underline",bg='light green',relief='ridge').place(x=200,y=100)
        Label(root3,text="First Name",font="Arial 12 ").place(x=70,y=200)
        Label(root3,text="Middle  Name",font="Arial 12 ").place(x=70,y=225)
        Label(root3,text="Last Name",font="Arial 12 ").place(x=70,y=250)
        Label(root3,text="Company Name",font="Arial 12 ").place(x=70,y=275)
        Label(root3,text="Address",font="Arial 12 ").place(x=70,y=300)
        Label(root3,text="city",font="Arial 12 ").place(x=70,y=325)
        Label(root3,text="Pincode",font="Arial 12 ").place(x=70,y=350)
        Label(root3,text="Website URL",font="Arial 12 ").place(x=70,y=375)
        Label(root3,text="Date of Birth",font="Arial 12 ").place(x=70,y=400)
        Label(root3,text="Phone number",font="Aerial 12 ").place(x=70,y=425)
        Label(root3,text="Email id ",font="Aerial 12 ").place(x=70,y=450)
        
##        x=cur.execute("select fname,mname,lname,cname,address,city,pincode,websiteurl,dob from maindb").fetchall()
##        print x
        e11=Entry(root3,font="Arial 12 ")
        e11.place(x=240,y=200)
        e11.insert(END,M[0][1])
        e22=Entry(root3,font="Arial 12 ")
        e22.place(x=240,y=225)
        e22.insert(END,M[0][2])
        e33=Entry(root3,font="Arial 12 ")
        e33.place(x=240,y=250)
        e33.insert(END,M[0][3])
        e44=Entry(root3,font="Arial 12 ")
        e44.place(x=240,y=275)
        e44.insert(END,M[0][4])
        e55=Entry(root3,font="Arial 12 ")
        e55.place(x=240,y=300)
        e55.insert(END,M[0][5])
        e66=Entry(root3,font="Arial 12 ")
        e66.place(x=240,y=325)
        e66.insert(END,M[0][6])
        e77=Entry(root3,font="Arial 12 ")
        e77.place(x=240,y=350)
        e77.insert(END,M[0][7])
        e88=Entry(root3,font="Arial 12 ")
        e88.place(x=240,y=375)
        e88.insert(END,M[0][8])
        e99=Entry(root3,font="Arial 12 ")
        e99.place(x=240,y=400)
        e99.insert(END,M[0][9])
        e1010=Entry(root3,font="Arial 12 ")
        e1010.place(x=240,y=420)
        pno=cur.execute("select pno from phonedb where contactid=?",(cid[0][0],)).fetchall()
        print (pno[0][0],'pno')
        email=cur.execute("select email from emaildb where contactid=?",(cid[0][0],)).fetchall()

        #print v2.get()

        e1010.insert(END,pno[0][0])
        e1111=Entry(root3,font="Arial 12 ")
        e1111.place(x=240,y=450)
        e1111.insert(END,email[0][0])
        print ('e',e9.get())
        def close():
            root3.destroy()
        def update():
            a=e11.get()
            print (cid[0])
            cur.execute("update maindb set fname=? where contactid=?",(e11.get(),cid[0][0]))
            cur.execute("update maindb set mname=? where contactid=?",(e22.get(),cid[0][0]))
            cur.execute("update maindb set lname=? where contactid=?",(e33.get(),cid[0][0]))
            cur.execute("update maindb set cname=? where contactid=?",(e44.get(),cid[0][0]))
            cur.execute("update maindb set address=? where contactid=?",(e55.get(),cid[0][0]))
            cur.execute("update maindb set city=? where contactid=?",(e66.get(),cid[0][0]))
            cur.execute("update maindb set pincode=? where contactid=?",(e77.get(),cid[0][0]))
            cur.execute("update maindb set websiteurl=? where contactid=?",(e88.get(),cid[0][0]))
            cur.execute("update maindb set dob=? where contactid=?",(e99.get(),cid[0][0]))
            cur.execute("update phonedb set pno=? where contactid=?",(e1010.get(),cid[0][0]))
            cur.execute("update emaildb set email=? where contactid=?",(e1111.get(),cid[0][0]))
            con.commit()
            print ("Data Updated")
            tkMessageBox.showinfo('updated','Data updated successfully')
            root3.destroy()
            root2.destroy()
            
            
        Button(root3,text="Update",font="Arial 12 bold",command=update,activebackground="Magenta",activeforeground="Black",bg="Cyan",relief='ridge').place(x=200,y=600)
        Button(root3,text="Close",font="Arial 12 bold",command=close,activebackground="Magenta",activeforeground="Black",bg="Cyan",relief='ridge').place(x=400,y=600)
        root3.mainloop()


    lb.bind("<<ListboxSelect>>",selectitem)
    e13.bind("<KeyRelease>",ser)
    root2.mainloop()
    
#close function
def close():
        flag=tkMessageBox.askyesno('OOPS','You are closing the app')
        if flag==1:
            root.destroy()
            

Button(root,text="Save",font="Arial 12 bold ",command=indata,activebackground="Magenta",activeforeground="Black",bg="Cyan",relief='ridge').place(x=80,y=550)
Button(root,text="Search",font="Arial 12 bold",command=search,activebackground="Magenta",activeforeground="Black",bg="Cyan",relief='ridge').place(x=220,y=550)
Button(root,text="Close",font="Arial 12 bold",command=close,activebackground="Magenta",activeforeground="Black",bg="Cyan",relief='ridge').place(x=340,y=550)
Button(root,text="Edit",font="Arial 12 bold",command=edit,activebackground="Magenta",activeforeground="Black",bg="Cyan",relief='ridge').place(x=460,y=550)

root.mainloop()

