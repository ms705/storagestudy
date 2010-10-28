'''
Created on 23 Jul 2010

@author: ms705
'''
import os

from gui.surveyScanningDialog import surveyScanningDialog
from gui.checkableDirModel import CheckableFSModel

import ui_folderselection
from PyQt4 import QtGui
from PyQt4.QtCore import *

from common import utils

class surveyFolderSelectionDialog(QtGui.QDialog):
    
    def next(self):
        # check if we have actually selected some folders
        dirs = self.dir_model.getCheckList()
        if dirs == []:
            reply = QtGui.QMessageBox.warning(self, 'No directories selected',
            "You have not selected any directories. Would you like to attempt to work " + 
            "out your home directory automatically?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                homeDirPath = os.getenv("HOME","")
                if homeDirPath != "":
                    self.dir_model.addCheck(homeDirPath)
                else:
                    utils.debug_print("Could not work out the home directory", utils.ERR)
                    QtGui.QMessageBox.critical(self, 'Failed to detect home directory', 
                       "Failed to detect your home directory automatically. Please go back and select it manually.", QtGui.QMessageBox.Ok)
                    return
            else:
                return

        # run the scan
        utils.debug_print("Folders selected:", utils.SUCC, False)
        print dirs
        self.close()
        d = surveyScanningDialog(self.app, dirs, self.token)
        d.setAttribute(Qt.WA_DeleteOnClose)
        d.exec_()

    def __init__(self, owner, token):        
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_folderselection.Ui_surveyDialog()
        self.ui.setupUi(self)
        self.app = owner;
        self.token = token;

        # signal/slot connections
        self.connect(self.ui.btnCancel, SIGNAL('clicked()'), self.cancel)
        self.connect(self.ui.btnNext, SIGNAL('clicked()'), self.next)
    
        # set up the directory tree
        index = QModelIndex()
        self.dir_model = CheckableFSModel()
        filters = QDir.AllDirs|QDir.Readable|QDir.NoDotAndDotDot
        self.dir_model.setData(index, Qt.Checked, Qt.CheckStateRole)
        self.dir_model.setFilter(filters)
        self.dir_model.setReadOnly(True)
        self.ui.directoryTree.setModel(self.dir_model)
        self.ui.directoryTree.setColumnHidden(1, True)
        self.ui.directoryTree.setColumnHidden(2, True)
        self.ui.directoryTree.setColumnHidden(3, True)
        self.ui.directoryTree.expandToDepth(0) 

        #d = QtGui.QApplication.desktop()
        #print d.width(), " by ", d.height() 

        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

        #vpos = d.height() / 2 - (self.height() / 2);
        #if (d.width() > 2*d.height()):
        #    hpos = d.width() / 4 - (self.width() / 2);
        #else:
        #    hpos = d.width() / 2 - (self.width() / 2);
        #self.move(hpos, vpos);


    def cancel(self):
        if self.confirmClose():
            quit()

    
    def closeEvent(self, event):
        if not self.done: 
            if self.confirmClose():
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

        
    def confirmClose(self):
        reply = QtGui.QMessageBox.question(self, 'Confirm cancellation',
            "Are you sure you want to cancel? This will mean that all data entered " +  
            "is lost and no results are submitted to the researchers.", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        return (reply == QtGui.QMessageBox.Yes)
    