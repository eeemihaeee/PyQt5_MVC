# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 32)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_plus = QtWidgets.QLabel(self.centralwidget)
        self.lbl_plus.setGeometry(QtCore.QRect(130, 0, 47, 14))
        self.lbl_plus.setObjectName("lbl_plus")
        self.lbl_equal = QtWidgets.QLabel(self.centralwidget)
        self.lbl_equal.setGeometry(QtCore.QRect(300, 0, 47, 14))
        self.lbl_equal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_equal.setObjectName("lbl_equal")
        self.le_result = QtWidgets.QLineEdit(self.centralwidget)
        self.le_result.setGeometry(QtCore.QRect(340, 0, 113, 20))
        self.le_result.setObjectName("le_result")
        self.le_c = QtWidgets.QLineEdit(self.centralwidget)
        self.le_c.setGeometry(QtCore.QRect(0, 0, 113, 20))
        self.le_c.setObjectName("le_c")
        self.le_d = QtWidgets.QLineEdit(self.centralwidget)
        self.le_d.setGeometry(QtCore.QRect(170, 0, 113, 20))
        self.le_d.setObjectName("le_d")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_plus.setText(_translate("MainWindow", "+"))
        self.lbl_equal.setText(_translate("MainWindow", "="))
