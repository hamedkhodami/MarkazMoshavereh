from tkinter import *
from customtkinter import *
from pl import login
import pyodbc


if __name__=="__main__":
    screen=CTk()
    screen.geometry("%dx%d+%d+%d" % (700,600,500,100))
    Pageme = login.App(screen)
    screen.title("خوش آمدید")
    screen.iconbitmap("hospital.ico")
    screen.resizable(False,False)
    set_appearance_mode("light")
    screen.mainloop()

