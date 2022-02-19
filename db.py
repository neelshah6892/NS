#from sqlalchemy import create_engine
#from sqlalchemy_utils import create_database, database_exists, drop_database
import pandas as pd
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QIcon
        
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Reconcilation')
        #self.setWindowIcon(QIcon('web.png'))        
        self.show()


    def twoa():
        file1 = filedialog.askopenfilename()
        df1 = pd.read_excel(file1, sheet_name='Sheet1')
        df1 = df1.parse('Sheet1')
        df1.head()
        df1.shape()
        df1 = pd.DataFrame(file1)

    def inward():
        try:
            file2 = filedialog.askopenfilename()
            #df2 = pd.read_excel(file2, sheet_name='Sheet1')
            #df2 = df2.parse('Sheet1')
        except(Exception) as e:
            print(e)
        finally:
            print("ok")

    def merge():
        df = pd.concat([df1,df2])
        print(df.shape())
        df.tail()

    def pan():


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())