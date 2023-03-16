# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pre_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.Qt import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap

class Ui_MainWindow_pre(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 80, 351, 81))
        self.label.setObjectName("label")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(290, 190, 161, 61))
        self.pushButton_login.setStyleSheet(
            "QPushButton{color:#F0FFFF}"  # 按键前景色
            "QPushButton{background-color:#7EC0EE}"  # 按键背景色
            #"QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{font:bold 18px}"
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_creat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_creat.setGeometry(QtCore.QRect(290, 280, 161, 61))
        self.pushButton_creat.setStyleSheet(
            "QPushButton{color:#F0FFFF}"  # 按键前景色
            "QPushButton{background-color:#7EC0EE}"  # 按键背景色
            #"QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{font:bold 18px}"
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.pushButton_creat.setObjectName("pushButton_creat")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(290, 370, 161, 61))
        self.pushButton_exit.setStyleSheet(
            "QPushButton{color:#F0FFFF}"  # 按键前景色
            "QPushButton{background-color:#7EC0EE}"  # 按键背景色
            #"QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{font:bold 18px}"
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.pushButton_exit.setObjectName("pushButton_exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # palette = QPalette()
        # palette.setBrush(QPalette.Background,QBrush(QPixmap("img/background/pre_login.jpg")))
        # MainWindow.setPalette(palette)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("img/background/bkg.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "高铁异物检测系统"))
        MainWindow.setWindowIcon(QIcon("title.ico"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#363636;\">高铁铁轨异物检测系统</span></p></body></html>"))
        self.pushButton_login.setText(_translate("MainWindow", "账号登陆"))
        self.pushButton_creat.setText(_translate("MainWindow", "注册账号"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出程序"))

