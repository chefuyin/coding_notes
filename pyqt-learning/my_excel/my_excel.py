# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from Ui_my_excel import Ui_MainWindow
from glob import glob
from os.path import join
import os,re,shutil
from xlrd import open_workbook


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    my_dir = ''
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionClose_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionQuit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionDocumentation_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionAbout_us_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        print('ok')
        self.my_dir = QFileDialog.getExistingDirectory(self, '选择文件夹','/')
        print(self.my_dir)
        # print(glob(join(self.my_dir,'*.xlsx')))
        # for i in glob(join(self.my_dir,'*.xlsx')):
        #     print(i.replace("\\","\/"))


        
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # # TODO: not implemented yet
        # raise NotImplementedError
        print('search')
        print(self.my_dir)
        # 使用glob方法匹配文件
        list = glob(join(self.my_dir, '*.xlsx'))
        print(list)
        # print(glob(join(self.my_dir, '*.xlsx')))
        print('text is :',self.lineEdit.text())
        my_key_words=re.split(' ',self.lineEdit.text())
        # print(my_key_words)
        num=0
        for i in list:
        #     print(i)
            wb = open_workbook(i)
            for s in wb.sheets():
                for row in range(s.nrows):
                    for col in range(s.ncols):
                        value =s.cell(row, col).value
                        if  value:
                            # print(s.cell(row, col).value,'is',type(s.cell(row, col).value))
                            for key_word in my_key_words:
                                if type(value) is not 'string':
                                    value=str(value)#暂未解决时间的问题，后续再说
                                    if len(value) > len(key_word):
                                        if key_word in value:
                                            # print(i)
                                            num=num+1
                                            self.textBrowser.append('找到第{}个文件'.format(num))
                                            self.textBrowser.append(i)
                                            if not os.path.exists(self.my_dir+'\\符合条件的'):
                                                os.mkdir(self.my_dir+'\\符合条件的')
                                                self.textBrowser.append('创建文件夹成功:{}'.format(self.my_dir+'\\符合条件的'))
                                            else:
                                                self.textBrowser.append('文件夹已存在，不需要重复创建')
                                            self.textBrowser.append('正在复制文件……')
                                            shutil.copy(i,self.my_dir+'\\符合条件的')
                                            self.textBrowser.append('当前文件复制成功')
                                            #重复复制的文件问题暂未解决
                                    else:
                                        if value in key_word:
                                            num=num+1
                                            # print(i)
                                            self.textBrowser.append('找到第{}个文件'.format(num))
                                            self.textBrowser.append(i)
                                            if not os.path.exists(self.my_dir+'\\符合条件的'):
                                                os.mkdir(self.my_dir+'\\符合条件的')
                                                self.textBrowser.append('创建文件夹成功:{}'.format(self.my_dir+'\\符合条件的'))
                                            else:
                                                self.textBrowser.append('文件夹已存在，不需要重复创建')
                                            self.textBrowser.append('正在复制文件……')
                                            shutil.copy(i,self.my_dir+'\\符合条件的')
                                            self.textBrowser.append('当前文件复制成功')

        self.textBrowser.append('一共复制了{}个文件'.format(num))




        # #使用OS方法匹配文件
        # if os.path.isdir(self.my_dir):
        #     # print(os.listdir(self.my_dir))
        #     for my_file in os.listdir(self.my_dir):
        #         # print(my_file)
        #         if my_file[-5:]=='.xlsx' or my_file[-4:]=='xls':
        #             print(self.my_dir+'/'+my_file)

    # @pyqtSlot(str)
    # def on_lineEdit_textEdited(self, p0):
    #     """
    #     Slot documentation goes here.
    #
    #     @param p0 DESCRIPTION
    #     @type str
    #     """
    #     # TODO: not implemented yet
    #     raise NotImplementedError


        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()  
    ui.show()
    sys.exit(app.exec_())
    
    
