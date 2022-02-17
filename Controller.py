import os
import sys
from os.path import dirname, realpath, join
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUiType
import pandas as pd


scriptDir = dirname(realpath(__file__))
From_Main, _ = loadUiType(join(dirname(__file__), "Main.ui"))


class MainWindow(QWidget, From_Main):
    palabras = []
    listaPalabras = ""

    def __init__(self):
        super(MainWindow, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)

        self.ButtonAbrir.clicked.connect(self.AbrirArchivo)
        self.BtnGenerar.clicked.connect(self.DatosColumnas)

    def AbrirArchivo(self):
        global path
        try:
            path = QFileDialog.getOpenFileName(
                self, 'Abrir archivo', os.getenv('HOME'), 'CSV(*.csv)')[0]
            self.all_data = pd.read_csv(path)
        except:
            print(path)

    def getPalabras(self):
        pass
    
    def trabajarPalabras(self):
        global palabras
        palabras = self.ui.FiltrarPalabra.text().split()
        count = 0
        palabrasString = []

        for i in palabras:
            count = count + 1
            if count < len(palabras):
                palabrasString.append( i +"|")
            else:
                palabrasString.append(i)

        print(palabrasString)
        global listaPalabras
        listaPalabras = "".join(palabrasString)
        print(listaPalabras)
        self.ui.FiltrarPalabra.setText("")
        return listaPalabras 
    
    def guardarArchivoFiltrado(self):
        palabrasfiltradas = path[path['Texto'].str.contains(listaPalabras, case=False, na=False, regex=True)]
        #palabrasfiltradas.to_csv("C:/Users/USER/Downloads/PalabraClave.csv")
        palabrasfiltradas.to_csv(os.path.abspath("PalabraClave.csv"))
            
    def DatosColumnas(self):
        numColomn = self.spinBox.value()
        if numColomn == 0:
            Numfilas = len(self.all_data.index)
        else:
            Numfilas = numColomn
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(Numfilas)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(Numfilas):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


app = QApplication(sys.argv)
sheet = MainWindow()
sheet.show()
sys.exit(app.exec_())