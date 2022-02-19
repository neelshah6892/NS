import pandas as pd
from tkinter import filedialog
import xlsxwriter
from tkinter import *

file = filedialog.askopenfilename()
df1 = pd.read_excel(file, sheet_name='Sheet1')
#print("Total rows: {0}".format(len(df1)))
# print(list(df1))
df1 = file.parse('Sheet1')
df1
'''df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
writer = pd.ExcelWriter('simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()'''

class Mainapp:
    def __init__(self, master, text):
        frame = Frame(master)
        frame.pack()
        self.btn1 = Button(frame, text=text, command=self.twoa)

    def twoa(self):
        file = filedialog.askopenfilename()
        df1 = pd.read_excel(file, sheet_name='Sheet1')
        #print("Total rows: {0}".format(len(df1)))
        #print(list(df1))
        df1 = file.parse('Sheet1')
        df1

    def inward(self):
        file = filedialog.askopenfilename()
        df2 = pd.read_excel(file, sheet_name='Sheet1')
        #print("Total rows: {0}".format(len(df1)))
        #print(list(df1))
        df2 = file.parse('Sheet1')
        df2

if __name__=='__main__':
    root=Tk()
    Mainapp(root, "TWOA")
    root.mainloop()