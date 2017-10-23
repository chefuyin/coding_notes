import sys
from PyQt5.QtGui import (QIcon,QFont)
from PyQt5.QtWidgets import (QWidget,QGridLayout,QHBoxLayout,QLineEdit,
                            QLCDNumber,QSlider,
                             QVBoxLayout,QLabel,QAction,QTextEdit,
                             qApp,QMainWindow,QDesktopWidget,QToolTip,
                             QPushButton,QApplication,QMessageBox)
from PyQt5.QtCore import (QCoreApplication,Qt,pyqtSignal,QObject)

# part4 event sender

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c=Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('EMIT SINGAL')
        self.show()

    def mousePressEvent(self,event):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



# #part3 event object
# class Example(QMainWindow):#注意父类不要错了
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         btn1 = QPushButton("Button 1",self)
#         btn1.move(30,50)
#
#         btn2 = QPushButton("Button 2",self)
#         btn2.move(150,50)
#
#         btn1.clicked.connect(self.buttonClicked)
#         btn2.clicked.connect(self.buttonClicked)
#
#         self.statusBar()
#
#         self.setGeometry(300,300,190,150)
#         self.setWindowTitle("Event sender")
#         self.show()
#
#     def buttonClicked(self):
#
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text()+'was pressed')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())







# part2 reimpletmenting event handler
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Event handler')
#         self.show()
#
#     def keyPressEvent(self, e):
#         if e.key()==Qt.Key_Escape:
#             self.close()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())





# # part1 singal&slot
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         lcd =QLCDNumber(self)
#         sld =QSlider(Qt.Horizontal,self)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
#
#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Signal &slot')
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())



