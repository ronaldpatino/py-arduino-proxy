# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Main.ui'
#
# Created: Thu May 12 22:41:26 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(754, 566)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 20, 661, 461))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/images/Arduino-Uno.png);\n"
"background-position: top left;\n"
"background-repeat: none;\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pinEnabled13 = QtGui.QCheckBox(self.frame)
        self.pinEnabled13.setGeometry(QtCore.QRect(200, 70, 21, 21))
        self.pinEnabled13.setText(_fromUtf8(""))
        self.pinEnabled13.setObjectName(_fromUtf8("pinEnabled13"))
        self.pinEnabled12 = QtGui.QCheckBox(self.frame)
        self.pinEnabled12.setGeometry(QtCore.QRect(240, 70, 16, 21))
        self.pinEnabled12.setText(_fromUtf8(""))
        self.pinEnabled12.setObjectName(_fromUtf8("pinEnabled12"))
        self.pinEnabled11 = QtGui.QCheckBox(self.frame)
        self.pinEnabled11.setGeometry(QtCore.QRect(280, 70, 16, 21))
        self.pinEnabled11.setText(_fromUtf8(""))
        self.pinEnabled11.setObjectName(_fromUtf8("pinEnabled11"))
        self.pinEnabled10 = QtGui.QCheckBox(self.frame)
        self.pinEnabled10.setGeometry(QtCore.QRect(320, 70, 16, 21))
        self.pinEnabled10.setText(_fromUtf8(""))
        self.pinEnabled10.setObjectName(_fromUtf8("pinEnabled10"))
        self.pinEnabled9 = QtGui.QCheckBox(self.frame)
        self.pinEnabled9.setGeometry(QtCore.QRect(360, 70, 16, 21))
        self.pinEnabled9.setText(_fromUtf8(""))
        self.pinEnabled9.setObjectName(_fromUtf8("pinEnabled9"))
        self.pinEnabled8 = QtGui.QCheckBox(self.frame)
        self.pinEnabled8.setGeometry(QtCore.QRect(400, 70, 16, 21))
        self.pinEnabled8.setText(_fromUtf8(""))
        self.pinEnabled8.setObjectName(_fromUtf8("pinEnabled8"))
        self.pinMode13 = QtGui.QPushButton(self.frame)
        self.pinMode13.setGeometry(QtCore.QRect(200, 90, 16, 27))
        self.pinMode13.setAutoFillBackground(False)
        self.pinMode13.setCheckable(False)
        self.pinMode13.setChecked(False)
        self.pinMode13.setDefault(False)
        self.pinMode13.setFlat(False)
        self.pinMode13.setObjectName(_fromUtf8("pinMode13"))
        self.pinMode12 = QtGui.QPushButton(self.frame)
        self.pinMode12.setGeometry(QtCore.QRect(240, 90, 16, 27))
        self.pinMode12.setObjectName(_fromUtf8("pinMode12"))
        self.pinMode11 = QtGui.QPushButton(self.frame)
        self.pinMode11.setGeometry(QtCore.QRect(280, 90, 16, 27))
        self.pinMode11.setObjectName(_fromUtf8("pinMode11"))
        self.pinMode10 = QtGui.QPushButton(self.frame)
        self.pinMode10.setGeometry(QtCore.QRect(320, 90, 16, 27))
        self.pinMode10.setObjectName(_fromUtf8("pinMode10"))
        self.pinMode9 = QtGui.QPushButton(self.frame)
        self.pinMode9.setGeometry(QtCore.QRect(360, 90, 16, 27))
        self.pinMode9.setObjectName(_fromUtf8("pinMode9"))
        self.pinMode8 = QtGui.QPushButton(self.frame)
        self.pinMode8.setGeometry(QtCore.QRect(400, 90, 16, 27))
        self.pinMode8.setObjectName(_fromUtf8("pinMode8"))
        self.pinValue11 = QtGui.QSlider(self.frame)
        self.pinValue11.setGeometry(QtCore.QRect(280, 180, 29, 91))
        self.pinValue11.setMaximum(255)
        self.pinValue11.setOrientation(QtCore.Qt.Vertical)
        self.pinValue11.setObjectName(_fromUtf8("pinValue11"))
        self.pinValue10 = QtGui.QSlider(self.frame)
        self.pinValue10.setGeometry(QtCore.QRect(320, 180, 29, 91))
        self.pinValue10.setMaximum(255)
        self.pinValue10.setOrientation(QtCore.Qt.Vertical)
        self.pinValue10.setObjectName(_fromUtf8("pinValue10"))
        self.pinValue9 = QtGui.QSlider(self.frame)
        self.pinValue9.setGeometry(QtCore.QRect(360, 180, 29, 91))
        self.pinValue9.setMaximum(255)
        self.pinValue9.setOrientation(QtCore.Qt.Vertical)
        self.pinValue9.setObjectName(_fromUtf8("pinValue9"))
        self.label13 = QtGui.QLabel(self.frame)
        self.label13.setGeometry(QtCore.QRect(180, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label13.setFont(font)
        self.label13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label13.setObjectName(_fromUtf8("label13"))
        self.label12 = QtGui.QLabel(self.frame)
        self.label12.setGeometry(QtCore.QRect(220, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label12.setFont(font)
        self.label12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label12.setObjectName(_fromUtf8("label12"))
        self.label11 = QtGui.QLabel(self.frame)
        self.label11.setGeometry(QtCore.QRect(260, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label11.setFont(font)
        self.label11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label11.setObjectName(_fromUtf8("label11"))
        self.label10 = QtGui.QLabel(self.frame)
        self.label10.setGeometry(QtCore.QRect(300, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label10.setFont(font)
        self.label10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label10.setObjectName(_fromUtf8("label10"))
        self.label9 = QtGui.QLabel(self.frame)
        self.label9.setGeometry(QtCore.QRect(340, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label9.setFont(font)
        self.label9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label9.setObjectName(_fromUtf8("label9"))
        self.label8 = QtGui.QLabel(self.frame)
        self.label8.setGeometry(QtCore.QRect(380, 50, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label8.setFont(font)
        self.label8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label8.setObjectName(_fromUtf8("label8"))
        self.lcdPWM11 = QtGui.QLCDNumber(self.frame)
        self.lcdPWM11.setGeometry(QtCore.QRect(260, 270, 40, 23))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lcdPWM11.setFont(font)
        self.lcdPWM11.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.lcdPWM11.setNumDigits(4)
        self.lcdPWM11.setObjectName(_fromUtf8("lcdPWM11"))
        self.lcdPWM10 = QtGui.QLCDNumber(self.frame)
        self.lcdPWM10.setGeometry(QtCore.QRect(300, 270, 40, 23))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lcdPWM10.setFont(font)
        self.lcdPWM10.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.lcdPWM10.setNumDigits(4)
        self.lcdPWM10.setObjectName(_fromUtf8("lcdPWM10"))
        self.lcdPWM9 = QtGui.QLCDNumber(self.frame)
        self.lcdPWM9.setGeometry(QtCore.QRect(340, 270, 40, 23))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lcdPWM9.setFont(font)
        self.lcdPWM9.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.lcdPWM9.setNumDigits(4)
        self.lcdPWM9.setObjectName(_fromUtf8("lcdPWM9"))
        self.led13 = QtGui.QLabel(self.frame)
        self.led13.setGeometry(QtCore.QRect(200, 30, 21, 21))
        self.led13.setStyleSheet(_fromUtf8("background-image: none;\n"
"background: none;\n"
""))
        self.led13.setText(_fromUtf8(""))
        self.led13.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/led-off.png")))
        self.led13.setObjectName(_fromUtf8("led13"))
        self.led12 = QtGui.QLabel(self.frame)
        self.led12.setGeometry(QtCore.QRect(240, 30, 21, 21))
        self.led12.setStyleSheet(_fromUtf8("background-image: none;\n"
"background: none;\n"
""))
        self.led12.setText(_fromUtf8(""))
        self.led12.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/led-off.png")))
        self.led12.setObjectName(_fromUtf8("led12"))
        self.led11 = QtGui.QLabel(self.frame)
        self.led11.setGeometry(QtCore.QRect(280, 30, 21, 21))
        self.led11.setStyleSheet(_fromUtf8("background-image: none;\n"
"background: none;\n"
""))
        self.led11.setText(_fromUtf8(""))
        self.led11.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/led-off.png")))
        self.led11.setObjectName(_fromUtf8("led11"))
        self.led10 = QtGui.QLabel(self.frame)
        self.led10.setGeometry(QtCore.QRect(320, 30, 21, 21))
        self.led10.setStyleSheet(_fromUtf8("background-image: none;\n"
"background: none;\n"
""))
        self.led10.setText(_fromUtf8(""))
        self.led10.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/led-off.png")))
        self.led10.setObjectName(_fromUtf8("led10"))
        self.led9 = QtGui.QLabel(self.frame)
        self.led9.setGeometry(QtCore.QRect(360, 30, 21, 21))
        self.led9.setStyleSheet(_fromUtf8("background-image: none;\n"
"background: none;\n"
""))
        self.led9.setText(_fromUtf8(""))
        self.led9.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/led-off.png")))
        self.led9.setObjectName(_fromUtf8("led9"))
        self.led8 = QtGui.QLabel(self.frame)
        self.led8.setGeometry(QtCore.QRect(400, 30, 21, 21))
        self.led8.setStyleSheet(_fromUtf8("background-image: none;\n"
"background: none;\n"
""))
        self.led8.setText(_fromUtf8(""))
        self.led8.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/led-off.png")))
        self.led8.setObjectName(_fromUtf8("led8"))
        self.dw13_l = QtGui.QPushButton(self.frame)
        self.dw13_l.setGeometry(QtCore.QRect(200, 150, 16, 21))
        self.dw13_l.setObjectName(_fromUtf8("dw13_l"))
        self.dw12_l = QtGui.QPushButton(self.frame)
        self.dw12_l.setGeometry(QtCore.QRect(240, 150, 16, 21))
        self.dw12_l.setObjectName(_fromUtf8("dw12_l"))
        self.dw11_l = QtGui.QPushButton(self.frame)
        self.dw11_l.setGeometry(QtCore.QRect(280, 150, 16, 21))
        self.dw11_l.setObjectName(_fromUtf8("dw11_l"))
        self.dw10_l = QtGui.QPushButton(self.frame)
        self.dw10_l.setGeometry(QtCore.QRect(320, 150, 16, 21))
        self.dw10_l.setObjectName(_fromUtf8("dw10_l"))
        self.dw9_l = QtGui.QPushButton(self.frame)
        self.dw9_l.setGeometry(QtCore.QRect(360, 150, 16, 21))
        self.dw9_l.setObjectName(_fromUtf8("dw9_l"))
        self.dw8_l = QtGui.QPushButton(self.frame)
        self.dw8_l.setGeometry(QtCore.QRect(400, 150, 16, 21))
        self.dw8_l.setObjectName(_fromUtf8("dw8_l"))
        self.label_read_pin = QtGui.QLabel(self.frame)
        self.label_read_pin.setGeometry(QtCore.QRect(60, 70, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_read_pin.setFont(font)
        self.label_read_pin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_read_pin.setObjectName(_fromUtf8("label_read_pin"))
        self.label_pinMode = QtGui.QLabel(self.frame)
        self.label_pinMode.setGeometry(QtCore.QRect(60, 100, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_pinMode.setFont(font)
        self.label_pinMode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_pinMode.setObjectName(_fromUtf8("label_pinMode"))
        self.label_digitalWrite = QtGui.QLabel(self.frame)
        self.label_digitalWrite.setGeometry(QtCore.QRect(60, 130, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_digitalWrite.setFont(font)
        self.label_digitalWrite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_digitalWrite.setObjectName(_fromUtf8("label_digitalWrite"))
        self.label_digitalRead = QtGui.QLabel(self.frame)
        self.label_digitalRead.setGeometry(QtCore.QRect(60, 30, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_digitalRead.setFont(font)
        self.label_digitalRead.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_digitalRead.setObjectName(_fromUtf8("label_digitalRead"))
        self.label_analogWrite = QtGui.QLabel(self.frame)
        self.label_analogWrite.setGeometry(QtCore.QRect(60, 180, 121, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_analogWrite.setFont(font)
        self.label_analogWrite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_analogWrite.setObjectName(_fromUtf8("label_analogWrite"))
        self.dw13_h = QtGui.QPushButton(self.frame)
        self.dw13_h.setGeometry(QtCore.QRect(200, 130, 16, 21))
        self.dw13_h.setObjectName(_fromUtf8("dw13_h"))
        self.dw12_h = QtGui.QPushButton(self.frame)
        self.dw12_h.setGeometry(QtCore.QRect(240, 130, 16, 21))
        self.dw12_h.setObjectName(_fromUtf8("dw12_h"))
        self.dw11_h = QtGui.QPushButton(self.frame)
        self.dw11_h.setGeometry(QtCore.QRect(280, 130, 16, 21))
        self.dw11_h.setObjectName(_fromUtf8("dw11_h"))
        self.dw10_h = QtGui.QPushButton(self.frame)
        self.dw10_h.setGeometry(QtCore.QRect(320, 130, 16, 21))
        self.dw10_h.setObjectName(_fromUtf8("dw10_h"))
        self.dw9_h = QtGui.QPushButton(self.frame)
        self.dw9_h.setGeometry(QtCore.QRect(360, 130, 16, 21))
        self.dw9_h.setObjectName(_fromUtf8("dw9_h"))
        self.dw8_h = QtGui.QPushButton(self.frame)
        self.dw8_h.setGeometry(QtCore.QRect(400, 130, 16, 21))
        self.dw8_h.setObjectName(_fromUtf8("dw8_h"))
        self.pushButtonReadPin = QtGui.QPushButton(self.centralwidget)
        self.pushButtonReadPin.setGeometry(QtCore.QRect(20, 490, 85, 27))
        self.pushButtonReadPin.setObjectName(_fromUtf8("pushButtonReadPin"))
        self.checkboxAutoReadPins = QtGui.QCheckBox(self.centralwidget)
        self.checkboxAutoReadPins.setGeometry(QtCore.QRect(120, 490, 141, 21))
        self.checkboxAutoReadPins.setObjectName(_fromUtf8("checkboxAutoReadPins"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pinValue11, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdPWM11.display)
        QtCore.QObject.connect(self.pinValue10, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdPWM10.display)
        QtCore.QObject.connect(self.pinValue9, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdPWM9.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled13.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled12.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled11.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled10.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled9.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinEnabled8.setToolTip(QtGui.QApplication.translate("MainWindow", "Enabled / Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode13.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode13.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode12.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode12.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode11.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode11.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode10.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode10.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode9.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode9.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode8.setToolTip(QtGui.QApplication.translate("MainWindow", "Input / Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinMode8.setText(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pinValue11.setToolTip(QtGui.QApplication.translate("MainWindow", "PWM Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinValue10.setToolTip(QtGui.QApplication.translate("MainWindow", "PWM Output", None, QtGui.QApplication.UnicodeUTF8))
        self.pinValue9.setToolTip(QtGui.QApplication.translate("MainWindow", "PWM Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label13.setText(QtGui.QApplication.translate("MainWindow", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.label12.setText(QtGui.QApplication.translate("MainWindow", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.label11.setText(QtGui.QApplication.translate("MainWindow", "~11", None, QtGui.QApplication.UnicodeUTF8))
        self.label10.setText(QtGui.QApplication.translate("MainWindow", "~10", None, QtGui.QApplication.UnicodeUTF8))
        self.label9.setText(QtGui.QApplication.translate("MainWindow", "~9", None, QtGui.QApplication.UnicodeUTF8))
        self.label8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.dw13_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw13_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw12_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw12_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw11_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw11_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw10_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw10_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw9_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw9_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.dw8_l.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(LOW)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw8_l.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.label_read_pin.setText(QtGui.QApplication.translate("MainWindow", "Read pin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pinMode.setText(QtGui.QApplication.translate("MainWindow", "pinMode()", None, QtGui.QApplication.UnicodeUTF8))
        self.label_digitalWrite.setText(QtGui.QApplication.translate("MainWindow", "digitalWrite()", None, QtGui.QApplication.UnicodeUTF8))
        self.label_digitalRead.setText(QtGui.QApplication.translate("MainWindow", "digitalRead()", None, QtGui.QApplication.UnicodeUTF8))
        self.label_analogWrite.setText(QtGui.QApplication.translate("MainWindow", "PWM ~ analogWrite()", None, QtGui.QApplication.UnicodeUTF8))
        self.dw13_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw13_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw12_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw12_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw11_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw11_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw10_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw10_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw9_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw9_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.dw8_h.setToolTip(QtGui.QApplication.translate("MainWindow", "digitalWrite(HIGH)", None, QtGui.QApplication.UnicodeUTF8))
        self.dw8_h.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonReadPin.setText(QtGui.QApplication.translate("MainWindow", "Read PINs", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxAutoReadPins.setText(QtGui.QApplication.translate("MainWindow", "Continuously read PINs", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
