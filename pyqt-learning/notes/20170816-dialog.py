import sys
from PyQt5.QtGui import (QIcon,QFont,QColor)
from PyQt5.QtWidgets import (QWidget,QGridLayout,QHBoxLayout,QLineEdit,
                            QLCDNumber,QSlider,QInputDialog,
                            QFrame,QColorDialog,
                             QVBoxLayout,QLabel,QAction,QTextEdit,
                             qApp,QMainWindow,QDesktopWidget,QToolTip,
                             QPushButton,QApplication,QMessageBox)
from PyQt5.QtCore import (QCoreApplication,Qt,pyqtSignal,QObject)

# part2颜色对话框
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0,0,0)

        self.btn =QPushButton('Dialog',self)
        self.btn.move(20,20)

        self.btn.clicked.connect(self.showDialog)

        self.frm =QFrame(self)
        self.frm.setStyleSheet("Qwidget { background-color :%s}"% col.name())
        self.frm.setGeometry(130,22,100,100)

        self.setGeometry(300,300,250,180)
        self.setWindowTitle('color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("Qwidget {background-color :%s}" % col.name())

if __name__=='__main__':
    app= QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())


# # part1 input dialog
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.btn=QPushButton('Dialog',self)
#         self.btn.move(20,20)
#         self.btn.clicked.connect(self.showDialog)
#
#         self.le = QLineEdit(self)
#         self.le.move(130,22)
#         self.setGeometry(300,300,290,150)
#         self.setWindowTitle('Input dialog')
#         self.show()
#
#     def showDialog(self):
#         text,ok = QInputDialog.getText(self,'Input Dialog','Enter your name:')
#         if ok:
#             self.le.setText(str(text))
#
# if __name__=='__main__':
#     app= QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())
