"""
    Created by: Ronald Javalde
    For final project in CPE009
"""
import random
import backsql
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from ttkbootstrap import *


# ============================== CRUD ======================================#

# Show all data from the data base

def viewall():
    cleartable()
    if backsql.checktable() is False:
        messagebox.showerror("ATTENTION!", "NO INFORMATION FOUND")
    else:
        for row in backsql.show():
            tree.insert(parent='', index='end', text='', values=(row[0], row[1], row[2]))


# Clea the tree view

def refreshall():
    """
    Clear the table of treeview then show the list again
    """
    cleartable()
    viewall()


def cleartable():
    """
    Remove all the value in the tree table
    """
    for _ in tree.get_children():
        tree.delete(_)


# Clear input fields

def clearfields():
    """
    Remove all inputted fields
    """
    website.set('')
    username.set('')
    password.set('')


# Password Generator

def generate():
    """
    It will generate randomise password for the user for desired length of password
    """
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alplc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpuc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symb = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
            '~', '>', '*', '<']

    password_lcletters = [random.choice(alplc) for _ in range(random.randint(8, 10))]
    password_ucletters = [random.choice(alpuc) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symb) for _ in range(random.randint(2, 4))]
    password_numb = [random.choice(digits) for _ in range(random.randint(2, 4))]
    ps_list = password_lcletters + password_ucletters + password_numb + password_symbols
    random.shuffle(ps_list)

    ps = "".join(ps_list)
    password.set(ps)


# Save to database

def savetodb():
    """
    Save all inputted data into database
    """
    if (website.get() and username.get() and password.get()) == "":
        messagebox.showerror("ATTENTION", "NO INPUT!")
    else:
        backsql.submit(website.get(), username.get(), password.get())
        tree.insert(parent='', index='end', text='', values=(website.get(), username.get(), password.get()))
        clearfields()


# Erase record to database

def eraseinfo():
    """
    Delete the record
    """
    if backsql.checktable() is False:
        messagebox.showerror("ATTENTION!", "NO INFORMATION TO BE DELETED")
    else:
        selected = tree.focus()
        value = tree.item(selected, 'value')
        backsql.deleterecord(value[2])
        refreshall()


# Update the records

def updateinfo():
    selected = tree.focus()
    value = tree.item(selected, 'value')
    backsql.updaterecord(website.get(), username.get(), password.get())
    refreshall()


def catch(event):
    website.set('')
    username.set('')
    password.set('')
    selected = tree.focus()
    value = tree.item(selected, 'value')
    website.set(value[0])
    username.set(value[1])
    password.set(value[2])


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
ttk.Button(root, text="Save to Database", style="success.TButton", width=21, command=savetodb).place(x=275, y=375)
ttk.Button(root, text="Generate Password", style="success.Outline.Tbutton", width=21, command=generate).place(x=440,
                                                                                                              y=375)
ttk.Button(root, text="Delete", style="danger.TButton", width=21, command=eraseinfo).place(x=750, y=500)
ttk.Button(root, text="Show All", width=21, command=viewall).place(x=750, y=540)
ttk.Button(root, text="Update", width=21, command=updateinfo).place(x=750, y=580)


def updateselected(event):
    """
    Take all selected data then we can fill up
    """
    website.set('')
    username.set('')
    password.set('')
    selected = tree.focus()
    value = tree.item(selected, 'value')
    website.set(value[0])
    username.set(value[1])
    password.set(value[2])


# Tree View
# TODO Lagyan ng command para gawing clickable 'yong treeview + navi-view 'yong mga iniinput
tree = ttk.Treeview(root, height=10, )
tree['columns'] = ( "Website", "User", "Password")
tree.column("#0", width=0, stretch=NO)
tree.column("Website", width=200, anchor=W)
tree.column("User", width=200, anchor=W)
tree.column("Password", width=200, anchor=W)
tree.heading("#0", text="")
tree.heading("Website", text="Website")
tree.heading("User", text="Email/Username")
tree.heading("Password", text="Password")
tree.bind("<ButtonRelease-1>", updateselected)
tree.place(x=100, y=450)

root.mainloop()
