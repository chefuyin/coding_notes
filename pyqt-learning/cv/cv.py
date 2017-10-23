# -*- coding: utf-8 -*-

"""
Module implementing cv_control.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_cv import Ui_MainWindow


class cv_control(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(cv_control, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        print(self.lineEdit.text())
        print(self.dateEdit.text())
        print(self.lineEdit_5.text())
        print(self.lineEdit_7.text())
        print(self.textBrowser.toPlainText())
        print(self.textBrowser_2.toPlainText())
        print(self.textBrowser_3.toPlainText())
        
        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)   
    ui = cv_control()
    ui.show()
    sys.exit(app.exec_())
