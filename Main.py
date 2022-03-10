import sys
from view.vista_main_ui import Ui_MainWindow

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *

class MainWin(QMainWindow): 
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.Mainwindow = Ui_MainWindow()
        self.Mainwindow.setupUi(self)
        
        self.show()

if __name__ =="__main__":    
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec_())