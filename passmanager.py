"""
    Created by: Ronald Javalde
    For final project in CPE009
"""
import random
import csv
from tkinter import ttk
from tkinter import *
from ttkbootstrap import *

# ============================== CRUD ======================================#
def save():
    print()


# ============================== UI SETUP  =================================#

# Window
root = Tk()

style = Style(theme="darkly").master
root.title("Password Manager")
root.geometry("1024x740")
root.iconbitmap("photo/icon2.ico")
root.resizable(width=FALSE, height=FALSE)

# Logo inside
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="photo/smalllogo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

# Texts
Label(root, text="Website:", font=("Monsterrat", 16)).place(x=135, y=225)
Label(root, text="Email/Username:", font=("Monsterrat", 16)).place(x=100, y=275)
Label(root, text="Password:", font=("Monsterrat", 16)).place(x=135, y=325)

# Entries
website = StringVar()
username = StringVar()
password = StringVar()

ttk.Entry(root, width=50, textvariable=website).place(x=275, y=225)
ttk.Entry(root, width=50, textvariable=username).place(x=275, y=275)
ttk.Entry(root, width=50, textvariable=password).place(x=275, y=325)

# Buttons
# TODO Lagyan ng command 'yong button + delete and show all + refresh
ttk.Button(root, text="Save to Database", style="success.TButton", width=21).place(x=275, y=375)
ttk.Button(root, text="Update", width=21).place(x=440, y=375)
ttk.Button(root, text="Delete", style="danger.TButton", width=21).place(x=600, y=500)

# Tree View
# TODO Lagyan ng command para gawing clickable 'yong treeview + navi-view 'yong mga iniinput
tree = ttk.Treeview(root, height=10,)
tree['columns'] = ("Website", "User", "Password")
tree.column("#0", width=0, stretch=NO)
tree.column("Website", width=160, anchor=W)
tree.column("User", width=160, anchor=W)
tree.column("Password", width=160, anchor=W)
tree.heading("#0", text="")
tree.heading("Website", text="Website")
tree.heading("User", text="Email/Username")
tree.heading("Password", text="Password")
tree.place(x=100, y=450)


root.mainloop()

