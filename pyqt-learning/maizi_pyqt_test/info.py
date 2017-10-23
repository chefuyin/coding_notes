# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_info import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print('tool1')
    
    @pyqtSlot()
    def on_toolButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print('tool2')
    
    @pyqtSlot()
    def on_toolButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print('tool3')
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_str = self.lineEdit.text()
        my_str2 = self.lineEdit_2.text()
        my_str3 = self.lineEdit_3.text()
        my_str4= self.lineEdit_4.text()
        my_str5= self.lineEdit_5.text()
        print(my_str, my_str2, my_str3, my_str4, my_str5, sep ='\n')
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print('tool5')
