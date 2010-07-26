'''
Created on 23 Jul 2010

@author: ms705
'''

import os
import ui_scanning

from PyQt4 import QtGui, QtCore

from common import utils
from walker import walker


class surveyScanningDialog(QtGui.QDialog):
    
    def __init__(self, owner):        
        QtGui.QMainWindow.__init__(self)
        self.ui = ui_scanning.Ui_scanDialog()
        self.ui.setupUi(self)

        # signal/slot connections
        #self.connect(self.ui.btnCancel, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
    
        #vpos = d.height() / 2 - (self.height() / 2);
        #if (d.width() > 2*d.height()):
        #    hpos = d.width() / 4 - (self.width() / 2);
        #else:
        #    hpos = d.width() / 2 - (self.width() / 2);
        #self.move(hpos, vpos);
        self.center()

    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

        # launch directory walker
        #homeDirPath = os.getenv("HOME","")
        #utils.debug_print("Your home directory is: " + homeDirPath)
        
        #w = walker.Walker()
        #w.walk("/local/scratch/ms705/survey/HomeDirSurvey")
        #w.walk(homeDirPath)
        