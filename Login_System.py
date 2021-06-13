from tkinter import *
from tkinter.simpledialog import askstring
import os
import re

def register():
	global register
	register = Toplevel(root)
	register.title("Register")
	register.geometry("550x350")
	register.configure(bg="Black")
	register.resizable(False,False)

	global username,password
	global username_entry,password_entry
	global Lbl
	
	Lbl = Label(register,text="",font=("Helvatica",15),bg="Black")

	username = StringVar()
	password = StringVar()

	Label(register,text="Please Enter details below [* are required]",bg="Black",fg="White",font=("Helvatica",15)).pack(pady=17)
	
	username_label = Label(register,text="Username: *",fg="White",bg="Black")
	username_label.pack()
	username_entry = Entry(register,textvariable=username,fg="White",bg="Black")
	username_entry.pack(pady=10)

	password_label = Label(register,text="Password *",bg="Black",fg="White")
	password_label.pack()
	password_entry = Entry(register,textvariable=password,show="*",fg="White",bg="Black")
	password_entry.pack(pady=10)

	sup_button = Button(register,bg="White",text="Register",width=10,font=("Nexa",22),command=register_verify)
	sup_button.pack(pady=10)

	Lbl.pack()

def register_verify():
	username_info = username.get()
	password_info = password.get()
	global list

	list = os.listdir()
	if username_info in list:
		Lbl.configure(text="Username already taken",fg="Red")
	
	elif username_info == "" or username == " ":
		Lbl.configure(text="Invalid username, try another",fg="Red")
	
	elif len(password_info) < 8:
		Lbl.configure(text="Invalid password, try stronger one",fg="Red")
	
	else :
		file = open(username_info,"w")
		file.write(username_info + "\n" + password_info)
		file.close()
		Lbl.configure(text="Registration success",fg="Green")
	username_entry.delete(0,END)
	password_entry.delete(0,END)

def login():
	global login_check,login,username_login,password_login,username_enter,password_enter
	
	username_login = StringVar()
	password_login = StringVar()
	
	login = Toplevel(root)
	login.configure(bg="Black")
	login.geometry("310x290")
	login.resizable(False,False)
	
	login_check = Label(login,text="",bg="Black",font=("Nexa",15))
	
	username_lbl = Label(login,text="Username",bg="Black",fg="White")
	username_lbl.pack(pady=10)
	username_enter = Entry(login,textvariable=username_login,bg="Black",fg="White")
	username_enter.pack(pady=5)

	password_lbl = Label(login,text="Password", bg="Black",fg="White")
	password_lbl.pack(pady=5)
	password_enter = Entry(login,textvariable=password_login,bg="Black",fg="White",show="*")
	password_enter.pack(pady=10)
	
	login_button = Button(login,text="Login",bg="White",fg="Black",width=10,font=("Nexa",22),command=login_verify)
	login_button.pack(pady=10)
	
	login_check.pack()

def login_verify():
	username1 = username_login.get()
	password1 = password_login.get()

	if username1 in os.listdir():
		file1 = open(username1, "r")
		read = file1.read().splitlines()
		if password1 in read:
			login_check.configure(text="Successfully logged in",fg="Green")
		else : 
			login_check.configure(text="Incorrect credentials!",fg="Red")	
	else :
		login_check.configure(text="User not found!",fg="Red")

	username_enter.delete(0,END)
	password_enter.delete(0,END)

def main_account_screen():
	global root
	root = Tk()
	root.title("Login System")
	root.geometry('550x300')
	root.configure(bg="Black")
	root.resizable(False,False)

	home_label = Label(root,text="Welcome",font=("Helvatica",32),fg="White",bg="Black")
	home_label.pack(pady=30)

	loginn = Button(root,text="Login",font=("Nexa",22),bg="White",fg="Black",width=10,command=login)
	loginn.pack(pady=0)

	signup = Button(root,text="Sign UP",font=("Nexa",22),bg="White",fg="Black",width=10,command=register)
	signup.pack(pady=5)

	root.mainloop()

main_account_screen()