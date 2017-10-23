# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ella\Documents\GitHub\pyqt-learning\hello\HelloWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.Button_ok = QtWidgets.QPushButton(Dialog)
        self.Button_ok.setGeometry(QtCore.QRect(80, 170, 75, 23))
        self.Button_ok.setObjectName("Button_ok")
        self.Button_close = QtWidgets.QPushButton(Dialog)
        self.Button_close.setGeometry(QtCore.QRect(230, 170, 75, 23))
        self.Button_close.setObjectName("Button_close")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(73, 100, 231, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.Button_close.clicked['bool'].connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_ok.setText(_translate("Dialog", "OK"))
        self.Button_close.setText(_translate("Dialog", "Quit"))
        self.label.setText(_translate("Dialog", " this is my first PROGRAM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

