import mysql.connector
import random
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter import *

# ========================= DATABASE ===============================#
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Bellion_1",
    port=3306
)