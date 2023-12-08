from tkinter import*
from tkinter import messagebox

def login():
    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo(""," plz fill the blank")

    elif (username=="CHINNU" and password=="8296188192"):
        messagebox.showinfo("","login success")

    else:
        messagebox.showinfo("","incorrect username and password")
root=Tk()
root.title("login")
root.geometry("800x500")


global entry1
global entry2

Label(root,text="username").place(x=20,y=20)
Label(root,text="password").place(x=20,y=70)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=30)
entry2=Entry(root,bd=5)
entry2.place(x=140,y=70)

Button(root,text="Login",command=login,height=3,width=13,bd=6,bg="green").place(x=100,y=120)
root.mainloop()
