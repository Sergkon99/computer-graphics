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
        MainWindow.resize(744, 600)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.canvas.setAutoFillBackground(True)
        self.canvas.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.pb_draw_line = QtWidgets.QPushButton(self.centralwidget)
        self.pb_draw_line.setGeometry(QtCore.QRect(620, 130, 111, 23))
        self.pb_draw_line.setObjectName("pb_draw_line")
        self.le_line_x1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_line_x1.setGeometry(QtCore.QRect(620, 10, 113, 20))
        self.le_line_x1.setObjectName("le_line_x1")
        self.le_line_y1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_line_y1.setGeometry(QtCore.QRect(620, 40, 113, 20))
        self.le_line_y1.setObjectName("le_line_y1")
        self.le_circle_r = QtWidgets.QLineEdit(self.centralwidget)
        self.le_circle_r.setGeometry(QtCore.QRect(620, 230, 113, 20))
        self.le_circle_r.setObjectName("le_circle_r")
        self.le_circle_x = QtWidgets.QLineEdit(self.centralwidget)
        self.le_circle_x.setGeometry(QtCore.QRect(620, 170, 113, 20))
        self.le_circle_x.setObjectName("le_circle_x")
        self.le_circle_y = QtWidgets.QLineEdit(self.centralwidget)
        self.le_circle_y.setGeometry(QtCore.QRect(620, 200, 113, 20))
        self.le_circle_y.setObjectName("le_circle_y")
        self.pb_draw_circle = QtWidgets.QPushButton(self.centralwidget)
        self.pb_draw_circle.setGeometry(QtCore.QRect(620, 260, 111, 23))
        self.pb_draw_circle.setObjectName("pb_draw_circle")
        self.le_line_x2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_line_x2.setGeometry(QtCore.QRect(620, 70, 113, 20))
        self.le_line_x2.setObjectName("le_line_x2")
        self.le_line_y2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_line_y2.setGeometry(QtCore.QRect(620, 100, 113, 20))
        self.le_line_y2.setObjectName("le_line_y2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 21))
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
        self.pb_draw_line.setText(_translate("MainWindow", "PushButton"))
        self.pb_draw_circle.setText(_translate("MainWindow", "PushButton"))
