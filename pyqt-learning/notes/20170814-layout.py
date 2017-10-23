import sys
from PyQt5.QtGui import (QIcon,QFont)
from PyQt5.QtWidgets import (QWidget,QGridLayout,QHBoxLayout,QLineEdit,
                             QVBoxLayout,QLabel,QAction,QTextEdit,
                             qApp,QMainWindow,QDesktopWidget,QToolTip,
                             QPushButton,QApplication,QMessageBox)
from PyQt5.QtCore import QCoreApplication
# part4 REVIEW
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author=QLabel('Author')
        review=QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit= QLineEdit()
        reviewEdit= QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setLayout(grid)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Review')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



# # part3 网格布局
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         grid =QGridLayout()
#         self.setLayout(grid)
#         names =['Cls','Bck','','Close',
#                 '7','8','9','/',
#                 '4','5','6','*',
#                 '1','2','3','-',
#                 '0','.','=','+']
#         positions = [(i,j)for i in range(5) for j in range(4)]
#         for positon,name in zip(positions,names):
#             if name =='':
#                 continue
#             button = QPushButton(name)
#             grid.addWidget(button,*positon)
#
#             self.move(300,150)
#             self.setWindowTitle('calculator')
#             self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())




# # part2箱布局
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#
#         vbox=QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)#不能漏了
#
#         self.setGeometry(300,300,300,150)
#         self.setWindowTitle('Buttons')
#         self.show()
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())



# # part1 绝对定位
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         lbl1 =QLabel('Zetcode',self)
#         lbl1.move(15,10)
#
#         lbl2 = QLabel('tutorials',self)
#         lbl2.move(35,40)
#
#         lbl3 = QLabel('for programmers',self)
#         lbl3.move(55,70)
#
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Absolute')
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())