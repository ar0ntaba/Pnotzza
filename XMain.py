import os
import sys
import time
import math
import xml.etree.ElementTree as xml

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 633)
        self.setWindowIcon(QtGui.QIcon('iconpiz.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1001, 661))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("MainPage.png"))
        self.label.setObjectName("label")
        self.BtnMain = QtWidgets.QPushButton(self.centralwidget)
        self.BtnMain.setGeometry(QtCore.QRect(160, 500, 241, 51))
        self.BtnMain.setAutoFillBackground(False)
        self.BtnMain.setText("")
        self.BtnMain.setAutoDefault(True)
        self.BtnMain.setDefault(True)
        self.BtnMain.setFlat(True)
        self.BtnMain.setObjectName("BtnMain")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1000, 661)
        LoginWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.setWindowIcon(QtGui.QIcon('iconpiz.png'))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 661))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("LoginPage.png"))
        self.label.setObjectName("label")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(440, 420, 121, 31))
        self.Login.setText("")
        self.Login.setAutoDefault(True)
        self.Login.setFlat(True)
        self.Login.setObjectName("Login")
        self.userline = QtWidgets.QLineEdit(self.centralwidget)
        self.userline.setEnabled(True)
        self.userline.setGeometry(QtCore.QRect(433, 242, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.userline.setFont(font)
        self.userline.setFrame(False)
        self.userline.setClearButtonEnabled(True)
        self.userline.setPlaceholderText("Username")
        self.userline.setObjectName("userline")
        self.passline = QtWidgets.QLineEdit(self.centralwidget)
        self.passline.setGeometry(QtCore.QRect(433, 315, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.passline.setFont(font)
        self.passline.setFrame(False)
        self.passline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passline.setClearButtonEnabled(True)
        self.passline.setPlaceholderText("********")
        self.passline.setObjectName("passline")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))

# PIZZA TIME!
class Ui_PizzaWindow(object):
    def setupUi(self, PizzaWindow):
        PizzaWindow.setObjectName("PizzaWindow")
        PizzaWindow.resize(999, 661)
        self.setWindowIcon(QtGui.QIcon('iconpiz.png'))
        self.centralwidget = QtWidgets.QWidget(PizzaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pnotzza = QtWidgets.QLabel(self.centralwidget)
        self.pnotzza.setGeometry(QtCore.QRect(0, 0, 1001, 661))
        self.pnotzza.setText("")
        self.pnotzza.setPixmap(QtGui.QPixmap("Window1.png"))
        self.pnotzza.setObjectName("pnotzza")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(78, 173, 25, 25))
        self.btn1.setText("")
        self.btn1.setFlat(True)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(238, 173, 25, 25))
        self.btn2.setText("")
        self.btn2.setFlat(True)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(398, 173, 25, 25))
        self.btn3.setText("")
        self.btn3.setFlat(True)
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(558, 173, 25, 25))
        self.btn4.setText("")
        self.btn4.setFlat(True)
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(77, 426, 25, 25))
        self.btn5.setText("")
        self.btn5.setFlat(True)
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(238, 426, 25, 25))
        self.btn6.setText("")
        self.btn6.setFlat(True)
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(398, 426, 25, 25))
        self.btn7.setText("")
        self.btn7.setFlat(True)
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(558, 426, 25, 25))
        self.btn8.setText("")
        self.btn8.setFlat(True)
        self.btn8.setObjectName("btn8")
        self.checkout = QtWidgets.QPushButton(self.centralwidget)
        self.checkout.setGeometry(QtCore.QRect(670, 587, 321, 55))
        self.checkout.setText("")
        self.checkout.setFlat(True)
        self.checkout.setObjectName("checkout")
        self.spin1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spin1.setEnabled(False)
        self.spin1.setGeometry(QtCore.QRect(800, 85, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin1.sizePolicy().hasHeightForWidth())
        self.spin1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.spin1.setFont(font)
        self.spin1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spin1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spin1.setAutoFillBackground(False)
        self.spin1.setStyleSheet("QSpinBox::down-button {\n"
                                "    subcontrol-position: center left;\n"
                                "    height: 20px;\n"
                                "    width: 24px;\n"
                                "}\n"
                                "QSpinBox::up-button {\n"
                                "    subcontrol-position: center right;\n"
                                "    height: 20px;\n"
                                "    width: 27px;\n"
                                "}")
        self.spin1.setWrapping(False)
        self.spin1.setFrame(False)
        self.spin1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin1.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin1.setAccelerated(True)
        self.spin1.setProperty("showGroupSeparator", True)
        self.spin1.setMaximum(20)
        self.spin1.setSingleStep(1)
        self.spin1.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin1.setDisplayIntegerBase(10)
        self.spin1.setObjectName("spin1")
        self.spin2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spin2.setEnabled(False)
        self.spin2.setGeometry(QtCore.QRect(800, 125, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin2.sizePolicy().hasHeightForWidth())
        self.spin2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.spin2.setFont(font)
        self.spin2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spin2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spin2.setAutoFillBackground(False)
        self.spin2.setStyleSheet("QSpinBox::down-button {\n"
                                "    subcontrol-position: center left;\n"
                                "    height: 20px;\n"
                                "    width: 24px;\n"
                                "}\n"
                                "QSpinBox::up-button {\n"
                                "    subcontrol-position: center right;\n"
                                "    height: 20px;\n"
                                "    width: 27px;\n"
                                "}")
        self.spin2.setWrapping(False)
        self.spin2.setFrame(False)
        self.spin2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin2.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin2.setAccelerated(True)
        self.spin2.setProperty("showGroupSeparator", True)
        self.spin2.setMaximum(20)
        self.spin2.setSingleStep(1)
        self.spin2.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin2.setDisplayIntegerBase(10)
        self.spin2.setObjectName("spin2")
        self.spin3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spin3.setEnabled(False)
        self.spin3.setGeometry(QtCore.QRect(800, 167, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin3.sizePolicy().hasHeightForWidth())
        self.spin3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.spin3.setFont(font)
        self.spin3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spin3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spin3.setAutoFillBackground(False)
        self.spin3.setStyleSheet("QSpinBox::down-button {\n"
                                "    subcontrol-position: center left;\n"
                                "    height: 20px;\n"
                                "    width: 24px;\n"
                                "}\n"
                                "QSpinBox::up-button {\n"
                                "    subcontrol-position: center right;\n"
                                "    height: 20px;\n"
                                "    width: 27px;\n"
                                "}")
        self.spin3.setWrapping(False)
        self.spin3.setFrame(False)
        self.spin3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin3.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin3.setAccelerated(True)
        self.spin3.setProperty("showGroupSeparator", True)
        self.spin3.setMaximum(20)
        self.spin3.setSingleStep(1)
        self.spin3.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin3.setDisplayIntegerBase(10)
        self.spin3.setObjectName("spin3")
        self.spin4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spin4.setEnabled(False)
        self.spin4.setGeometry(QtCore.QRect(800, 205, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin4.sizePolicy().hasHeightForWidth())
        self.spin4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.spin4.setFont(font)
        self.spin4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spin4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spin4.setAutoFillBackground(False)
        self.spin4.setStyleSheet("QSpinBox::down-button {\n"
                                "    subcontrol-position: center left;\n"
                                "    height: 20px;\n"
                                "    width: 24px;\n"
                                "}\n"
                                "QSpinBox::up-button {\n"
                                "    subcontrol-position: center right;\n"
                                "    height: 20px;\n"
                                "    width: 27px;\n"
                                "}")
        self.spin4.setWrapping(False)
        self.spin4.setFrame(False)
        self.spin4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin4.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin4.setAccelerated(True)
        self.spin4.setProperty("showGroupSeparator", True)
        self.spin4.setMaximum(20)
        self.spin4.setSingleStep(1)
        self.spin4.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin4.setDisplayIntegerBase(10)
        self.spin4.setObjectName("spin4")
        self.spin5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spin5.setEnabled(False)
        self.spin5.setGeometry(QtCore.QRect(800, 245, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin5.sizePolicy().hasHeightForWidth())
        self.spin5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.spin5.setFont(font)
        self.spin5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spin5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spin5.setAutoFillBackground(False)
        self.spin5.setStyleSheet("QSpinBox::down-button {\n"
                                "    subcontrol-position: center left;\n"
                                "    height: 20px;\n"
                                "    width: 24px;\n"
                                "}\n"
                                "QSpinBox::up-button {\n"
                                "    subcontrol-position: center right;\n"
                                "    height: 20px;\n"
                                "    width: 27px;\n"
                                "}")
        self.spin5.setWrapping(False)
        self.spin5.setFrame(False)
        self.spin5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin5.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin5.setAccelerated(True)
        self.spin5.setProperty("showGroupSeparator", True)
        self.spin5.setMaximum(20)
        self.spin5.setSingleStep(1)
        self.spin5.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin5.setDisplayIntegerBase(10)
        self.spin5.setObjectName("spin5")
        self.spin6 = QtWidgets.QSpinBox(self.centralwidget)
        self.spin6.setEnabled(False)
        self.spin6.setGeometry(QtCore.QRect(800, 287, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin6.sizePolicy().hasHeightForWidth())
        self.spin6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.spin6.setFont(font)
        self.spin6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spin6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spin6.setAutoFillBackground(False)
        self.spin6.setStyleSheet("QSpinBox::down-button {\n"
                                "    subcontrol-position: center left;\n"
                                "    height: 20px;\n"
                                "    width: 24px;\n"
                                "}\n"
                                "QSpinBox::up-button {\n"
                                "    subcontrol-position: center right;\n"
                                "    height: 20px;\n"
                                "    width: 27px;\n"
                                "}")
        self.spin6.setWrapping(False)
        self.spin6.setFrame(False)
        self.spin6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin6.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin6.setAccelerated(True)
        self.spin6.setProperty("showGroupSeparator", True)
        self.spin6.setMaximum(20)
        self.spin6.setSingleStep(1)
        self.spin6.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin6.setDisplayIntegerBase(10)
        self.spin6.setObjectName("spin6")
        self.spin7 = QtWidgets.QSpinBox(self.centralwidget)
        self.spin7.setEnabled(False)
        self.spin7.setGeometry(QtCore.QRect(800, 327, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin7.sizePolicy().hasHeightForWidth())
        self.spin7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.spin7.setFont(font)
        self.spin7.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spin7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spin7.setAutoFillBackground(False)
        self.spin7.setStyleSheet("QSpinBox::down-button {\n"
                                "    subcontrol-position: center left;\n"
                                "    height: 20px;\n"
                                "    width: 24px;\n"
                                "}\n"
                                "QSpinBox::up-button {\n"
                                "    subcontrol-position: center right;\n"
                                "    height: 20px;\n"
                                "    width: 27px;\n"
                                "}")
        self.spin7.setWrapping(False)
        self.spin7.setFrame(False)
        self.spin7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin7.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin7.setAccelerated(True)
        self.spin7.setProperty("showGroupSeparator", True)
        self.spin7.setMaximum(20)
        self.spin7.setSingleStep(1)
        self.spin7.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin7.setDisplayIntegerBase(10)
        self.spin7.setObjectName("spin7")
        self.spin8 = QtWidgets.QSpinBox(self.centralwidget)
        self.spin8.setEnabled(False)
        self.spin8.setGeometry(QtCore.QRect(800, 367, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin8.sizePolicy().hasHeightForWidth())
        self.spin8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.spin8.setFont(font)
        self.spin8.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin8.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.spin8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spin8.setAutoFillBackground(False)
        self.spin8.setStyleSheet("QSpinBox::down-button {\n"
                                "    subcontrol-position: center left;\n"
                                "    height: 20px;\n"
                                "    width: 24px;\n"
                                "}\n"
                                "QSpinBox::up-button {\n"
                                "    subcontrol-position: center right;\n"
                                "    height: 20px;\n"
                                "    width: 27px;\n"
                                "}")
        self.spin8.setWrapping(False)
        self.spin8.setFrame(False)
        self.spin8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin8.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin8.setAccelerated(True)
        self.spin8.setProperty("showGroupSeparator", True)
        self.spin8.setMaximum(20)
        self.spin8.setSingleStep(1)
        self.spin8.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spin8.setDisplayIntegerBase(10)
        self.spin8.setObjectName("spin8")
        self.p1 = QtWidgets.QLabel(self.centralwidget)
        self.p1.setGeometry(QtCore.QRect(947, 85, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.p1.setFont(font)
        self.p1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QLabel(self.centralwidget)
        self.p2.setGeometry(QtCore.QRect(947, 130, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.p2.setFont(font)
        self.p2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QLabel(self.centralwidget)
        self.p3.setGeometry(QtCore.QRect(947, 170, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.p3.setFont(font)
        self.p3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.p3.setObjectName("p3")
        self.p4 = QtWidgets.QLabel(self.centralwidget)
        self.p4.setGeometry(QtCore.QRect(947, 210, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.p4.setFont(font)
        self.p4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QLabel(self.centralwidget)
        self.p5.setGeometry(QtCore.QRect(947, 250, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.p5.setFont(font)
        self.p5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QLabel(self.centralwidget)
        self.p6.setGeometry(QtCore.QRect(947, 290, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.p6.setFont(font)
        self.p6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.p6.setObjectName("p6")
        self.p7 = QtWidgets.QLabel(self.centralwidget)
        self.p7.setGeometry(QtCore.QRect(947, 330, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.p7.setFont(font)
        self.p7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.p7.setObjectName("p7")
        self.p8 = QtWidgets.QLabel(self.centralwidget)
        self.p8.setGeometry(QtCore.QRect(947, 370, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.p8.setFont(font)
        self.p8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.p8.setObjectName("p8")
        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(947, 435, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.total.setFont(font)
        self.total.setObjectName("total")
        self.change = QtWidgets.QLabel(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(948, 516, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.change.setFont(font)
        self.change.setObjectName("change")
        self.cash = QtWidgets.QLineEdit(self.centralwidget)
        self.cash.setGeometry(QtCore.QRect(923, 476, 60, 18))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.cash.setFont(font)
        self.cash.setMaxLength(6)
        self.cash.setFrame(False)
        self.cash.setClearButtonEnabled(False)
        self.cash.setObjectName("cash")
        PizzaWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PizzaWindow)
        QtCore.QMetaObject.connectSlotsByName(PizzaWindow)

    def retranslateUi(self, PizzaWindow):
        _translate = QtCore.QCoreApplication.translate
        PizzaWindow.setWindowTitle(_translate("PizzaWindow", "Pizza Time !"))
        self.p1.setText(_translate("PizzaWindow", "0"))
        self.p2.setText(_translate("PizzaWindow", "0"))
        self.p3.setText(_translate("PizzaWindow", "0"))
        self.p4.setText(_translate("PizzaWindow", "0"))
        self.p5.setText(_translate("PizzaWindow", "0"))
        self.p6.setText(_translate("PizzaWindow", "0"))
        self.p7.setText(_translate("PizzaWindow", "0"))
        self.p8.setText(_translate("PizzaWindow", "0"))
        self.total.setText(_translate("PizzaWindow", "0"))
        self.change.setText(_translate("PizzaWindow", "0"))
##---|FUNCTIONS|---###

class Start(QtWidgets.QMainWindow, Ui_MainWindow):

    switch = QtCore.pyqtSignal()
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.BtnMain.clicked.connect(self.BtnClicked1)

    def BtnClicked1(self):
        self.switch.emit()
        self.close()

class Login(QtWidgets.QMainWindow, Ui_LoginWindow):

    switch2 = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.Login.clicked.connect(self.LogClicked)

    def LogClicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("Login")
        msg.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        if self.userline.text() == 'admin' and self.passline.text() == 'admin':
            msg.setText('Welcome')
            msg.exec_()
            self.switch2.emit()
            self.close()

        else:
            msg.setText('Incorrect Password')
            msg.exec_()

class Pizza(QtWidgets.QMainWindow, Ui_PizzaWindow):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.btn1.clicked.connect(self.enable1)
        self.btn2.clicked.connect(self.enable2)
        self.btn3.clicked.connect(self.enable3)
        self.btn4.clicked.connect(self.enable4)
        self.btn5.clicked.connect(self.enable5)
        self.btn6.clicked.connect(self.enable6)
        self.btn7.clicked.connect(self.enable7)
        self.btn8.clicked.connect(self.enable8)

        self.spin1.valueChanged['int'].connect(self.Q1)
        self.spin2.valueChanged['int'].connect(self.Q2)
        self.spin3.valueChanged['int'].connect(self.Q3)
        self.spin4.valueChanged['int'].connect(self.Q4)
        self.spin5.valueChanged['int'].connect(self.Q5)
        self.spin6.valueChanged['int'].connect(self.Q6)
        self.spin7.valueChanged['int'].connect(self.Q7)
        self.spin8.valueChanged['int'].connect(self.Q8)
        #self.cash.editingFinished.connect(self.compute)
        self.checkout.clicked.connect(self.receipt)
#####
    def enable1(self):
        self.spin1.setEnabled(True)
    def enable2(self):
        self.spin2.setEnabled(True)
    def enable3(self):
        self.spin3.setEnabled(True)
    def enable4(self):
        self.spin4.setEnabled(True)
    def enable5(self):
        self.spin5.setEnabled(True)
    def enable6(self):
        self.spin6.setEnabled(True)
    def enable7(self):
        self.spin7.setEnabled(True)
    def enable8(self):
        self.spin8.setEnabled(True) 
####
    

    def receipt(self):

        def GenerateXML(fileName):

            xtotal = totes
            xcash = Customer_Cash
            xchange = Transaction

            root = xml.Element("Receipt")
            cl = xml.Element("Transaction")
            root.append(cl)

            Total = xml.SubElement(cl, "Total")
            Total.text = str(xtotal)

            Cash= xml.SubElement(cl, "Cash")
            Cash.text = str(xcash)

            Change = xml.SubElement(cl, "Change")
            Change.text = str(xchange)

            tree = xml.ElementTree(root)
            with open(fileName,"wb") as files:
                tree.write(files)
        ############LINEEND########

        num1 = (self.spin1.value()*100)        
        num2 = (self.spin2.value()*110)
        num3 = (self.spin3.value()*120)
        num4 = (self.spin4.value()*150)
        num5 = (self.spin5.value()*120)
        num6 = (self.spin6.value()*130)
        num7 = (self.spin7.value()*140)
        num8 = (self.spin8.value()*100)
        totes = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)
        Customer_Cash = int(self.cash.text())
        Transaction = (Customer_Cash - totes)

        msg = QMessageBox()
        msg.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        if Customer_Cash >= totes:
            self.change.setNum(Customer_Cash - totes)

            reply=QMessageBox.question(self,'Message','Finish Ordering ?  ',QMessageBox.Yes|QMessageBox.No,QMessageBox.No )

            if reply==QMessageBox.Yes:

                reply2=QMessageBox.question(self,'Message','Do you want to print your receipt ?  ',QMessageBox.Yes|QMessageBox.No,QMessageBox.No )

                if reply2==QMessageBox.Yes:
                    GenerateXML("PrintedReceipt.xml")

                    msg.setText("Receipt Printed\n Thank You for ordering! ")
                    msg.exec_()
                    msg.close()
                else:
                    msg.setText("Thank You ! :)")
                    msg.exec_()
                    msg.close()
            else:
                pass

        elif Customer_Cash < totes:
            msg.setText("Insufficient Cash")
            msg.exec_()
            msg.close()
        else:
            msg.setText("Invalid Input")
            msg.exec_()
            msg.close()

        

#---------------------------------------------#PRICES#---------------------------------------------#
    def Q1(self):
        num1 = (self.spin1.value()*100)        
        num2 = (self.spin2.value()*110)
        num3 = (self.spin3.value()*120)
        num4 = (self.spin4.value()*150)
        num5 = (self.spin5.value()*120)
        num6 = (self.spin6.value()*130)
        num7 = (self.spin7.value()*140)
        num8 = (self.spin8.value()*100)
        totes = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)
        self.p1.setNum(num1)
        self.p1.adjustSize()
        self.total.setNum((totes))
        self.total.adjustSize()

    def Q2(self):
        num1 = (self.spin1.value()*100)        
        num2 = (self.spin2.value()*110)
        num3 = (self.spin3.value()*120)
        num4 = (self.spin4.value()*150)
        num5 = (self.spin5.value()*120)
        num6 = (self.spin6.value()*130)
        num7 = (self.spin7.value()*140)
        num8 = (self.spin8.value()*100)
        totes = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)

        self.p2.setNum(num2)
        self.p2.adjustSize()
        self.total.setNum((totes))
        self.total.adjustSize()

    def Q3(self):

        num1 = (self.spin1.value()*100)        
        num2 = (self.spin2.value()*110)
        num3 = (self.spin3.value()*120)
        num4 = (self.spin4.value()*150)
        num5 = (self.spin5.value()*120)
        num6 = (self.spin6.value()*130)
        num7 = (self.spin7.value()*140)
        num8 = (self.spin8.value()*100)
        totes = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)

        self.p3.setNum(num3)
        self.p3.adjustSize()
        self.total.setNum((totes))
        self.total.adjustSize()

    def Q4(self):

        num1 = (self.spin1.value()*100)        
        num2 = (self.spin2.value()*110)
        num3 = (self.spin3.value()*120)
        num4 = (self.spin4.value()*150)
        num5 = (self.spin5.value()*120)
        num6 = (self.spin6.value()*130)
        num7 = (self.spin7.value()*140)
        num8 = (self.spin8.value()*100)
        totes = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)

        self.p4.setNum(num4)
        self.p4.adjustSize()
        self.total.setNum((totes))
        self.total.adjustSize()
      
    def Q5(self):

        num1 = (self.spin1.value()*100)        
        num2 = (self.spin2.value()*110)
        num3 = (self.spin3.value()*120)
        num4 = (self.spin4.value()*150)
        num5 = (self.spin5.value()*120)
        num6 = (self.spin6.value()*130)
        num7 = (self.spin7.value()*140)
        num8 = (self.spin8.value()*100)
        totes = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)

        self.p5.setNum(num5)
        self.p5.adjustSize()
        self.total.setNum((totes))
        self.total.adjustSize()

    def Q6(self):

        num1 = (self.spin1.value()*100)        
        num2 = (self.spin2.value()*110)
        num3 = (self.spin3.value()*120)
        num4 = (self.spin4.value()*150)
        num5 = (self.spin5.value()*120)
        num6 = (self.spin6.value()*130)
        num7 = (self.spin7.value()*140)
        num8 = (self.spin8.value()*100)
        totes = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)

        self.p6.setNum(num6)
        self.p6.adjustSize()
        self.total.setNum((totes))
        self.total.adjustSize()
       
    def Q7(self):

        num1 = (self.spin1.value()*100)        
        num2 = (self.spin2.value()*110)
        num3 = (self.spin3.value()*120)
        num4 = (self.spin4.value()*150)
        num5 = (self.spin5.value()*120)
        num6 = (self.spin6.value()*130)
        num7 = (self.spin7.value()*140)
        num8 = (self.spin8.value()*100)
        totes = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)

        self.p7.setNum(num7)
        self.p7.adjustSize()
        self.total.setNum((totes))
        self.total.adjustSize()

    def Q8(self):

        num1 = (self.spin1.value()*100)        
        num2 = (self.spin2.value()*110)
        num3 = (self.spin3.value()*120)
        num4 = (self.spin4.value()*150)
        num5 = (self.spin5.value()*120)
        num6 = (self.spin6.value()*130)
        num7 = (self.spin7.value()*140)
        num8 = (self.spin8.value()*100)
        totes = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8)

        self.p8.setNum(num8)
        self.p8.adjustSize()
        self.total.setNum((totes))
        self.total.adjustSize() 
        
class Controller():
    def __init__(self):
        pass
    # SHOW START

    def show_start(self):
        self.start = Start()
        self.start.switch.connect(self.show_login)
        self.start.show()

    # SHOW MAIN MENU
    def show_login(self):
        self.login = Login()
        self.login.show()
        self.login.switch2.connect(self.show_pizza)

    def show_pizza(self):
        self.pizza = Pizza()
        self.pizza.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
