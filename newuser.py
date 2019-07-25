import os
from  tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image

def fun():
    os.system("python menu.py")

newuser = Tk()
newuser.geometry('600x400')
l1=Label(newuser,text=" Yo ! Food ",font = "Times 30 bold")
#l1.pack()
img=ImageTk.PhotoImage(Image.open(r"burito.jpg"))
label = Label(newuser,image=img)
label.image = img # keep a reference!
label.place(x=0,y=0)

label_1 = Label(newuser, text="First name")
label_1.place(x=290,y=42)
entry_1 = Entry(newuser)
entry_1.place(x=395,y=40)

label_2 = Label(newuser, text="Last name")
label_2.place(x=290,y=82)
entry_2 = Entry(newuser)
entry_2.place(x=395,y=80)

label_3 = Label(newuser, text="Email")
label_3.place(x=300,y=122)
entry_3 = Entry(newuser)
entry_3.place(x=395,y=120)

label_4 = Label(newuser, text="Username")
label_4.place(x=290,y=162)
entry_4 = Entry(newuser)
entry_4.place(x=395,y=160)

label_5 = Label(newuser, text="Password")
label_5.place(x=290,y=202)
entry_5 = Entry(newuser)
entry_5.place(x=395,y=200)

label_6 = Label(newuser, text="Confirm Password")
label_6.place(x=260,y=242)
entry_6 = Entry(newuser)
entry_6.place(x=395,y=240)

label_7 = Label(newuser, text="Address")
label_7.place(x=290,y=282)
entry_7 = Text(newuser,width=15,height=2)
entry_7.place(x=395,y=280)

label_8 = Label(newuser, text="Contact no.",width=8)
label_8.place(x=290,y=327)
entry_8 = Entry(newuser)
entry_8.place(x=395,y=325)

btn1 = Button(newuser, text=" Sign up ",command=fun)
btn1.place(x=350,y=370)

l1=Label(newuser,text=" FOODIES APP ",font = "Times 20 bold")
l1.place(x=78,y=355)
newuser.mainloop()
