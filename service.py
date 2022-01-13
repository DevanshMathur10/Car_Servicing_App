import mysql.connector as sql
from tkinter import *
import re
import os
from PIL import Image
from PIL import ImageTk
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS=os.environ.get('PYMAIL')
EMAIL_PASSWORD=os.environ.get('PYPASS')

#import vehicles

#con=sql.connect(user=os.environ.get('SQLNAME'),password=os.environ.get('SQLPASS'),host=os.environ.get('SQLHOST'),database="automotives")
#c=con.cursor()
#TABLES = {}
"""
TABLES['cars']=('''
CREATE TABLE services(
    name text,
    company text,
    model text,
    licenseno text
)
''')
"""
#c.execute(TABLES["cars"])

def servicingwindow():
    root2=Toplevel()
    root2.title("SERVICING")
    root2.geometry("650x300")
    root2.state('zoomed')
    root2.configure(bg='#7f4ca6')
    
    myimg2=Image.open("C:/Users/dr_de/Documents/VS/EL PROJ/MIDSEMPROJ/back2.png")
    newimg2=ImageTk.PhotoImage(myimg2)
    imglbl=Label(root2,image=newimg2)
    imglbl.place(x=0, y=0, relwidth=1, relheight=1)

    frame1=Frame(root2,bg='#7f4ca6')
    frame1.place(x=760,y=390,anchor='center')
    
    con=sql.connect(user=os.environ.get('SQLNAME'),password=os.environ.get('SQLPASS'),host=os.environ.get('SQLHOST'),database="automotives")
    c=con.cursor()

    selcom=StringVar()
    selmod=StringVar()
    servar=StringVar()

    ser=("""SELECT service FROM servicereq""")
    c.execute(ser)
    serrec=c.fetchall()
    servicenames=list(serrec)

    com=("""SELECT DISTINCT company FROM cars""")
    c.execute(com)
    comrec=c.fetchall()
    companies=list(comrec)

    comen=Entry(frame1)
    moden=Entry(frame1)
    seren=Entry(frame1)

    selcom.set("Choose Company")
    selmod.set("Choose Model")
    servar.set("Choose Service")

    model_box=OptionMenu(frame1,selmod,"")
    model_box.configure(state=DISABLED)
    model_box.grid(row=2,column=1)

    def loadcars(companyname):
        global selcomstr
        global selcomstr1
        global selmodstr1
        con=sql.connect(user=os.environ.get('SQLNAME'),password=os.environ.get('SQLPASS'),host=os.environ.get('SQLHOST'),database="automotives")
        c=con.cursor()
        comen.delete(0,END)
        comen.insert(0,selcom.get())
        selcomstr=re.sub("[(),]","",comen.get())
        selcomstr1=re.sub("[(),'']","",comen.get())

        mod="""SELECT model FROM cars WHERE company="""+selcomstr
        c.execute(mod)
        modrec=c.fetchall()
        cars=list(modrec)
        model_box=OptionMenu(frame1,selmod,*cars)
        model_box.grid(row=2,column=1)
        
        con.close()

    def showcost(servicename):
        global cosstr
        con=sql.connect(user=os.environ.get('SQLNAME'),password=os.environ.get('SQLPASS'),host=os.environ.get('SQLHOST'),database="automotives")
        c=con.cursor()

        seren.delete(0,END)
        seren.insert(0,servar.get())
        serenstr2=re.sub("[(),]","",seren.get())
        cosname="""SELECT cost FROM servicereq WHERE service="""+serenstr2
        c.execute(cosname)
        cos=c.fetchall()
        cosstr=re.sub("[()[\],]","",str(cos))
        
        cost=Label(frame1,text="The cost for your service is ₹ "+cosstr+" .",font=("Book Antiqua",30),background='#7f4ca6')
        cost.grid(row=6,column=0,columnspan=2,sticky=W+E) 
        cost.forget()

        con.close()

    name=Label(frame1,text="Your Name",background='#7f4ca6',font=('Book Antiqua', 10))
    name.grid(row=0,column=0,padx=8,pady=(5,0))
    company=Label(frame1,text="Car Company",background='#7f4ca6',font=('Book Antiqua', 10))
    company.grid(row=1,column=0)
    model=Label(frame1,text="Car Model",background='#7f4ca6', font=('Book Antiqua', 10))
    model.grid(row=2,column=0)
    sername=Label(frame1,text="Service Required",background='#7f4ca6', font=('Book Antiqua', 10))
    sername.grid(row=3,column=0)  
    licenseno=Label(frame1,text="License No.",background='#7f4ca6', font=('Book Antiqua', 10))
    licenseno.grid(row=4,column=0)   

    name_box=Entry(frame1,width=35,borderwidth=2)
    name_box.grid(row=0,column=1,pady=(5,0))
    company_box=OptionMenu(frame1,selcom,*companies,command=loadcars)
    company_box.grid(row=1,column=1)
    sername_box=OptionMenu(frame1,servar,*servicenames,command=showcost)
    sername_box.grid(row=3,column=1)
    licenseno_box=Entry(frame1,width=35,borderwidth=2)
    licenseno_box.grid(row=4,column=1,padx=10)
    em_box=Entry(frame1,width=35,borderwidth=2,fg='#696969')
    em_box.insert(0,'Enter your email here for the receipt')
    em_box.grid(row=7,column=0,columnspan=2,pady=(3,10))

    def temp_text(e):
        em_box.delete(0,"end")

    em_box.bind("<FocusIn>", temp_text)

    def saverecord():
        global frec
        con=sql.connect(user=os.environ.get('SQLNAME'),password=os.environ.get('SQLPASS'),host=os.environ.get('SQLHOST'),database="automotives")
        c=con.cursor()
        
        moden.delete(0,END)
        moden.insert(0,selmod.get())
        selmodstr1=re.sub("[(),'']","",moden.get())

        seren.delete(0,END)
        seren.insert(0,servar.get())
        serenstr1=re.sub("[(),'']","",seren.get())

        addrec=("""INSERT INTO services 
              (name,company,model,licenseno,service,cost) 
              VALUES (%(name)s,%(company)s,%(model)s,%(licenseno)s,%(servicename)s,%(cost)s)""")

        record={
            'name':str(name_box.get()),
            'company':str(selcomstr1),
            'model':str(selmodstr1),
            'licenseno':str(licenseno_box.get()),
            'servicename':str(serenstr1),
            'cost':str(cosstr)

        }      
    
        c.execute(addrec,record)
        con.commit()

        list1=[key.upper()+" : "+value.upper() for key,value in record.items()]
        rec=''
        for x in list1:
            rec+="\n"+x+"\n"
        frec=rec.strip()

        body=frec
        message=EmailMessage()
        message['Subject']=" RECEIPT FOR SERVICE "
        message['From']=EMAIL_ADDRESS
        message['To']=str(em_box.get())
        message.set_content(body)

        con.close()
        root2.destroy()

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)

    submitbtn=Button(frame1,text="SEND FOR SERVICE",command=saverecord)
    submitbtn.grid(row=5,column=0,columnspan=2,padx=10,pady=5,ipadx=32,sticky=W+E)

    con.close()
    root2.mainloop()

#con.close()
servicingwindow()
 
