# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Jul 23 15:00:16 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Qt4Test(object):
    def setupUi(self, Qt4Test):
        Qt4Test.setObjectName("Qt4Test")
        Qt4Test.resize(449, 364)
        self.pushButton = QtGui.QPushButton(Qt4Test)
        self.pushButton.setGeometry(QtCore.QRect(340, 320, 88, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Qt4Test)
        QtCore.QMetaObject.connectSlotsByName(Qt4Test)

    def retranslateUi(self, Qt4Test):
        Qt4Test.setWindowTitle(QtGui.QApplication.translate("Qt4Test", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Qt4Test", "&Next", None, QtGui.QApplication.UnicodeUTF8))

