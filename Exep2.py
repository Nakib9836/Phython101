from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title("Nakib Biker Shop")
GUI.geometry('500x500')


L1=Label(GUI,text='Program record Motorbike',font='Angsana',fg='blue')
L1.pack()


def Button1():
    text = '125 คัน'
    messagebox.showinfo('Stock Honda',text)


FB1= LabelFrame(GUI)
FB1.place(x=60,y=80)
B1=ttk.Button(FB1,text='Honda',command=Button1)
B1.pack(ipadx=20,ipady=20)


def Button2():
    text = '30 คัน'
    messagebox.showinfo('Stock Yamaha',text)


FB2= LabelFrame(GUI)
FB2.place(x=60,y=150)
B2=ttk.Button(FB2,text='Yamaha',command=Button2)
B2.pack(ipadx=20,ipady=20)


def Button3():
    text = '40 คัน'
    messagebox.showinfo('Stock Suzuki',text)


FB3= LabelFrame(GUI)
FB3.place(x=60,y=220)
B3=ttk.Button(FB3,text='Yamaha',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()

