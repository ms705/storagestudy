'''
Created on 23 Jul 2010

@author: ms705
'''
from gui.surveyScanningDialog import surveyScanningDialog

import ui_main
from PyQt4 import QtGui, QtCore


class surveyWelcomeDialog(QtGui.QDialog):
    
    def next(self):
        print "next clicked"
        d = surveyScanningDialog(self.app)
        d.show()

    def __init__(self, owner):        
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_main.Ui_surveyDialog()
        self.ui.setupUi(self)
        self.app = owner;

        # signal/slot connections
        self.connect(self.ui.btnCancel, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        self.connect(self.ui.btnNext, QtCore.SIGNAL('clicked()'), self.next)
    
        d = QtGui.QApplication.desktop()
        print d.width(), " by ", d.height() 

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

