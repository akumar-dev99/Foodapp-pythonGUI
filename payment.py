from tkinter import *
import tkinter.messagebox as mb

from PIL import ImageTk,Image
root=Tk()
root.title("payment options")
root.geometry("600x400")
global img
img=ImageTk.PhotoImage(Image.open(r"burito.jpg"))
def fourth():
    if (len(e12.get())==16 and len(e33.get())==16):
         ans=mb.askquestion("Confirm?","You will now be charged for your order.Continue?")
         if ans=='yes':
             a= mb.askquestion('showinfo', "payment successfully done...do you want to continue??")
             if a=='yes':
                 master1.withdraw()
                 root.deiconify()
             else:
                 master1.withdraw()


    else:
         mb.showinfo('showinfo', "invalid info")
def second():

    global master1
    master1 = Toplevel()

    master1.geometry("569x500")
    img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\amit_\OneDrive\Desktop\payment.png"))
    label2 = Label(master1, image=img2)
    label2.image = img2
    label2.place(x=0, y=0)
    Label(master1, text="credit card number ").place(x=100,y=200)

    Label(master1, text="valid upto ").place(x=100,y=250)
    Label(master1, text="card holder name ").place(x=100,y=300)
    Label(master1, text="enter aadhar card no ").place(x=100,y=350)
    global e12,e33

    e12 = Entry(master1)

    e12.place(x=300,y=200)

    e11 = Entry(master1)
    e22 = Entry(master1)
    e33 = Entry(master1)

    e11.place(x=300,y=250)
    e22.place(x=300,y=300)
    e33.place(x=300,y=350)
    Button(master1, text='done', command=fourth).place(x=300,y=400)


def payment():
    global v
    if v.get()==1:
        root.withdraw()

        order=Toplevel()
        order.title("order placed")
        order.geometry("600x400")
        img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\amit_\OneDrive\Desktop\burito.jpg"))
        label1 = Label(order, image=img1)
        label1.image=img1
        label1.place(x=0,y=0)
        label2 = Label(order, text="order successfully placed")
        label2.place(x=350,y=100)
    else:
        root.withdraw()
        second()


label=Label(root,image=img)
label.place(x=0,y=0)
label1=Label(root,text="choose the payment option")
label1.place(x=350,y=100)
global v
v = IntVar()
r1=Radiobutton(root,text="cash on delivery",variable=v,value=1)
r1.place(x=350,y=150)
r2=Radiobutton(root,text="credit/debit card",variable=v,value=2)
r2.place(x=350,y=200)
b=Button(root,text="submit",command=payment)
b.place(x=350,y=300)

root.mainloop()