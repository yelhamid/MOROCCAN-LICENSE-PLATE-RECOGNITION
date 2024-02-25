from PyQt5 import QtGui, QtWidgets,QtCore
import sys
from menu import Ui_Form
from imag import  Ui_MainWindow
from vid import Ui_MainWindow1

def affiche():
    MainWindow.show()
    Form.close()

def affiche1():
    MainWindow1.show()
    Form.close()

def menu():
    Form.show()
    MainWindow.close()
    ui1.IMGBF.clear()
    ui1.imgaf.clear()
    ui1.LICENPLA.clear()

def menu1():
    Form.show()
    MainWindow1.close()
    ui2.VID.clear()
    ui2.play=False
    ui2.DROLICEN.clear()
    ui2.PLAQUE.clear()
def videim():
    ui1.imgaf.clear()
    ui1.LICENPLA.clear()

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

MainWindow = QtWidgets.QMainWindow()
ui1 = Ui_MainWindow()
ui1.setupUi(MainWindow)

MainWindow1 = QtWidgets.QMainWindow()
ui2 = Ui_MainWindow1()
ui2.setupUi(MainWindow1)

ui.pushButton.clicked.connect(affiche)
ui.pushButton_2.clicked.connect(affiche1)
ui1.MENUPRIN.clicked.connect(menu)
ui2.MENUPRIN.clicked.connect(menu1)
ui1.CHARIM.clicked.connect(videim)

Form.show()
sys.exit(app.exec_())
