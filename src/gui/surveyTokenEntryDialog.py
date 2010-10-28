'''
Created on 23 Jul 2010

@author: ms705
'''
from gui.surveyFolderSelectionDialog import surveyFolderSelectionDialog

import ui_tokenentry
from PyQt4 import QtGui, QtCore

from common import utils

class surveyTokenEntryDialog(QtGui.QDialog):
    
    def next(self):
        utils.debug_print("Token entry screen confirmed", utils.SUCC)
        self.done = True
        self.ui.lblPleaseWait.setVisible(True);
        self.ui.lblExamplePic.setVisible(False);
        self.ui.progressBar.setVisible(True);

        self.ui.lblToken.setEnabled(False);
        self.ui.txtToken.setEnabled(False);
        self.ui.btnNext.setEnabled(False);
        self.ui.btnCancel.setEnabled(False);
        
        self.app.processEvents();
        
        d = surveyFolderSelectionDialog(self.app, str(self.ui.txtToken.text()))
        d.setAttribute(QtCore.Qt.WA_DeleteOnClose)    
        self.close()
        d.exec_()


    def __init__(self, owner):        
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_tokenentry.Ui_surveyDialog()
        self.ui.setupUi(self)
        self.app = owner;
        self.done = False

        self.ui.lblPleaseWait.setVisible(False);
        self.ui.progressBar.setVisible(False);

        # signal/slot connections
        self.connect(self.ui.btnCancel, QtCore.SIGNAL('clicked()'), self.cancel)
        self.connect(self.ui.btnNext, QtCore.SIGNAL('clicked()'), self.next)
    
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
