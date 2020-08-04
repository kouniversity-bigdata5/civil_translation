# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testx.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

import tltk

class Ui_ThSegDialog(object):
    def setupUi(self, ThSegDialog):
        ThSegDialog.setObjectName("ThSegDialog")
        ThSegDialog.resize(691, 435)
        self.scrollArea = QtWidgets.QScrollArea(ThSegDialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 681, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.OuttextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.OuttextEdit.setGeometry(QtCore.QRect(3, -2, 671, 311))
        font = QtGui.QFont()
        font.setFamily("TH Sarabun New")
        font.setPointSize(18)
        self.OuttextEdit.setFont(font)
        self.OuttextEdit.setObjectName("OuttextEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.InFlineEdit = QtWidgets.QLineEdit(ThSegDialog)
        self.InFlineEdit.setGeometry(QtCore.QRect(90, 10, 581, 31))
        self.InFlineEdit.setObjectName("InFlineEdit")
        self.label_2 = QtWidgets.QLabel(ThSegDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 410, 421, 16))
        self.label_2.setObjectName("label_2")
        self.RunButton = QtWidgets.QPushButton(ThSegDialog)
        self.RunButton.setGeometry(QtCore.QRect(450, 370, 81, 32))
        self.RunButton.setObjectName("RunButton")
        self.InFpushButton = QtWidgets.QPushButton(ThSegDialog)
        self.InFpushButton.setGeometry(QtCore.QRect(0, 10, 82, 45))
        self.InFpushButton.setAutoFillBackground(False)
        self.InFpushButton.setObjectName("InFpushButton")
        self.SavepushButton = QtWidgets.QPushButton(ThSegDialog)
        self.SavepushButton.setGeometry(QtCore.QRect(470, 400, 71, 32))
        self.SavepushButton.setObjectName("SavepushButton")
        self.ExitpushButton = QtWidgets.QPushButton(ThSegDialog)
        self.ExitpushButton.setGeometry(QtCore.QRect(570, 400, 71, 32))
        self.ExitpushButton.setObjectName("ExitpushButton")
        self.progressBar = QtWidgets.QProgressBar(ThSegDialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 380, 421, 30))
        self.progressBar.setBaseSize(QtCore.QSize(0, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.chunkButton = QtWidgets.QPushButton(ThSegDialog)
        self.chunkButton.setGeometry(QtCore.QRect(610, 370, 81, 32))
        self.chunkButton.setObjectName("chunkButton")
        self.posButton = QtWidgets.QPushButton(ThSegDialog)
        self.posButton.setGeometry(QtCore.QRect(540, 370, 71, 32))
        self.posButton.setObjectName("posButton")

        self.retranslateUi(ThSegDialog)
        QtCore.QMetaObject.connectSlotsByName(ThSegDialog)

    def retranslateUi(self, ThSegDialog):
        _translate = QtCore.QCoreApplication.translate
        ThSegDialog.setWindowTitle(_translate("ThSegDialog", "Thai tokenization 3.1"))
        self.label_2.setText(_translate("ThSegDialog", "Department of Linguistics, Facyulty of Arts, Chulalongkorn University"))
        self.RunButton.setText(_translate("ThSegDialog", "segment"))
        self.InFpushButton.setText(_translate("ThSegDialog", "Input File"))
        self.SavepushButton.setText(_translate("ThSegDialog", "Save"))
        self.ExitpushButton.setText(_translate("ThSegDialog", "Exit"))
        self.chunkButton.setText(_translate("ThSegDialog", "chunk"))
        self.posButton.setText(_translate("ThSegDialog", "pos tag"))
                
            
    ### add this after generate py code from .ui to set action from button click events ################
        self.InFpushButton.clicked.connect(selectFile)
        self.RunButton.clicked.connect(ThaiSeg)
        self.SavepushButton.clicked.connect(saveFile)
        self.ExitpushButton.clicked.connect(exitProg)
        self.posButton.clicked.connect(ThaiPOSTag)
        self.chunkButton.clicked.connect(ThaiChunk)

#### another doalog for message display   generated from Qtdesign
class Ui_DialogS(object):
    def setupUi(self, DialogS):
        DialogS.setObjectName("DialogS")
        DialogS.resize(217, 85)
        DialogS.setToolTipDuration(0)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogS)
        self.buttonBox.setGeometry(QtCore.QRect(60, 40, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DialogS)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(DialogS)
        self.buttonBox.accepted.connect(DialogS.accept)
        self.buttonBox.rejected.connect(DialogS.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogS)

    def retranslateUi(self, DialogS):
        _translate = QtCore.QCoreApplication.translate
        DialogS.setWindowTitle(_translate("DialogS", "Dialog"))
        self.label.setText(_translate("DialogS", "Output file is saved"))

#### another doalog for message display  generated from Qtdesign
class Ui_DialogD(object):
    def setupUi(self, DialogD):
        DialogD.setObjectName("DialogD")
        DialogD.resize(217, 85)
        DialogD.setToolTipDuration(0)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogD)
        self.buttonBox.setGeometry(QtCore.QRect(60, 40, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DialogD)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(DialogD)
        self.buttonBox.accepted.connect(DialogD.accept)
        self.buttonBox.rejected.connect(DialogD.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogD)

    def retranslateUi(self, DialogD):
        _translate = QtCore.QCoreApplication.translate
        DialogD.setWindowTitle(_translate("DialogD", "Dialog"))
        self.label.setText(_translate("DialogD", "Finish"))


##### add module to handle events
def selectFile():
    global Filename
    xx = QWidget()
    (Filename, x1) = QFileDialog.getOpenFileName(xx)
    print(Filename)
    ui.InFlineEdit.setText(Filename)
    return(1)

def ThaiPOSTag():
    ui.OuttextEdit.clear()
    Filename = ui.InFlineEdit.text()
    completed = 0
    InFile = open(Filename,'r',encoding='utf-8')
    lines = InFile.readlines()
    fileLength = len(''.join(lines))
    tltk.nlp.pos_load()
    for line in lines:
        out = ''
        lstx = []
        pg1 = len(line) * 100 / fileLength
        line = line.rstrip()
        lstx = tltk.nlp.pos_tag(line)
        for lst in lstx:
            for (w, pos) in lst:
                out += w+'/'+pos+'|'
            out += '<s/>'    
        ui.OuttextEdit.appendPlainText(out)
        completed += pg1
        ui.progressBar.setValue(completed)

#### add this line to enable progress bar update, another method is to create another thread
        QApplication.processEvents()
    completed = 100    
    DialogD.show()
    return(1)    
    
    
def ThaiSeg():
    ui.OuttextEdit.clear()
    Filename = ui.InFlineEdit.text()
    completed = 0
    InFile = open(Filename,'r',encoding='utf-8')
    lines = InFile.readlines()
    fileLength = len(''.join(lines))
    out = ''
    for line in lines:
        pg1 = len(line) * 100 / fileLength
        line = line.rstrip()
        out = tltk.nlp.word_segment(line)
        ui.OuttextEdit.appendPlainText(out)
        completed += pg1
        ui.progressBar.setValue(completed)

#### add this line to enable progress bar update, another method is to create another thread
        QApplication.processEvents()
    completed = 100    
    DialogD.show()
    return(1)


def ThaiChunk():
    ui.OuttextEdit.clear()
    Filename = ui.InFlineEdit.text()
    completed = 0
    InFile = open(Filename,'r',encoding='utf-8')
    lines = InFile.readlines()
    fileLength = len(''.join(lines))
    out = ''
    for line in lines:
        pg1 = len(line) * 100 / fileLength
        line = line.rstrip()
        out = tltk.nlp.chunk(line)
        ui.OuttextEdit.appendPlainText(out)
        completed += pg1
        ui.progressBar.setValue(completed)

#### add this line to enable progress bar update, another method is to create another thread
        QApplication.processEvents()
    completed = 100    
    DialogD.show()
    return(1)
    

def saveFile():
    Filename = ui.InFlineEdit.text() + '.tok'
    OutFile = open(Filename, 'w')
    out = ui.OuttextEdit.toPlainText()
    OutFile.write(out)
    DialogS.show() 
    return(1)

def exitProg():
    sys.exit()

if __name__ == "__main__":
    global ui
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThSegDialog = QtWidgets.QDialog()
    ui = Ui_ThSegDialog()
    ui.setupUi(ThSegDialog)

    DialogS = QtWidgets.QDialog()
    ui2 = Ui_DialogS()
    ui2.setupUi(DialogS)

    DialogD = QtWidgets.QDialog()
    ui3 = Ui_DialogD()
    ui3.setupUi(DialogD)
    
    ThSegDialog.show()
    sys.exit(app.exec_())

