'''
Created on 23 Jul 2010

@author: ms705
'''
from gui.surveyFolderSelectionDialog import surveyFolderSelectionDialog

import ui_welcome
from PyQt4 import QtGui, QtCore

from common import utils

class surveyWelcomeDialog(QtGui.QDialog):
    
    def next(self):
        utils.debug_print("Welcome screen confirmed", utils.SUCC)
        self.close()
        d = surveyFolderSelectionDialog(self.app)
        d.setAttribute(QtCore.Qt.WA_DeleteOnClose)    
        d.exec_()

    def __init__(self, owner):        
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_welcome.Ui_surveyDialog()
        self.ui.setupUi(self)
        self.app = owner;

        # signal/slot connections
        self.connect(self.ui.btnCancel, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
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

