# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_loadcity.ui'
#
# Created: Thu Mar 06 23:39:09 2014
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

class Ui_loadCity(object):
    def setupUi(self, loadCity):
        loadCity.setObjectName(_fromUtf8("loadCity"))
        loadCity.resize(435, 200)
        self.buttonBox = QtGui.QDialogButtonBox(loadCity)
        self.buttonBox.setGeometry(QtCore.QRect(30, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.locationName = QtGui.QComboBox(loadCity)
        self.locationName.setGeometry(QtCore.QRect(160, 40, 241, 51))

        self.locationName.setObjectName(_fromUtf8("locationName"))
        self.locationName.addItem("New York City")
        self.locationName.addItem("Bronx")
        self.locationName.addItem("Brooklyn")
        self.locationName.addItem("Queens")
        self.locationName.addItem("Nassau County")
        self.locationName.addItem("Suffolk County")


        self.label = QtGui.QLabel(loadCity)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(loadCity)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), loadCity.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), loadCity.reject)
        QtCore.QMetaObject.connectSlotsByName(loadCity)

    def retranslateUi(self, loadCity):
        loadCity.setWindowTitle(_translate("loadCity", "Dialog", None))
        self.label.setText(_translate("loadCity", "Location:", None))

