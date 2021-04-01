#import module
from tkinter import *
from tkinter import messagebox

#configure
ws = Tk()
ws.title("Login Page")
ws.geometry("320x250")

#funtions
def checkCred():
    email = email_tf.get()
    pwd = pwd_tf.get()
    print(email, pwd)

    if email == "python" and pwd == "guides":
        return messagebox.showinfo("Login", "Login Sucessfully!")
    else:
        return messagebox.showerror("Login", "Login Failed!")

def success_msg():
    return messagebox.showinfo("Signup", "Sign-up Succesfully")

def register():
    ws = Tk()
    ws.title("Register")
    ws.geometry("300x250")
    Label(ws, text = "Enter Name").place(x = 50, y = 20, anchor = "center")
    nTf = Entry(ws).place(x = 170, y = 20, anchor = CENTER)
    Label(ws, text = "Enter Email").place(x = 50, y = 60, anchor = "center")
    eTf = Entry(ws).place(x = 170, y = 60, anchor = CENTER)
    Label(ws, text = "Enter Password").place(x = 50, y = 100, anchor = "center")
    pTf = Entry(ws).place(x = 170, y = 100, anchor = CENTER)
    Label(ws, text = "re-enter Password").place(x = 50, y = 140, anchor = "center")
    rpTf = Entry(ws).place(x = 170, y = 140, anchor = CENTER)
    Button(ws, text = "Register", command = success_msg).place(x = 100, y = 180, anchor = CENTER)

#write code
email_lb = Label(ws, text = "Enter Email")
email_tf = Entry(ws)
pwd_lb = Label(ws, text = "Enter Password")
pwd_tf = Entry(ws)
login_btn = Button(ws, text = "Login", command = checkCred)
reg_btn = Button(ws, text = "Register", command = register)

#placeholder
email_lb.place(x=50, y=40, anchor=CENTER)
email_tf.place(x=170, y=40, anchor=CENTER)
pwd_lb.place(x=50, y=80, anchor=CENTER)
pwd_tf.place(x=170, y=80, anchor=CENTER)
login_btn.place(x=100, y=120, anchor=CENTER)
reg_btn.place(x=180, y=120, anchor=CENTER)

#inifinite loop
ws.mainloop()