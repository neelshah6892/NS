import pandas as pd
from tkinter import filedialog
import xlrd
from tkinter import ttk

dialog1 = filedialog.askopenfilename()
dataset1 = pd.read_excel(dialog1, sheet_name='Sheet1')
columns1 = list(dataset1.columns)

for i in dataset1.index:
    print(dataset1[i])
