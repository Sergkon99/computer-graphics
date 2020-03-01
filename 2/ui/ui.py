# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 200, 47, 13))
        self.label.setObjectName("label")
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 600, 500))
        self.canvas.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.pb_default = QtWidgets.QPushButton(self.centralwidget)
        self.pb_default.setGeometry(QtCore.QRect(620, 10, 171, 31))
        self.pb_default.setObjectName("pb_default")
        self.pb_move_x = QtWidgets.QPushButton(self.centralwidget)
        self.pb_move_x.setGeometry(QtCore.QRect(620, 60, 81, 31))
        self.pb_move_x.setObjectName("pb_move_x")
        self.pb_move_y = QtWidgets.QPushButton(self.centralwidget)
        self.pb_move_y.setGeometry(QtCore.QRect(710, 60, 81, 31))
        self.pb_move_y.setObjectName("pb_move_y")
        self.le_move = QtWidgets.QLineEdit(self.centralwidget)
        self.le_move.setGeometry(QtCore.QRect(620, 100, 171, 20))
        self.le_move.setObjectName("le_move")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pb_default.setText(_translate("MainWindow", "По умолчанию"))
        self.pb_move_x.setText(_translate("MainWindow", "Сместить по X"))
        self.pb_move_y.setText(_translate("MainWindow", "Сместить по Y"))
