from tkinter import *
from PIL import Image
from tkvideo import tkvideo
from PIL import ImageTk
from emailsender import p
from emailsender import sendpass
import os
from service import servicingwindow
import mysql.connector as sql

con=sql.connect(user=os.environ.get('SQLNAME'),password=os.environ.get('SQLPASS'),host=os.environ.get('SQLHOST'),database="automotives")
c=con.cursor()

root=Tk()
root.title("LOGIN")
root.geometry("845x710")
root.configure(bg='#2E0063')
root.state('zoomed')

imglbl=Label(root)
imglbl.place(x=0, y=0, relwidth=1, relheight=1)
player = tkvideo("C:/Users/dr_de/Documents/VS/testnew2.mp4", imglbl,loop = 1, size = (1920,1080))
player.play()

#myimg1_=Image.open("C:/Users/dr_de/Documents/VS/EL PROJ/MIDSEMPROJ/back9.jpg")
#newimg1_=ImageTk.PhotoImage(myimg1_)
#imglbl=Label(root,image=newimg1_)
#imglbl.place(x=0, y=0, relwidth=1, relheight=1)

frame=Frame(root,bg='#2E0063', relief=RAISED)
frame.place(x=760,y=390,anchor='center')

email=Label(frame,text="Email",background="#2E0063",fg='white', font=('Book Antiqua', 11))
email.grid(row=0,column=0,padx=8,pady=(5,0))
password=Label(frame,text="Pass",background="#2E0063",fg='white', font=('Book Antiqua', 11))
password.grid(row=2,column=0)

email_box=Entry(frame,width=35,borderwidth=2)
email_box.grid(row=0,column=1,pady=(5,0),padx=10)
pass_box=Entry(frame,width=35,borderwidth=2)
pass_box.grid(row=2,column=1)

sendbtn=Button(frame,text="SEND OTP",command=lambda: sendpass(str(email_box.get())))
sendbtn.grid(row=1,column=1,columnspan=2,padx=10,pady=5,ipadx=50)

email_str=str(email_box.get())

slideshow=Frame(frame)
"""slideshow.grid(row=5,column=0,columnspan=2)

myimg1=Image.open("C:/Users/dr_de/Documents/VS/EL PROJ/MIDSEMPROJ/images/img (1).jpg")
myimg2=Image.open("C:/Users/dr_de/Documents/VS/EL PROJ/MIDSEMPROJ/images/img (2).jpg")
myimg3=Image.open("C:/Users/dr_de/Documents/VS/EL PROJ/MIDSEMPROJ/images/img (3).jpg")
myimg4=Image.open("C:/Users/dr_de/Documents/VS/EL PROJ/MIDSEMPROJ/images/img (4).jpg")
myimg5=Image.open("C:/Users/dr_de/Documents/VS/EL PROJ/MIDSEMPROJ/images/img (5).jpg")
myimg6=Image.open("C:/Users/dr_de/Documents/VS/EL PROJ/MIDSEMPROJ/images/img (6).jpg")
myimg7=Image.open("C:/Users/dr_de/Documents/VS/EL PROJ/MIDSEMPROJ/images/img (7).jpg")

resize1=myimg1.resize((420,280),Image.ANTIALIAS)
resize2=myimg2.resize((420,280),Image.ANTIALIAS)
resize3=myimg3.resize((420,280),Image.ANTIALIAS)
resize4=myimg4.resize((420,280),Image.ANTIALIAS)
resize5=myimg5.resize((420,280),Image.ANTIALIAS)
resize6=myimg6.resize((420,280),Image.ANTIALIAS)
resize7=myimg7.resize((420,280),Image.ANTIALIAS)

newimg1=ImageTk.PhotoImage(resize1)
newimg2=ImageTk.PhotoImage(resize2)
newimg3=ImageTk.PhotoImage(resize3)
newimg4=ImageTk.PhotoImage(resize4)
newimg5=ImageTk.PhotoImage(resize5)
newimg6=ImageTk.PhotoImage(resize6)
newimg7=ImageTk.PhotoImage(resize7)

l=Label(slideshow)
l.pack()

x=1

def move():
    global x
    if x == 8:
        x = 1
    if x == 1:
        l.config(image=newimg1)
    elif x == 2:
        l.config(image=newimg2)
    elif x == 3:
        l.config(image=newimg3)
    elif x == 4:
        l.config(image=newimg4)
    elif x == 5:
        l.config(image=newimg5)
    elif x == 6:
        l.config(image=newimg6)
    elif x == 7:
        l.config(image=newimg7)
    x = x+1
    frame.after(2000, move)

move()"""

def submitpass():
    if pass_box.get()==p:
        passshow=Label(frame,text=" CORRECT OTP ",background="#2E0063",fg='white', font=('arial', 9))
        passshow.grid(row=4,column=0,columnspan=2,padx=8)
        servicingwindow()
    else:
        passshow=Label(frame,text="INCORRECT OTP",background="#2E0063",fg='white', font=('arial', 9))
        passshow.grid(row=4,column=0,columnspan=2,padx=8)

checkbtn=Button(frame,text="CHECK OTP",command=submitpass)
checkbtn.grid(row=3,column=1,columnspan=2,padx=10,pady=5,ipadx=45)

con.close()
root.mainloop()
