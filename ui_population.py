# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_population.ui'
#
# Created: Fri Feb 21 10:09:21 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Population(object):
    def setupUi(self, Population):
        Population.setObjectName(_fromUtf8("Population"))
        Population.resize(546, 278)
        self.buttonBox = QtGui.QDialogButtonBox(Population)
        self.buttonBox.setGeometry(QtCore.QRect(60, 200, 371, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.mileButton = QtGui.QRadioButton(Population)
        self.mileButton.setGeometry(QtCore.QRect(240, 70, 153, 31))
        self.mileButton.setObjectName(_fromUtf8("mileButton"))
        self.kmButton = QtGui.QRadioButton(Population)
        self.kmButton.setGeometry(QtCore.QRect(240, 30, 153, 31))
        self.kmButton.setObjectName(_fromUtf8("kmButton"))
        self.lcdNumber = QtGui.QLCDNumber(Population)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 20, 211, 91))
        self.lcdNumber.setFrameShape(QtGui.QFrame.WinPanel)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalSlider = QtGui.QSlider(Population)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 140, 361, 51))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.loadFile = QtGui.QPushButton(Population)
        self.loadFile.setGeometry(QtCore.QRect(400, 30, 131, 45))
        self.loadFile.setObjectName(_fromUtf8("loadFile"))
        self.removeFile = QtGui.QPushButton(Population)
        self.removeFile.setGeometry(QtCore.QRect(400, 90, 131, 45))
        self.removeFile.setObjectName(_fromUtf8("removeFile"))

        self.retranslateUi(Population)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Population.reject)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(Population)

    def retranslateUi(self, Population):
        Population.setWindowTitle(_translate("Population", "Population", None))
        self.mileButton.setText(_translate("Population", "Miles", None))
        self.kmButton.setText(_translate("Population", "Kilometers", None))
        self.loadFile.setText(_translate("Population", "Load City", None))
        self.removeFile.setText(_translate("Population", "Remove City", None))