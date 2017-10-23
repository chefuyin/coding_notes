import sys
from PyQt5.QtGui import (QIcon,QFont)
from PyQt5.QtWidgets import (QWidget,QAction,QTextEdit,qApp,QMainWindow,QDesktopWidget,QToolTip,QPushButton,QApplication,QMessageBox)
from PyQt5.QtCore import QCoreApplication


# part4组件合并
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit =QTextEdit()
        self.setCentralWidget(textEdit)
        exitAction = QAction(QIcon('exit24.png'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        self.statusBar()
        menubar =self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('Main window')
        self.show()
if __name__=='__main__':
    app =QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


        # # part 3 工具栏
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         exitAction = QAction(QIcon('exit24.png'),'Exit',self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.triggered.connect(qApp.quit)
#
#         self.toolbar = self.addToolBar('Exit')
#         self.toolbar.addAction(exitAction)
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('Toolbar')
#         self.show()
#
# if __name__=='__main__':
#     app =QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())




# # part2菜单栏
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         exitAction = QAction(QIcon('exit.png'),'&Exit',self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(qApp.quit)
#         self.statusBar()
#         menubar =self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu.addAction(exitAction)
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('Menubar')
#         self.show()
#
# if __name__=='__main__':
#     app =QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# #part1 状态栏
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.statusBar().showMessage('Ready')
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Statusbar')
#         self.show()
#
# if __name__=='__main__':
#     app =QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())