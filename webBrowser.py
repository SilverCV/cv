# -*- coding: utf-8 -*-
"""
Created on 2018

@author: silver
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys

class MainWindwos(QMainWindow):

    def __init__(self,*args,**kwargs):
        super(MainWindwos,self).__init__(*args,**kwargs)
        self.setWindowTitle("browser")
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.baidu.com"))
        self.setCentralWidget(self.browser)
        nativab = QToolBar("Navigation")
        nativab.setIconSize(QSize(16,16))
        self.addToolBar(nativab)

        back_btn = QAction(QIcon(os.path.join('png','left-arrow.png')),'Back',self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        nativab.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join('png', 'right-arrow.png')), 'Forward', self)
        next_btn.setStatusTip("Forward to previous page")
        next_btn.triggered.connect(self.browser.forward)
        nativab.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join('png', 'reload.png')), "Relaod", self)
        reload_btn.setStatusTip("relaod the page")
        reload_btn.triggered.connect(self.browser.reload)
        nativab.addAction(reload_btn)

        home_btn = QAction(QIcon(os.path.join('png','home.png')),"主页",self)
        home_btn.setStatusTip("return to home page")
        home_btn.triggered.connect(self.nativegate_home)
        nativab.addAction(home_btn)
        nativab.addSeparator()
        self.httpIcon =  QLabel()
        nativab.addWidget(self.httpIcon)


        self.urledit = QLineEdit()
        nativab.addWidget(self.urledit)

        stop_btn = QAction(QIcon(os.path.join('png', 'cross.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading the page")
        stop_btn.triggered.connect(self.browser.stop)
        nativab.addAction(stop_btn)



        self.browser.urlChanged.connect(self.update_url)
        self.urledit.returnPressed.connect(self.goto_url)

    def nativegate_home(self):
        self.browser.setUrl(QUrl('http://www.baidu.com'))

    def goto_url(self):
        Url = QUrl(self.urledit.text())
        if Url.scheme() == '':
            Url.setScheme('http')

        self.browser.setUrl(Url)


    def update_url(self,q):
        if q.scheme() == 'https':
            self.httpIcon.setPixmap(QPixmap(os.path.join('png','002-lock.png')))
        else:
            self.httpIcon.setPixmap(QPixmap(os.path.join('png', '001-lock-1.png')))


        self.urledit.setText(q.toString())
        self.urledit.setCursorPosition(0)

if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("浏览器")
    brow = MainWindwos()
    brow.show()
    app.exec()