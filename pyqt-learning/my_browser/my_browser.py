# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:21:31 2017

@author: ella
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
#pyqt5目前已经移除了QtWebKit&QtWebKitWidgets
#旧的写法是from PyQt5.QtWebKitWidgets import QWebPage, QWebView
#新的写法是from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
import sys

class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle('Legal Browser')
        self.setWindowIcon(QIcon('icons/legal.png'))
        self.show()

        self.browser = QWebEngineView()
        url = "http://www.baidu.com"
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)

        navigation_bar =QToolBar('Navigation')
        navigation_bar.setIconSize(QSize(16,16))
        self.addToolBar(navigation_bar)

        back_button =QAction(QIcon('icons/back.png'),'Back',self)
        next_button =QAction(QIcon('icons/next.png'),'Forward',self)
        stop_button =QAction(QIcon('icons/cross.png'),'Stop',self)
        reload_button =QAction(QIcon('icons/renew.png'),'relaod',self)

        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

        self.urlbar = QLineEdit()
        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.renew_urlbar)

        self.urlbar.returnPressed.connect(self.navigate_to_url)

        self.tabs =QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabBarDoubleClicked.connect(self.tab_open_doublick)
        #此处有BUG
        self.tabs.currentChanged(self.current_tab_changed)

        self.add_new_tab(QUrl('http://sohu.com'),'Homepage')
        self.setCentralWidget(self.tabs)

        new_tab_action= QAction(QIcon('icons/add_page.png'),'New Page',self)

        new_tab_action.triggered.connect(self.add_new_tab())



    def renew_urlbar(self,q,browser =None):
        if browser!=self.tabs.currentWidget():
            return
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def navigate_to_url(self):
        q=QUrl(self.urlbar.text())
        if q.scheme() =='':
            q.setScheme('http')
        self.browser.setUrl(q)

    def add_new_tab(self,qurl,label):
        browser = QWebEngineView()
        browser.setUrl(qurl)
        self.tabs.addTab(browser,label)

        browser.urlChanged.connect(lambda qurl,browser = browser:
                                   self.renew_urlbar(qurl,browser))
    def tab_open_doubleclick(self,i):
        if i==-1:
            self.add_new_tab()

    def current_tab_changed(self,i):
        qurl=self.tabs.currentWidget().url()
        self.renew_urlbar(qurl,self.tabs.currentWidget())




if __name__ =='__main__':
    app = QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())






