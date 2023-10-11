#importing libraries
from tkinter import*
import tkinter as tk
from function_10_10_23 import login_function

#Creating a root window
root=tk.Tk()
root.title("Sign_in-Sign_up")
root.geometry("450x300")
root.resizable(0,0)

#creating labels
title_label=Label(root,text="Home Page",font=('Helvatical bold',20)).place(x=159,y=5)
user_id_label=Label(root,text="Enter your user id :").place(x=5,y=100)
password_label=Label(root,text="Enter your password :").place(x=5,y=130)

#creating entries
id_entry=Entry(root,width=35)
password_entry=Entry(root,width=35)
id_entry.place(x=129,y=100)
password_entry.place(x=130,y=130)


#Creating buttons

login_button=Button(root,text="Click here to log in",width=20,command=lambda: login_function(id_entry.get(),password_entry.get())).place(x=159,y=170)


root.mainloop()