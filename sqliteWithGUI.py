from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Treeview
import csv
import sqlite3

root = Tk()
root.title("Calculator")
#root.geometry("300x500")
root.configure()
Label1 = Label(root, text= "num: ")
Label1.grid(row=0,column=0)

num1 = Entry(root)
num1.grid(row=0,column=1)

label2 = Label(root, text="num2")
label2.grid(row=1,column=0)

num2 = Entry(root)
num2.grid(row=1,column=1)

def add_func():
    n1=int(num1.get())
    n2 = int(num2.get())
    answer = n1 + n2
    answer_label.configure(text=answer)

calculate_button = Button(root, text='-',command= add_func)
calculate_button.grid(row=3,column=1)

label3 = Label(root, text="num2")
label3.grid(row=3,column=0)

answer_label = Label(root,text="---")
answer_label.grid(row=3,column=1)
root.mainloop()