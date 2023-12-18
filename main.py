from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Simple Calculater")

lbl1 = Label(window, text="Enter 1st Number: ")
lbl1.place(x=50, y=50)

lbl2 = Label(window, text="Enter 2nd Number: ")
lbl2.place(x=50, y=100)

lbl3 = Label(window, text="Result: ")
lbl3.place(x=80, y=150)

t1 = Entry()
t1.place(x=180, y=50)

t2 = Entry()
t2.place(x=180, y=100)

t3 = Entry()
t3.place(x=180, y=150)


def add():
  num1 = int(t1.get())
  num2 = int(t2.get())
  sum = num1 + num2
  t3.insert(END, str(sum))


b1 = Button(window, text="Add", command=add)
b1.place(x=50, y=200)


def sub():
  num1 = int(t1.get())
  num2 = int(t2.get())
  sum = num1 - num2
  t3.insert(END, str(sub))


b2 = Button(window, text="Subtract", command=add)
b2.place(x=120, y=200)


def mul():
  num1 = int(t1.get())
  num2 = int(t2.get())
  product = num1 * num2
  t3.insert(END, str(product))


b3 = Button(window, text="Multiply", command=add)
b3.place(x=220, y=200)


def div():
  num1 = int(t1.get())
  num2 = int(t2.get())
  quotient = num1 / num2
  t3.insert(END, str(quotient))


b4 = Button(window, text="Divide", command=add)
b4.place(x=320, y=200)


def clear():
  t1.delete(0, END)
  t2.delete(0, END)
  t3.delete(0, END)


b5 = Button(window, text="Clear", command=clear)
b5.place(x=180, y=250)
