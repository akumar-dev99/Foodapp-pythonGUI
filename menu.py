import os
from  tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image
menu = Tk()
menu.geometry('1000x800')

img=ImageTk.PhotoImage(Image.open(r"burito.jpg"))
label = Label(menu,image=img)
label.image = img # keep a reference!
label.pack(fill=BOTH,expand=YES)


def menu():
    os.system("payment.py")


Label(menu, text=" Chinese ", font="Times 15 bold", width=15).place(x=420, y=40)
Label(menu,text="Quantity",font="Times 11 bold").place(x=687,y=90)
Label(menu, text=" Hakka Noodles ", font="Times 11 bold", width=15).place(x=420, y=120)
Label(menu, text="120.00", font="Times 11 bold", width=15).place(x=570, y=120)
Text(menu,width=6,height=1).place(x=690,y=120)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=120)

Label(menu, text=" Manchurian", font="Times 11 bold", width=15).place(x=420, y=150)
Label(menu, text="220.00", font="Times 11 bold", width=15).place(x=570, y=150)
Text(menu,width=6,height=1).place(x=690,y=150)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=150)

Label(menu, text=" Cheese Chilly", font="Times 11 bold", width=15).place(x=420, y=180)
Label(menu, text="180.00", font="Times 11 bold", width=15).place(x=570, y=180)
Text(menu,width=6,height=1).place(x=690,y=180)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=180)

Label(menu, text=" Fried Rice ", font="Times 11 bold", width=15).place(x=420, y=210)
Label(menu, text="200.00", font="Times 11 bold", width=15).place(x=570, y=210)
Text(menu,width=6,height=1).place(x=690,y=210)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=210)

Label(menu, text=" Chopsuey", font="Times 11 bold", width=15).place(x=420, y=240)
Label(menu, text="90.00", font="Times 11 bold", width=15).place(x=570, y=240)
Text(menu,width=6,height=1).place(x=690,y=240)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=240)

Label(menu, text=" Main Course ", font="Times 15 bold", width=15).place(x=420, y=290)

Label(menu, text=" Dal Makhni", font="Times 11 bold", width=15).place(x=420, y=350)
Label(menu, text="120.00", font="Times 11 bold", width=15).place(x=570, y=350)
Text(menu,width=6,height=1).place(x=690,y=350)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=350)

Label(menu, text=" Dal Tadka", font="Times 11 bold", width=15).place(x=420, y=390)
Label(menu, text="80.00", font="Times 11 bold", width=15).place(x=570, y=390)
Text(menu,width=6,height=1).place(x=690,y=390)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=390)


Label(menu, text=" Shahi Paneer", font="Times 11 bold", width=15).place(x=420, y=430)
Label(menu, text="200.00", font="Times 11 bold", width=15).place(x=570, y=430)
Text(menu,width=6,height=1).place(x=690,y=430)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=430)

Label(menu, text=" Kadhai Paneer", font="Times 11 bold", width=15).place(x=420, y=470)
Label(menu, text="210.00", font="Times 11 bold", width=15).place(x=570, y=470)
Text(menu,width=6,height=1).place(x=690,y=470)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=470)

Label(menu, text=" Pindi Chana", font="Times 11 bold", width=15).place(x=420, y=510)
Label(menu, text="170.00", font="Times 11 bold", width=15).place(x=570, y=510)
Text(menu,width=6,height=1).place(x=690,y=510)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=510)

Label(menu, text=" Breads ", font="Times 15 bold", width=15).place(x=420, y=570)

Label(menu, text=" Plain Naan", font="Times 11 bold", width=15).place(x=420, y=630)
Label(menu, text="12.00", font="Times 11 bold", width=15).place(x=570, y=630)
Text(menu,width=6,height=1).place(x=690,y=630)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=630)

Label(menu, text=" Butter Naan", font="Times 11 bold", width=15).place(x=420, y=670)
Label(menu, text="18.00", font="Times 11 bold", width=15).place(x=570, y=670)
Text(menu,width=6,height=1).place(x=690,y=670)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=670)

Label(menu, text=" Lachha Parantha", font="Times 11 bold", width=15).place(x=420, y=710)
Label(menu, text="20.00", font="Times 11 bold", width=15).place(x=570, y=710)
Text(menu,width=6,height=1).place(x=690,y=710)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=710)


Label(menu, text=" Stuffed Naan ", font="Times 11 bold", width=15).place(x=420, y=750)
Label(menu, text="20.00", font="Times 11 bold", width=15).place(x=570, y=750)
Text(menu,width=6,height=1).place(x=690,y=750)
Button(menu, text="Add to cart",font="Times 12 bold",width=15).place(x=780,y=750)
Button(menu,text="Proceed", command= menu, width=20).place(x=200,y=400)
menu.mainloop()
