#first page
import os
from tkinter import *
from PIL import ImageTk, Image
def menu():
    os.system('python menu.py')
def newuser():
    os.system('python newuser.py')
def login():
    os.system('python login.py')
firstpage=Tk()
firstpage.geometry('900x600')
l1=Label(firstpage,text=" Yo ! Food ",font = "Times 30 bold")#bg does not work with buttons on mac
l1.place(x=1,y=2)
l1=Button(firstpage,text=" Menu",bg="red",height=2,width=10,command=menu)
l1.place(x=615,y=2)
l1=Button(firstpage,text=" New user ",bg="red",height=2,width=10,command=newuser)
l1.place(x=710,y=2)
l1=Button(firstpage,text=" Login ",bg="red",height=2,width=10,command=login)
l1.place(x=805,y=2)
img=ImageTk.PhotoImage(Image.open(r"chicken.jpg"))
label = Label(firstpage,image=img)
label.image = img # keep a reference!
label.place(x=0,y=40)
l1=Label(firstpage,text=" Yo! ",font = "Times 30 bold")
l1.place(x=400,y=260)
l1=Label(firstpage,text="  Food  ",font = "Times 30 bold")
l1.place(x=380,y=310)

l1=Label(firstpage,text=" Restaurant ",font = "Times 30 bold")
l1.place(x=350,y=360)
firstpage.mainloop()