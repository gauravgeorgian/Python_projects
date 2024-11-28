import os
import tkinter
from tkinter import messagebox


os.environ['TCL_LIBRARY'] = r'C:\Users\rajat\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
window = tkinter.Tk()
window.title("Login Form")
window.geometry("300x200")
window.configure(bg="black")
def login():
    user = "gaurav12345"
    password = "12345"
    if username_entry.get() == user and password_entry.get() == password:
        messagebox.showinfo(title="Login Successful", message="You made it")
    else:
        messagebox.showinfo(title="Login Failed", message="Invalid credentials")


frame = tkinter.Frame(bg="black")

#widgets
login_label = tkinter.Label(frame, text='Login', bg="black",fg="magenta",font="Arial,16")
username_label = tkinter.Label(frame, text='Username',bg="black",fg="white",font="Arial,16")
username_entry = tkinter.Entry(frame,font="Arial,16")
password_entry = tkinter.Entry(frame, show='*',font="Arial,16")
password_label = tkinter.Label(frame, text='Password',bg="black",fg="white",font="Arial,16")
login_button = tkinter.Button(frame, text='Login',bg="magenta",fg="black",font="Arial,16",command=login)

#positioning of widgets
login_label.grid(row=0, column=0, columnspan=2,sticky='news',pady=40)
username_label.grid(row=1, column=0,pady=20)
password_label.grid(row=2, column=0)
username_entry.grid(row=1, column=1,pady=20)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0,columnspan=2,pady=30)

frame.pack()


window.mainloop()