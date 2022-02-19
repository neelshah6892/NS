from tkinter import *
import tkinter.messagebox as tkMessageBox
from tkinter import filedialog
import tkinter.ttk as ttk
import pandas as pd
import tkintertable
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class App():
    def __init__(self, master):
        tk.Frame = tk.Frame(master)
        Frame.pack()
        self.parent = parent
        root.title("Reconcilation")

        width = 1200
        height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)
        root.config(bg="#99ff99")

    def twoa():
	    global df1
	    file1 = filedialog.askopenfilename()
	    df1 = pd.read_excel(file1, sheet_name='Sheet1')

    def inward():
	    global df2
	    file2 = filedialog.askopenfilename()
	    df2 = pd.read_excel(file2, sheet_name="Sheet1")
            
    def merge():
        df = pd.concat([df1,df2])

    def reset():
        df = pd.concat([df1,df2])

# def pan():


        # ===Charts===# List Widget


        #===Frames===#
        Top = Frame(root, width=1200, height=100, relief="raise")
        Top.pack(side=TOP)
        Left = Frame(root, width=790, height=550, relief="raise")
        Left.pack(side=LEFT)
        Right = Frame(root, width=390, height=550, relief="raise")
        Right.pack(side=RIGHT)
        Buttons = Buttons = Frame(Top, width=300, height=100, relief="raise")
        Buttons.pack()


        #===Button Widgets===#
        btn1 = Button(Buttons, width=30, text="DATABASE 1", command=twoa)
        btn1.pack(side=LEFT)
        btn2 = Button(Buttons, width=30, text="DATABASE 2", command=inward)
        btn2.pack(side=LEFT)
        btn3 = Button(Buttons, width=30, text="START", command=merge)
        btn3.pack(side=LEFT)
        btn4 = Button(Buttons, width=30, text="RESET", command=reset)
        btn4.pack(side=LEFT,)

        #===MENUBAR===#
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Account")
        filemenu.add_command(label="Exit")
        menubar.add_cascade(label="File")
        root.config(menu=menubar)

        #===Main Screen Label===#
        Title = Frame(root, bd=1, relief=SOLID)
        Title.pack(pady=10)



#===Initialization===#
if __name__ == '__main__':
    root = tk.Tk(()
    app = App(root)
    root.mailloop()

