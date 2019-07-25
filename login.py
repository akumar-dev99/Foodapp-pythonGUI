#login
import os
from  tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image


def fun():
    username=entry_1.get()
    password=entry_2.get()
    if (username == 'admin' and password == 'secret'):
        os.system('python homepage.py')
    else:
        messagebox.showerror("Error", "Invalid login")

login = Tk()
login.geometry('600x400')
l1=Label(login,text=" FOODIES APP ",font = "Times 30 bold")
#l1.pack()
img=ImageTk.PhotoImage(Image.open(r"burito.jpg"))
label = Label(login,image=img)
label.image = img # keep a reference!
label.place(x=0,y=0)
label_1 = Label(login, text="username",width=8,font=10)
label_1.place(x=290,y=132)

entry_1 = Entry(login)
entry_1.place(x=380,y=130)

label_1 = Label(login, text="password",width=8,font= 10)
label_1.place(x=290,y=182)

entry_2 = Entry(login)
entry_2.place(x=380,y=180)

btn1 = Button(login, text=" Sign in ",command=fun)
btn1.place(x=350,y=260)

l1=Label(login,text=" FOODIES APP ",font = "Times 20 bold")
l1.place(x=78,y=355)
login.mainloop()
