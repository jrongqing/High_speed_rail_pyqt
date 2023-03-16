# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qdarkstyle

class Ui_MainWindow_check(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_in = QtWidgets.QLabel(self.centralwidget)
        self.label_in.setGeometry(QtCore.QRect(100, 190, 301, 211))
        self.label_in.setText("")
        self.label_in.setPixmap(QtGui.QPixmap("../../Downloads/等待发送 .png"))
        self.label_in.setObjectName("label_in")
        #信号槽链接显示子窗口槽函数
        #self.label_in.mouseDoubleClickSignal.connect(lambda :self.show_child_window)
        self.pushButton_in = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_in.setGeometry(QtCore.QRect(120, 70, 121, 51))
        self.pushButton_in.setStyleSheet(
            "QPushButton{color:#F0FFFF}"  # 按键前景色
            "QPushButton{background-color:#7EC0EE}"  # 按键背景色
            # "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{font:bold 18px}"
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.pushButton_in.setObjectName("pushButton_in")
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run.setGeometry(QtCore.QRect(430, 450, 121, 51))
        self.pushButton_run.setStyleSheet(
            "QPushButton{color:#F0FFFF}"  # 按键前景色
            "QPushButton{background-color:#7EC0EE}"  # 按键背景色
            # "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{font:bold 18px}"
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.pushButton_run.setObjectName("pushButton_run")

        self.pushButton_history = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_history.setGeometry(QtCore.QRect(690, 450, 121, 51))
        self.pushButton_history.setStyleSheet(
            "QPushButton{color:#F0FFFF}"  # 按键前景色
            "QPushButton{background-color:#7EC0EE}"  # 按键背景色
            # "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{font:bold 18px}"
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )
        self.pushButton_history.setObjectName("pushButton_run")


        self.label_out = QtWidgets.QLabel(self.centralwidget)
        self.label_out.setGeometry(QtCore.QRect(680, 190, 301, 211))
        self.label_out.setText("")
        self.label_out.setPixmap(QtGui.QPixmap("../../Downloads/等待发送 .png"))
        self.label_out.setObjectName("label_out")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 190, 121, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/传输(2).png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.pushButton_in.clicked.connect(self.openimage())

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("img/background/bkg.jpg")
        painter.drawPixmap(self.rect(), pixmap)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "异物检测系统"))
        MainWindow.setWindowIcon(QIcon("title.ico"))
        self.pushButton_in.setText(_translate("MainWindow", "导入图片"))
        self.pushButton_run.setText(_translate("MainWindow", "异物检测"))
        self.pushButton_history.setText(_translate("MainWindow", "历史查询"))




class myLabel(QLabel):
    _signal = pyqtSignal(str)#信号定义
    def __init__(self, parent=None):
        super(myLabel, self).__init__(parent)

    def mousePressEvent(self, e):  ##重载一下鼠标点击事件
            print("you clicked the label")
            self._signal.emit("正在检测中")
