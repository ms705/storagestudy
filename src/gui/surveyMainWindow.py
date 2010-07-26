'''
Created on 23 Jul 2010

@author: ms705
'''

import ui_main
from PyQt4 import QtGui, QtCore


class surveyMainWindow(QtGui.QDialog):
    
    def __init__(self, owner):        
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_main.Ui_surveyDialog()
        self.ui.setupUi(self)

        # signal/slot connections
        self.connect(self.ui.btnCancel, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
    
        d = QtGui.QApplication.desktop()
        print d.width(), " by ", d.height() 

        vpos = d.height() / 2 - (self.height() / 2);
        if (d.width() > 2*d.height()):
            hpos = d.width() / 4 - (self.width() / 2);
        else:
            hpos = d.width() / 2 - (self.width() / 2);
        self.move(hpos, vpos);
