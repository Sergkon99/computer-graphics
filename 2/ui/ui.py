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
        MainWindow.resize(820, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.canvas.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.pb_default = QtWidgets.QPushButton(self.centralwidget)
        self.pb_default.setGeometry(QtCore.QRect(620, 620, 191, 31))
        self.pb_default.setObjectName("pb_default")
        self.cb_global_figure = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_global_figure.setGeometry(QtCore.QRect(10, 620, 221, 20))
        self.cb_global_figure.setChecked(True)
        self.cb_global_figure.setObjectName("cb_global_figure")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(620, 10, 191, 91))
        self.groupBox.setObjectName("groupBox")
        self.le_move = QtWidgets.QLineEdit(self.groupBox)
        self.le_move.setGeometry(QtCore.QRect(10, 60, 171, 20))
        self.le_move.setObjectName("le_move")
        self.pb_move_y = QtWidgets.QPushButton(self.groupBox)
        self.pb_move_y.setGeometry(QtCore.QRect(100, 20, 81, 31))
        self.pb_move_y.setObjectName("pb_move_y")
        self.pb_move_x = QtWidgets.QPushButton(self.groupBox)
        self.pb_move_x.setGeometry(QtCore.QRect(10, 20, 81, 31))
        self.pb_move_x.setObjectName("pb_move_x")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(620, 110, 191, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pb_reflection_xy = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_reflection_xy.setGeometry(QtCore.QRect(10, 100, 171, 31))
        self.pb_reflection_xy.setObjectName("pb_reflection_xy")
        self.pb_reflection_x = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_reflection_x.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.pb_reflection_x.setObjectName("pb_reflection_x")
        self.pb_reflection_y = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_reflection_y.setGeometry(QtCore.QRect(10, 60, 171, 31))
        self.pb_reflection_y.setObjectName("pb_reflection_y")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 260, 191, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(6, 50, 51, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(6, 20, 51, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.le_scale_x = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_scale_x.setGeometry(QtCore.QRect(66, 20, 113, 20))
        self.le_scale_x.setObjectName("le_scale_x")
        self.le_scale_y = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_scale_y.setGeometry(QtCore.QRect(66, 50, 113, 20))
        self.le_scale_y.setObjectName("le_scale_y")
        self.pb_scale = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_scale.setGeometry(QtCore.QRect(10, 80, 171, 31))
        self.pb_scale.setObjectName("pb_scale")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(620, 390, 191, 221))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(16, 90, 161, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.le_rotate_from_point_y = QtWidgets.QLineEdit(self.groupBox_4)
        self.le_rotate_from_point_y.setGeometry(QtCore.QRect(66, 150, 113, 20))
        self.le_rotate_from_point_y.setObjectName("le_rotate_from_point_y")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(6, 120, 51, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pb_rotate_from_point = QtWidgets.QPushButton(self.groupBox_4)
        self.pb_rotate_from_point.setGeometry(QtCore.QRect(10, 180, 171, 31))
        self.pb_rotate_from_point.setObjectName("pb_rotate_from_point")
        self.pb_rotate = QtWidgets.QPushButton(self.groupBox_4)
        self.pb_rotate.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.pb_rotate.setObjectName("pb_rotate")
        self.le_rotate_from_point_x = QtWidgets.QLineEdit(self.groupBox_4)
        self.le_rotate_from_point_x.setGeometry(QtCore.QRect(66, 120, 113, 20))
        self.le_rotate_from_point_x.setObjectName("le_rotate_from_point_x")
        self.le_rotate_angle = QtWidgets.QLineEdit(self.groupBox_4)
        self.le_rotate_angle.setGeometry(QtCore.QRect(66, 20, 113, 20))
        self.le_rotate_angle.setObjectName("le_rotate_angle")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(6, 20, 51, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(6, 150, 51, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 21))
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
        self.pb_default.setText(_translate("MainWindow", "Сбросить"))
        self.cb_global_figure.setText(_translate("MainWindow", "Сохранять промежуточные состояния"))
        self.groupBox.setTitle(_translate("MainWindow", "Смещение"))
        self.pb_move_y.setText(_translate("MainWindow", "Сместить по Y"))
        self.pb_move_x.setText(_translate("MainWindow", "Сместить по X"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Отражение"))
        self.pb_reflection_xy.setText(_translate("MainWindow", "Отразить относительно X=Y"))
        self.pb_reflection_x.setText(_translate("MainWindow", "Отразить относительно Ox"))
        self.pb_reflection_y.setText(_translate("MainWindow", "Отразить относительно Oy"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Масштаб"))
        self.label_3.setText(_translate("MainWindow", "Oy:"))
        self.label_2.setText(_translate("MainWindow", "Ox:"))
        self.pb_scale.setText(_translate("MainWindow", "Приментить масштаб"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Поворот"))
        self.label_6.setText(_translate("MainWindow", "Относительно точки"))
        self.label.setText(_translate("MainWindow", "x:"))
        self.pb_rotate_from_point.setText(_translate("MainWindow", "Повернуть"))
        self.pb_rotate.setText(_translate("MainWindow", "Повернуть"))
        self.label_4.setText(_translate("MainWindow", "Угол:"))
        self.label_5.setText(_translate("MainWindow", "y:"))
