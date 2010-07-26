# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/main.ui'
#
# Created: Mon Jul 26 15:32:49 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_surveyDialog(object):
    def setupUi(self, surveyDialog):
        surveyDialog.setObjectName("surveyDialog")
        surveyDialog.setWindowModality(QtCore.Qt.NonModal)
        surveyDialog.resize(516, 512)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(surveyDialog.sizePolicy().hasHeightForWidth())
        surveyDialog.setSizePolicy(sizePolicy)
        surveyDialog.setMinimumSize(QtCore.QSize(516, 512))
        surveyDialog.setMaximumSize(QtCore.QSize(516, 512))
        surveyDialog.setSizeGripEnabled(False)
        surveyDialog.setModal(False)
        self.btnNext = QtGui.QPushButton(surveyDialog)
        self.btnNext.setGeometry(QtCore.QRect(410, 430, 88, 27))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.btnNext.setFont(font)
        self.btnNext.setObjectName("btnNext")
        self.label = QtGui.QLabel(surveyDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/res/uc-colour-small.png"))
        self.label.setObjectName("label")
        self.line = QtGui.QFrame(surveyDialog)
        self.line.setGeometry(QtCore.QRect(40, 130, 431, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtGui.QLabel(surveyDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(surveyDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 481, 281))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.line_2 = QtGui.QFrame(surveyDialog)
        self.line_2.setGeometry(QtCore.QRect(40, 410, 431, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtGui.QLabel(surveyDialog)
        self.label_4.setGeometry(QtCore.QRect(20, 460, 361, 16))
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(surveyDialog)
        self.label_5.setGeometry(QtCore.QRect(20, 440, 221, 16))
        self.label_5.setObjectName("label_5")
        self.btnCancel = QtGui.QPushButton(surveyDialog)
        self.btnCancel.setGeometry(QtCore.QRect(410, 470, 88, 27))
        self.btnCancel.setObjectName("btnCancel")

        self.retranslateUi(surveyDialog)
        QtCore.QMetaObject.connectSlotsByName(surveyDialog)

    def retranslateUi(self, surveyDialog):
        surveyDialog.setWindowTitle(QtGui.QApplication.translate("surveyDialog", "University of Cambridge -- Personal Storage Survey", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNext.setText(QtGui.QApplication.translate("surveyDialog", "&Next", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("surveyDialog", "Computer Laboratory -- Personal Storage Survey", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("surveyDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Thank your for participating in the Computer Laboratory Laboratory Personal Storage Survey.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">This survey will:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* ask you a few simple questions about how you store your personal data,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* scan your \"My Documents\" directory / home directory, gather some anonymised aggregate information and submit it,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* finally permanently remove itself from your computer.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">It will </span><span style=\" font-weight:600; font-style:italic;\">NOT</span><span style=\" font-style:italic;\">:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* leak any file names, file content or personal information,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* install persistent software on your computer.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You will be able to review all the data submitted before it is sent. Please click \"Next\" to continue.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("surveyDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.cl.cam.ac.uk/~ms705/research/storagesurvey/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.cl.cam.ac.uk/~ms705/research/storagesurvey/</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("surveyDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">For more information, visit:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("surveyDialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))

import qtresources_rc
