import sys
from PyQt5.QtGui import (QIcon,QFont,QColor)
from PyQt5.QtWidgets import (QWidget,QGridLayout,QHBoxLayout,QLineEdit,
                            QLCDNumber,QSlider,QInputDialog,QFileDialog,
                            QFrame,QColorDialog,QFontDialog,QSizePolicy,
                             QVBoxLayout,QLabel,QAction,QTextEdit,
                             qApp,QMainWindow,QDesktopWidget,QToolTip,
                             QPushButton,QApplication,QMessageBox)
from PyQt5.QtCore import (QCoreApplication,Qt,pyqtSignal,QObject)

# part2 QFile dialog
class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit =QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png','Open',self))
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAciton(openFile)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'Open file','home')
        if fname[0]:
            f=open(fname[0],'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__=='__main__':
    app= QApplication(sys.argv)
    ex= Example()
    sys.exit(app.exec_())





#part1 QFont Dialog
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         vbox =QVBoxLayout()
#
#         btn = QPushButton('Dialog',self)
#         btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
#
#         btn.move(20,20)
#
#         vbox.addWidget(btn)
#
#         btn.clicked.connect(self.showDialog)
#
#         self.lbl=QLabel('Knowledge only matters',self)
#         self.lbl.move(130,20)
#
#         vbox.addWidget(self.lbl)
#         self.setLayout(vbox)
#
#         self.setGeometry(300,300,250,180)
#         self.setWindowTitle('Font dialog')
#         self.show()
#
#     def showDialog(self):
#         font,ok = QFontDialog.getFont()
#         if ok:
#             self.lbl.setFont(font)
#
# if __name__=='__main__':
#     app= QApplication(sys.argv)
#     ex= Example()
#     sys.exit(app.exec_())

