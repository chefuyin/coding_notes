import sys
from PyQt5.QtGui import (QIcon,QFont)
from PyQt5.QtWidgets import (QWidget,QDesktopWidget,QToolTip,QPushButton,QApplication,QMessageBox)
from PyQt5.QtCore import QCoreApplication


#part6屏幕上的居中窗口
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(650,500)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
# #part5 message box
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Message box')
#         self.show()
#
#     def closeEvent(self,event):
#         reply = QMessageBox.question(self,'Message',
#                  "Are you sure to quit?",QMessageBox.Yes | QMessageBox.No,
#                  QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     ex= Example()
#     sys.exit(app.exec_())


# #part4 关闭窗口
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         qbtn= QPushButton('Quit',self)
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50, 50)
#
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Quit button')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())





# #part3 创建一个文本
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         QToolTip.setFont(QFont('sansserif',10))
#         self.setToolTip('this is a <b>Qwidget</b> widget')
#         btn=QPushButton('Button',self)
#         btn.setToolTip('this is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50,50)
#
#         self.setGeometry(500,300,300,200)
#         self.setWindowTitle('tooltips')
#         self.show()
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex= Example()
#     sys.exit(app.exec_())



# part2 简单的应用图标
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300,300,300,220)
#         self.setWindowTitle('Icon')
#         self.setWindowIcon(QIcon('web.png'))
#         self.show()
#
# if __name__=='__main__':
#     app =QApplication(sys.argv)
#     ex= Example()
#     sys.exit(app.exec_())


# part1简单窗口
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     w= QWidget()
#     w.resize(600,400)
#     w.move(600,300)
#     w.setWindowTitle('Charm Legal Assistor')
#     w.show()
#
#     sys.exit(app.exec())
